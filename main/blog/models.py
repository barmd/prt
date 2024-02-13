from django.db import models


#About personal information
class Info(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    image = models.ImageField(upload_to="articles/")
    file = models.FileField(upload_to="files/")
    phone = models.CharField(max_length=50)
    adress = models.TextField(max_length=300)
    spec = models.CharField(max_length=300)
    notes = models.TextField(max_length=600)
    bday = models.DateField(auto_now_add=False)
    
    
    def __str__(self):
        return self.name


#Expertise list infomation
class Expertise(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=50)
    notes = models.TextField(max_length=600)  
    desc = models.CharField(max_length=100)
    service = models.TextField(max_length=600)
    icon = models.TextField(max_length=600)

    def __str__(self):
        return self.name


#Links for social media
class Links(models.Model):
    name = models.CharField(max_length=100)
    url = models.TextField(max_length=400)
    icon = models.CharField(max_length=400)    

    def __str__(self):
        return self.name

#Information about education
class Education(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=50)
    notes = models.TextField(max_length=600)  

    def __str__(self):
        return self.name  


#Skills procents 
class Skills(models.Model):
    name = models.CharField(max_length=50)
    procent = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#Portfolio
class Portfolio(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=600)
    url = models.TextField(max_length=500)
    img = models.ImageField(upload_to="articles/")

    def __str__(self):
        return self.name

#Sertificates
class Sertificate(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField(max_length=700)
    image = models.ImageField(upload_to="article/")
    file = models.FileField(upload_to ="files/")

    def __str__(self):
        return self.name

#Contact
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.TextField(max_length=50)
    message = models.TextField(max_length=800)    

    def __str__(self):
        return self.name


