from flask import Flask, request, jsonify

app = Flask(__name__)

data_list = []


@app.route('/')
def hello():
    return "Hello, World!"


@app.route('/get_example', methods=['GET'])
def get_example():
    return jsonify({"message": "This is a GET request example."})


@app.route('/post_example', methods=['POST'])
def post_example():
    data = request.get_json()
    data_list.append(data)
    return jsonify({"message": "Data stored successfully!"})


@app.route('/put_example/<int:index>', methods=['PUT'])
def put_example(index):
    if 0 <= index < len(data_list):
        new_data = request.get_json()
        data_list[index] = new_data
        return jsonify({"message": f"Data at index {index} updated successfully!"})
    else:
        return jsonify({"error": "Index out of range"}), 404


@app.route('/delete_example/<int:index>', methods=['DELETE'])
def delete_example(index):
    if 0 <= index < len(data_list):
        deleted_data = data_list.pop(index)
        return jsonify({"message": f"Data at index {index} deleted successfully!", "deleted_data": deleted_data})
    else:
        return jsonify({"error": "Index out of range"}), 404


@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify({"data": data_list})


if __name__ == '__main__':
    app.run(debug=True)
