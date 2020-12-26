from server.server import app
from service.daily_sentence import get_shanbay_daily_sentence

@app.route("/shanbay/daily/sentence")
def shanbay_daily_sentence():
    get_shanbay_daily_sentence()
    return "done"

def init_english_api():
    app.run()