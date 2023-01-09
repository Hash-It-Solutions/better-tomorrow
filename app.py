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

import os
import base64

app = Flask(__name__)
app.secret_key = 'asdasdasdasdasdasdasaasdasdasdasd12312312daveqvq34c'


UPLOAD_FOLDER = 'static/img/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CLIENT_ID = "2d3158d36137249"
im = pyimgur.Imgur(CLIENT_ID)

ENV = 'dev'

if ENV == 'dev' :
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
    app.config['SECRET_KEY'] = 'asdasdasdasdasdasdasdaveqvq34c'
      
else:
    app.debug = False
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

    subscription = db.relationship('subscription', backref='user')

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
    

class Courses(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(80))
    course_description = db.Column(db.String(500))
    ###
    # course_language = db.Column(db.String(80))
    ###
    course_image = db.Column(db.String(80))
    course_price = db.Column(db.String(80))
    course_module = db.relationship('Modules', backref='course')
 
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
    test_image = db.Column(db.String(80))
    test_price = db.Column(db.String(80))
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'))
    test_module = db.relationship('MockTestQuestion', backref='test')

class MockTestQuestion(db.Model):
    __tablename__ = 'mocktestquestion'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(80))
    image_url = db.Column(db.String(80), nullable=True)

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
    note_image = db.Column(db.String(80))
    note_filename = db.Column(db.String(80))
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'))

class VideoRec(db.Model):
    __tablename__ = 'videorec'
    id = db.Column(db.Integer, primary_key=True)
    video_name = db.Column(db.String(80))
    video_description = db.Column(db.String(500))
    video_url = db.Column(db.String(80))
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

@app.route('/courses/<int:id>', methods=['GET', 'POST'])
def course(id):
    courses = Courses.query.all()
    course = Courses.query.get(id)
    modules = Modules.query.filter_by(course_id=id)
    return render_template('main/course-detail.html', user=current_user, course=course, modules=modules, courses=courses)





































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
    db.session.commit()
    return redirect(url_for('admin_users_view', id=sub.user_id))


@app.route('/admin/users/delete/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_users_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('admin_users'))

@app.route('/admin/course/', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_course():
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
                            course_price=request.form['price'])
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
    if request.method == 'POST':
        try:
            notes_pdfs = request.files.getlist('notes_pdf')
            for pdf in notes_pdfs:
                pdf_filename = secure_filename(pdf.filename)
                basedir = os.path.abspath(os.path.dirname(__file__))
                pdf.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], pdf_filename))
                note = Notes(note_filename=pdf_filename,
                            module_id=id)
                db.session.add(note)
                db.session.commit()
            return redirect(url_for('admin_modules_notes', id=id))
        except Exception as e:
            flash('Error adding Note :- '+str(e))
    return render_template('admin/notes.html', notes=notes, module=module)

@app.route('/admin/modules/notes/delete/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_notes_delete(id):
    note = Notes.query.get(id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('admin_modules_notes', id=note.module_id))

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
                                # test_duration=request.form['duration'],
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
            return redirect(url_for('admin_modules_mocktest_QNA', id=id))
        except Exception as e:
            flash('Error adding Question :- '+str(e))
    return redirect(url_for('admin_modules_mocktest_QNA',id=id))

@app.route('/admin/modules/mocktest/Questions/delete/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_mocktest_Questions_delete(id):
    question = MockTestQuestion.query.get(id)
    db.session.delete(question)
    db.session.commit()
    return redirect(url_for('admin_modules_mocktest_QNA', id=question.mock_test_id))

@app.route('/admin/modules/mocktest/Questions/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_modules_mocktest_Questions_edit(id):
    question = MockTestQuestion.query.get(id)
    if request.method == 'POST':
        question.question = request.form['question']
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