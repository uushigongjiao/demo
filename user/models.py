import datetime
from django.db import models

class User(models.Model):

    SEX = (
        ('男','男'),
        ('女','女'),
    )
    nickname = models.CharField(max_length=32,unique=True)
    phonenum = models.CharField(max_length=16,unique=True)


    sex = models.CharField(default='男',choices=SEX,max_length=8)
    birth_year = models.IntegerField(default=2000,)
    birth_day = models.IntegerField(default=1,)
    birth_month = models.IntegerField(default=1,)
    avatar = models.CharField(max_length=512)
    locationg = models.CharField(max_length=32)

    @property
    def age(self):
        today = datetime.date.today()
        birthday = datetime.date(self.birth_year,self.birth_month,self.birth_day)
        times = (today - birthday) // 365
        return times

    @property
    def profile(self):
        if not hasattr(self,'_profile'):
            _profile, _ = Profile.objects.get_or_create(id=self.id)
            self._profile = _profile
        return self._profile





class Profile(models.Model):
    SEX = (
        ('男', '男'),
        ('女', '女'),
    )

    location = models.CharField(max_length=32,verbose_name='目标城市')

    min_distance = models.IntegerField(default=1,verbose_name='最小查找范围')
    max_distance = models.IntegerField(default=10,verbose_name='最大查找范围')

    min_dating_age = models.IntegerField(default=18,verbose_name='最小交友年龄')
    max_dating_age = models.IntegerField(default=50,verbose_name='最大交友年龄')

    dating_sex = models.CharField(max_length=8,choices=SEX,verbose_name='匹配性别')
    vibration = models.BooleanField(default=True,verbose_name='是否开始震动')
    only_matche = models.BooleanField(default=True,verbose_name='不让匹配的人看我相册')
    auto_play = models.BooleanField(default=True,verbose_name='是否自动播放视频')