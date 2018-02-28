from flask import render_template, request, views
from vesselapp.models import Vessel, VesselSchedule, VesselPosition, VesselMovement
from datetime import datetime as dt
from datetime import timedelta
from dtservice import get_dt_range, DEFAULT_SELECTION


class ScheduleView(views.MethodView):
    def get(self):
        dt_choice = request.args.get('dt')
        selection = dt_choice if dt_choice else DEFAULT_SELECTION
        s, e = get_dt_range(selection)
        schedule = Vessel.query.filter(Vessel.arv_dt >= s).filter(Vessel.arv_dt < e)
        return render_template('schedule.html', schedule=schedule)


class VesselView(views.MethodView):
    def get(self):
        vessels = Vessel.query.all()
        vessel_choice = request.args.get('vs')
        selection = vessel_choice if vessel_choice else vessels[0].v_id
        schedule = VesselSchedule.query.filter(VesselSchedule.vessel_ref == selection)
        position = VesselPosition.query.filter(VesselPosition.vessel_ref == selection)
        movement = VesselMovement.query.filter(VesselMovement.vessel_ref == selection)
        return render_template('vessel.html', \
            vessels=vessels, \
            schedule=schedule, \
            position=position, \
            movement=movement)
