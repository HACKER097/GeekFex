from API import get_prediction
from flask import Flask, request, render_template, jsonify

MODEL_PATH = "model.h5"

app = Flask(__name__)

@app.route("/checkurl", methods=["GET"])
def checkurl():
    url = request.args.get("url") 
    prediction = get_prediction(url,MODEL_PATH)

    if prediction<=50:
        staus = "safe"
    if prediction>50 and prediction<75:
        staus = "moderate"
    else:
        staus = "severe"

    return prediction

if __name__=="__main__":
    app.run()
