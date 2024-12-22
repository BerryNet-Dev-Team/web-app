import os
import json
import uuid
from dotenv import load_dotenv
import datetime
load_dotenv() 

from flask import Blueprint, request, redirect, jsonify, abort, g
from ..database.dbConnection import db
from ..models.scene import Scene
from ..security.decorators_utils import auth_required
from ..cloudServices.minioConnections import minioClient

scenes = Blueprint('scenes', __name__, url_prefix='/scenes')

@scenes.route('getScenePresignedUrls', methods=['GET'])
@auth_required(["ADMIN"])
def getScenePresignedUrls():
    folderName = str(uuid.uuid4().hex)
    s3Host = os.getenv('S3_LIVE_BASE_URL')

    # Generate live and upload urls for the scene image
    try:
        imgObjectKey = f"dataset/{folderName}/img.jpg"
        imgLiveUrl = f"{s3Host}/{imgObjectKey}"
        imgUploadUrl = minioClient.presigned_put_object(
            os.getenv('S3_BUCKET'),
            imgObjectKey,
            os.getenv('S3_PRESIGNED_EXPIRATION')
        )
    except Exception as exc:
        print(exc)
        abort(500, 'Error getting presigned url for img')

    # Generate live and upload urls for the scene map
    try:
        mapObjectKey = f"dataset/{folderName}/map.txt"
        mapLiveUrl = f"{s3Host}/{imgObjectKey}"
        mapUploadUrl = minioClient.presigned_put_object(
            os.getenv('S3_BUCKET'),
            mapObjectKey,
            os.getenv('S3_PRESIGNED_EXPIRATION')
        )
    except Exception as exc:
        print(exc)
        abort(500, 'Error getting presigned url for txt')

    # Setup response data
    responseData = {
        "mapUrls": { "uploadURL":mapUploadUrl, "liveURL":mapLiveUrl },
        "imgUrls": { "uploadURL":imgUploadUrl, "liveURL":imgLiveUrl }
    }

    return jsonify(responseData), 200

@scenes.route('addScene', methods=['POST'])
@auth_required(["ADMIN"])
def addScene():
    try:
        req = request.json
    except:
        abort(400, 'BAD REQUEST')
    
    # Check if request has enough properties needed
    required_keys = ['name', 'imageUrl', 'mapUrl']
    if not all(key in req for key in required_keys):
        abort(400, 'BAD REQUEST')

    # Get request properties
    name = req['name']
    imageUrl = req['imageUrl']
    mapUrl = req['mapUrl']

    new_scene = Scene(
        name=name,
        imageUrl=imageUrl,
        mapUrl=mapUrl,
        uploadedOn=datetime.datetime.now()
    )

    try:
        db.session.add(new_scene)
        db.session.commit()
    except:
        abort(500, 'Error while saving scene')

    return jsonify({"message: scene added successfully"}), 200