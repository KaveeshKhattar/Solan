from django.contrib import admin
from django.urls import path, include
from ciscoapp import views
from django.conf import settings
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', views.index, name='index'),
	path('view_students', views.get_students, name='get_students'),
	path('studentsByRange', views.searchStudentsByRange, name='searchStudentsByRange'),
    path('inputStudentRange', views.inputStudentRange, name='inputStudentRange'),
    path('insertStudentHtml', views.insertStudentHtml, name='insertStudentHtml'),
	path('insertStudent', views.insertStudent, name='insertStudent'),
	path('deleteStudentHtml', views.deleteStudentHtml, name='deleteStudentHtml'),
	path('deleteStudent', views.deleteStudent, name='deleteStudent'),
	path('updateStudentHtml', views.updateStudentHtml, name='updateStudentHtml'),
	path('updateStudent', views.updateStudent, name='updateStudent'),
	path('loginStudentHtml', views.loginStudentHtml, name='loginStudentHtml'),
	path('Login', views.Login, name='Login'),
	path('subchpHtml', views.subchpHtml, name='subchpHtml'),
	path('subchp', views.subchp, name='subchp'),
	path('retrieve', views.retrieve, name='retrieve'),
	path('viewBank', views.viewBank, name='viewBank'),
    path('enterBank', views.enterBank, name='enterBank'),
	path('dashboardS.html', views.dashboardS, name='dashboardS'),
	path('accounts/', include('django.contrib.auth.urls')),
	#path('testModal', views.testModal, name='testModal'),
    path('enter_questions', views.enterBank, name='enter_questions'),
    path('QuestionOfTheWeekS.html', views.QuestionOfTheWeekS, name='QuestionOfTheWeekS')
]