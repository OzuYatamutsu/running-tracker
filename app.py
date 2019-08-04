from runningtracker.api.routes import api
from runningtracker.frontend.routes import frontend
from flask import Flask, redirect

# Init app and register child blueprints
app = Flask(__name__, static_folder=None)
app.register_blueprint(api)
app.register_blueprint(frontend)


@app.route('/')
def redirect_index_to_frontend():
    return redirect('frontend.index')
