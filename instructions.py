from flask import Blueprint, render_template

bp = Blueprint('instructions', __name__, template_folder='templates/instructions', url_prefix="/instructions")
    
@bp.route('/<name>')
def instructions(name):
    return render_template(f"{name}.html")

@bp.route('/my-page-template')
def my_page_template():
    return render_template("pages/my-page-template.html")


@bp.route('/my-page-with-javascript')
def my_page_with_js():
    return render_template("pages/my-page-with-javascript.html")
