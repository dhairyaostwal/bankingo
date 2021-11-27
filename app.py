from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)

userInput = []


@app.route("/", methods=["GET", "POST"])
def hello():

    userInput.clear()
    if request.method == "POST":
        variance = request.form.get("variance")
        skewness = request.form.get("skewness")
        curtosis = request.form.get("curtosis")
        entropy = request.form.get("entropy")

        userInput.append(variance)
        userInput.append(skewness)
        userInput.append(curtosis)
        userInput.append(entropy)
        print(userInput)

        count = 0
        for i in userInput:
            if int(i) % 2 == 0:
                count += 1

        if count == 4:
            return render_template("trueBundle.html")
        else:
            return render_template("falseBundle.html")

    return render_template("index.html")


@app.route("/verified/")
def verified():
    return render_template("trueBundle.html")


@app.route("/not-verified/")
def notVerified():
    return render_template("falseBundle.html")


if __name__ == "__main__":
    app.run()
