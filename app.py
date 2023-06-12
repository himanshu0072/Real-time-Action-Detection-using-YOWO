from flask import Flask, flash, render_template, request, redirect, url_for, session, url_for
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from project_orm import User
from project_orm import Support
from utils import *
import os
from werkzeug.utils import secure_filename
import pickle

app = Flask(__name__)
app.secret_key = "Himashu dev"
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
sess = Session()

app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 30 # 2MB
app.config['UPLOAD_EXTENSIONS'] = ['.mp4','.mov']
app.config['UPLOAD_PATH'] = 'uploads'

def load_action_list():
    with open('static/actions.txt', 'rb') as f:
        return str(pickle.load(f))


@app.route('/upload',methods=['POST'])
def upload_file(): 
    uploaded_file = request.files.get('file')     
                      # we are getting file from FORM
    filename = secure_filename(uploaded_file.filename)              # clean the filename n store it in variable
    if filename != '':                                              # if the filename is not empty then
        file_ext = os.path.splitext(filename)[1]                    # get the extension from filename abc.png ['abc','.png']
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:         # if extension is not valid
            flash('invalid extension','danger')
            return redirect("dashboard")                          # then stop execution else
        path = os.path.join('static',app.config['UPLOAD_PATH'],filename)     # make os compatible path string
        uploaded_file.save(path) 
        session['url'] = path    
    flash('Video uploaded now Click on Start Detection','success')                               # then save the file with original name 
    return redirect(url_for('dashboard'))    

@app.route('/')
def index():
    return render_template('index.html', title='| Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = sess.query(User).filter_by(email=email).first()
        if user:
            if password == user.password:
                session['logged_in'] = True
                session['user_name'] = user.name
                flash('Login successful!', 'success')
                # Perform the necessary actions after successful login
                return redirect('/dashboard') 
            else:
                flash('Invalid email or password', 'danger')
        else:
            flash('Incorrect email or password', 'danger')
    return render_template('login.html', title='| Login now')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        gender = request.form.get('gender')
        if name and len(name) >= 3:
            if email and '@' in email and validate_email(email):
                if password and len(password) >= 6:
                    try: 
                        newuser = User(name = name, email = email, password = password, gender = gender)
                        sess.add(newuser)
                        sess.commit()
                        flash('registration successful', 'success')
                        return redirect('/login')
                    except:
                        flash('Account already exists', 'danger')
                else:
                    flash('Password length should be minimum 6 character', 'danger')
            else:
                flash('Email is invalid', 'danger')
        else:
            flash('Enter a Valid Name', 'danger')

    return render_template('register.html', title = '| register now')

@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    return render_template('forgot.html', title = '| forgot password')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/whyus')
def whyus():
    return render_template('whyus.html', title = '| Why us🤔')


@app.route('/support', methods=['GET', 'POST'])
def support():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        query = request.form.get('query')
        if name and len(name) >= 3:
            if email and '@' in email and validate_email(email):
                if phone and len(phone) == 10 :
                    try: 
                        newquery = Support(name = name, email = email, phone = phone, query = query)
                        sess.add(newquery)
                        sess.commit()
                        flash('We got your Query ✅. Our team will contact you soon', 'success')
                        return redirect('/support')
                    except:
                        flash('Some error occured', 'danger')
                else:
                    flash('Invalid Phone Number ! Enter a 10 digit valid number', 'danger')
            else:
                flash('Email is invalid', 'danger')
        else:
            flash('Enter a Valid Name', 'danger')
    return render_template('support.html', title = "| Support Desk")


@app.route('/dashboard')
def dashboard():
    if 'logged_in' in session:
        user_name = session.get('user_name')
        return render_template('dashboard.html', title = "| Dashboard", user_name = user_name)
    else:
        flash('Login Required', 'danger')
        return redirect('/login')



@app.route('/result/camera')
def result_camera():
    import subprocess
    subprocess.call('python test_video_ava.py --cfg cfg/ava.yaml'.split(), shell=True)
    return redirect('/result')

@app.route('/result/video')
def result_video():
    import subprocess
    if 'url' in session:
        # flash('Detection Started Please wait.....', 'success')
        cmd =f"python test_video_ava.py --cfg cfg/ava.yaml --url {session['url']}".split()
        print(cmd)
        subprocess.call(cmd, shell=True) 
        return redirect('/result') 
    else:
        return redirect('/dashboard')

@app.route('/result')
def result():
    if 'logged_in' in session:
        actions = load_action_list()
        file = '/static/actions.txt'
        return render_template('result.html', title = '| result', actions=set(actions.split('|')), file=file)
    else:
        flash('Login Required', 'danger')
        return redirect('/login')

# this section is for admin login and managing data

@app.route('/adminlogin', methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        emailID = request.form.get('email')
        passwordID = request.form.get('password')
        print(emailID, passwordID)
        name = "Himanshu Prajapati"
        if emailID == "himanshu@gmail.com" and passwordID == "123456":
            session['logged_in'] = True
            session['user_name'] = name
            flash('Login successful!', 'success')
            # Perform the necessary actions after successful login
            return redirect('/adminDashboard')        
        else:
            flash('Incorrect email or password', 'danger')
    return render_template('admin.html', title="| login now")

@app.route('/adminDashboard')
def adminDashboard():
    if 'logged_in' in session:
        user_name = session.get('user_name')
        return render_template('adminDashboard.html', title = "| Dashboard", user_name = user_name)
    else:
        flash('Admin Login Required', 'danger')
        return redirect('/adminlogin')

@app.route('/adminlogout')
def adminlogout():
    session.clear()
    return redirect('/adminlogin')

@app.route('/manageUsers')
def manageUsers():
    if 'logged_in' in session:
        users = sess.query(User).all()
    else:
        flash('Admin Login Required', 'danger')
        return redirect('/adminlogin')
    return render_template("manageUsers.html", title = "| all users", users = users)

@app.route('/manageQueries')
def manageQueries():
    if 'logged_in' in session:
        users = sess.query(Support).all()
    else:
        flash('Admin Login Required', 'danger')
        return redirect('/adminlogin')
    return render_template("manageQueries.html", title = "| all users", users = users)

@app.route('/lastDetectedActions')
def lastDetectedActions():
    if 'logged_in' in session:
        actions = load_action_list()
        file = '/static/actions.txt'
    else:
        flash('Admin Login Required', 'danger')
        return redirect('/adminlogin')
    return render_template("manageLastDetection.html", title = "| Last Detection", actions=set(actions.split('|')), file=file)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
