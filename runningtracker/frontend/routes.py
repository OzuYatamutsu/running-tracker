from flask import Blueprint, render_template
from test.mock.mock_template_data import MOCK_TEMPLATED_HISTORICAL_DATA


frontend = Blueprint(
    'frontend', __name__,
    template_folder='templates',
    static_folder='static'
)


@frontend.route('/')
def index():
    return render_template(
        "index.html",
        **MOCK_TEMPLATED_HISTORICAL_DATA
    )
