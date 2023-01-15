#flask boilerpalte
from flask import Flask, request, jsonify, render_template, url_for ,redirect, session, flash, send_from_directory, send_file

from functools import wraps
#sql
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
#migration

from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
# from flask_admin import Admin, AdminIndexView
# from flask_admin.contrib.sqla import ModelView
import pyimgur

import datetime
import os
import base64


import xlrd
 


app = Flask(__name__)
app.secret_key = 'asdasdasdasdasdasdasaasdasdasdasd12312312daveqvq34c'


UPLOAD_FOLDER = 'static/img/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CLIENT_ID = "2d3158d36137249"
im = pyimgur.Imgur(CLIENT_ID)

ENV = 'prod'

if ENV == 'dev' :
    app.debug = True
    PROPPLER_PATH = r'C:\Program Files\poppler-0.68.0\bin'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
    app.config['SECRET_KEY'] = 'asdasdasdasdasdasdasdaveqvq34c'
    URL = 'http://192.168.29.166:5000/'
      
else:
    URL = 'https://better-tomorrow-intl.herokuapp.com/'
    app.debug = False
    PROPPLER_PATH = r'vendor\poppler\bin'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SECRET_KEY'] = SECRET_KEY
    
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.user_type != 'admin':
            return redirect(url_for('forbidden'))
        return f(*args, **kwargs)
    return decorated_function


def teacher_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.user_type != 'teacher':
            return redirect(url_for('forbidden'))
        return f(*args, **kwargs)
    return decorated_function


# class MyAdminIndexView(AdminIndexView):
#     def is_accessible(self):
#         return current_user.is_authenticated and current_user.user_type == 'admin'

#     def inaccessible_callback(self, name, **kwargs):
#         if current_user.is_authenticated:
#             return redirect(url_for('forbidden'))
#         else:
#             return redirect(url_for('login'))

# admin = Admin(app, index_view=MyAdminIndexView())

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    phone = db.Column(db.String(80), unique=True)   
    name = db.Column(db.String(80))
    password = db.Column(db.String(512))
    user_type = db.Column(db.String(80))
    user_sub_type = db.Column(db.String(80))
    user_sub_id = db.Column(db.String(80))
    email_confirmation_code = db.Column(db.String, default=False)
    email_confirmed = db.Column(db.String, default=False)

    test_result = db.relationship('MockTestResults', backref='user')
    subscription = db.relationship('subscription', backref='user')
    classes = db.relationship('Classes', backref='user')


class Whatsapp(db.Model):
    __tablename__ = 'whatsapp'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    number = db.Column(db.String(80))
    message = db.Column(db.String(500))
    is_active = db.Column(db.String(80))


class subscription(db.Model):
    __tablename__ = 'subscription'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(500))
    price = db.Column(db.String(80))
    duration = db.Column(db.String(80))
    duration_type = db.Column(db.String(80))
    course_id = db.Column(db.String(80))
    is_active = db.Column(db.String(80))
    notes_access = db.Column(db.Boolean)
    mocktest_access = db.Column(db.Boolean)
    video_access = db.Column(db.Boolean)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Requets(db.Model):
    __tablename__ = 'requests'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    staus = db.Column(db.String(80))
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())



 


class Courses(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(80))
    course_description = db.Column(db.String(500))
    ###
    # course_language = db.Column(db.String(80))
    ###
    is_active = db.Column(db.Boolean)
    course_image = db.Column(db.String(80))
    course_price = db.Column(db.String(80))
    course_module = db.relationship('Modules', backref='course')
    course_class = db.relationship('Classes', backref='course')



class Classes(db.Model):
    __tablename__ = 'classes'
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(80))
    class_date = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    class_time = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    teacher_id = db.Column(db.Integer, db.ForeignKey('users.id'))

     

 
class Modules(db.Model):
    __tablename__ = 'modules'
    id = db.Column(db.Integer, primary_key=True)
    module_name = db.Column(db.String(80))
    module_description = db.Column(db.String(500))
    module_image = db.Column(db.String(80))
    
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    module_mocktest = db.relationship('MockTest', backref='module_mocktest')
    module_notes = db.relationship('Notes', backref='module_notes')
    module_videos = db.relationship('VideoRec', backref='module_videos')

class MockTest(db.Model):
    __tablename__ = 'mocktest'
    id = db.Column(db.Integer, primary_key=True)
    test_name = db.Column(db.String(80))
    test_description = db.Column(db.String(500))
    test_duration = db.Column(db.String(80))
    max_marks = db.Column(db.String(80))
    test_image = db.Column(db.String(80))
    test_price = db.Column(db.String(80))
    total_questions = db.Column(db.Integer)
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'))
    test_module = db.relationship('MockTestQuestion', backref='test')
    test_results = db.relationship('MockTestResults', backref='test')

class MockTestResults(db.Model):
    __tablename__ = 'mocktestresults'
    id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('mocktest.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    marks_obtained = db.Column(db.String(80))
    time_taken = db.Column(db.String(80))
    test_status = db.Column(db.String(80))
    test_taken_on = db.Column(db.String(80))
    test_attempt = db.relationship('MocktestAttempt', backref='test_attempt')

class MocktestAttempt(db.Model):
    __tablename__ = 'mocktestattempt'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(80))
    choosen_answer = db.Column(db.String(80))
    correct_answer = db.Column(db.String(80))

    test_id = db.Column(db.Integer, db.ForeignKey('mocktestresults.id'))


class MockTestQuestion(db.Model):
    __tablename__ = 'mocktestquestion'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(80))
    image_url = db.Column(db.String(80), nullable=True)
    explanation = db.Column(db.String(2500))

    mock_test_id = db.Column(db.Integer, db.ForeignKey('mocktest.id'))
    mocktestanswer = db.relationship('MockTestAnswer', backref='question', lazy=True)

class MockTestAnswer(db.Model):
    __tablename__ = 'mocktestanswer'
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(80))
    is_correct = db.Column(db.Boolean)
    question_id = db.Column(db.Integer, db.ForeignKey('mocktestquestion.id'))


class Notes(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    note_name = db.Column(db.String(80))
    note_description = db.Column(db.String(500))
    # note_image = db.Column(db.String(80))
    # note_filename = db.Column(db.String(80))
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'))
    note_images = db.relationship('NoteImages', backref='note')

class NoteImages(db.Model):
    __tablename__ = 'noteimages'
    id = db.Column(db.Integer, primary_key=True)
    note_id = db.Column(db.Integer, db.ForeignKey('notes.id'))
    image_url = db.Column(db.String(80))

class VideoRec(db.Model):
    __tablename__ = 'videorec'
    id = db.Column(db.Integer, primary_key=True)
    video_name = db.Column(db.String(80))
    video_description = db.Column(db.String(500))
    video_url = db.Column(db.String(80))
    video_date = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    video_price = db.Column(db.String(80))
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'))
    

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        user=current_user
    else:
        user=None
    courses = Courses.query.all()
    return render_template('main/index.html', user=user, courses=courses)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            user = User.query.filter_by(name=username).first()
            if user:
                print(user.password)
                if user.password == password:
                    if request.form.get('remember_me') == 'on':
                        print('remember me')
                        login_user(user, remember=True)
                    else:
                        print('not remember me')
                        login_user(user)
                    return redirect(url_for('index'))
                else:
                    flash('Invalid username or password')
                    return render_template('login.html')
            else:
                flash('User not found')
                return render_template('login.html')
        except Exception as e:
            print(e)
            flash('Error' + str(e) )
        return render_template('login.html')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index')) 

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        phone = request.form['phone']
        name = request.form['name']
        password = request.form['password']
        user_type = 'student'
        # user_sub_type = request.form['user_sub_type']
        # user_sub_id = request.form['user_sub_id']
        # email_confirmation_code = request.form['email_confirmation_code']
        # email_confirmed = request.form['email_confirmed']
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email address already exists')
            return render_template('register.html')
        new_user = User(email=email, phone=phone, name=name, password=password, user_type=user_type)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/about-us', methods=['GET', 'POST'])
def about_us():
    courses = Courses.query.all()
    return render_template('main/about-us.html', user=current_user, courses=courses)

@app.route('/contact-us', methods=['GET', 'POST'])

def contact_us():
    courses = Courses.query.all()
    return render_template('main/contact-us.html', user=current_user, courses=courses)

@app.route('/courses', methods=['GET', 'POST'])
def courses():
    courses = Courses.query.all()
    return render_template('main/courses.html', user=current_user, courses=courses)

@app.route('/courses/<param>', methods=['GET', 'POST'])
def courses_c(param):
    courses = Courses.query.all()
    course = Courses.query.get(1)
    modules = Modules.query.filter_by(course_id=course.id).all()
    status = 'apply'
    if current_user.is_authenticated:
        request = Requets.query.filter_by(user_id=current_user.id).all()
        for req in request:
            if req.staus == 'pending':
                status = 'pending'
                break
            elif req.staus == 'accepted':
                status = 'accepted'
                break
            else:
                status = 'apply'
    
    if param == 'haad':
        courses_name = 'HAAD'
        course_price = course.course_price
        couese_image = 'departments-2.jpg'
        courses_description = 'All healthcare professionals including doctors, technicians, dentists, pharmacists and traditional practitioners; especially outside the UAE can now apply online for a medical license to work in the UAE. Each type of professional can apply for the fully-online Examination & Evaluation System (EES) in their own country, thus reducing costs and time. Nurses too must obtain their license from HAAD depending on whether they are applying to be a registered nurse, registered midwife, nurse practitioner, mental health nurse, pediatric nurse, community nurse or assistant .'
    elif param == 'dha':
        courses_name = 'DHA'
        course_price = course.course_price
        couese_image = 'departments-2.jpg'
        courses_description = 'In Dubai, UAE, the DHA exam is a nationwide examination for healthcare professional licenses. This examination is administered by the Dubai Health Authority (DHA) who also manages the professional licensing of medical professionals and oversees the overall health system in Dubai. With a primary degree qualification and two years of clinical experience, you are eligible to enroll for the DHA exam. On passing the exam, you will become one among the medical industry that protects public health and improves the quality of life within the Emirate of Dubai.'
    elif param == 'PROMETRICS':
        courses_name = 'PROMETRICS'
        course_price = course.course_price
        couese_image = 'departments-2.jpg'
        courses_description = 'Prometric is a wholly owned subsidiary of Educational Testing Services (ETS) and a trusted provider of technology-based testing and assessment solutions. It is a testing and evaluation provider that operates test centers in more than 160 countries. For Foreign nurses who want to work in Saudi Arabia, Oman and Qatar must be eligible for the Prometric exam. In the Nurse Exam of Oman Prometric and Saudi, Qatar, candidates have two and a half hours to complete 70 and 100 questions in multiple choice format. This is a computer-based test and results are available immediately after the test.'
    return render_template('main/c-course-details.html',param=param, 
                                                        user=current_user, 
                                                        courses=courses, 
                                                        courses_name=courses_name, 
                                                        courses_description=courses_description,
                                                        course=course, 
                                                        course_price=course_price, 
                                                        couese_image=couese_image,
                                                        status=status,
                                                        modules=modules) 
    
@app.route('/courses/<int:id>', methods=['GET', 'POST'])
def course(id):
    courses = Courses.query.all()
    course = Courses.query.get(id)
    modules = Modules.query.filter_by(course_id=id)
    return render_template('main/course-detail.html', user=current_user, course=course, modules=modules, courses=courses)


















































def getCourses():
    subscriptions = subscription.query.filter_by(user_id=current_user.id).all()
    courses = []
    if not subscriptions:
        return Courses.query.all()
    for sub in subscriptions:
        if sub.is_active == '1':
            c = Courses.query.get(sub.course_id)
            if c not in courses:
                courses.append(c)
    return Courses.query.all()

def isSubActive(course_id):
    try:
        sub = subscription.query.filter_by(user_id=current_user.id, course_id=str(course_id)).first()
        if sub:
            if sub.is_active == '1':
                return True
        return False
    except:
        return False


@app.route('/student', methods=['GET', 'POST'])
@login_required
def student():
    return render_template('student/index.html', user=current_user, Nav_courses=getCourses(), isSubActive=isSubActive( getCourses()[0].id), users=User.query.all())
                




@app.route('/student/mocktests/modules/<int:id>', methods=['GET', 'POST'])
@login_required
def mocktests_mod(id):
    modules = Modules.query.filter_by(course_id=id).all()
    return render_template('student/mocktest-mod.html', user=current_user, Nav_courses=getCourses(), isSubActive=isSubActive( getCourses()[0].id), users=User.query.all()  , modules=modules)



@app.route('/student/mocktests/<int:id>', methods=['GET', 'POST'])
@login_required
def mocktests(id):
    module = Modules.query.get(id)
    mocktests = MockTest.query.filter_by(module_id=id).all()
    return render_template('student/mocktest.html', user=current_user, Nav_courses=getCourses(), isSubActive=isSubActive( getCourses()[0].id), users=User.query.all()  , module=module, mocktests=mocktests)


@app.route('/student/mocktests/<int:id>/brief', methods=['GET', 'POST'])
@login_required
def mocktests_brief(id):
    mocktest = MockTest.query.get(id)
    return render_template('student/mocktest/brief.html', user=current_user, Nav_courses=getCourses(), isSubActive=isSubActive( getCourses()[0].id), users=User.query.all()  , mocktest=mocktest)


@app.route('/student/mocktests/<int:id>/start', methods=['GET', 'POST'])
@login_required
def mocktests_start(id):
    Q = {'question': '', 'choices': [], 'answer': ''}
    questions = []
    mocktest = MockTest.query.get(id)
    mocktest_questions = MockTestQuestion.query.filter_by(mock_test_id=id).all()
    for question in mocktest_questions:
        Q['question'] = question.question
        mocktest_answers = MockTestAnswer.query.filter_by(question_id=question.id).all()
        Q['choices'] = [answer.answer for answer in mocktest_answers]
        Q['answer'] = [answer.answer for answer in mocktest_answers if answer.is_correct][0]

        questions.append(Q)
        Q = {'question': '', 'choices': [], 'answer': ''}

    print(questions)
        
            
    return render_template('student/mocktest/quiz.html', user=current_user, Nav_courses=getCourses(), isSubActive=isSubActive( getCourses()[0].id), users=User.query.all()  , mocktest=mocktest, questions=questions , URL=URL)


@app.route('/student/mocktests/<int:id>/sendResult', methods=['GET', 'POST'])
@login_required
def mocktests_result(id):
    mocktest = MockTest.query.get(id)
    questions = MockTestQuestion.query.filter_by(mock_test_id=id).all()
    if request.method == 'POST':
        print(request.json)
        print(request.json['user_id'])
        quiz_results = request.json
        results = MockTestResults(
                    user_id=current_user.id,
                    test_id=mocktest.id,
                    marks_obtained=quiz_results['score'],
                    test_taken_on=datetime.datetime.now(),
                    time_taken=quiz_results['time'],
                )
        db.session.add(results)
        db.session.commit()

        for question in quiz_results['questions']:
            attempt = MocktestAttempt(
                        test_id=results.id,
                        question=question['question'],
                        correct_answer=question['answer'],
                        choosen_answer=quiz_results['answers'][quiz_results['questions'].index(question)]

            )
            db.session.add(attempt)
            db.session.commit()
        return jsonify({'status': 'success', 'id': results.id})
    return jsonify({'status': 'error'})


@app.route('/student/mocktests/<int:id>/result', methods=['GET', 'POST'])
@login_required
def mocktests_result_view(id):
    results = MockTestResults.query.get(id)
    mocktest = MockTest.query.get(results.test_id)
    questions = MockTestQuestion.query.filter_by(mock_test_id=mocktest.id).all()
    answers = MockTestAnswer.query.all()
    attempts = MocktestAttempt.query.filter_by(test_id=results.id).all()
    return render_template('student/mocktest/results.html', user=current_user, Nav_courses=getCourses(), isSubActive=isSubActive( getCourses()[0].id), users=User.query.all()  , 
                                                mocktest=mocktest, results=results, 
                                                attempts=attempts, answers=answers, 
                                                questions=questions)


@app.route('/student/mocktests/<int:id>/attempts/view', methods=['GET', 'POST'])
@login_required
def mocktests_attempts_view(id):
    mocktest = MockTest.query.get(id)
    attempts = MockTestResults.query.filter_by(test_id=id).all()
    return render_template('student/quiz-attempts.html', user=current_user, Nav_courses=getCourses(), isSubActive=isSubActive( getCourses()[0].id), users=User.query.all()  , mocktest=mocktest, attempts=attempts)






@app.route('/student/video/modules/<int:id>', methods=['GET', 'POST'])
@login_required
def video_mod(id):
    modules = Modules.query.filter_by(course_id=id).all()
    return render_template('student/video-mod.html', user=current_user, Nav_courses=getCourses(), isSubActive=isSubActive( getCourses()[0].id), users=User.query.all()  , modules=modules)

@app.route('/student/video/<int:id>', methods=['GET', 'POST'])
@login_required
def video(id):
    module = Modules.query.get(id)
    videos = VideoRec.query.filter_by(module_id=id).all()
    return render_template('student/videos.html', user=current_user, Nav_courses=getCourses(), isSubActive=isSubActive( getCourses()[0].id), users=User.query.all()  , module=module, videos=videos)


@app.route('/student/notes/modules/<int:id>', methods=['GET', 'POST'])
@login_required
def notes_mod(id):
    modules = Modules.query.filter_by(course_id=id).all()
    return render_template('student/notes-mod.html', user=current_user, Nav_courses=getCourses(), isSubActive=isSubActive( getCourses()[0].id), users=User.query.all()  , modules=modules)

@app.route('/student/notes/<int:id>', methods=['GET', 'POST'])
@login_required
def notes(id):
    module = Modules.query.get(id)
    notes = Notes.query.filter_by(module_id=id).all()
    noteImages = NoteImages.query.all() 
    return render_template('student/notes.html', user=current_user, Nav_courses=getCourses(), isSubActive=isSubActive( getCourses()[0].id), users=User.query.all()  , module=module, notes=notes, noteImages=noteImages)

@app.route('/student/notes/<int:id>/view', methods=['GET', 'POST'])
@login_required
def notes_view(id):
    note = Notes.query.get(id)
    noteImages = NoteImages.query.filter_by(note_id=id).all()
    return render_template('student/note-view.html', user=current_user, Nav_courses=getCourses(), isSubActive=isSubActive( getCourses()[0].id), users=User.query.all()  , note=note, noteImages=noteImages)



# -----------------------------------------------------------Admin Routes------------------------------------------------------------




@app.route('/forbidden', methods=['GET', 'POST'])
def forbidden():
    return render_template('403.html')

@app.route('/admin/', methods=['GET', 'POST'])
@login_required
@admin_required
def admin():
    return render_template('admin/index.html')
 
@app.route('/admin/users', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_users():
    users = User.query.all()
    return render_template('admin/users.html', users=users)

@app.route('/admin/users/add', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_users_add():
    if request.method == 'POST':
        user = User(
            name=request.form['name'],
            email=request.form['email'],
            password=request.form['password'],
            user_type=request.form['role'],
            phone=request.form['phone'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('admin_users'))

@app.route('/admin/users/view/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_users_view(id):
    user = User.query.get(id)
    subscriptions = subscription.query.filter_by(user_id=id).all()
    def status(stat):
        if str(stat) == 'on':
            return 1
        else:
            return 0
    if request.method == 'POST':
        sub = subscription(user_id=id, 
                            name=request.form['name'],
                            description=request.form['description'],
                            price=request.form['price'],
                            course_id=request.form['course'],
                            duration=request.form['duration'],
                            duration_type=request.form['duration_type'],
                            notes_access=status(request.form.get('notes_access')),
                            video_access=status(request.form.get('video_access')),
                            mocktest_access=status(request.form.get('mocktest_access')),
                            is_active=status(request.form.get('is_active')))
        db.session.add(sub)
        db.session.commit()
        return redirect(url_for('admin_users_view', id=id))
    return render_template('admin/viewUser.html', user=user, subscriptions=subscriptions)

@app.route('/admin/users/delete/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_users_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('admin_users'))


@app.route('/admin/users/sub/delete/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_users_sub_delete(id):
    sub = subscription.query.get(id)
    db.session.delete(sub)
    db.session.commit()
    return redirect(url_for('admin_users_view', id=sub.user_id))

@app.route('/admin/users/sub/action/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_users_sub_action(id):
    sub = subscription.query.get(id)
    if sub.is_active == "1":
        sub.is_active = "0"
    else:
        sub.is_active = "1"
    db.session.commit()
    return redirect(url_for('admin_users_view', id=sub.user_id))

@app.route('/changeStatus/<int:id>/<parm>', methods=['GET', 'POST'])
@login_required
@admin_required
def changeStatus(id, parm):
    sub = subscription.query.get(id)
    course = Courses.query.get(id)
    if parm == "notes_access":
        if sub.notes_access:
            sub.notes_access = False
        else:
            sub.notes_access = True
    elif parm == "video_access":
        if sub.video_access:
            sub.video_access = False
        else:
            sub.video_access = True
    elif parm == "mocktest_access":
        if sub.mocktest_access:
            sub.mocktest_access = False
        else:
            sub.mocktest_access = True
    elif parm == "course":
        if course.is_active:
            course.is_active = False
        else:
            course.is_active = True

    db.session.commit()
    return redirect(url_for('admin_users_view', id=sub.user_id))





@app.route('/admin/users/requests', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_users_requests():
    requests = Requets.query.all()
    users = User.query.all()
    courses = Courses.query.all()
    return render_template('admin/viewRequests.html', requests=requests, users=users, courses=courses)

@app.route('/admin/users/requests/add/<int:user_id>/<int:course_id>', methods=['GET', 'POST'])
@login_required
def users_requests_add(user_id, course_id):
    user = User.query.get(user_id)
    course = Courses.query.get(course_id)
    req = Requets(user_id=user_id, course_id=course_id, staus="pending")
    db.session.add(req)
    db.session.commit()
    return redirect(url_for('courses'))

    


@app.route('/admin/users/sub/add/<int:id>/<int:req_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_users_sub_add(id,req_id):
    user = User.query.get(id)
    courses = Courses.query.all()
    requests = Requets.query.get(req_id)
    def status(stat):
        if str(stat) == 'on':
            return 1
        else:
            return 0
    if request.method == 'POST':
        sub = subscription(user_id=id, 
                            name=request.form['name'],
                            description=request.form['description'],
                            # price=request.form['price'],
                            course_id=request.form['course'],
                            # duration=request.form['duration'],
                            # duration_type=request.form['duration_type'],
                            notes_access=status(request.form.get('notes_access')),
                            video_access=status(request.form.get('video_access')),
                            mocktest_access=status(request.form.get('mocktest_access')),
                            is_active=status(request.form.get('is_active')))
        db.session.add(sub)
        db.session.commit()
        requests.staus = "accepted"
        requests.date = datetime.datetime.now()
        db.session.commit()
        return redirect(url_for('admin_users_requests'))
    return render_template('admin/addSub.html', user=user, courses=courses)

@app.route('/admin/users/requests/reject/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_users_requests_reject(id):
    requests = Requets.query.get(id)
    requests.staus = "rejected"
    requests.date = datetime.datetime.now()
    db.session.commit()
    return redirect(url_for('admin_users_requests'))













@app.route('/admin/course/', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_course():
    def status(stat):
        if str(stat) == 'on':
            return 1
        else:
            return 0
    courses = Courses.query.all()
    if request.method == 'POST':
        try:
            img = request.files['course_image']
            img_filename = secure_filename(img.filename)
            basedir = os.path.abspath(os.path.dirname(__file__))
            img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
            upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title=img_filename)
            course = Courses(course_name=request.form['name'], 
                            course_description=request.form['description'],
                            course_image=upload_image.link,
                            course_price=request.form['price'],
                            is_active=status(request.form['is_active']))
            print(course)
            db.session.add(course)
            db.session.commit()
            os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
            return redirect(url_for('admin_course'))
        except Exception as e:
            
            flash('Error adding Course :- '+str(e))
            # return jsonify({'return': 'error adding Course :- '+str(e)})
    return render_template('admin/viewCourse.html', courses=courses)

@app.route('/admin/course/delete/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_course_delete(id):
    course = Courses.query.get(id)
    db.session.delete(course)
    db.session.commit()
    return redirect(url_for('admin_course'))

@app.route('/admin/course/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_course_edit(id):
    course = Courses.query.get(id)
    if request.method == 'POST':
        course.course_name = request.form['name']
        course.course_description = request.form['description']
        course.course_price = request.form['price']
        db.session.commit()
        return redirect(url_for('admin_course'))
    return 'edit course'

@app.route('/admin/modules/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules(id):
    course = Courses.query.get(id)
    modules = Modules.query.filter_by(course_id=id).all()
    if request.method == 'POST':
        try: 
            img = request.files['module_image']
            img_filename = secure_filename(img.filename)
            basedir = os.path.abspath(os.path.dirname(__file__))
            img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
            upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title=img_filename)
            module = Modules(module_name=request.form['name'], 
                            module_description=request.form['description'],
                            module_image=upload_image.link,
                            course_id=id)
            db.session.add(module)
            db.session.commit()
            os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
            return redirect(url_for('admin_modules', id=id))
        except Exception as e:
            flash('Error adding Module :- '+str(e))
    return render_template('admin/viewModules.html', modules=modules, course=course)

@app.route('/admin/modules/delete/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_delete(id):
    module = Modules.query.get(id)
    db.session.delete(module)
    db.session.commit()
    return redirect(url_for('admin_modules', id=module.course_id))

@app.route('/admin/modules/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_edit(id):
    module = Modules.query.get(id)
    if request.method == 'POST':
        module.module_name = request.form['name']
        module.module_description = request.form['description']
        db.session.commit()
        return redirect(url_for('admin_modules', id=module.course_id))
    return 'edit module'



# ------------------------ Module Contents ------------------------ #
@app.route('/admin/modules/contents/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_contents(id):
    module = Modules.query.get(id)
    return render_template('admin/moduleContents.html', module=module)


@app.route('/admin/modules/notes/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_notes(id):
    module = Modules.query.get(id)
    notes = Notes.query.filter_by(module_id=id).all()
    noteImages = NoteImages.query.all()
    # if request.method == 'POST':
    #     try:
    #         notes_pdfs = request.files.getlist('notes_pdf')
    #         for pdf in notes_pdfs:
    #             pdf_filename = secure_filename(pdf.filename)
    #             basedir = os.path.abspath(os.path.dirname(__file__))
    #             pdf.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], pdf_filename))
    #             note = Notes(note_name=request.form['name'],#######################
    #                         module_id=id)
    #             db.session.add(note)
    #             db.session.commit()

    #             images = convert_from_path(UPLOAD_FOLDER+pdf_filename,poppler_path=r'C:\Program Files\poppler-0.68.0\bin', fmt='jpg')
    #             for i in range(len(images)):
    #                 # images[i].save('page'+ str(i) +'.jpg', 'JPEG')
    #                 images[i].save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], pdf_filename + 'page'+ str(i) +'.jpg'), 'JPEG')
    #                 upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'],  pdf_filename + 'page'+ str(i) +'.jpg'), title= pdf_filename + 'page'+ str(i) +'.SSjpg')
    #                 noteImg = NoteImages(note_id=note.id, image_url=upload_image.link)
    #                 db.session.add(noteImg)
    #                 db.session.commit()
    #                 os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'],  pdf_filename + 'page'+ str(i) +'.jpg'))
    #             os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], pdf_filename))
    #         return redirect(url_for('admin_modules_notes', id=id))
    #     except Exception as e:
    #         flash('Error adding Note :- '+str(e))
    return render_template('admin/notes.html', notes=notes, module=module, noteImages=noteImages)

# @app.route('/admin/modules/notes/upload/<int:id>', methods=['GET', 'POST'])
# @login_required
# @admin_required
# def admin_modules_notes_upload(id):
#     module = Modules.query.get(id)
#     notes = Notes.query.filter_by(module_id=id).all()
#     if request.method == 'POST':
#         try:
#             notes_pdfs = request.files.getlist('notes_pdf')
#             for pdf in notes_pdfs:
#                 pdf_filename = secure_filename(pdf.filename)
#                 basedir = os.path.abspath(os.path.dirname(__file__))
#                 pdf.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], pdf_filename))
#                 note = Notes(note_name=request.form['name'],note_description=request.form['description'],
#                             module_id=id)
#                 db.session.add(note)
#                 db.session.commit()

#                 images = convert_from_path(UPLOAD_FOLDER+pdf_filename,poppler_path=PROPPLER_PATH, fmt='jpg')
#                 for i in range(len(images)):
#                     # images[i].save('page'+ str(i) +'.jpg', 'JPEG')
#                     images[i].save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], pdf_filename + 'page'+ str(i) +'.jpg'), 'JPEG')
#                     upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'],  pdf_filename + 'page'+ str(i) +'.jpg'), title= pdf_filename + 'page'+ str(i) +'.SSjpg')
#                     noteImg = NoteImages(note_id=note.id, image_url=upload_image.link)
#                     db.session.add(noteImg)
#                     db.session.commit()
#                     os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'],  pdf_filename + 'page'+ str(i) +'.jpg'))
#                 os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], pdf_filename))
#             return redirect(url_for('admin_modules_notes', id=id))
#         except Exception as e:
#             return jsonify({'error': str(e)})
    
#     return 'no post'

@app.route('/admin/modules/notes/upload/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_notes_upload(id):
    module = Modules.query.get(id)
    notes = Notes.query.filter_by(module_id=id).all()
    if request.method == 'POST':
        try:
            note = Notes(note_name=request.form['name'],note_description=request.form['description'],
                            module_id=id)
            db.session.add(note)
            db.session.commit()
            images = request.files.getlist('notes_pdf')
            for img in images:
                img_filename = secure_filename(img.filename)
                basedir = os.path.abspath(os.path.dirname(__file__))
                img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title= img_filename)
                noteImg = NoteImages(note_id=note.id, image_url=upload_image.link)
                db.session.add(noteImg)
                db.session.commit()
                os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                
            return redirect(url_for('admin_modules_notes', id=id))
        except Exception as e:
            return jsonify({'error': str(e)})
    
    return 'no post'



@app.route('/admin/modules/notes/delete/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_notes_delete(id):
    note = Notes.query.get(id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('admin_modules_notes', id=note.module_id))

@app.route('/admin/modules/notes/delete/image/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_notes_delete_image(id):
    noteImg = NoteImages.query.get(id)
    note = Notes.query.get(noteImg.note_id)
    db.session.delete(noteImg)
    db.session.commit()
    return redirect(url_for('admin_modules_notes', id=note.module_id))

@app.route('/admin/modules/notes/add/image/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_notes_add_image(id):
    note = Notes.query.get(id)
    if request.method == 'POST':
        try:
            images = request.files.getlist('notes_pdf')
            for img in images:
                img_filename = secure_filename(img.filename)
                basedir = os.path.abspath(os.path.dirname(__file__))
                img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title= img_filename)
                noteImg = NoteImages(note_id=note.id, image_url=upload_image.link)
                db.session.add(noteImg)
                db.session.commit()
                os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                
            return redirect(url_for('admin_modules_notes', id=note.module_id))
        except Exception as e:
            return jsonify({'error': str(e)})
    
    return 'no post'
    

@app.route('/admin/modules/notes/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_notes_edit(id):
    note = Notes.query.get(id)
    if request.method == 'POST':
        note.note_name = request.form['name']
        note.note_description = request.form['description']
        db.session.commit()
        return redirect(url_for('admin_modules_notes', id=note.module_id))
    return 'edit note'

@app.route('/download/<filename>', methods=['GET', 'POST'])
def download(filename):
    try:
        basedir = os.path.abspath(os.path.dirname(__file__))
        uploads = os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename)
        return send_file(uploads, as_attachment=True)
    except Exception as e:
        return str(e)

@app.route('/admin/modules/mocktest/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_mocktest(id):
    module = Modules.query.get(id)
    mocktest = MockTest.query.all()


    if request.method == 'POST':
        pass
    return render_template('admin/mocktest.html', mocktest=mocktest, module=module)

@app.route('/admin/modules/mocktest/add/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_mocktest_add(id):
    if request.method == 'POST':
        try:
            img = request.files['test_image']
            img_filename = secure_filename(img.filename)
            basedir = os.path.abspath(os.path.dirname(__file__))
            img.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
            upload_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title=img_filename)
            mocktest = MockTest(module_id=id,
                                test_name=request.form['name'],
                                test_description=request.form['description'],
                                test_duration=request.form['test_duration'],
                                max_marks=request.form['max_marks'],
                                total_questions=0,
                                test_image = upload_image.link)
            db.session.add(mocktest)
            db.session.commit()
            os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
            return redirect(url_for('admin_modules_mocktest', id=id))
        except Exception as e:
            flash('Error adding Mock Test :- '+str(e))


@app.route('/admin/modules/mocktest/delete/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_mocktest_delete(id):
    mocktest = MockTest.query.get(id)
    db.session.delete(mocktest)
    db.session.commit()
    return redirect(url_for('admin_modules_mocktest', id=mocktest.module_id))

@app.route('/admin/modules/mocktest/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_mocktest_edit(id):
    mocktest = MockTest.query.get(id)
    if request.method == 'POST':
        mocktest.test_name = request.form['name']
        mocktest.test_description = request.form['description']
        db.session.commit()
        return redirect(url_for('admin_modules_mocktest', id=mocktest.module_id))
    return 'edit mocktest'

@app.route('/admin/modules/mocktest/QNA/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_mocktest_QNA(id):
    mocktest = MockTest.query.get(id)
    questions = MockTestQuestion.query.filter_by(mock_test_id=id).all()
    options = MockTestAnswer.query.all()
    return render_template('admin/mocktest_QNA.html', mocktest=mocktest, questions=questions, options=options)
 
@app.route('/admin/modules/mocktest/Questions/add/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_mocktest_Questions_add(id):
    mocktest = MockTest.query.get(id)
    if request.method == 'POST':
        try:
            question = MockTestQuestion(mock_test_id=id,
                                        question=request.form['question'])
            db.session.add(question)
            db.session.commit()
            mocktest.total_questions = mocktest.total_questions + 1
            db.session.commit()
            return redirect(url_for('admin_modules_mocktest_QNA', id=id))
        except Exception as e:
            flash('Error adding Question :- '+str(e))
            return str(e)
    return redirect(url_for('admin_modules_mocktest_QNA',id=id))

@app.route('/admin/modules/mocktest/Questions/add/execl/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_mocktest_Questions_add_execl(id):
    def ConvertStatus(status):
        if status == '1' or status == 1 or status == 'true' or status == 'TRUE':
            return True
        else:
            return False
    
    if request.method == 'POST':
        try:
            f = request.files['file']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
            loc = (UPLOAD_FOLDER+f.filename)
            wb = xlrd.open_workbook(loc)
            sheet = wb.sheet_by_index(0)
            sheet.cell_value(0, 0)
            mocktest = MockTest.query.get(id)
            for i in range(1, sheet.nrows):
                question = MockTestQuestion(mock_test_id=id,
                                            question=sheet.cell_value(i, 0),
                                            explanation=sheet.cell_value(i, 9))
                db.session.add(question)
                db.session.commit()
                # options1 = MockTestAnswer(question_id=question.id,)
                for j in range(1, 8):
                    if j%2 != 0:
                        option = MockTestAnswer(question_id=question.id,
                                                answer=sheet.cell_value(i,j),
                                                is_correct=ConvertStatus(sheet.cell_value(i,j+1)))
                        db.session.add(option)
                        db.session.commit()
                db.session.add(question)
                db.session.commit()
                mocktest.total_questions = mocktest.total_questions + 1
                db.session.commit()
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
                
                
                
            return redirect(url_for('admin_modules_mocktest_QNA', id=id))
        except Exception as e:
            flash('Error adding Question :- '+str(e))
            return redirect(url_for('admin_modules_mocktest_QNA', id=id))
    return redirect(url_for('admin_modules_mocktest_QNA',id=id))










@app.route('/admin/modules/mocktest/Questions/delete/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_mocktest_Questions_delete(id):
    question = MockTestQuestion.query.get(id)
    mocktest = MockTest.query.get(question.mock_test_id)
    db.session.delete(question)
    db.session.commit()
    mocktest.total_questions = mocktest.total_questions - 1
    db.session.commit()
    return redirect(url_for('admin_modules_mocktest_QNA', id=question.mock_test_id))

@app.route('/admin/modules/mocktest/Questions/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_mocktest_Questions_edit(id):
    question = MockTestQuestion.query.get(id)
    if request.method == 'POST':
        question.question = request.form['question']
        question.explanation = request.form['explanation']
        db.session.commit()
        return redirect(url_for('admin_modules_mocktest_QNA', id=question.mock_test_id))
    return 'edit question'

@app.route('/admin/modules/mocktest/Questions/Options/add/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_mocktest_Questions_Options_add(id):
    question = MockTestQuestion.query.get(id)
    def status(stat):
        if str(stat) == 'on':
            return 1
        else:
            return 0
    if request.method == 'POST':
        try:
            option = MockTestAnswer(question_id=id,
                                    answer=request.form['option'],
                                    is_correct=status(request.form.get('is_correct')))
            db.session.add(option)
            db.session.commit()
            return redirect(url_for('admin_modules_mocktest_QNA', id=question.mock_test_id))
        except Exception as e:
            flash('Error adding Option :- '+str(e))
    return redirect(url_for('admin_modules_mocktest_QNA', id=question.mock_test_id))

@app.route('/admin/modules/mocktest/Questions/Options/delete/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_mocktest_Questions_Options_delete(id):
    option = MockTestAnswer.query.get(id)
    q_id = MockTestQuestion.query.filter_by(id=option.question_id).first()

    db.session.delete(option)
    db.session.commit()
    return redirect(url_for('admin_modules_mocktest_QNA', id=q_id.id))

@app.route('/admin/modules/mocktest/Questions/Options/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_mocktest_Questions_Options_edit(id):
    option = MockTestAnswer.query.filter_by(id=id).first()
    q_id = MockTestQuestion.query.filter_by(id=option.question_id).first()
    def status(stat):
        if str(stat) == 'on':
            return 1
        else:
            return 0
    if request.method == 'POST':
        option.answer = request.form['option']
        option.is_correct = status(request.form.get('is_correct'))
        db.session.commit()
        return redirect(url_for('admin_modules_mocktest_QNA', id=q_id.id))
    return 'edit option'




@app.route('/admin/modules/videoRec/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_videoRec(id):
    module = Modules.query.get(id)
    videos = VideoRec.query.filter_by(module_id=id).all()
    users = User.query.all()
    subscriptions = subscription.query.all()
    emails = []
    for subs in subscriptions:
        for user in users:
            if subs.user_id == user.id and subs.video_access and subs.is_active == '1':
                if user.email not in emails:
                    emails.append(user.email)
            
    return render_template('admin/viewVideos.html', module=module, videos=videos, users=users , subscriptions=subscriptions, emails=emails)



@app.route('/admin/modules/videoRec/add/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_videoRec_add(id):
    module = Modules.query.get(id)
    if request.method == 'POST':
        try:
            video_url=request.form['video_url']
            if 'https://www.youtube.com/watch?v=' in video_url:
                video_url = video_url.replace('https://www.youtube.com/watch?v=','https://www.youtube.com/embed/')
            elif 'https://youtu.be/' in video_url:
                video_url = video_url.replace('https://youtu.be/','https://www.youtube.com/embed/')
            
            video = VideoRec(module_id=id,
                             video_name=request.form['video_name'],
                             video_date= datetime.datetime.strptime(request.form['video_date'], '%Y-%m-%d'),
                             video_url=video_url)
            db.session.add(video)
            db.session.commit()
            return redirect(url_for('admin_modules_videoRec', id=id))
        except Exception as e:
            flash('Error adding Video :- '+str(e))
    return redirect(url_for('admin_modules_videoRec', id=id))

@app.route('/admin/modules/videoRec/delete/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_videoRec_delete(id):
    video = VideoRec.query.get(id)
    db.session.delete(video)
    db.session.commit()
    return redirect(url_for('admin_modules_videoRec', id=video.module_id))

@app.route('/admin/modules/videoRec/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_videoRec_edit(id):
    video = VideoRec.query.get(id)
    if request.method == 'POST':
        video.video_name = request.form['video_name']
        video_date = datetime.datetime.strptime(request.form['video_date'], '%Y-%m-%d')
        video.video_date = video_date   
        video.video_url = request.form['video_url']
        db.session.commit()
        return redirect(url_for('admin_modules_videoRec', id=video.module_id))
    return 'edit video'

@app.route('/whatsapp', methods=['GET', 'POST'])
def whatsapp():
    whatsapp = Whatsapp.query.all()
    phone = whatsapp[0].number
    text = whatsapp[0].message
    phone = phone.replace(' ', '')
    text = text.replace(' ', '%20')
    return redirect('https://api.whatsapp.com/send?phone='+phone+'&text='+text)



@app.route('/admin/whatsapp/add/', methods=['GET', 'POST'])
@login_required
@admin_required
def whatsapp_add():
    whatsapp = Whatsapp.query.all()
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        text = request.form['text']
        whatsapp = Whatsapp(name=name, number=phone, message=text)
        db.session.add(whatsapp)
        db.session.commit()
        return redirect(url_for('whatsapp_add'))
    return render_template('admin/whatsapp.html', whatsapp=whatsapp)

@app.route('/admin/whatsapp/delete/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def whatsapp_delete(id):
    whatsapp = Whatsapp.query.get(id)
    db.session.delete(whatsapp)
    db.session.commit()
    return redirect(url_for('whatsapp_add'))

@app.route('/student/whatsapp/<phone>/<text>', methods=['GET', 'POST'])
@login_required
def student_whatsapp(phone, text):
    phone = phone.replace(' ', '')
    text = text.replace(' ', '%20')
    return redirect('https://api.whatsapp.com/send?phone='+phone+'&text='+text)