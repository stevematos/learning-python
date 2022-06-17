from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        data = {"data": "Hello World"}
        return jsonify(data)
    elif request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            json = request.json
            data = {"data": f"Hello World {json.get('name', '')} !"}
            return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

