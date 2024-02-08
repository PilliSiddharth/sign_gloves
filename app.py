from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive_message', methods=['POST'])
def receive_message():
    if request.method == 'POST':
        received_message = request.json  # Assuming JSON data is being sent
        print("Message received:", received_message)
        return jsonify({'message': 'Message received', 'data': received_message}), 200
    else:
        return 'Only POST requests are allowed\n'

if __name__ == '__main__':
    app.run(debug=True)
