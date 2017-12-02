from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():

    li1=['RAMA','1']
    li2=['Name','id']
    return render_template('index.html',li=li1)

@app.route('/pending/<userid>')
def pending(userid):
    li1 = ['RAMA', [['Rama Ganapathy', 'Madurai', 'rama@gmail.com', '1234 5678 9101', 'Success', 'Success'],
                    ['Rama Ganapathy', 'Madurai', 'rama@gmail.com', '1234 5678 9102', 'Rejected', 'Rejected'],
                    ['name', 'city', 'email', 'aadhaar', 'deepAuth status', 'gov status']]]
    return render_template('pending.html',li=li1)
if __name__ == '__main__':
    app.run(debug=True)
