from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
#import datetime
# cd=datetime.datetime.now().date;addedon=models.DateField(default=cd)


class usercomplaints(models.Model):
    # c=(
    #    ("M","Male"),("F","Female")
    # )
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=200)
    di = models.IntegerField(unique=True)
    sub = models.CharField(max_length=250)
    comp = models.TextField()
    addedon = models.DateField(auto_now_add=True)  # None
    # gender=models.CharField(max_length=10,choices=c)      #optional-->(,blank=True)
    # password=models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Complaint Table"

    # def __str__(self):   #wouldnt be neccessary if we are showing in tabel
    #    return self.name

    '''def __str__(self):
        return str(self.di) '''
    # def __str__(self):
    #   return self.name+" "+str(self.di)


'''class userprof(models.Model):                      #creates a table with name and his/her picture 
    name=models.CharField(max_length=250)
    pic=models.FileField(upload_to="profilespic/%Y/%m/%d")
    description=models.TextField()
    added_on=models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name              
'''


class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.IntegerField(unique=True)
    profie_pic = models.ImageField(
        upload_to="profiles", null=True)  # not working
    age = models.CharField(max_length=250, null=True)  # integer field
    amount = models.IntegerField(null=True)
    # age=models.Charield(max_length=250,nill=True,blank=True)
    # address=model.TextField(blank=True,null=True)
    # gender=models.CharField(max_length=250,null=True,blank=True)
    # added_on,update_on=models.DataTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class transfer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gbd = models.CharField(max_length=10, unique=True)
    value = models.IntegerField()
    user = models.CharField(max_length=15)
    pin = models.CharField(max_length=10)

    def __str__(self):
        return self.user
