from flask import Flask, render_template, request
import pickle
import numpy as np

model=pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('signIn.html')


@app.route('/predict', methods=['POST'])
def predict():
#    print(request.form)
    int_features = [float(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict(final)
#    output='{0:.{1}f}'.format(prediction[0][1], 2)
    return render_template('result_html.html', pred="{}".format(prediction))

@app.route('/home')
def homepage():
    return render_template('crophtml.html')

@app.route('/contact')
def contactus():
    return render_template('ContactUs.html')


@app.route('/about')
def aboutus():
    return render_template('AboutUs.html')
    
if __name__ == '__main__':
    app.run(debug=True)
