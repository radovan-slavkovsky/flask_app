from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/docker')
def docker():
    return render_template('docker.html')

#if __name__ == '__main__':
#    app.run(debug=True)

if __name__ == "__main__":
   app.run(host="0.0.0.0", debug=True, port=int(os.environ.get("PORT", 5000)))
