import logging
from flask import Flask, send_from_directory

from blueprints.main.views import main_blueprint
from blueprints.loader.views import loader_blueprint

app = Flask(__name__)

logging.basicConfig(level=logging.INFO) #filename='basic.log',


app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run()

