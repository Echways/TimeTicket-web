from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Event(models.Model):
    eventtitle = models.CharField('Название мероприятия', max_length=100, default="")
    eventstartday = models.DateTimeField('Начало мероприятия', default=datetime.now())
    eventendday = models.DateTimeField('Конец мероприятия', default=datetime.now())
    eventdescription = models.CharField('Описание мероприятия', max_length=500, default="")
    ticketprice = models.IntegerField('Цена билета', default=0)
    eventminage = models.IntegerField('Минимальный возраст для посещения', default=0)
    ticket = models.ImageField('Билет', upload_to='imgs/events/', default=0)
    eventpic = models.ImageField('Промо-фото', upload_to='imgs/events/', default=0)
    hostpic = models.ImageField('Фото организатора', upload_to='imgs/events/avatars/', default=0)

    hostname = models.SlugField('Организатор', max_length=100, default="", allow_unicode=1)
    hostemail = models.EmailField('Почта организатора', max_length=100, default="")
    hosttg = models.CharField('Телеграм организатора', max_length=100, default="")

    def __str__(self):
        return self.eventtitle

    def get_absolute_url(self):
        return reverse('main', kwargs={'pk': self.pk})


class ProductVideo(models.Model):
    video = models.FileField(upload_to='video/', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    product = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='File')


class RegisterEvent(models.Model):
    name = models.CharField('Имя', max_length=100, default="")
    surname = models.CharField('Фамилия', max_length=100, default="")
    email = models.EmailField('Ваша почта', max_length=100, default="")
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='RegisterEvent')


class Profile(models.Model):
    user = models.OneToOneField('main.NewUser', on_delete=models.CASCADE)
    mobileph = models.IntegerField()
    email = models.EmailField()
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)

class NewUser(AbstractUser):
    email = models.EmailField(null=True)
    mobilephone = models.CharField('Номер телефона',max_length=12,default='')
    middle_name = models.CharField('Отчество',max_length=100,default='')
    # password1 = models.CharField('Пароль', max_length=100)
    # password2 = models.CharField('Ещё раз', max_length=100)
