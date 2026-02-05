from flask import Flask, request, jsonify
import time
import logging
import requests

SERVICE_NAME = "service-b"
SERVICE_A_BASE = "http://127.0.0.1:8080"
TIMEOUT_SECONDS = 0.5  # required: must use a timeout

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

@app.get("/call-echo")
def call_echo():
    msg = request.args.get("msg", "")
    url = f"{SERVICE_A_BASE}/echo"

    try:
        r = requests.get(url, params={"msg": msg}, timeout=TIMEOUT_SECONDS)
        r.raise_for_status()
        return jsonify(
            serviceB="ok",
            serviceA=r.json()
        ), 200

    except requests.exceptions.Timeout:
        logger.error("service=%s error=timeout calling=%s timeout_s=%.2f",
                     SERVICE_NAME, url, TIMEOUT_SECONDS)
        return jsonify(error="Service A timeout"), 503

    except requests.exceptions.ConnectionError:
        logger.error("service=%s error=service_a_down calling=%s", SERVICE_NAME, url)
        return jsonify(error="Service A unavailable"), 503

    except requests.exceptions.RequestException as e:
        logger.error("service=%s error=upstream_error calling=%s details=%s",
                     SERVICE_NAME, url, str(e))
        return jsonify(error="Service A error"), 503

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081)


