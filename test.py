

quiz = {
    "score": 5,
    "user_id": "1",
    "questions": [
      {
        "question": "q1",
        "choices": [
          "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
          "etraset sheets containing Lorem Ipsum passages, and more recently ",
          "etraset sheets containing Lorem Ipsum passages, and more recently ",
          "etraset sheets containing Lorem Ipsum passages, and more recently "
        ],
        "answer": "Lorem Ipsum is simply dummy text of the printing and typesetting industry"
      },
      {
        "question": "q2",
        "choices": [
          "etraset sheets containing Lorem Ipsum passages, and more recently ",
          "etraset sheets containing Lorem Ipsum passages, and more recently ",
          " with desktop publishing software like Aldus PageMaker including versions of Lore",
          "etraset sheets containing Lorem Ipsum passages, and more recently "
        ],
        "answer": "etraset sheets containing Lorem Ipsum passages, and more recently "
      },
      {
        "question": "q3",
        "choices": [
          "etraset sheets containing Lorem Ipsum passages, and more recently ",
          " with desktop publishing software like Aldus PageMaker including versions of Lore",
          "etraset sheets containing Lorem Ipsum passages, and more recently ",
          " with desktop publishing software like Aldus PageMaker including versions of Lore"
        ],
        "answer": "etraset sheets containing Lorem Ipsum passages, and more recently "
      },
      {
        "question": "q4",
        "choices": [
          " with desktop publishing software like Aldus PageMaker including versions of Lore",
          "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
          " with desktop publishing software like Aldus PageMaker including versions of Lore",
          "Lorem Ipsum is simply dummy text of the printing and typesetting industry"
        ],
        "answer": "Lorem Ipsum is simply dummy text of the printing and typesetting industry"
      },
      {
        "question": "q5",
        "choices": [
          "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
          "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
          "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
          "etraset sheets containing Lorem Ipsum passages, and more recently "
        ],
        "answer": "Lorem Ipsum is simply dummy text of the printing and typesetting industry"
      },
      {
        "question": "q6",
        "choices": [
          "etraset sheets containing Lorem Ipsum passages, and more recently ",
          "etraset sheets containing Lorem Ipsum passages, and more recently ",
          "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
          "etraset sheets containing Lorem Ipsum passages, and more recently "
        ],
        "answer": "Lorem Ipsum is simply dummy text of the printing and typesetting industry"
      },
      {
        "question": "q7",
        "choices": [
          "etraset sheets containing Lorem Ipsum passages, and more recently ",
          "etraset sheets containing Lorem Ipsum passages, and more recently ",
          "etraset sheets containing Lorem Ipsum passages, and more recently ",
          "etraset sheets containing Lorem Ipsum passages, and more recently "
        ],
        "answer": "etraset sheets containing Lorem Ipsum passages, and more recently "
      },
      {
        "question": "q8",
        "choices": [
          " with desktop publishing software like Aldus PageMaker including versions of Lore",
          " with desktop publishing software like Aldus PageMaker including versions of Lore",
          "etraset sheets containing Lorem Ipsum passages, and more recently ",
          " with desktop publishing software like Aldus PageMaker including versions of Lore"
        ],
        "answer": " with desktop publishing software like Aldus PageMaker including versions of Lore"
      },
      {
        "question": "q9",
        "choices": [
          "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
          "etraset sheets containing Lorem Ipsum passages, and more recently ",
          "etraset sheets containing Lorem Ipsum passages, and more recently ",
          "Lorem Ipsum is simply dummy text of the printing and typesetting industry"
        ],
        "answer": "etraset sheets containing Lorem Ipsum passages, and more recently "
      },
      {
        "question": "q10",
        "choices": [
          "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
          "etraset sheets containing Lorem Ipsum passages, and more recently ",
          " with desktop publishing software like Aldus PageMaker including versions of Lore",
          "etraset sheets containing Lorem Ipsum passages, and more recently "
        ],
        "answer": "etraset sheets containing Lorem Ipsum passages, and more recently "
      }
    ],
    "answers": [
     "etraset sheets containing Lorem Ips um passages, and more recently ",
      "etraset sheets containing Lorem Ipsum passages, and more recently ",
      " with desktop publishing software like Aldus PageMaker including versions of Lore",
      "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
      "etraset sheets containing Lorem Ipsum passages, and more recently ",
      "etraset sheets containing Lorem Ipsum passages, and more recently ",
      "etraset sheets containing Lorem Ipsum passages, and more recently ",
      " with desktop publishing software like Aldus PageMaker including versions of Lore",
      "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
      "etraset sheets containing Lorem Ipsum passages, and more recently "
    ],
    "time": 11.406
  }



for q in quiz['questions']:
    print(q['question'])
   
    print(quiz['answers'][quiz['questions'].index(q)])
    



























# # import module
# from pdf2image import convert_from_path
# from PIL import ImageFile
# ImageFile.LOAD_TRUNCATED_IMAGES = True
# UPLOAD_FOLDER = 'static/img/uploads/'
# import os
 
# # Store Pdf with convert_from_path function
# images = convert_from_path('static/img/uploads/ccna.pdf' ,poppler_path=r'C:\Program Files\poppler-0.68.0\bin', fmt='jpg')
# basedir = os.path.abspath(os.path.dirname(__file__))
# for i in range(len(images)):
   
#       # Save pages as images in the pdf
#     images[i].save(os.path.join(basedir,UPLOAD_FOLDER , 'page'+ str(i) +'.jpg' ), 'JPEG')



# # from app import app,MockTest, MockTestQuestion, MockTestAnswer, db
# # Q = {'question': '', 'choices': [], 'answer': ''}
# # questions = []
# # id=1
# # with app.app_context():
# #   mocktest = MockTest.query.get(id)
# #   mocktest_questions = MockTestQuestion.query.filter_by(mock_test_id=id).all()
# #   for question in mocktest_questions:
# #       print(question.question)
# #       Q['question'] = question.question
# #       mocktest_answers = MockTestAnswer.query.filter_by(question_id=id).all()
# #       Q['choices'] = [answer.answer for answer in mocktest_answers]
# #       Q['answer'] = [answer.answer for answer in mocktest_answers if answer.is_correct][0]
# #       questions.append(Q)
# #       Q = {'question': '', 'choices': [], 'answer': ''}
# #   print(questions)