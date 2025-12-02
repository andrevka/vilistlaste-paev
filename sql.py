import sqlite3

from flask import Blueprint, render_template, request

from models import create_sqlite_connection

conn = create_sqlite_connection()

bp = Blueprint("sql", __name__)

@bp.route("/sql-practice", methods=["GET", "POST"])
def exerciseSql():
    if request.method == "GET":
        return render_template("instructions/pages/sql-practice-page.html")
    
    sql = request.form.get("sql")
    
    print("Starting to execute sql: " + sql)
    
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        
        conn.commit()
        
        results = cursor.fetchall()
        headers=[col[0] for col in cursor.description] if cursor.description else []
        
        return render_template("instructions/pages/sql-practice-page.html", results=results, headers=headers)
    except Exception as e:
        return render_template("instructions/pages/sql-practice-page.html", error=e)