from server.server import app

@app.route("/health_check")
def health():
    return "success"

def init_api():
    app.run()