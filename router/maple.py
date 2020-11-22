from server.server import app
from service.maple_service import get_page_bulletin
from flask import jsonify

@app.route("/maple")
def maple():
    return jsonify(get_page_bulletin())

def init_maple_api():
    app.run()