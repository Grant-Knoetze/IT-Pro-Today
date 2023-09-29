from flask import Flask, jsonify
import random
import string

app = Flask(__name__)

# Function to generate a random username
def generate_username():
    username = ''.join(random.choice(string.ascii_letters) for _ in range(6))
    return username

# Function to generate a random password
def generate_password():
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    return password

# API route to generate login details
@app.route('/generate-login-details', methods=['GET'])
def generate_login_details():
    username = generate_username()
    password = generate_password()
    login_details = {
        'username': username,
        'password': password
    }
    return jsonify(login_details)

if __name__ == '__main__':
    app.run(debug=True)
