# -*- coding: utf-8 -*-

from flask import Flask
from vesselapp import settings

app = Flask(settings.APP_NAME)
app.config.from_object(settings)
