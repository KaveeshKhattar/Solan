from django.db import connection
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django import template
import json as simplejson
from django.contrib.auth import authenticate, logout,login
from .models import Student
from .models import login
from .models import question
from .models import subject
from .models import points
from .models import *
from tablib import Dataset
import csv, sys, os, django
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.conf import settings
import datetime

User = get_user_model()

register = template.Library()
@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False

#loads the home page
def index(request):
    return render(request, 'ciscoapp/home.html')

#returns a list of students to be used for leaderboard and generating student report
def get_students(request):
    print ("get_students")
    st_lst =  Student.objects.all()
    print (str(st_lst))
    context_dict = {}
    return render(request, 'ciscoapp/view_students.html', {'st_lst': st_lst})

#used to search students based on their roll numbers
def searchStudentsByRange(request):
    startingRoll = request.POST['startRoll']
    endRoll = request.POST['endRoll']
    print ("startingRoll is " + str(startingRoll))
    print ("endRoll is " + str(endRoll))
    st_lst = Student.objects.raw('select * from students where roll_nbr between ' + str(startingRoll) + ' and ' + str(endRoll) )
    return render(request, 'ciscoapp/view_students.html', {'st_lst': st_lst})

#CHECK
def inputStudentRange(request):
    st_lst =  Student.objects.all()
    return render(request, 'ciscoapp/enter_range.html', {'st_lst': st_lst})

#CHECK
def insertStudentHtml(request):
    return render(request, 'ciscoapp/insert_student.html')

#used to register new students and view the newly formed list of students
def insertStudent(request):
    rollNbr = request.POST['rollNbr']
    studentName = request.POST['studentName']
    subject = request.POST['subject']
    standard = request.POST['standard']
    args = (rollNbr,studentName,subject,standard)
    query = "INSERT INTO students(roll_nbr, student_name, subject, standard) " \
            "VALUES(%s,%s, %s, %s)"
    cursor = connection.cursor()
    cursor.execute(query,args)
    st_lst = Student.objects.raw('select * from students')
    return render(request, 'ciscoapp/view_students.html', {'st_lst': st_lst})

#loads the webpage for deleting a student
def deleteStudentHtml(request):
    return render(request, 'ciscoapp/delete_student.html')

#used when a student needs to be deleted and then returns the newly formed list of students
def deleteStudent(request):
    rollNbr1=request.POST['rollNbr1']
    print('roll number is :' + str(rollNbr1))
    args=(rollNbr1,)
    query = " DELETE FROM students WHERE roll_nbr=%s "
    cursor = connection.cursor()
    cursor.execute(query, args)
    st_lst = Student.objects.raw('select * from students')
    return render(request, 'ciscoapp/view_students.html', {'st_lst': st_lst})

#loads the webpage to modify a student's data
def updateStudentHtml(request):
    return render(request, 'ciscoapp/update_student.html')

#updates any data related to the student and displays the list of students along with the updations
def updateStudent(request):
    rollNbr2 = request.POST['rollNbr2']
    studentName = request.POST['studentName']
    print('roll number is :' + str(rollNbr2))
    args=(studentName,rollNbr2)
    query = "UPDATE students SET student_name = %s WHERE roll_nbr = %s"
    cursor = connection.cursor()
    cursor.execute(query,args)
    st_lst = Student.objects.raw('select * from students')
    return render(request, 'ciscoapp/view_students.html', {'st_lst': st_lst})

#loads the login page for the student
def loginStudentHtml(request):
    return render(request, 'ciscoapp/login_student.html')

#verifies the entered email id and password while logging in
def Login(request):
    email=request.POST['email']
    password=request.POST['password']
    login_lst = login.objects.raw("select * from login where email_id= " + "'" + str(email) + "'" + " and password=" + "'" + str(password) + "'")
    print(login_lst)
    if login_lst != None:
        return HttpResponse('you have logged in successfully!')
    else:
        return render(request, 'ciscoapp/view_students.html', {'login_lst': login_lst})

#CHECK
def subchpHtml(request):
    return render(request, 'ciscoapp/sub_chp.html')

#helps in selecting the subject and chapter to view the question bank and to submit questions
def subchp(request):
    sub=request.POST['sub']
    chp=request.POST['chp']
    print('subject is : ', str(sub))
    print(' is : ', str(chp))
    args=(sub,chp)
    query = 'select sub from subject'
    cursor = connection.cursor()
    cursor.execute(query,args)
    sub_chp_lst = Subject.objects.raw('select sub from subject')
    return render(request, 'ciscoapp/sub_chp.html', {'sub_chp_lst': sub_chp_lst})

#used to retrieve all the questions submitted by all the students
def retrieve(request):
	print ("get_students")
	q_lst =  questions.objects.all()
	print (str(q_lst))
	context_dict = {}
	return render(request, 'ciscoapp/QuestionBank.html', {'q_lst': q_lst})

#used to display the student's dashboard and the leaderboard comprising of the student's name and their corresponding points
def dashboardS(request):
    query_result1 = points.objects.filter(
        login__user__email=str(request.user.email))
    pointsObject = query_result1[0]
    query = "select * from point order by points DESC LIMIT 5"
    print(query)
    query_result5 = points.objects.raw(query)
    print(query_result5)
    subjects = subject123.objects.all()
    print(subjects)
    return render(request, 'ciscoapp/dashboardS.html', {'query_results': query_result5, 'pointsObject': pointsObject, 'subjects': subjects})

#CHECK
def dashboardT(request):
    query_result1 = points.objects.filter(
        login__user__email=str(request.user.email))
    subjects = subject123.objects.all()
    print(subjects)
    return render(request, 'ciscoapp/dashboardT.html',{'subjects': subjects})

#used to load the home page
def homepage(request):
    return render(request, 'ciscoapp/index.html')

#used to view all the questions or questions of a particular subject and chapter entered by students and teachers
def viewBank(request):
    subject=request.POST.get('selectsubject')
    chapter=request.POST.get('selectchapter')
    if chapter == "All":
        print('subject is : ', str(subject))
        print('chapter is : ', "All Questions")
        query = "select * from question where subject = " + "'" + str(subject) + "'"
    else:
        print('subject is : ', str(subject))
        print('chapter is : ', str(chapter))
        query = "select * from question where subject = " + "'" + str(subject) + "'" + " and chapter = " + "'" + str(chapter) + "'"
    questions = question.objects.raw(query)
    return render(request, 'ciscoapp/QuestionBank.html', {'questionList': questions})

#used when submitting questions
def enterBank(request):
    subject1 = request.POST.get('selectsubject3')
    chapter1 = request.POST.get('selectchapter3')
    question1 = request.POST['questionID']
    username1 = request.POST['username']
    print(type(question1))
    print(type(subject1))
    print(type(chapter1))
    args = (subject1, chapter1, question1)
    print('subject is : ', str(subject1))
    print('chapter is : ', str(chapter1))
    print('question is : ', str(question1))
    query = "insert into question VALUES " +  "(" + "'" + str(subject1) + "'" + "," + "'" + str(chapter1) + "'" + "," + "'" + str(question1) + "'" + ","  + "'" + "n" + "'" + "," + "'" + str(username1) + "'" + ")"
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    query_result1 = points.objects.filter(login__user__email=str(request.user.email))
    pointsObject = query_result1[0]
    pointsObject.points += 1
    pointsObject.save()
    st_lst = question.objects.raw('select * from question')
    return render(request, 'ciscoapp/enter_questions.html', {'st_lst': st_lst})

#used when modifying and managing the questions entered by students
def student_q_manage(request):
    subject = request.POST.get('selectsubject2')
    chapter = request.POST.get('selectchapter2')
    print('subject is : ', str(subject))
    print('chapter is : ', str(chapter))
    request.session['subject23'] = subject
    request.session['chapter23'] = chapter
    request.session['subject53'] = subject
    request.session['chapter53'] = chapter
    query = "select * from question where subject = " + "'" + \
        str(subject) + "'" + " and chapter = " + "'" + str(chapter) + "'"
    questions = question.objects.raw(query)
    return render(request, 'ciscoapp/B1.html', {'questionList': questions})

#Displays the student entered by the user that has logged in
def myquestions(request):
    username9 = request.user.username
    query = "select * from question where username = " + "'" + \
        str(username9) + "'"
    questions = question.objects.raw(query)
    return render(request, 'ciscoapp/B5.html', {'questionList': questions})

#Generates student report for teachers ordering students by points
def GenReport(request):
    query = "select * from point order by points DESC "
    query_results = points.objects.raw(query)
    return render(request, 'ciscoapp/GenReport.html', {'query_results': query_results})

#CHECK
def editquestion(request):
    question2 = request.POST['question123']
    #request.session['question33'] = question2
    print('question2 is : ', str(question2))
    question5 = request.POST['question456']
    subject23 = request.session['subject23']
    chapter23 = request.session['chapter23']
    print('question5 is : ', str(question5))
    query = "update question set  question = " + "'" + \
        str(question5) + "'" + " where question = " + \
        "'" + str(question2) + "'" + "and subject = " + "'" + str(subject23) + "'" + " and chapter = " + "'" + str(chapter23) + "'"
    print(query)
    questions = question.objects.raw(query)
    args = (question2,question5)
    cursor = connection.cursor()
    cursor.execute(query)
    return render(request, 'ciscoapp/enter_questions.html')

#Allows the teacher to edit questions that are submitted by the student
def editquestion2(request):
    question2 = request.POST['question123']
    print('question2 is : ', str(question2))
    question5 = request.POST['question456']
    subject23 = request.POST['subject123']
    chapter23 = request.POST['chapter123']
    print('question5 is : ', str(question5))
    query = "update question set  question = " + "'" + \
        str(question5) + "'" + " where question = " + \
        "'" + str(question2) + "'" + "and subject = " + "'" + str(subject23) + \
        "'" + " and chapter = " + "'" + str(chapter23) + "'"
    print(query)
    questions = question.objects.raw(query)
    args = (question2, question5)
    cursor = connection.cursor()
    cursor.execute(query)
    return render(request, 'ciscoapp/enter_questions.html')

#CHECK
def deletequestion(request):
    question9 = request.POST['question333']
    print(question9)
    subject33 = request.session['subject23']
    chapter33 = request.session['chapter23']
    query = "delete from  question where question = " + \
        "'" + str(question9) + "'" + "and subject = " + "'" + str(subject33) + \
        "'" + " and chapter = " + "'" + str(chapter33) + "'"
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    return render(request, 'ciscoapp/Deletequestion.html')

#Deletes the question that the teacher wishes to delete
def deletequestion2(request):
    question9 = request.POST['question333']
    print(question9)
    subject33 = request.POST['subject123']
    chapter33 = request.POST['chapter123']
    query = "delete from  question where question = " + \
        "'" + str(question9) + "'" + "and subject = " + "'" + str(subject33) + \
        "'" + " and chapter = " + "'" + str(chapter33) + "'"
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    return render(request, 'ciscoapp/Deletequestion.html')

#CHECK
def questionoftheweekstudent(request):
    query = "select * from qotw "
    print(query)
    question234 = question.objects.raw(query)
    return render(request, 'ciscoapp/QuestionoftheweekS.html', {'questionList': question234})

#Posts the answer submitted by student for question of the week
def qotwstudent(request):
    studans = request.POST['studans']
    query = "select * from  qotw  "
    print(query)
    questions = question.objects.raw(query)
    return render(request, 'ciscoapp/qotwsubmit.html', {'questionList': questions, 'studans': studans})

#CHECK
def questionoftheweekteacher(request):
    question11 = request.POST['question111']
    subject43 = request.session['subject23']
    chapter43 = request.session['chapter23']
    print(question11)
    request.session['question112'] = question11
    request.session['subject112'] = subject43
    request.session['chapter112'] = chapter43
    query = "select * from question where question = " + "'" + \
        str(question11) + "'" + "and subject =" + "'" + str(subject43) + "'" + "and chapter =" + "'" + str(chapter43) + "'"
    print(query)
    questions = question.objects.raw(query)
    return render(request, 'ciscoapp/qotw.html', {'question1123': questions})
    print(question1123)

#Function that posts the question selected by the teacher as the question of the week and the options entered by the teacher too
def qotw(request):
    question112 = request.session['question112']
    subject113 = request.session['subject112']
    chapter113 = request.session['chapter112']
    opt1 = request.POST['option1']
    opt2 = request.POST['option2']
    opt3 = request.POST['option3']
    opt4 = request.POST['option4']
    ans = request.POST['ans']
    print(question112)
    print(opt1)
    print(opt2)
    query123= "delete from qotw"
    print(query123)
    query = "insert into qotw VALUES " + "(" + "'" + str(subject113) + "'" + "," + "'" + str(chapter113) + "'" + "," + \
     "'" + str(question112) + "'" + "," + "'" + str(opt1) + "'" + "," + "'" + str(opt2) + "'" + "," + "'" + str(opt3) + \
        "'" + "," + "'" + str(opt4) + "'" + "," + "'" + str(ans) + "'" + ")"
    print(query)
    cursor = connection.cursor()
    cursor.execute(query123)
    cursor.execute(query)
    return render(request, 'ciscoapp/enter_questions.html')

#Function that is implemented when the student enters the correct answer for the question of the week
def rightans(request):
    query_result1 = points.objects.filter(
        login__user__email=str(request.user.email))
    pointsObject = query_result1[0]
    pointsObject.points += 1
    pointsObject.save()
    return render(request, 'ciscoapp/qotwsubmit1.html')

#Function that is implemented when the student enters the incorrect answer for the question of the week
def wrongans(request):
    query_result1 = points.objects.filter(
        login__user__email=str(request.user.email))
    pointsObject = query_result1[0]
    pointsObject.points += 0
    pointsObject.save()
    return render(request, 'ciscoapp/qotwsubmit1.html')

#Selects question of the week that is displayed when a student wishes to answer it
def QuestionOfTheWeekS(request):
    query = "select * from  qotw  "
    print(query)
    questions = question.objects.raw(query)
    return render(request, 'ciscoapp/QuestionoftheweekS.html', {'questionList': questions})

#CHECK
def questions(request):
    return render(request, 'ciscoapp/QuestionoftheweekS.html')

#CHECK
def subject896(request):
    subjects = subject123.objects.all()
    print (subjects)
    return render(request, 'ciscoapp/countries.html', {'subjects': subjects})

#CHECK
def getdetails(request):
    subject456 = request.GET['cnt1']
    print ("ajax subject ", subject456)
    result_set = []
    all_chapters = []
    answer = str(subject456[1:-1])
    selected_subject = subject123.objects.get(name=answer)
    print ("selected subject ", selected_subject)
    all_chapters = selected_subject.chapter123_set.all()
    for chapter in all_chapters:
        print ("chapter", chapter.name)
        result_set.append({'name': chapter.name})
    return HttpResponse(simplejson.dumps(result_set),content_type='application/json')

#Functionality to bulk add users using csv files
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        file_data = myfile.read().decode("utf-8").splitlines()
        data = csv.reader(file_data, delimiter=",")
        for row in data:
            print(row)
            if row[0] != "Number":
                Post=User()
                Post.password = row[0]
                Post.is_superuser = "0"
                Post.username = row[1]
                Post.first_name = row[2]
                Post.email = row[4]
                Post.is_staff = "1"
                Post.is_active = "1"
                Post.date_joined = datetime.datetime.now()
                Post.last_name=row[3]
                Post.save()
                u = User.objects.get(username=row[1])
                my_group = Group.objects.get(name=row[5])
                my_group.user_set.add(u)
                u.set_password(row[0])
    return render(request, 'upload.html')