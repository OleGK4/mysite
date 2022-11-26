import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User


def get_name_file(instance, filename):
    return 'portal/file'.join([get_random_string(5) + '_' + filename])


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# class User(AbstractUser):
#     name = models.CharField(max_length=200, verbose_name='Имя', blank=False)
#     surname = models.CharField(max_length=200, verbose_name='Фамилия', blank=False)
#     patronymic = models.CharField(max_length=200, verbose_name='Отчество', blank=True)
#     username = models.CharField(max_length=200, verbose_name='Логин', unique=True, blank=False)
#     email = models.EmailField(max_length=200, verbose_name='Почта', unique=True, blank=False)
#     password = models.CharField(max_length=200, verbose_name='Пароль', blank=False)
#     user_file = models.ImageField(max_length=200, upload_to=get_name_file, blank=False, null=True,
#                                   validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
#     USERNAME_FIELD = 'username'
#
#     def __str__(self):
#         return str(self.name) + ' ' + str(self.surname)
#
#     class Meta:
#         ordering = ['name']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
