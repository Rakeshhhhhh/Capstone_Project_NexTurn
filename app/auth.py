from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    # Add secure authentication logic here
    return username == "admin" and password == "secret"