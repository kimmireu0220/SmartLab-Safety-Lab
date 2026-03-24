import os

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# 실험실 구역별 초기 상태 데이터
lab_status = {
    "zone_1": {"status": "safe", "message": "정상 - 흄후드 가동 중", "time": "-"},
    "zone_2": {"status": "safe", "message": "정상 - 고온 가열기 대기", "time": "-"},
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/status", methods=["GET"])
def get_status():
    return jsonify(lab_status)


@app.route("/api/update", methods=["POST"])
def update_status():
    data = request.json
    zone = data.get("zone")
    status = data.get("status")
    message = data.get("message")
    time = data.get("time")

    if zone in lab_status:
        lab_status[zone] = {"status": status, "message": message, "time": time}
        return jsonify({"result": "success"})
    return jsonify({"result": "fail"}), 400


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
