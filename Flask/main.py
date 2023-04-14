from website import create_app
from flask import Flask, request
from flask_restful import Api, Resource
from website.frontend import bp

app = create_app()


if __name__ == "__main__":
    app.register_blueprint(bp)
    app.run(host = "localhost", port = 8080, debug=True)
