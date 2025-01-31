import os
#from flask_httpauth import HTTPBasicAuth
#from flask_caching import Cache

pjdir = os.path.abspath(os.path.dirname(__file__))
POSTGRES = {
    'user': 'aehzefdybddfcl',
    'password': '2ce386813249e02b9049ed23201cf2a6a5c5f9710b8f34cb73d74240fe9ca2fc',
    'db': 'ddmsht4bl80g3n',
    'host': 'ec2-107-21-201-238.compute-1.amazonaws.com',
    'port': '5432',
}

class Config(object):
    pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://ebuijlzvchiehu:c4613c281271dda2f7b1deec47dfe1506d4c87e23d905916b614aaac1f23ea92@ec2-174-129-252-228.compute-1.amazonaws.com:5432/d39479odedb5t7'
 #'postgresql://%(user)s:%(password)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    DEBUG = False
    ENV = "production"

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(pjdir, 'data.sqlite')
    DEBUG = True
    ENV = "development"

config = {
    'development': DevConfig,
    'production': ProdConfig,
    'default': DevConfig
}

#auth = HTTPBasicAuth()
#cache = Cache(config={'CACHE_TYPE': 'simple'})