from django.shortcuts import render, HttpResponse
from a1.dbshell import *

# Create your views here.
# AUTOMIC TRANSACTION
# --------------------------------------------------------------------------
# when we run our proj if it runs successfully it show the following things
# Request URL: http://127.0.0.1:8000/welcome/
# Request Method: GET
# Status Code: 200 OK
# Remote Address: 127.0.0.1:8000
# Referrer Policy: strict-origin-when-cross-origin
# -------------------------------------------------------------------------
# views----> fun based and class based views in this file we are writing business logic

# status code----> all err will be showed to the client cuz debug = True by default in developing phase in settings.py file, we need to make it False in deployment phase
# categories 
# 1xx
# 2xx--- 200 ok  
# 3xx--- 301 redirect to another web page using a link, when we get err on any page we need to redirect to some other page
    # reference to check how the page is redirected to another page::https://stackoverflow.com/questions/3172929/abc
# 4xx---404 when url is not present(page not found) client side err our client is browser
    # if any printing mistake in our code that will be considered as server side error
# 5xx---500 internal server error or server side error

              
# request-----> GET and POST

# to test our proj we have to download POSTMAN  once after download we need to install and then sign in with google
# QUERY PARAMS--->Query Parameters --->syntax==?key=value--->example==?name=abc we can pass it at the end of the url 
# To access this query param in our program we need to use request.GET.get('name') or simply print(request.GET)

def welcome(request):  # To test this we have an app POSTMAN 
    # print(request)                   # simply prints the name of the method
    # print(request.method)           # returns the name of the method whether it is GET or POST
    # print(request.user)             # returns the name of the user 
    # print(request.__dict__)         # prints so many things like req method, remote host, path, server port, server name and port etc.
    # print(request.GET.get('name'))     # returns only the name we have used as the value of the dict key abc
    # print(request.GET)              # returns the query set of the query params <QueryDict: {'name': ['abc']}>
                                # when we pass multiple query params<QueryDict: {'name': ['abc'], 'surname': ['pqr'], 'age': ['30']}>
    # print(request.GET['age'])     # if we print the type it will return as str cuz everything in url is only str type

    # To display the data to UI
    # s1 = Student1.objects.get(id=1)                   # this is for the single record only 
    # all_studs = Student1.objects.all()                # Error will not accept this as it returns the query set so we have to convert it into a list using map and lambda
    all_studs = list(Student1.objects.values())
    print(all_studs)
    final_lst = list(map(lambda x: x['name'], all_studs))
    # return HttpResponse(f'Welcome to Django Application!!\nThe list of the students present in your database: {s1}')
    return HttpResponse(f'Welcome to Django Application!!\nThe list of the students present in your database: {final_lst}')


def sample(request):
    return render(request, 'sample2.html')      # we have to save all html files in template folder inside our app that is a1


def home(request):
    return render(request, 'home.html')
