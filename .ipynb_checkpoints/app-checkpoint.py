#importing libraries
import pickle
from flask import Flask, render_template, request


#creating instance of the class
app = Flask(__name__,template_folder="templates")

# Load Model
clf = pickle.load(open('models/MNB_model.sav', 'rb'))

with open('Vectors/vectorizer.pkl', 'rb') as handle:
    tf_vec = pickle.load(handle)


#to tell flask what url shoud trigger the function index()
@app.route('/')
def home():
    return render_template('Home.html')



# Route 'predict' accepts POST request
@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = tf_vec.transform(data).reshape(1, -1)
        my_prediction = clf.predict(vect)
    return render_template('result.html', prediction = my_prediction)
    
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

    
    
    
    
    
    
    
    


