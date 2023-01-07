from app import db,app, User
from werkzeug.security import generate_password_hash, check_password_hash

def createDb(self):
    with app.app_context():
        db.create_all() 
        print("Database created")
        #add admin user
        admin = User(email="admin@test.com", phone="1234567890", name="admin", password=generate_password_hash("admin"), user_type="admin", user_sub_type="admin", user_sub_id="admin")
        db.session.add(admin)
        db.session.commit()
        print("Admin user created")
createDb(self=None)