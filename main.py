from flask import Flask, render_template, request
import pickle
import numpy as np
import jwt
import time

model = pickle.load(open('data_p.pickle', 'rb'))

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def index():
    data1 = request.form['high']
    data2 = request.form['low']
    data3 = request.form['close']
    data4 = request.form['volume']
    arr = ([[data1,data2,data3,data4]])
    pred = model.predict(arr)
    return render_template('after.html', data=pred)

# @app.route('/dashboard')
# def dashboard():
#     METABASE_SITE_URL = "http://localhost:3000"
#     METABASE_SECRET_KEY = "294f31a32370af3cd396006e512654728896544468d687bef7dec42800cacf16"

#     payload = {
#             "resource": {"dashboard": 2},
#             "params": {},
#             "exp": round(time.time()) + (60 * 10) # 10 minute expiration
#     }
#     token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

#     iframeUrl = METABASE_SITE_URL + "/embed/dashboard/" + token + "#bordered=true&titled=true"
#     return render_template('dashboard.html', iframeUrl = iframeUrl)

if __name__ == "__main__":
    app.run(debug=True)