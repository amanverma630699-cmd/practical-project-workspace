import numpy as np
import pandas as pd

from flask import Flask, render_template, request
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)


df=pd.read_csv("C:\\Users\\amanv\\OneDrive\\Desktop\\ML_pratice\\Machine Learning project\\Project_3\\web\\insurance.csv")
df["sex"] = df["sex"].map({
    "male": 0,
    "female": 1
})

df["smoker"] = df["smoker"].map({
    "yes": 0,
    "no": 1
})

df["region"] = df["region"].map({   
    "southeast": 0,
    "southwest": 1,
    "northeast": 2,
    "northwest": 3
})
X = df[
    ["age", "sex", "bmi", "children", "smoker", "region"]
].values

y = df["charges"].values
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=0
)
lr = LinearRegression()
lr.fit(X_train, y_train)
r2_score = lr.score(X_test, y_test)     
@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        age = float(request.form["age"])
        sex = int(request.form["sex"])
        bmi = float(request.form["bmi"])
        children = int(request.form["children"])
        smoker = int(request.form["smoker"])
        region = int(request.form["region"])

        input_data = np.array([
            [age, sex, bmi, children, smoker, region]
        ])

        prediction = lr.predict(input_data)[0]

    return render_template(
        "index.html",
        prediction=prediction,
        r2_score=r2_score
    )


if __name__ == "__main__":
    app.run(debug=True)