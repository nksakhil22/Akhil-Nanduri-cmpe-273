from flask import Flask, request, jsonify
import time
import logging

SERVICE_NAME = "service-a"

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger(SERVICE_NAME)

@app.before_request
def start_timer():
    request._start_time = time.perf_counter()

@app.after_request
def log_request(response):
    latency_ms = (time.perf_counter() - request._start_time) * 1000
    logger.info(
        "service=%s endpoint=%s status=%s latency_ms=%.2f",
        SERVICE_NAME, request.path, response.status_code, latency_ms
    )
    return response

@app.get("/health")
def health():
    return jsonify(status="ok"), 200

@app.get("/echo")
def echo():
    msg = request.args.get("msg", "")
    return jsonify(echo=msg), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)

