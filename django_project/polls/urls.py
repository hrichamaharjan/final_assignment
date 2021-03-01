
# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('polls/', include('polls.urls')),
    # path('admin/', admin.site.urls),
    path('',views.home,name='polls-home'),
    path('about/',views.about,name='polls-about'),
    path('getForm/', views.get_product_form, name='polls-getForm'),
    path('getPersonForm/', views.get_person_form, name='polls-getPersonForm'),

    path('addStudents/', views.post_student),
    path('getStudents/', views.get_Student )
]