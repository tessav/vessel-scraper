# -*- coding: utf-8 -*-

# app info
APP_NAME = 'scraper'

# flask config
DEBUG = True
SECRET_KEY = 'scraper'

# postgresql connection
SQLALCHEMY_DATABASE_URI = 'postgresql://adminroot:vesseldb12345@localhost:5432/vessel'
SQLALCHEMY_TRACK_MODIFICATIONS = True
