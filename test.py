
# import module
from pdf2image import convert_from_path
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
UPLOAD_FOLDER = 'static/img/uploads/'
import os
 
# Store Pdf with convert_from_path function
images = convert_from_path('static/img/uploads/ccna.pdf' ,poppler_path=r'C:\Program Files\poppler-0.68.0\bin', fmt='jpg')
basedir = os.path.abspath(os.path.dirname(__file__))
for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save(os.path.join(basedir,UPLOAD_FOLDER , 'page'+ str(i) +'.jpg' ), 'JPEG')



# from app import app,MockTest, MockTestQuestion, MockTestAnswer, db
# Q = {'question': '', 'choices': [], 'answer': ''}
# questions = []
# id=1
# with app.app_context():
#   mocktest = MockTest.query.get(id)
#   mocktest_questions = MockTestQuestion.query.filter_by(mock_test_id=id).all()
#   for question in mocktest_questions:
#       print(question.question)
#       Q['question'] = question.question
#       mocktest_answers = MockTestAnswer.query.filter_by(question_id=id).all()
#       Q['choices'] = [answer.answer for answer in mocktest_answers]
#       Q['answer'] = [answer.answer for answer in mocktest_answers if answer.is_correct][0]
#       questions.append(Q)
#       Q = {'question': '', 'choices': [], 'answer': ''}
#   print(questions)