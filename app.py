from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/test", methods=["GET"])
def test():
    x_forwarded_for = request.headers.get("X-Forwarded-For", "Not Found")
    remote_addr = request.remote_addr
    return jsonify({
        "x-forwarded-for": x_forwarded_for,
        "remote-addr": remote_addr
    })

@app.route("/getheader", methods=["GET"])
def getheader():
    headers = dict(request.headers)
    return jsonify(headers)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
