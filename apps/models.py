from django.db import models

# Create your models here.
from apps.storage import generate_img_path, fss_share


class Overview(models.Model):
    pass


class Research(models.Model):
    title = models.CharField(max_length=256,null=False,blank=True,verbose_name="research title")
    file = models.FileField(storage=fss_share, upload_to=generate_img_path, null=True, verbose_name="视频文件")
    shortDescription = models.TextField(null=False,blank=True,verbose_name="shortly description")
    longDescription = models.TextField(null=False,blank=True,verbose_name="long description")
    member = models.ManyToManyField('Member', related_name="research", verbose_name="member")


class Publication(models.Model):
    title = models.CharField(max_length=256,null=False,blank=True,verbose_name="publications title")
    link = models.CharField(max_length=512,null=False,blank=True,verbose_name="publications link")
    pdf = models.CharField(max_length=512, null=False, blank=True, verbose_name="publications pdf link")
    journal = models.CharField(max_length=256, null=False, blank=True, verbose_name="journal")
    author = models.ManyToManyField('Member', related_name="author_pub", verbose_name="author")
    funding = models.ManyToManyField('Funding', related_name="funding_pub", verbose_name="funding")


class Member(models.Model):
    name = models.CharField(max_length=256,null=False,blank=True,verbose_name="name")
    identity = models.CharField(max_length=256,null=False,blank=True,verbose_name="title")
    file = models.FileField(storage=fss_share, upload_to=generate_img_path, null=True, verbose_name="视频文件")
    description = models.CharField(max_length=1024,null=False,blank=True,verbose_name="description")
    mail = models.EmailField(max_length=64,null=True,blank=True,verbose_name="email")
    fax = models.CharField(max_length=16,null=True,blank=True,verbose_name="fax number")
    phone = models.CharField(max_length=32,null=True,blank=True,verbose_name="mobile phone")
    directions = models.ManyToManyField(Research,related_name="research_member",verbose_name="research which join in")

    isLeader = models.BooleanField(default=False,verbose_name="is professor")


class Funding(models.Model):
    pass


PHOTO_TYPE = (
    (0,'lab'),
    (1,'group')
)


class Photo(models.Model):
    type = models.CharField(max_length=256,choices=PHOTO_TYPE,null=False,blank=True,verbose_name="name")
    title = models.CharField(max_length=32,null=False,blank=True,verbose_name="title")
    file = models.FileField(storage=fss_share, upload_to=generate_img_path, null=True, verbose_name="视频文件")
