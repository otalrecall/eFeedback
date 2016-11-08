from django.db import models


class Check(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(default='', max_length=1000)

    def __str__(self):
        return self.name


class CheckList(models.Model):
    name = models.CharField(max_length=200)
    checks = models.ManyToManyField(Check)

    def __str__(self):
            return self.name


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1200)
    checkList = models.ForeignKey(CheckList, null=True)
    feedb_templ_1 = models.CharField(default='', max_length=200)
    feedb_templ_2 = models.CharField(default='', max_length=200)

    def __str__(self):
        return self.name


class Solution(models.Model):
    creation_date = models.DateTimeField(null=True)
    student_email = models.EmailField(max_length=70, blank=True, null=True)
    content = models.CharField(default='', max_length=3000)
    task = models.ForeignKey(Task, null=False)

    def __str__(self):
        return self.content


class State(models.Model):
    value = models.BooleanField(default=False)
    solution = models.ForeignKey(Solution, null=False)
    chk = models.ForeignKey(Check, null=False)

    def __str__(self):
            return str(self.value)