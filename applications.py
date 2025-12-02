from flask import Blueprint, render_template

bp = Blueprint('applications', __name__, template_folder='templates/application', url_prefix="/application")
    
@bp.route('/<name>')
def application(name):
    return render_template(f"{name}.html")