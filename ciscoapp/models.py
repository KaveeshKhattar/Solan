from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils import timezone

#A table containing all relevant information regarding students
class Student(models.Model):
    roll_nbr = models.IntegerField(primary_key=True,default = 0, db_column='roll_nbr', null=False)
    student_name = models.CharField(max_length=30, db_column = 'student_name', null = False)
    subject = models.CharField(max_length=20)
    standard = models.IntegerField(default = 0, db_column='standard')
    class Meta:
        db_table = 'students'
        verbose_name_plural = 'students'
    def __str__(self):
        return str(self.roll_nbr) + ' Name => ' + str(self.student_name)

#Login table
class login(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'login'
        verbose_name_plural = 'logins'
    def __str__(self):
        return str(self.id)

#CHECK
class subject(models.Model):
    sub=models.CharField(max_length=50, db_column='sub', null=False)
    chp=models.CharField(max_length=25, db_column='chp', null=True)
    class Meta:
        db_table = 'subject'
        verbose_name_plural = 'subjects'
    def __str__(self):
        return str(self.id)

#A table containing all the questions in the question bank
class question(models.Model):
    subject=models.CharField(primary_key=True,max_length=80,db_column='subject', null=False)
    chapter=models.CharField(max_length=80,db_column='chapter', null=False)
    question=models.CharField(max_length=1000, db_column = 'question', null = False)
    qotw = models.CharField(max_length=1, db_column='qotw', default='n')
    username = models.CharField(max_length=100, db_column='username', null=False)
    class Meta:
        db_table = 'question'
        verbose_name_plural = 'questions'

#A table containing data on the question selected as the question of the week, the four options and the correct answer
class qotw(models.Model):
    subject=models.CharField(primary_key=True,max_length=80,db_column='subject', null=False)
    chapter=models.CharField(max_length=80,db_column='chapter', null=False)
    question=models.CharField(max_length=1000, db_column = 'question', null = False)
    option1 = models.CharField(max_length=500, db_column='option1', null=False)
    option2 = models.CharField(max_length=500, db_column='option2', null=False)
    option3 = models.CharField(max_length=500, db_column='option3', null=False)
    option4 = models.CharField(max_length=500, db_column='option4', null=False)
    ans = models.CharField(max_length=5,db_column='ans', null=False)
    class Meta:
        db_table = 'qotw'
        verbose_name_plural = 'qotw'

#A table with all the points earned by students
class points(models.Model):
    points = models.IntegerField(default=0, db_column='points', null=False)
    login = models.ForeignKey(login, on_delete=models.CASCADE)
    class Meta:
        db_table = 'point'
        verbose_name_plural = 'points'

#A table containing all the chapters inn a subject
class chapter123(models.Model):
    name = models.CharField(max_length=50)
    subject = models.ForeignKey("subject123", on_delete=models.CASCADE, )
    def __unicode__(self):
        return u'%s' % (self.name)

#A table containing all the subjects
class subject123(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return u'%s' % (self.name)
#CHECK
class Person(models.Model):
    name = models.CharField(max_length=30,  db_column='username', null=False)
    email = models.EmailField( blank=False)
    points= models.IntegerField(default=0, db_column='points', null=False)
    def __str__(self):
        return str(self.id)