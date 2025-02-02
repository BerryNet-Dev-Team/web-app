import os
import json
import uuid
from dotenv import load_dotenv
import datetime
load_dotenv() 

from flask import Blueprint, request, redirect, jsonify, abort, g
from ..database.dbConnection import db
from ..models.inference import Inference
from ..security.decorators_utils import auth_required
from ..cloudServices.minioConnections import minioClient

inferences = Blueprint('inferences', __name__, url_prefix='/inferences')

@inferences.route('/getBaseImgPresignedUrls', methods=['GET'])
@auth_required()
def getBaseImgPresignedUrls():
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
        print(exc)
        abort(500, 'Error getting presigned url for img')

    # Setup response data
    responseData = { "uploadURL":imgUploadUrl, "liveURL":imgLiveUrl, "imgObjectKey": imgObjectKey }

    return jsonify(responseData), 200

@inferences.route('/addInference', methods=['POST'])
@auth_required()
def addInference():
    try:
        req = request.json
    except:
        abort(400, 'BAD REQUEST')

    # Check if request has enough properties needed
    required_keys = ['name', 'baseImageUrl', 'generatedImageUrl']
    if not all(key in req for key in required_keys):
        abort(400, 'BAD REQUEST')

    # Get request properties
    name = req['name']
    baseImageUrl = req['baseImageUrl']
    generatedImageUrl = req['generatedImageUrl']

    new_inference = Inference(
        userId=g.uid,
        name=name,
        baseImageUrl=baseImageUrl,
        generatedImageUrl=generatedImageUrl,
        createdOn=datetime.datetime.now()
    )

    try:
        db.session.add(new_inference)
        db.session.commit()
    except:
        abort(500, 'Error while saving inference')

    return jsonify({"message": "inference added successfully"}), 200