# from app1.models import Student
from a1.models import *
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model                # Attrubute err fun has no att objects in py3.10
# User = get_user_model                                         # key err as __name__not in globals


# from .admin import admin
# ----------------------------------------------
# to execute python scripts in django shell 
# exec(open(r'F:\B8\PyDjangoProject\my_first_django_project\app1\dbshell.py').read())
# ----------------------------------------------

# to get all data from the database
# all_stud = Student.objects.all()              #student is the class name, objects is manager, all is to fetch the all data from the database
# print(all_stud)                               # returns result in queryset
# print(list(all_stud))                          # returns result in list of objects

# for i in all_stud:
#     print(i)
#     # print(i.__dict__)

# ---------------------------------------------

# get a record by id
# per3 = Student.objects.get(id=3)
# print(per3)

# try:
#     per6 = Student.objects.get(id=6)
#     print(per6)
# except Student.DoesNotExist:
#     print('Student does not exists')


# -------------------------------------------------

# get the records with same age
# # returns the records whose age is 25
# per = Student.objects.filter(age=25)
# print(list(per))
# print(per.query)                                                  # to check the query of the given stmt.

# per = Student.objects.get(id=1, address='pune')                   # output-->Saya
# print(per)

# per = Student.objects.filter(id=1, address='pune')                # output--> <QuerySet [<Student: Saya>]>  
# print(per)                                                        # here , means and. Both the conditions must be true

# -----------------------------------------------

# modify or update existing record
# p1 = Student.objects.get(id=1)                                # first fetch the record
# p1.address = 'Pune'                                           # assign the new value
# print(p1.__dict__)                                            # check whether changes applied 
# p1.save()                                                     # save the changes to get applied in the database

# ------------------------------------------------

# delete the record from the database
# p5 = Student.objects.get(id=5)
# p5.delete()

# -----------------------------------------------
#  way to add or insert data to the database
# s1 = Student(id=5, name='Kavya', age=24, mobile=9845123678, address='Pune')
# s1.save()

# ------------------------------------------------

# another way to insert record in database using create. Here no need to save data explicitely it saved automatically by create method
# Student.objects.create(id=6, name='Shravan', age=23, mobile=9855213786, address='Panvel')

# -------------------------------------------------

#  to know the methods of manager
# print(dir(Student.objects))
"""
'_update', 'aggregate', 'alias', 'all', 'annotate', 'auto_created', 'bulk_create', 'bulk_update', 'check', \
'complex_filter', 'contribute_to_class', 'count', 'create', 'creation_counter', 'dates', 'datetimes', 'db', \
'db_manager', 'deconstruct', 'defer', 'difference', 'distinct', 'earliest', 'exclude', 'exists', 'explain', 'extra',\
'filter', 'first', 'from_queryset', 'get', 'get_or_create', 'get_queryset', 'in_bulk', 'intersection', 'iterator',\
'last', 'latest', 'model', 'name', 'none', 'only', 'order_by', 'prefetch_related', 'raw', 'reverse', 'select_for_update',\
'select_related', 'union', 'update', 'update_or_create', 'use_in_migrations', 'using', 'values', 'values_list'

"""

# -------------------------------------------------

# insert multiple records using bulk create
# s7 = Student(id=7, name='Trisha', age=22, mobile=9842663678, address='Pune')
# s8 = Student(id=8, name='Bhavana', age=29, mobile=7255123678, address='Nashik')
# s9 = Student(id=9, name='Nidhi', age=27, mobile=8945123678, address='Mumbai')
# s10 = Student(id=10, name='Anand', age=28, mobile=9845124562, address='Nanded')

# Student.objects.bulk_create([s7, s8, s9, s10])

# -------------------------------------------------

# to count the number of records present in the database
# print(Student.objects.count())

# -------------------------------------------------

# to delete all records
# Student.objects.all().delete()

# -------------------------------------------------

# To delete multiple records
# Student.objects.filter(age=25).delete()

# -------------------------------------------------
# check the name is present or not which starts and ends with the perticular letter
# print(Student.objects.filter(name__startswith='R'))
# print(Student.objects.filter(name__startswith='a'))
# print(Student.objects.filter(name__endswith='a'))
# print(Student.objects.exclude(name__startswith='S'))
# print(Student.objects.exclude(name__endswith='a'))

# --------------------------------------------------
# check whether perticular records exists or not
# print(Student.objects.filter(id=1).exists())
# print(Student.objects.filter(id=11).exists())
# print(Student.objects.filter(name='Nivya').exists())
# print(Student.objects.filter(name='Siya').exists())

# -------------------------------------------------      
# arrange the records in a particular sequence               
# print(Student.objects.all().order_by('id'))                             # ascending order of ids
# print(Student.objects.all().order_by('-id'))                            # reverse or descending order of ids
# print(Student.objects.all().order_by('name'))                            # ascending order of names 
# print(Student.objects.all().order_by('-name'))                           # order descending order of names

# -------------------------------------------------
#  we will get this all things in django orm cookbook
# -------------------------------------------------

# to fetch the details of a specific person or student using a user defined method show_details
# Student.objects.get(id=1).show_details()

#  to fetch the details of all students in details
# all_stud = Student.objects.all()
# for stud in all_stud:                                  # we can also use this too for stud in Student.objects.all() 
#     stud.show_details()

# ------------------------------------------------
# get data above specific age limit
# Student.get_data_above_age()

# to check and tally the records 
# all_stud = Student.objects.all()
# for stud in all_stud:
#     print(stud.__dict__)

# -------------------------------------------------
# to know the users information
# we have to import ----> from django.contrib.auth.models import User
# user_data = User.objects.all()
# print(user_data)                                        # res in queryset
# print(list(user_data))                                  # res in list containing objects
# ---------------------------------------------------

#  to create user and superuser
# User.objects.create_user(username='Parth', password='Admin@123')
# #User.objects.create_superuser(username=, password=, email=)

# -----------------------------------------------------
# __contains                                            # returns the name which contains given letter
# print(Student.objects.filter(name__contains='y'))

# -----------------------------------------------------
# all_stud_dict = Student.objects.all().values()
# print(list(all_stud_dict))

# for stud in all_stud_dict:
#     print(stud, type(stud))                              # record in a dict and type as dict

# -----------------------------------------------------------
#  if we want specific fields like id name and age

# all_stud_dict = Student.objects.all().values('id', 'name', 'age')         # returns queryset of dict of all records
# print(list(all_stud_dict))                                                returns list of dict of all records

# name_list = []
# for i in all_stud_dict:
#     # name_list.append(i['name'])
#     name_list.append(i.get('name'))
# print(name_list)

# id_lst = []
# for i in all_stud_dict:
#     id_lst.append(i['id'])
# print(id_lst)

# -----------------------------------------------------------
# Three ways to calculate average age of all students
# age_lst = []
# all_stud_dict = Student.objects.all().values('id', 'name', 'age')
# for i in all_stud_dict:
#     age_lst.append(i['age'])
# print(age_lst)
# avg = sum(age_lst)//len(age_lst)
# print(f'Average age of all students: {avg}')

# another way to calculate an avg
# all_stud_dict = Student.objects.all().values()
# # print(all_stud_dict)
# age_lst = list(map(lambda x: x['age'], all_stud_dict))
# # print(age_lst)
# avg = sum(age_lst)//len(age_lst)
# print(f'Average age of all students: {avg}')


# by defining a classmethod to calculate an avg we can simply call that function to get the result 
# Student.get_avg_age()

# -----------------------------------------------------------
# all_records = Student.objects.all().values_list()       # returns query set of list of tuples
# print(list(all_records))                                # returns list of tuples
# for i in all_records:
#     print(i)

# ------------------------------------------------------------
#------------------------------------------------------------
# database changed to mysql
# press ctrl+Z to come out of the shell and again run the changes
# first google mysql database settings for django write code for connection in settings.py before migrating create a database with the same name as we given in settings.py
# then in console py manage.py check to check for conn establishment
# if showed an err for mysqlclient we need to install as pip install mysqlclient and again confirm using check
# No need to makemigrations as we didn't change in models.just use py manage.py migrate to migrate data to the database
# then create a superuser to insert data using UI
# we can use command as User.objects.create_superuser()

# User.objects.create_user(username='Bhavi', password='Admin@123', email='bhavi@gmail.com')
# to get all records
# print(Student.objects.all())


# ways to update the is_active field means if it is inactive means soft deleted the record and if removed entirely then it is hard delete
# data = Student.objects.filter(id__in[3, 5])
# data[0].is_active = False
# data[1].is_active = True

# s1 = Student.objects.get(id=2)
# s1.is_active = False
# s1.save()

# data = Student.objects.filter(id__in=[3, 5])
# for i in data:
#     i.is_active = False
#     i.save()

# -------------------------------------------------
# update query in django

# Student.objects.filter(id__in=[3, 5]).update(is_active=False)

# --------------------------------------------------
# by defining get active and inactive data method we can just call that methods here to get the res
# print(Student.get_active_data())
# print(Student.get_inactive_data())

# ---------------------------------------------------
# model manager         # Once have created mm classes and obj come out of shell and then run py script 
# print(Student.activestud.all())                             # returns all inactive data
# print(Student.inactivesutd.all())                         # returns all active data
# print(Student.objects.all())                              # returns all records both active and inactive also


# to create a record using model manager(active class obj.)
# Student.activestud.create(id=6, name='Raj', age=21, mobile='7865445232', address='Pune')

# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------

#  Relationships project
clgs = College.objects.all()
princi = Principal.objects.all()
dept = Department.objects.all()
studs = Student1.objects.all()
subjs = Subject.objects.all()
# print(list(clgs), '\n', list(princi), '\n', list(dept), '\n', list(studs), '\n', list(subjs))

# dept = Department.objects.all()
# for dept in dept:
#     print(dept)
#     # print(dept.__dict__)
# print()

# clg = clgs[0]                                       # clg se princi fetch karana easy to fetch data in onetoone field
# clg = College.objects.first()
# print(clg.principal)                                     # only returns the name of princi
# print(clg.princi.__dict__)                             # returns the dict of princi


# princi = Principal.objects.first()                         # to fetch college using principal princi is the obj of principal
# print(princi.college)                                      # we can fetch college using obj of principal i.e princi

# to know the methods of clg we can simply print dir(clg)
# print(dir(College))

# dept = Department.objects.first()                       # department se college fetch karana hai
# print(dept.college)

# department se students fetch karana
# dept = Department.objects.first()
# print(f'Student of {dept} department: {list(dept.student1_set.all())}')
# print(f'Department Name: {dept.name}, students: {list(dept.student1_set.all())}')

# depts = Department.objects.all()
# dept = depts[1]
# print(f'Student of {dept} department: {list(dept.student1_set.all())}')

# dept = depts[2]
# print(f'Student of {dept} department: {list(dept.student1_set.all())}')


# to make a dict of department with students 
# d = {}
# depts = Department.objects.all()
# for dept in depts:
#     d[dept.name] = list(dept.student1_set.all())
# print(d)

#  student se department fetch karna 
# s1 = Student1.objects.first()
# print(s1.dept)                                      # we have used dept var in student1 class to define a relation

# studs = Student1.objects.all()
# s4 = studs[3]
# print(s4.dept)

# s7 = studs[6]
# print(s7.dept)

# to make a dict of all studs with their department
# def stud_dept_dict():
# studs = Student1.objects.all()
# stud_dept_dict = {}
# for stud in studs:
#     # stud_dept_dict[stud.name] = stud.dept
#     stud_dept_dict[stud.name] = stud.dept.name
# print(stud_dept_dict)

# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# Using related_name
# try to saggregate all students according to depts in a specific list for that create a new python file and type code in that
# to avoid using department_set.all student_set.all we have to pass related_name as a parameter in models.py file

# college se prici
# clg = College.objects.get(id=1)
# print(clg.princi)


# # college se depts
# print(clg.depts.all())


# # Department se students
# dept = Department.objects.get(id=1)
# print(dept.studs.all())

# dept = Department.objects.get(id=2)
# print(dept.studs.all())

# dept = Department.objects.get(id=3)
# print(dept.studs.all())


# # students se dept
# stud_dic = {}
# stud = Student1.objects.filter(id__in=[1, 2, 3])
# for s in stud:
#     stud_dic[s] = s.dept.name    
# print(stud_dic)


# stud_dic = {}
# stud = Student1.objects.filter(id__in=[4, 5, 6])
# for s in stud:
#     stud_dic[s] = s.dept.name    
# print(stud_dic)


# stud_dic = {}
# stud = Student1.objects.filter(id__in=[7, 8, 9])
# for s in stud:
#     stud_dic[s] = s.dept.name    
# print(stud_dic)


# # dept se subj
# dept = Department.objects.get(id=1)
# print(f'subjects of {dept} are : {list(dept.subjs.all())}')

# dept = Department.objects.get(id=2)
# print(f'subjects of {dept} are : {list(dept.subjs.all())}')

# dept = Department.objects.get(id=3)
# print(f'subjects of {dept} are : {list(dept.subjs.all())}')

# dept = Department.objects.all()
# for dep in dept:
#     print(list(dep.subjs.all()))

# using list comprehension we get list of all subjs at a time
# lst = [list(dep.subjs.all()) for dep in Department.objects.all()]
# print(lst)


# # subj se students 
# subj = Subject.objects.get(id=1)
# print(subj.student.all())

# subj se dept 
# subj = Subject.objects.get(id=2)
# print(subj.dept)

# # clg se students          Err in this please resolve
# clg = College.objects.get(id=1)
# clg = College.objects.first()
# print(clg.depts.all()[0].studs.all())
# print(clg.depts.all()[1].studs.all())
# print(clg.depts.all()[2].studs.all())

# stud_lt = []
# for i in clg.depts.all():
#     stud_lt.extend(i.studs.all())           # if we use append here it will return queryset as it is so we use extend to make it return a list
# print(stud_lt)
# using lst comprehension

# lst = [list(i.studs.all()) for i in clg.depts.all()]
# print(lst)

# # to fetch college name from student .where there is no connection between stud and college directly, students se college name fetch karna hai

# s1 = Student1.objects.get(id=4)
# print(s1.dept.college.name)                         # stud has dept and college has name reverse directions

# s1 = Student1.objects.get(id=1)
# print(s1.dept)
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
#  # Insertion of data into database
# insert college 
# College.objects.create(name='COEP', adr='Pune')           # no need to save it explicitely

# insert princi
# c1 = College.objects.get(id=2)
# # p1 = Principal(name='Divya', qual='PHD', exc=10, college_id=2)          # we can directly pass clg id or else use clg obj
# p1 = Principal(name='Divya', qual='PHD', exp=10, college=c1)
# p1.save()                                                                # as we are creating an obj of a class need to save it 

# insert dept
# c1 = College.objects.get(id=2)
# d = Department(name='Production', dept_str=70, college=c1)
# d.save()

# insert student
# d4 = Department.objects.get(id=4)
# Student1.objects.create(name='Rita', age=23, marks=79, dept=d4)
# Student1.objects.create(name='Prisha', age=22, marks=88, dept=d4)
# Student1.objects.create(name='Spruha', age=21, marks=87, dept=d4)


# d = Department.objects.get(id=4)
# print(dir(d.studs))
"""
'_update', 'add', 'aggregate', 'alias', 'all', 'annotate', 'auto_created', 'bulk_create', 'bulk_update', \
'check', 'complex_filter', 'contribute_to_class', 'core_filters', 'count', 'create', 'creation_counter', 'dates', \
'datetimes', 'db', 'db_manager', 'deconstruct', 'defer', 'difference', 'distinct', 'do_not_call_in_templates', \
'earliest', 'exclude', 'exists', 'explain', 'extra', 'field', 'filter', 'first', 'from_queryset', 'get', 'get_or_create', \
'get_prefetch_queryset', 'get_queryset', 'in_bulk', 'instance', 'intersection', 'iterator', 'last', 'latest', 'model',\
 'name', 'none', 'only', 'order_by', 'prefetch_related', 'raw', 'reverse', 'select_for_update', 'select_related', 'set',\
 'union', 'update', 'update_or_create', 'use_in_migrations', 'using', 'values', 'values_list'
"""

# s1, s2, s3 = Student1.objects.filter(id__gt=9)                        #list unpacking
# d = Department.objects.get(id=4)                            # way to add students in one dept that is one to many
# d.studs.add(s1, s2, s3)

# try for remove

# ---------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------
# please uncomment logger for this 
# if we use logger in settings file and run following code it will display the query in details
# all_studs = Student1.objects.all()[0]       #gives or returns name of the first record
# print(all_studs)

# all_studs = Student1.objects.all()[0:3]         # returns first 3 records as stops at 3, 0th, 1st and 2nd
# print(all_studs)

# all_studs = Student1.objects.all()[6]             # returns 7th record as starting counting from 0  
# print(all_studs)

# all_studs = Student1.objects.all()[10]              # returns 11 th record
# print(all_studs)

# student se dept
# all_studs = Student1.objects.all()                  # displays all depts of all students but with different different queries means using so many queries to display one stmt res
# for stud in all_studs:                              # to overcome this drawback we must use select_related in which it returns the same res with only one query
#     print(stud.dept)            


# ---------------------------------------------------------------------------
# SELECT RELATED 
# STUDENT se DEPT  fetch karna using selected_related
# student se dept fetch karna hai
# all_studs = Student1.objects.select_related('dept')   # saves execution time of a program by using only one query 
# for stud in all_studs:
#     print(stud.dept)

'''
select department.id, department.name, department.dept_str
from department 
inner join student1
on department.id = student1.dept_id
'''
# -----------------------------------------------------------------------------------
# fetch students based on following 
# print(Student1.objects.filter(dept__id=1))
# print(Student1.objects.filter(dept__college__name='COEP'))
# print(Student1.objects.filter(dept__college__name__startswith='P'))
# print(Student1.objects.filter(dept__college__name__in=['COEP', 'PCCOE']))
# -------------------------------------------------------------------------------
# try for many to many for students and subjects                        

# # # # subj se students 
# sub1 = Subject.objects.get(id=1)
# # print(sub1.student.all())                       # without using related name
# print(sub1.dept.studs.all())                       # with using realted name

# # student se subjects
# s1 = Student1.objects.get(id=1)
# # print(stud.subject_set.all())      # without using related name
# print(s1.dept.subj.all())        # with using related name

# ----------------------------------------------------------
# ----------------------------------------------------------

# many to many carmodels and fueltype
#  to add carmodels to the database
# c100 = CarModel.objects.create(name='c100')
# c200 = CarModel.objects.create(name='c200')
# c300 = CarModel.objects.create(name='c300')

# print(CarModel.objects.all())

# add fueltype to the database
# gas = FuelType.objects.create(name='gas')
# diesel = FuelType.objects.create(name='diesel')
# hybrid = FuelType.objects.create(name='hybrid')

# print(FuelType.objects.all())


# c100 = CarModel.objects.get(id=1)
# c200 = CarModel.objects.get(id=2)
# c300 = CarModel.objects.get(id=3)
# all_fuels = FuelType.objects.all()
# for f in all_fuels:
#     # c100.fuelType.add(f)
#     c200.fuelType.add(f)
#     c300.fuelType.add(f)

# another way to add or insert fueltype 
# c100 = CarModel.objects.get(id=1)
# c100.fuelType.create(name='Bio Diesel')

# without using related_name
# to car model se fuel fetch karna ah
# c100 = CarModel.objects.get(id=1)
# print(c100.fuelType.all())

# c200 = CarModel.objects.get(id=2)
# print(c200.fuelType.all())

# c300 = CarModel.objects.get(id=3)
# print(c300.fuelType.all())

# fueltype se carmodel fetch karna
# gas = FuelType.objects.get(id=1)
# print(gas.carmodel_set.all())                           # always use class name in lowercase
# output
# <QuerySet [<CarModel: c100>, <CarModel: c200>, <CarModel: c300>]>


# biodiesel = FuelType.objects.get(id=4)
# print(biodiesel.carmodel_set.all())
# # output
# <QuerySet [<CarModel: c100>]>

# using realated_name
# biodiesel = FuelType.objects.get(id=4)
# print(biodiesel.cm.all())
# output
# <QuerySet [<CarModel: c100>]>

# fetch carmodels
# print(CarModel.objects.filter(fuelType__name__startswith='g'))      # carmodel ke pass fuelType hai so we can use of it 
# output
# <QuerySet [<CarModel: c100>, <CarModel: c200>, <CarModel: c300>]>


# fueltype fetch karna  
# print(FuelType.objects.filter(cm__name__startswith='c'))            # fueltype ke pass carmodel nahi hai but carmodel ke pass fueltype hai so we can use related name in this case
# output
# <QuerySet [<FuelType: gas>, <FuelType: diesel>, <FuelType: hybrid>, <FuelType: Bio Diesel>, <FuelType: gas>, <FuelType: die
# sel>, <FuelType: hybrid>, <FuelType: gas>, <FuelType: diesel>, <FuelType: hybrid>]>


# fetch fueltype
# print(FuelType.objects.filter(cm__name__startswith='c').distinct())  # it considers only one among those fueltypes are repeating
# output
# <QuerySet [<FuelType: gas>, <FuelType: diesel>, <FuelType: hybrid>, <FuelType: Bio Diesel>]>


# fetch fueltype
# print(FuelType.objects.filter(cm__name='c300'))
# output
# <QuerySet [<FuelType: gas>, <FuelType: diesel>, <FuelType: hybrid>]>

# distinct ----- gives only single occurence of two values which are same, means removes duplicates
# group_concat ----- gives all values in a row separated by comma



# remove fueltypes of carmodels
# c100 = CarModel.objects.get(id=1)
# gas = FuelType.objects.get(id=1)
# c100.fuelType.remove(gas) 
# print(c100.fuelType.all())

# c200 = CarModel.objects.get(id=2)
# # gas = FuelType.objects.get(id=1)
# diesel = FuelType.objects.get(id=2)
# hybrid = FuelType.objects.get(id=3)
# c200.fuelType.remove(diesel, hybrid)
# print(c200.fuelType.all())


# delete carmodels
# car3 = CarModel.objects.get(id=3)         # car model no 3 will get deleted
# car3.delete()

# car2 = CarModel.objects.filter(fuelType__name__startswith='B')        # car model no 1 gets deleted as contains fuel with name biodiesel
# car2.delete()

# clear the relation set of two tables  
# c200 = CarModel.objects.get(id=2)
# c200.fuelType.clear()

# to set the relation set again 
# c200 = CarModel.objects.get(id=2)
# diesel = FuelType.objects.get(id=2)
# hybrid = FuelType.objects.get(id=3)
# c200.fuelType.set([diesel, hybrid])


# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------
# django orm is orm for django.. orm is object relational mapper which allows us to interact with database
# yes we can also perform direct query in python django to interact with database for that we have to import connection from django.db
# sqlalchemy is the orm for flask framework

# Perform direct sql query in django to fetch the records from the database
#  this is called raw sql because we are using here only sql queries instead of orm queries
# from django.db import connection
# cursor = connection.cursor()                        # this will considers default database from settings.py stud_relations

# one way to fetch data using query 
# cursor.execute('''select * from student1;''')       # this will returns all records from student1 table   
# data = cursor.fetchall()
# print(data)
# output
'''
((1, 21, 78, 1, 'Kavya'), (2, 22, 77, 1, 'Bhavi'), (3, 22, 78, 1, 'Sakshi'), \
(4, 23, 78, 2, 'Chetana'), (5, 21, 67, 2, 'Sai'), (6, 23, 89, 2, 'Nidhi'), (7, 22, 78, 3, 'Kaviraj'), \
(8, 21, 87, 3, 'Ruhi'), (9, 22, 85, 3, 'Devansh'), (10, 23, 79, 4, 'Rita'), (11, 22, 88, 4, 'Prisha'), \
(12, 21, 87, 4, 'Spruha'))
'''

# cursor.execute('''select * from student1;''') 
# data = cursor.fetchmany(3)                      # this will returns first two recrds from the student1 table
# print(data)
# output
# ((1, 21, 78, 1, 'Kavya'), (2, 22, 77, 1, 'Bhavi'))


# cursor.execute('''select * from student1;''')
# data = cursor.fetchmany(2)                      # this will again returns next two records from the same table
# print(data)
# output
# ((3, 22, 78, 1, 'Sakshi'), (4, 23, 78, 2, 'Chetana'))

# another way to fetch data using queries
# data = Student1.objects.raw('select * from student1')
# for stud in data:
#     print(stud.__dict__)


# -----------------------------------------------------------------------------------------------------------
# IMPORTANT KEY POINTS:
# multitenanat application in this we are using multiple databases in a same app.. for that we have to provde settings in settings file
# after that have to migrate the newly defined database before that we need to hit command py manage.py check to check everything whether ok or not
# then run py manage.py migrate --database='name of newly defined databse'
# after migrating database we need to first insert some records in it using create
# database router --- if we use this we dont need to use using
# when we use multiple databases in our project when we insert data from UI it will get inserted into the default database
# if we want to insert data in other or extra db we want to insert it explicitely with "using" method
# if we dont want to use using everytime then we have to use db setting which includes router setting


# SECOND_DATABASE = 'extra_db'
# once we have used new db we have to migrate the models on that db using py manage.py migrate --database=name of the new db
# data = Student1.objects.using(SECOND_DATABASE).all()
# print(list(data)) 

# princ = Principal.objects.using(SECOND_DATABASE).all()
# print(princ)


# To insert data into the extra db that is sqlite3 we have used that as second_db

# to insert college
# c1 = College.objects.using(SECOND_DATABASE).create(name='PCCOE', adr='Akurdi')              


# to insert principal
# c1 = College.objects.using(SECOND_DATABASE).get(id=1)                                        
# p1 = Principal.objects.using(SECOND_DATABASE).create(name='Lalita', qual='PHD', exp=10, college=c1)
# # p1 = Principal.objects.using(SECOND_DATABASE).create(name='Lalita', qual='PHD', exp=10, college_id=1)


# to insert the dept
# c1 = College.objects.using(SECOND_DATABASE).get(id=1)
# d1 = Department.objects.using(SECOND_DATABASE).create(name='IT', dept_str=60, college=c1)   
# d2 = Department.objects.using(SECOND_DATABASE).create(name='CSE', dept_str=60, college=c1)


# to insert students
# d1 = Department.objects.using(SECOND_DATABASE).get(id=1)
# s1 = Student1.objects.using(SECOND_DATABASE).create(name='Siya', age=21, marks=89, dept=d1) 
# s2 = Student1.objects.using(SECOND_DATABASE).create(name='Rita', age=23, marks=85, dept=d1)
# s3 = Student1.objects.using(SECOND_DATABASE).create(name='Prisha', age=22, marks=74, dept=d1)


# d2 = Department.objects.using(SECOND_DATABASE).get(id=2)
# s4 = Student1.objects.using(SECOND_DATABASE).create(name='Harsh', age=21, marks=67, dept=d2)
# s5 = Student1.objects.using(SECOND_DATABASE).create(name='Yash', age=22, marks=90, dept=d2)
# s6 = Student1.objects.using(SECOND_DATABASE).create(name='Archit', age=23, marks=80, dept=d2)


# to insert subjects
# d1 = Department.objects.using(SECOND_DATABASE).get(id=1)
# sb1 = Subject.objects.using(SECOND_DATABASE).create(name='Data Science',is_practical=True, dept=d1)
# sb2 = Subject.objects.using(SECOND_DATABASE).create(name='Computer Programming',is_practical=True, dept=d1)

# d2 = Department.objects.using(SECOND_DATABASE).get(id=2)
# sb3 = Subject.objects.using(SECOND_DATABASE).create(name='Operating System', is_practical=True, dept=d2)
# sb4 = Subject.objects.using(SECOND_DATABASE).create(name='Machine Learning', is_practical=True, dept=d2)

