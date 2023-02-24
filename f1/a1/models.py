from django.db import models

# Create your models here.
# Create your models here.
# orm model ---object relational mapper
# models file is used to interact with the database for creation of db create a class

# Model manager
# class ActiveStudent(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(is_active=True)

# class InactiveStudent(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(is_active=False)


# class Student(models.Model):             # this will creates a table
#     # id = models.IntegerField()        # no need to add this as django provides it by default
#     name = models.CharField(max_length=200)
#     age = models.IntegerField()
#     mobile = models.CharField(max_length=20)
#     address = models.CharField(max_length=200)
#     email = models.EmailField(null=True)
#     date_joined = models.DateTimeField(auto_now=True, null=True)
#     date_updated = models.DateTimeField(auto_now=True, null=True)
#     is_active = models.BooleanField(default=True)
#     activestud = ActiveStudent()
#     inactivesutd = InactiveStudent()
#     objects = models.Manager()                              # all_data instead of objects is recommended to avoid confusion while performing crud


#     class Meta:
#         db_table = 'student'

#     def __str__(self):
#         return f'{self.name}'

#     def show_details(self):
#         print(f'''----------------------------------------------------
# Name: {self.name}
# Age: {self.age}
# Mobile: {self.mobile}
# Address: {self.address}''')

#     @classmethod                                        # we use classmethod cuz we have to deal with multiple objects
#     def get_data_above_age(cls):
#         print(cls.objects.filter(age__gte=25))       # dunder methods associated with manager --> __gte, __gt, __lt, __lte, __startswith, __endswith, __contains

#     @classmethod
#     def get_avg_age(cls):
#         '''Average age of all students'''
#         all_stud_dict = cls.objects.all().values()
#         age_lst = list(map(lambda x: x['age'], all_stud_dict))
#         avg = sum(age_lst)//len(age_lst)
#         print('Average age of all students: ', avg)

#     @classmethod
#     def get_active_data(cls):
#         return cls.objects.filter(is_active=True)

#     @classmethod
#     def get_inactive_data(cls):
#         return cls.objects.filter(is_active=False)


# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
# student relationships

class CommonClass(models.Model):
    name = models.CharField(max_length=100, null=True)

    class Meta:
        abstract = True                # by defining this table of this class can't be created which we don't need

    def __str__(self):
        return f'{self.name}'


class College(CommonClass):
    adr = models.CharField(max_length=100, null=True)
    # est_date = models.DateField()

    class Meta:
        db_table = 'college'

    
class Principal(CommonClass):
    qual = models.CharField(max_length=10, null=True)
    exp = models.IntegerField(null=True)
    college = models.OneToOneField(College, on_delete=models.CASCADE, related_name='princi')
    class Meta:
        db_table = 'principal'


class Department(CommonClass):
    dept_str = models.IntegerField(null=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='depts')
    class Meta:
        db_table = 'department'
        unique_together = (('name', 'college'),)    # when we insert dept insertion will get repeating to avoid this we make name of dept and id of college as unique so that it wont be repeated

# once we have applied changes to meta class we need to makemigrations and migrate

class Student1(CommonClass):
    age = models.IntegerField(null=True)
    marks = models.IntegerField(null=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='studs')
    class Meta:
        db_table = 'student1'


class Subject(CommonClass):
    is_practical = models.BooleanField(null=True)
    student = models.ManyToManyField(Student1)
    # student = models.ManyToManyField('Subject.Student1')
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='subj')
    class Meta:
        db_table = 'subject'


# composite key is key which is duplicate and is not allowed in mysql will raise an err id name age of two stud should not  be same
# get models from database
# Entity relationship diagram or UML diagram we can use tool draw.io to make that diagram
# py manage.py inspectdb > test_models.py is command to get models from the table...it creates a test_models.py file and show models of the all tables there
# we can create a models of any database using inspectdb command for that we need to provide the name of the same database in settings file

# ---------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
# car and fuel type models relations many to many

# class FuelType(models.Model):
#     name = models.CharField(max_length=200)

#     class Meta:
#         db_table = 'fueltype'
    
#     def __str__(self):
#         return self.name

# class CarModel(models.Model):
#     name = models.CharField(max_length=200)
#     fuelType = models.ManyToManyField(FuelType, related_name='cm')

#     class Meta:
#         db_table = 'carmodel'
#     def __str__(self):
#         return self.name