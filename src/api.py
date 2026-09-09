from flask import Flask, jsonify




#Flask Routing
#@app.route('/hello/<username>')
#def show_user_message(username):
#    return 'Hello %s' % username

#but we might only want hello

#in windows you gotta use curl.exe instead of just curl like in linux :P
#curl.exe http://127.0.0.1:5000/hello




app = Flask(__name__) #creates the flask application thingy

@app.route('/hello', methods=['GET']) #ifsomeone sends get request to the /hello execute the function below
def hello():
    return jsonify({"message": "Hello"})


#running program
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)