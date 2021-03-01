from django.shortcuts import render
from .models import Product,Student
from .forms import ProductForm
from.forms import PersonForm
from django.http import HttpResponse

# post=[{
#     'author':'Hricha Maharjan',
#     'title':'Polls Post1',
#     'content':'First post content'
# },
#
# {
#     'author':'gaurav jha',
#     'title':'Polls Post1',
#     'content':'First post content'
# }
#     ]


def home(request):
    post=Product.objects.all()
    context={
        'posts':post
    }
    return render(request,'blog/home.html',context)
def about(request):

    return render(request,'blog/about.html')
def get_product_form(request):
    form=ProductForm()
    context={
        'form':form
    }
    return render(request,'blog/getProductForms.html',context)
def get_person_form(request):
    form=PersonForm()
    context={
        'form':form
    }
    return render(request,'blog/getPersonForms.html',context)
def post_student(request):
    if request.method=="POST":
        data=request.POST
        firstname=data['firstname']
        lastname=data['lastname']
        batch=data['batch']
        category=data['category']
        image_url=data['image_url']
        student=Student.objects.create(firstname=firstname,
                                       lastname=lastname,
                                       batch=batch,
                                       category=category,
                                       image_url=image_url)
        if student:
            return HttpResponse("Success")
        else:
            return HttpResponse("Failed")
    return render(request,'blog/addStudents.html')
def get_Student(request):
    students=Student.objects.all()
    context={
        'students':students
    }
    return render(request,'blog/getStudents.html',context)
