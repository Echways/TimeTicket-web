from django.db import models
from datetime import datetime


class Event(models.Model):
    eventname = models.CharField('Название мероприятия', max_length=100, default="")
    eventstartday = models.DateTimeField('Начало мероприятия', default=datetime.now())
    eventendday = models.DateTimeField('Конец мероприятия', default=datetime.now())
    eventdescription = models.CharField('Описание мероприятия', max_length=500, default="")
    ticketprice = models.IntegerField('Цена билета', default=0)
    eventminage = models.IntegerField('Минимальный возраст для посещения', default=0)
    evemntpic = models.ImageField('Промо-фото', upload_to='imgs/events/', default=0)

    hostname = models.SlugField('Организатор', max_length=100, default="", allow_unicode=1)
    hostemail = models.EmailField('Почта организатора', max_length=100, default="")
    hosttg = models.CharField('Телеграм', max_length=100, default="")


    def __str__(self):
        return self.eventname
