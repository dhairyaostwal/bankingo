from flask import Flask, render_template, request
import pickle

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

        # converting string to float values
        for i in range(len(userInput)):
            userInput[i] = float(userInput[i])
        print("User input: ", userInput)

        # testing our pickle file
        with open('pickleOutput2', 'rb') as f:
            mp = pickle.load(f)
            
        pickle_test = mp.predict([userInput])
        print("Predicted Output: ", pickle_test)

        if pickle_test[0]==1:
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

if __name__ == '__main__':
    app.debug = True
    app.run()