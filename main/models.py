import sys
from django.db import models
from django.utils.timezone import now
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from datetime import date

subcategory_choices=(('categorya', 'Category A'),
                     ('categoryb', 'Category B'),
                     ('categoryc', 'Category C'),
                     ('categorybc', 'CategoryB/C')
                     )
category_choices = (('synopsis', 'Synopsis '),
                     ('nonsynopsis', 'Non-Synopsis '),
                     )

class about(models.Model):
    intro = models.TextField(default="", null=True, blank=True)
    images = models.ImageField(upload_to='media', default="", null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.images = self.compressImage(self.images)
        super(about, self).save(*args, **kwargs)

    def compressImage(self,images):
        imageTemproary = Image.open(images)
        imageTemproary = imageTemproary.convert('RGB')
        outputIoStream = BytesIO()
        imageTemproary.save(outputIoStream , format='JPEG', quality=60)
        outputIoStream.seek(0)
        images = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % images.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return images

    def __str__(self):
        return self.intro

class director(models.Model):
    name = models.CharField(max_length=500,default="")
    text = models.TextField(default="")
    designation = models.CharField(max_length=500,default="")
    images = models.ImageField(upload_to='media', default="")

    def save(self, *args, **kwargs):
        if not self.id:
            self.images = self.compressImage(self.images)
        super(director, self).save(*args, **kwargs)

    def compressImage(self,images):
        imageTemproary = Image.open(images)
        imageTemproary = imageTemproary.convert('RGB')
        outputIoStream = BytesIO()
        imageTemproary.save(outputIoStream , format='JPEG', quality=60)
        outputIoStream.seek(0)
        images = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % images.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return images

class img_slider(models.Model):
    images = models.ImageField(upload_to='gallery', default="")
    caption = models.CharField(max_length=500,default="", null=True, blank=True)
    pub_date = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        if not self.id:
            self.images = self.compressImage(self.images)
        super(img_slider, self).save(*args, **kwargs)

    def compressImage(self,images):
        imageTemproary = Image.open(images)
        imageTemproary = imageTemproary.convert('RGB')
        outputIoStream = BytesIO()
        imageTemproary.save(outputIoStream , format='JPEG', quality=70)
        outputIoStream.seek(0)
        images = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % images.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return images

    class Meta:
        ordering = ['-pub_date',]

class staff(models.Model):
    name = models.CharField(max_length=500,default="")
    designation = models.CharField(max_length=1000,default="")
    contact = models.CharField(max_length=1500,default="", null=True, blank=True)

    def __str__(self):
        return self.name

class faq(models.Model):
    question = models.TextField(default="")
    answer = models.TextField(default="")

    def __str__(self):
        return self.question

class feedback(models.Model):
    name = models.CharField(max_length=500,default="")
    email = models.CharField(max_length=1000,default="")
    subject = models.CharField(max_length=1500,default="")
    message = models.TextField(default="")
    posting_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

class guideline(models.Model):
    text = models.TextField(default="")

    def __str__(self):
        return self.text

class announcement(models.Model):
    text = models.TextField(default="")
    image = models.ImageField(upload_to='media', default="", null=True, blank=True)
    file = models.FileField(upload_to='files', default="", null=True, blank=True)
    pub_date = models.DateField(default=now)
    time = models.TimeField(default=now)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-pub_date','-time']

class sop(models.Model):
    title = models.CharField(max_length=80,default="")
    Description = models.CharField(max_length=120,default="", null=True, blank=True)
    file = models.FileField(upload_to='sops', default="")
    pub_date = models.DateTimeField(default=now)

    class Meta:
        ordering = ['-pub_date',]

    def __str__(self):
        return self.title

class certificate(models.Model):
    title = models.CharField(max_length=80,default="")
    Description = models.CharField(max_length=120,default="", null=True, blank=True)
    file = models.FileField(upload_to='certificates', default="")
    pub_date = models.DateTimeField(default=now)

    class Meta:
        ordering = ['-pub_date',]

    def __str__(self):
        return self.title

class gallery(models.Model):
    images = models.ImageField(upload_to='gallery', default="")
    caption = models.CharField(max_length=500,default="", null=True, blank=True)
    pub_date = models.DateTimeField(default=now)

    class Meta:
        ordering = ['-pub_date',]

    def save(self, *args, **kwargs):
        if not self.id:
            self.images = self.compressImage(self.images)
        super(gallery, self).save(*args, **kwargs)

    def compressImage(self,images):
        imageTemproary = Image.open(images)
        imageTemproary = imageTemproary.convert('RGB')
        outputIoStream = BytesIO()
        imageTemproary.save(outputIoStream , format='JPEG', quality=50)
        outputIoStream.seek(0)
        images = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % images.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return images

class project(models.Model):
    author = models.CharField(max_length=1500,default="",null=True, blank=True)
    title = models.CharField(max_length=1500,default="")
    category =models.CharField(max_length=150, choices=category_choices, default="")
    subcategory =models.CharField(max_length=150, choices=subcategory_choices, default="")
    description = models.TextField(default="",null=True, blank=True)
    file = models.FileField(upload_to='projects', default="", null=True, blank=True)
    pub_date = models.DateTimeField(default=now)

    class Meta:
        ordering = ['-pub_date',]

    def __str__(self):
        return self.title

class event(models.Model):
    title = models.CharField(max_length=1500,default="")
    description = models.TextField(default="",null=True, blank=True)
    venue = models.CharField(max_length=5000,default="")
    eventdate = models.DateField()
    time = models.TimeField( default="", null=True, blank=True)

    def __str__(self):
        return self.title

    def month(self):
        return self.eventdate.strftime('%b')

    def year(self):
        return self.eventdate.strftime('%Y')

    def dateday(self):
        return self.eventdate.strftime("%d")

    class Meta:
        ordering = ['-eventdate','time']
