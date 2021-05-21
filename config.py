import os
from ibm_botocore.client import Config
import ibm_boto3
import os
from datetime import date
from dotenv import load_dotenv

# Load dotenv file
load_dotenv()


class Config(object):
    DEBUG = False
    TESTING = False

    # Specify Directories 
    CFG = os.path.join(os.getcwd(), "app/cfg/yolov3.cfg")
    LABELS = os.path.join(os.getcwd(), "app/data/coco.names")
    MODEL_FOLDER =  os.path.join(os.getcwd(), "app/model/")
    MODEL_WEIGHTS_FOLDER = os.path.join(os.getcwd(), "app/weights/")
    MODEL_WEIGHTS = os.path.join(os.getcwd(), "app/weights/yolov3.weights")
    UPLOAD_FOLDER = os.path.join(os.getcwd(), "app/uploads/") 

    # Specify COS BUCKET Credentials
    APIKEY = os.environ.get("apikey")
    ENDPOINTS = os.environ.get("endpoints")
    IAM_APIKEY_DESCRIPTION = os.environ.get("iam_apikey_description")
    IAM_APIKEY_NAME = os.environ.get("iam_apikey_name")
    IAM_ROLE_CRN = os.environ.get("iam_role_crn")
    IAM_SERVICEID_CRN = os.environ.get("iam_serviceid_crn")
    RESOURCE_INSTANCE_ID = os.environ.get("resource_instance_id")
    AUTH_ENDPOINT = os.environ.get("auth_endpoint")
    SERVICE_ENDPOINT = os.environ.get("service_endpoint")
    BUCKET_NAME = os.environ.get("bucket_name")



    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True

    SESSION_COOKIE_SECURE = False