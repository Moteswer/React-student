from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    CLASS_CHOICES = (
        ('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'), ('V', 'V'),
        ('VI', 'VI'), ('VII', 'VII'), ('VIII', 'VIII'), ('IX', 'IX'),
        ('X', 'X'), ('XI', 'XI'), ('XII', 'XII'),
    )
    class_level = models.CharField(max_length=5, choices=CLASS_CHOICES,default = '')
    division = models.CharField(max_length=5)
    
    GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'))
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name
