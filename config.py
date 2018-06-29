class Config(object):
    """
    This is the shared common configurations
    """
    # Put any configurations here that are common across all environments
 
class DevelopmentConfig(Config):
    """
    This is the development configurations
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True #Display queries to console
 
class ProductionConfig(Config):
    """
    This is the production configurations
    """
    DEBUG = False
    SQLALCHEMY_ECHO = False #Do not Display queries to console
 
app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
