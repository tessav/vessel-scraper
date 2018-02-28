from vesselapp import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy(app)


class Vessel(db.Model):
    v_id = db.Column(db.Integer, primary_key=True)
    v_name = db.Column(db.String(256))
    arv_dt = db.Column(db.DateTime)
    vs = db.relationship('VesselSchedule', backref='vessel', lazy=True)
    vp = db.relationship('VesselPosition', backref='vessel', lazy=True)
    cargo = db.Column(db.String(64))
    qty = db.Column(db.String(32))
    v_type = db.Column(db.String(8))
    agent = db.Column(db.String(64))
    updated_on = db.Column(db.DateTime(timezone=True), server_default=func.now())


class VesselSchedule(db.Model):
    vs_id = db.Column(db.Integer, primary_key=True)
    arv_dt = db.Column(db.DateTime)
    vessel_ref = db.Column(db.Integer, db.ForeignKey('vessel.v_id'), nullable=False)
    cargo = db.Column(db.String(64))
    qty = db.Column(db.String(32))
    v_type = db.Column(db.String(8))
    agent = db.Column(db.String(64))
    scraped_on = db.Column(db.DateTime(timezone=True), server_default=func.now())
# 
# class VesselMovement(db.Model):
#     pass


class VesselPosition(db.Model):
    vp_id = db.Column(db.Integer, primary_key=True)
    berth = db.Column(db.String(8))
    v_type = db.Column(db.String(8))
    fc = db.Column(db.String(1))
    berth_date = db.Column(db.DateTime)
    vessel_ref = db.Column(db.Integer, db.ForeignKey('vessel.v_id'), nullable=False)
    cargo = db.Column(db.String(64))
    qty = db.Column(db.String(32))
    day_handling = db.Column(db.String(16))
    up_to_day_handling = db.Column(db.String(16))
    balance = db.Column(db.String(16))
    load_port = db.Column(db.String(32))
    agent = db.Column(db.String(64))
    scraped_on = db.Column(db.DateTime(timezone=True), server_default=func.now())
