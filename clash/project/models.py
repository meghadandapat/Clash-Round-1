from django.db import models
from django.contrib.auth.models import User


class Questions(models.Model):
    question_level = models.CharField(max_length=225, blank=True)
    question = models.CharField(max_length=255, blank=True)
    option_A = models.CharField(max_length=255, blank=True)
    option_B = models.CharField(max_length=255, blank=True)
    option_C = models.CharField(max_length=255, blank=True)
    option_D = models.CharField(max_length=255, blank=True)
    correct_answer = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.question


class Response(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=255, blank=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.first_name+f' ({self.selected_answer})'


class Register(models.Model):  # extended user model
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user')
    phone = models.IntegerField(default=0)
    level = models.CharField(max_length=15, default='fe')
    language = models.CharField(max_length=15)
    total_score = models.IntegerField(default=0)
    quelist = models.TextField(max_length=255, default="[]")
    marks = models.IntegerField(default=1)
    status = models.BooleanField(default=True)
    logouttime = models.DateTimeField(blank=True, null=True, default=None)
    extra_time = models.IntegerField(default=0)
    time_rem = models.IntegerField(default=1680)
    get_chance = models.IntegerField(default=0)
    queflist = models.TextField(max_length=255, default="[]")
    quefulllist = models.TextField(max_length=255, default="[]")
    visionlst = models.TextField(max_length=255, default="[]")
    spin_wheel = models.BooleanField(default=False)
    checkpoint = models.IntegerField(default=0)
    flag = models.IntegerField(default=-1)
    freezetimestart = models.DateTimeField(blank=True, null=True, default=None)
    flashblind = models.IntegerField(default=0)
    spincount = models.IntegerField(default=2)
    progress = models.IntegerField(default=0)
    getassured = models.BooleanField(default=False)
    freezebar = models.BooleanField(default=False)
    allow = models.BooleanField(default=False)
    predicted_score = models.IntegerField(default=0)
    correct_answered = models.IntegerField(default=0)
    length = models.IntegerField(default=0)
    freezeflag = models.IntegerField(default=0)
    refresh = models.IntegerField(default=0)
    permit = models.IntegerField(default=1)
    tab=models.IntegerField(default=2)

    def __str__(self):
        return self.user.first_name+f' ({self.user.username})'
