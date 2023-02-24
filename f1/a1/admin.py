from django.contrib import admin
# from a1.models import *
from .models import *

# exec(open(r'F:\B8\DjangoP\f1\a1\dbshell.py').read())
# Register your models here.
admin.site.register([College, Principal, Department, Student1, Subject])
