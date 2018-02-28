# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from vesselapp.models import db, Vessel, VesselSchedule

class ScraperPipeline(object):

    def process_item(self, item, spider):
        vessel = self.get_vessel(item['vessel'])
        vs = VesselSchedule()
        vs.arv_dt = item['arv_dt']
        vs.vessel = vessel
        vs.cargo = item['cargo']
        vs.qty = item['qty']
        vs.v_type = item['v_type']
        vs.agent = item['agent']
        db.session.add(vs)
        db.session.commit()
        self.update_vessel(vessel, vs)
        return item


    def get_vessel(self, name):
        vessel = Vessel.query.filter_by(v_name= name).all()
        if not vessel:
            vessel = Vessel()
            vessel.v_name = name
            db.session.add(vessel)
            db.session.commit()
        return vessel


    def update_vessel(self, vessel, vs):
        # FIXME: need to adjust for case where a vessel has >1 schedules
        vessel.arv_dt = vs.arv_dt
        vessel.cargo = vs.cargo
        vessel.qty = vs.qty
        vessel.v_type = vs.v_type
        vessel.agent = vs.agent
        db.session.commit()
