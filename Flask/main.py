from flask import Flask
from flask_restful import Api, Resource
from website.main_API import *
import pymysql
from flask_sqlalchemy import SQLAlchemy
from google.cloud.sql.connector import Connector, IPTypes
from website.models.sql_table import db, Packages_table, add_package
from website.frontend import bp
import requests

def getconn():
    with Connector() as connector:
        conn = connector.connect(
            ## get from sql into doc, need to configure to env file
        )
        return conn



def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(PackagesList,"/packages")
    api.add_resource(RegistryReset,"/reset")
    api.add_resource(Package,"/package/<string:id>")
    api.add_resource(PackageCreate,"/package")
    api.add_resource(PackageRate,"/package/<string:id>/rate")
    api.add_resource(PackageHistory,"/package/byName/<string:name>")
    api.add_resource(PackageByRegExGet,"/package/byRegex/<string:rate>")
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://461-user:461-test@/Module-Registry?unix_socket=/cloudsql/module-registry-ece461:us-central1:ece461-module-registry"

    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        "creator": getconn
    }
    db.init_app(app)
    return app

app = create_app()

@app.get("/")
def hello():
    """Return a friendly HTTP greeting."""
    who = request.args.get("who", default="World")
    return f"Hello {who}!\n"

if __name__ == "__main__":
    app.register_blueprint(bp)
    app.run(host = "localhost", port = 8080, debug=True)

# from flask import Flask, request

# app = Flask(__name__)






# if __name__ == "__main__":
#     # Development only: run "python main.py" and open http://localhost:8080
#     # When deploying to Cloud Run, a production-grade WSGI HTTP server,
#     # such as Gunicorn, will serve the app.
#     app.run(host="localhost", port=8080, debug=True)
