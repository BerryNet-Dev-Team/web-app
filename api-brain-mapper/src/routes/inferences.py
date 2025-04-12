import os
import json
import uuid
from dotenv import load_dotenv
import datetime
import requests
load_dotenv() 

from flask import Blueprint, request, redirect, jsonify, abort, g
from logs.logger import logger

from ..database.dbConnection import db
from ..models.inference import Inference
from ..security.decorators_utils import auth_required
from ..cloudServices.minioConnections import getMinioClient
from ..cloudServices.nnApiConnections import NnAPIClient

# Instantiate a NnAPIClient
nnClient = NnAPIClient(
    base_url=os.getenv('NN_API_HOST'),
    secret_key=os.getenv('NN_API_SECRET_KEY'),
)

# Define router prefix
inferences = Blueprint('inferences', __name__, url_prefix='/inferences')

# ------- All the routes -------
@inferences.route('/getBaseImgPresignedUrls', methods=['GET'])
@auth_required()
def getBaseImgPresignedUrls():
    # Instantiate a minio client
    minioClient = getMinioClient()

    # Creates unique foldername
    folderName = str(uuid.uuid4().hex)

    # Configure s3 constants for inferences bucket
    s3Bucket= os.getenv('S3_BUCKET_INFERENCES_RESULTS')
    s3LiveUrl = os.getenv('S3_LIVE_BASE_URL') + s3Bucket
    presignedExpTime = int(os.getenv('S3_PRESIGNED_EXPIRATION'))

    # Generate live and upload urls for the image
    try:
        imgObjectKey = f"{folderName}/original_img.jpg"
        imgLiveUrl = f"{s3LiveUrl}/{imgObjectKey}"
        imgUploadUrl = minioClient.presigned_put_object(
            s3Bucket,
            imgObjectKey,
            expires=datetime.timedelta(seconds=presignedExpTime)
        )
    except Exception as exc:
        logger.exception('Presigned S3 error')
        abort(500, 'Error getting presigned url for img')

    # Setup response data
    responseData = { "uploadURL":imgUploadUrl, "liveURL":imgLiveUrl, "imgObjectKey": imgObjectKey }

    return jsonify(responseData), 200

@inferences.route('/generateInference', methods=['POST'])
@auth_required()
def generateInference():
    try:
        req = request.json
    except:
        abort(400, 'BAD REQUEST')

    # Check if request has enough properties needed
    required_keys = ['name', 'imgUrl', 'imgObjectKey']
    if not all(key in req for key in required_keys):
        abort(400, 'BAD REQUEST')

    # Get request properties
    name = req['name']
    baseImageUrl = req['imgUrl']
    imgObjectKey = req['imgObjectKey']

    # Make API call to ANN-API to make the inference
    try:
        payload = {'imgObjectKey': imgObjectKey}
        json_response = nnClient.generateInference(payload)
        generatedImageUrl = json_response['generatedImgUrl']
    except Exception as exc:
        logger.exception(f'Error generating inference for {imgObjectKey}')
        abort(500, 'Error generating inference')

    # Make new instance of inference model
    new_inference = Inference(
        userId=g.uid,
        name=name,
        baseImageUrl=baseImageUrl,
        generatedImageUrl=generatedImageUrl,
        createdOn=datetime.datetime.now()
    )

    # Save inference in DB
    try:
        db.session.add(new_inference)
        db.session.commit()
    except Exception as exc:
        logger.exception(f'Error saving in DB inference of {imgObjectKey}')
        abort(500, 'Error while saving inference')

    # Respond with the generatedImageUrl
    return jsonify({'generatedImgUrl': generatedImageUrl}), 200
