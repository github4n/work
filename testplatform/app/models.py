from django.db import models
from django.contrib.auth.models import User

#
# class Person(models.Model):
#     name = models.CharField(max_length=30)
#     age = models.IntegerField()
#
#     def __str__(self):
#         return self.name
#
#
# class Article(models.Model):
#     title = models.CharField(u'标题', max_length=256)
#     content = models.TextField(u'内容')
#
#     pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
#     update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)
#
#     def __str__(self):
#         return self.title
#
#
# class MyUser(models.Model):
#     user = models.OneToOneField(User)
#     nickname = models.CharField(max_length=16)
#     permission = models.IntegerField(default=1)
#
#     def __unicode__(self):
#         return self.user.username
