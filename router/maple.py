from server.server import app
from service.maple_service import get_realtime_bulletin, get_init_bulletin, init_redis_bulletin
from flask import jsonify, request

@app.route("/maple/realtime_bulletin")
def realtime_bulletin():
    return jsonify(get_realtime_bulletin())

@app.route("/maple/init_bulletin")
def init_bulletin():
    date = request.values.get("date")
    return jsonify(get_init_bulletin(date))

@app.route("/test")
def test():
    init_redis_bulletin()
    return jsonify("test")

def init_maple_api():
    app.run()

def init_redis_data():
    init_redis_bulletin()
