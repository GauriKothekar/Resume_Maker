
from flask import Flask , render_template , request , redirect,url_for , session , send_file , Response

from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash
import pdfkit
import os


app = Flask(__name__)
app.secret_key = 'mysecretgk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://hr:hr@127.0.0.1/xe'
db = SQLAlchemy(app)


@app.route('/')
def home():
    if 'name' in session:
        return render_template("resume_template")
    else:
        return render_template("index.html")


@app.route('/resume_1')
def resume_1():
    return render_template("resume_1.html")

@app.route('/resume_2')
def resume_2():
    return render_template("resume_2.html")

@app.route('/resume_template')
def resume_template():
    if 'name' in session:
        return render_template("resume_template")
    else:
        return render_template("index.html")

   # return render_template("resume_template.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']


        user = Regist.query.filter_by(name=name).first()

        if user:
            return render_template('resume_template.html')
             # Redirect to the user's profile page
        else:
            error = 'Invalid username or password'
            return render_template('login.html')



    return render_template('login.html')

class Regist(db.Model):
    name=db.Column(db.String(20))
    mob = db.Column(db.Integer())
    course = db.Column(db.String(20))
    year = db.Column(db.String(10))
    email = db.Column(db.String(20))
    password = db.Column(db.String(20) , primary_key=True)


@app.route('/register',methods =['GET','POST'])
def register():
    if request.method == 'POST':
        'add entry to DB'
        name = request.form.get('name')
        mob=request.form.get('mob')
        course=request.form.get('course')
        year = request.form.get('year')
        email = request.form.get('email')
        password = request.form.get('password')


        insert = Regist(name=name , mob=mob,course=course,year=year,email=email,password=password)
        db.session.add(insert)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template("register.html")


# class YourTable(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     email = db.Column(db.String(50))
#     # Define other columns of the table
#
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         # Retrieve form data
#         name = request.form.get('name')
#         email = request.form.get('email')
#         # Retrieve other form fields
#
#         # Create a new instance of the model
#         new_entry = YourTable(name=name, email=email)
#         # Set values for other fields
#
#         # Add and commit the new entry to the database
#         db.session.add(new_entry)
#         db.session.commit()
#
#     return render_template("register.html")

# @app.route('/download')
# def download_file():
#     filename = 'path/to/your/out.pdf'
#     return send_file(filename, attachment_filename='downloaded_file.pdf', as_attachment=True)


@app.route('/logout')
def logout():
    session.pop('name', None)
    return redirect(url_for('/'))


# class Data(db.Model):
#     name=db.Column(db.String(20))
#     phnum = db.Column(db.Integer())
#     ucareerob = db.Column(db.String(20))
#     collage = db.Column(db.String(10))
#     achivement = db.Column(db.String(20))
#     dob = db.Column(db.DateTime(20))
#     city = db.Column(db.String(10))
#     uaboutself= db.Column(db.String(20))
#     month = db.Column(db.String(20))
#     skills = db.Column(db.String(10))
#     email = db.Column(db.String(20), primary_key=True)
#     state = db.Column(db.String(20))
#     course = db.Column(db.String(10))
#     year = db.Column(db.String(20))
#     fname = db.Column(db.String(20))
#     mname = db.Column(db.String(10))
#     paddress = db.Column(db.String(20))







if(__name__ == "__main__"):
    with app.app_context():
        db.create_all()
        app.run(debug=True)