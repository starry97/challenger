from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['POST'])
def result():
    """
    Please call url "http://localhost/8000"
    """
    username = request.form['username']
    input_address = request.form['input_address']
    return 'Received !' # response to your request.

if __name__ == "__main__":
     app.run(host='0.0.0.0', port=8000)