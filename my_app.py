from flask import Flask, jsonify

demoapp = Flask(__name__)

@demoapp.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello, World!', 'status': 'success'}), 200

if __name__ == '__main__':
    demoapp.run(debug=True)
