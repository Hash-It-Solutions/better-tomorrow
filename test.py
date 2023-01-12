
# # import module
# from pdf2image import convert_from_path
 
 
# # Store Pdf with convert_from_path function
# images = convert_from_path('ICE_CUBE_BASIC-_Invoice.pdf',poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
 
# for i in range(len(images)):
   
#       # Save pages as images in the pdf
#     images[i].save('page'+ str(i) +'.jpg', 'JPEG')



from app import app,MockTest, MockTestQuestion, MockTestAnswer, db
Q = {'question': '', 'choices': [], 'answer': ''}
questions = []
id=1
with app.app_context():
  mocktest = MockTest.query.get(id)
  mocktest_questions = MockTestQuestion.query.filter_by(mock_test_id=id).all()
  for question in mocktest_questions:
      print(question.question)
      Q['question'] = question.question
      mocktest_answers = MockTestAnswer.query.filter_by(question_id=id).all()
      Q['choices'] = [answer.answer for answer in mocktest_answers]
      Q['answer'] = [answer.answer for answer in mocktest_answers if answer.is_correct][0]
      questions.append(Q)
      Q = {'question': '', 'choices': [], 'answer': ''}
  print(questions)