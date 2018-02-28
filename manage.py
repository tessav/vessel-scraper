#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_script import Manager
from vesselapp import app
from vesselapp.models import db
from vesselapp.routes import site
from scraper.runner import run_spiders

app.register_blueprint(site)
manager = Manager(app)


@manager.command
def migrate():
    db.create_all()

@manager.command
def dropdb():
    db.drop_all()

@manager.command
def crawl():
    run_spiders()

if __name__ == '__main__':
    manager.run()
