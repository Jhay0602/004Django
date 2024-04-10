from django.db import models

# Create your models here.
class BaseModel (models.Model):
    created_at =models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at =models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
class College (BaseModel) :
    college_name = models.CharField (max_length=150)

    def _str_(self):
        return self.college_name

class Program (BaseModel) :
    prog_name = models.CharField (max_length=150)

    def _str_(self):
        return self.prog_name
    
class Organization(BaseModel):
    name = models.CharField(max_length= 250)
    college = models.ForeignKey(
    College, null=True, blank=True, on_delete=models.CASCADE
)
    description = models.CharField(max_length=500)

    def _str_(self):
        return self.self_name
    
class Student(BaseModel):
    student_id =models.CharField(max_length=15) 
    lastname =models.CharField(max_length=25) 
    firstname =models.CharField(max_length=25)
    middlename =models.CharField(max_length=25, blank=True, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.lastname}, {self.firstname}"
    
class Orgmember(BaseModel):
     student = models.ForeignKey(Student, on_delete=models.CASCADE)
     organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
     date_joined = models.DateField()

