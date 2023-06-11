from flask import Flask,render_template,request,jsonify
from chat import get_response
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

def isBlank (myString):
    return not (myString and myString.strip())

@app.get("/")
def home():
    return render_template("base.html")

@app.post("/predict")
def postBotResponse():
    query = request.get_json().get("message")
    print("Query :: " + query)
    if isBlank(query):
        response = "Please Enter a valid Query!!"
    else:
        response = get_response(query)
    
    print("Respnse :: " + response)
    message = {"answer":response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True,port=5001)