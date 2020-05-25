from flask import Flask, render_template, url_for, request, Response, redirect
import livelocation

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index3.html')

@app.route('/signin')
def sign_in():
    return render_template('single.html')

@app.route('/my_map', methods=['POST'])
def my_map():
    name = request.form['name']
    email = request.form['email']
    number = request.form['number']
    location = request.form['location']

    livelocation.create_map(name, location)
    
    return render_template('my_map.html')

if __name__ == '__main__':
    app.run(debug = True)