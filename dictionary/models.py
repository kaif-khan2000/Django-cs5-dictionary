from django.db import models

# Create your models here.
class semester(models.Model):
    sno = models.AutoField(primary_key=True)
    sem = models.IntegerField()

    def __str__(self):
        return ("sem: "+str(self.sem))

class subject(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 20)
    semester = models.ForeignKey('semester',on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + str(self.semester.sem) + " sem"
class module(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 20)
    desc = models.TextField(max_length=255)
    semester = models.ForeignKey('semester',on_delete=models.CASCADE)
    subject = models.ForeignKey('subject',on_delete=models.CASCADE)