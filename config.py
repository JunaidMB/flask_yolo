import os 
class Config(object):
    DEBUG = False
    TESTING = False

    CFG = os.path.join(os.getcwd(), "app/cfg/yolov3.cfg")
    LABELS = os.path.join(os.getcwd(), "app/data/coco.names")
    MODEL_FOLDER =  os.path.join(os.getcwd(), "app/model/")
    MODEL_WEIGHTS = os.path.join(os.getcwd(), "app/weights/yolov3.weights")
    UPLOAD_FOLDER = os.path.join(os.getcwd(), "app/uploads/") 

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True

    SESSION_COOKIE_SECURE = False