from flask import render_template
from app import create_app

app = create_app()
# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template("home/404.html"), 404
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)