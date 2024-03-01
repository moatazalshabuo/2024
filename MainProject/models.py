from django.db import models
import uuid
# Create your models here.

url = 'https://mapi.fezzantechx.ly'
class BesicData(models.Model):
    title = models.CharField(max_length=125)
    from_date = models.DateField()
    to_date = models.DateField(null=True,blank=True)
    about = models.TextField(null=True,blank=True)
    
class Organizers(models.Model):
    name = models.CharField(max_length=150)
    pic = models.ImageField(upload_to='Organizers/%Y/%m/%d/')
    face_link = models.CharField(max_length=125,null=True,blank=True)
    x_link = models.CharField(max_length=125,null=True,blank=True)
    web_site = models.CharField(max_length=125,null=True,blank=True)
    phone = models.CharField(max_length=125,null=True,blank=True)
    
    def get_img(self):
        if self.pic:
            return url+self.pic.url
        
class Shepherds(models.Model):
    name = models.CharField(max_length=150)
    pic = models.ImageField(upload_to='Shepherds/%Y/%m/%d/')
    face_link = models.CharField(max_length=125,null=True,blank=True,default='')
    x_link = models.CharField(max_length=125,null=True,blank=True,default='')
    web_site = models.CharField(max_length=125,null=True,blank=True,default='')
    type = models.CharField(max_length=125,choices=(('gold','gold'),('silver','silver'),('bronze','bronze')))
    
    def get_img(self):
        if self.pic:
            return url+self.pic.url
        

class Schedule(models.Model):
    title = models.CharField(max_length=120)
    descripe = models.TextField(null=True,blank=True,default='لم يتم اضافة تفاصيل ')
    from_time = models.CharField(max_length=6)
    to_time = models.CharField(max_length=6)
    day = models.DateField()
    
    
    
class Speakers(models.Model):
    name = models.CharField(max_length=150)
    pic = models.ImageField(upload_to='Speakers/%Y/%m/%d/')
    type = models.CharField(max_length=125,null=True,blank=True,default='')
    
    def get_img(self):
        if self.pic:
            return url+self.pic.url
        
class Booking(models.Model):
    Choise_suite = (
        ('A1',"A1"),
        ('A2',"A2"),
        ('A3',"A3"),
        ('A4',"A4"),
        ('B1',"B1"),
        ('B2',"B2"),
        ('B3',"B3"),
        ('B4',"B4"),
        ('B5',"B5"),
        ('B6',"B6"),
        ('S1',"S1"),
        ('C1',"C1"),
        ('G1',"G1"),
        )
    Status_Choice = ((1,"Hold"),(2,'accepted'),(3,'rejected'))
    Cname = models.CharField(max_length=50)
    Cno = models.FloatField()
    Cemail = models.EmailField(max_length=150)
    detiles = models.TextField(blank=True, null=True)
    Suite_number = models.CharField(max_length=10,choices=Choise_suite)
    status = models.IntegerField(choices=Status_Choice,blank=True,default=1)
    
class Project(models.Model):
    name = models.CharField(max_length=50)
    phone = models.FloatField()
    email = models.EmailField(max_length=254)
    project_title = models.CharField(max_length=100)
    project_type = models.CharField(max_length=100)
    universty = models.CharField(blank=True, null=True,max_length=100)
    status = models.IntegerField(default=1,blank=True, null=True)
    detiles = models.TextField(blank=True, null=True)
    class Meta:
        ordering = ["-id"]

class Gustis(models.Model):
    name = models.CharField(max_length=50)
    phone = models.FloatField(unique=True)
    id_user = models.CharField(max_length=25,blank=True, null=True)
    status = models.IntegerField(default=1,blank=True, null=True)
    email = models.EmailField(blank=True, null=True, max_length=254)
    
    
class Clouds(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=20,blank=True, null=True)
    descripe = models.TextField(blank=True, null=True)
    img = models.CharField(max_length=250,blank=True, null=True)
    status = models.IntegerField(default=0,blank=True, null=True)
    
class CloudsGustis(models.Model):
    clouds = models.ForeignKey(Clouds,on_delete=models.CASCADE)
    gusti = models.ForeignKey(Gustis,on_delete=models.CASCADE)
    status = models.BooleanField(default=False,blank=True, null=True)
    
class Players(models.Model):
    name = models.CharField(max_length=50)
    phone = models.FloatField(unique=True)
    status = models.IntegerField(default=1,blank=True, null=True)
    type = models.CharField(blank=True, null=True, max_length=254)
    