from django.db import models


class item(models.Model):

    Status = [
        ('none','None'),
        ('genshin impact','Genshin Impact'),
        ('honkai Starial','Honkai Starial'),
        ('honkai implact3rd','Honkai implact3rd'),

    ]

    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image_relative_url_0 = models.CharField(max_length=300, null=True,blank=True)
    image_relative_url_1 = models.CharField(max_length=300, null=True,blank=True)
    image_relative_url_2 = models.CharField(max_length=300, null=True,blank=True)
    image_relative_url_3 = models.CharField(max_length=300, null=True,blank=True)
    image_relative_url_4 = models.CharField(max_length=300, null=True,blank=True)
    image_relative_url_5 = models.CharField(max_length=300, null=True,blank=True)
    GameName = models.CharField(max_length=20, choices=Status ,default='none')  
    description = models.TextField(null=True,blank=True)
    full_des = models.TextField(null=True,blank=True)
    addtime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name






class ContactMesssage (models.Model):
    title = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    detial = models.TextField(blank=True, null=True)
    sendtime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class blog(models.Model):
    
    Status = [
        ('none','None'),
        ('genshin impact','Genshin Impact'),
        ('honkai Starial','Honkai Starial'),
        ('honkai implact3rd','Honkai implact3rd'),
        ('other','Other')
    ]

    name = models.CharField(max_length=60)
    writer = models.CharField(max_length=60)
    image_relative_url_blog = models.CharField(max_length=300, null=True,blank=True)
    gamename = models.CharField(max_length=20, choices=Status ,default='none')  
    mini_description = models.TextField(max_length=50 ,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    addtime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
# Create your models here.
