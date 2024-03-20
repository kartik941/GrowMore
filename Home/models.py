from django.db import models
from django.core.validators import EmailValidator, validate_email

class feedback(models.Model):
    user = models.CharField(max_length = 225)
    contact = models.BigIntegerField()
    email = models.EmailField()
    msg = models.CharField(max_length = 255)


    def __str__(self):
        return self.email

class reg(models.Model):
    fname = models.CharField(max_length=122)
    lname = models.CharField(max_length=122,null=False)
    email = models.EmailField()
    password = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.email


class con(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122,validators=[validate_email])
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.email

