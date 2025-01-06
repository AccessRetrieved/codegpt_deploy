class Config:
    pass

class DevConfig(Config):
    TESTING = True
    DEBUG = True
    
class ProdConfig(Config):
    DEBUG = False
    TESTING = False