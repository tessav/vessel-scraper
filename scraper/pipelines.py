# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from vesselapp.models import db, Vessel, VesselSchedule, VesselMovement, VesselPosition

class ScraperPipeline(object):

    def process_item(self, item, spider):
        if spider.name == 'schedule':
            self.process_schedule(item, spider)
        elif spider.name == 'position':
            self.process_position(item, spider)
        elif spider.name == 'movement':
            self.process_movement(item, spider)


    def process_schedule(self, item, spider):
        spider.logger.info('schedule', item)
        vessel = self.get_vessel(item['vessel'])
        vs = VesselSchedule()
        vs.arv_dt = item['arv_dt']
        vs.vessel_ref = vessel.v_id
        vs.cargo = item['cargo']
        vs.qty = item['qty']
        vs.v_type = item['v_type']
        vs.agent = item['agent']
        db.session.add(vs)
        db.session.commit()
        self.update_vessel(vessel, vs)
        return item


    def process_position(self, item, spider):
        spider.logger.info('position', item)
        vessel = self.get_vessel(item['vessel'])
        vp = VesselPosition()
        vp.berth = item['berth']
        vp.v_type = item['v_type']
        vp.fc = item['fc']
        vp.berth_date = item['berth_date']
        vp.vessel_ref = vessel.v_id
        vp.cargo = item['cargo']
        vp.qty = item['qty']
        vp.day_handling = item['day_handling']
        vp.up_to_day_handling = item['up_to_day_handling']
        vp.balance = item['balance']
        vp.load_port = item['load_port']
        vp.agent = item['agent']
        db.session.add(vp)
        db.session.commit()
        return item


    def process_movement(self, item, spider):
        spider.logger.info('movement', item)
        vessel = self.get_vessel(item['vessel'])
        vm = VesselMovement()
        vm.move_date = item['move_date']
        vm.berth_allotted = item['berth_allotted']
        vm.status = item['status']
        vm.boarding_time = item['boarding_time']
        vm.vessel_ref = vessel.v_id
        db.session.add(vm)
        db.session.commit()
        return item


    def get_vessel(self, name):
        vessel = Vessel.query.filter_by(v_name= name).all()
        if not vessel:
            ves = Vessel()
            ves.v_name = name
            db.session.add(ves)
            db.session.commit()
        else:
            ves = vessel[0]
        return ves


    def update_vessel(self, vessel, vs):
        # FIXME: need to adjust for case where a vessel has >1 schedules
        vessel.arv_dt = vs.arv_dt
        vessel.cargo = vs.cargo
        vessel.qty = vs.qty
        vessel.v_type = vs.v_type
        vessel.agent = vs.agent
        db.session.commit()
