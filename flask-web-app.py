from flask import Flask
from flask import request
from flask import render_template
from mapquestBackend import calculateDirection

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        orig = request.form['start']
        dest = request.form['dest']

        tripDuration, totalKm, directionList, json_status = calculateDirection(orig, dest)
        if json_status == 0:
            return render_template("index.html", tripDuration=tripDuration, totalKm=totalKm, directionList=directionList, orig=orig, dest=dest, request=request)
        elif json_status == 402:
            message = f"Status Code: {json_status}; Invalid user inputs for one or both locations."
            return render_template("baseError.html", message=message, jsonStatus=json_status)
        elif json_status == 611:
            message = f"Status Code: {json_status}; Missing an entry for one or both locations."
            return render_template("baseError.html", message=message, jsonStatus=json_status)
        else:
            message = f"For Status Code: {json_status}; Refer to: https://developer.mapquest.com/documentation/directions-api/status-codes"
            return render_template("baseError.html", message=message, jsonStatus=json_status)
      
    else:
        return render_template("index.html")



if __name__ == "__main__":
    app.run()
