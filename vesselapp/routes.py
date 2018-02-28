from flask import Blueprint
import vesselapp.views as Views

site = Blueprint(
    name='site',
    import_name=__name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/site',
    url_prefix=None,
)

site.add_url_rule('/', view_func=Views.ScheduleView.as_view('schedule'))
site.add_url_rule('/vessel', view_func=Views.VesselView.as_view('vessel'))
