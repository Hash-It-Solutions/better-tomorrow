from django.db import models
from course.models import Course
# Create your models here.
class CourseSubjects(models.Model):
    id=models.IntegerField(primary_key=True)
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE)