from django.db import models
from django_quill.fields import QuillField
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.


class Class(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    number = models.IntegerField(primary_key=True)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.number)+" "+self.name


class Chapter(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    number = models.IntegerField(primary_key=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    of_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.number)+" "+self.name


class Keyword(models.Model):
    name = models.CharField(unique=True, max_length=100,
                            null=False, blank=False)

    def __str__(self) -> str:
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    number = models.IntegerField(primary_key=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    content = QuillField()
    keywords = models.ManyToManyField(Keyword)
    read_time = models.IntegerField(default=1)

    def __str__(self) -> str:
        return str(self.number)+" "+self.name


class McqOption(models.Model):
    text = models.CharField(max_length=100, null=False, blank=False)
    correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.text


class Mcq(models.Model):
    question = models.CharField(max_length=100, null=False, blank=False)
    description = QuillField(default="")
    options = models.ManyToManyField(McqOption)
    answer = models.TextField(max_length=500, blank=True, null=True)
    topic = models.ForeignKey(Topic, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.question + str(self.topic)


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    marked_correct = models.BooleanField(default=False)
    option = models.ForeignKey(McqOption, on_delete=models.CASCADE,related_name="user_answer")

    def __str__(self) -> str:
        return self.user.username+" "+self.option.text+str(self.option.correct)+" "+str(self.marked_correct)

class ExamPapers(models.Model):
    file = models.FileField(upload_to='exam_papers/', max_length=10485760,
                                validators=[FileExtensionValidator(allowed_extensions=['pdf','doc','docx','txt'])])
    name=models.CharField(max_length=256)
    of_class=models.ForeignKey(Class,on_delete=models.CASCADE,related_name='exampaper_class')
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE,null=True,blank=True)
    chapter=models.ForeignKey(Chapter,on_delete=models.CASCADE,null=True,blank=True)

class CaseStudies(models.Model):
    file = models.FileField(upload_to='case_studies/', max_length=10485760,
                                validators=[FileExtensionValidator(allowed_extensions=['pdf','doc','docx','txt'])])
    name=models.CharField(max_length=256)
    of_class=models.ForeignKey(Class,on_delete=models.CASCADE,related_name='case_studies_class')
    chapter=models.ForeignKey(Chapter,on_delete=models.CASCADE,null=True,blank=True)
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE,null=True,blank=True)

class CheatSheet(models.Model):
    file = models.FileField(upload_to='cheat_sheet/', max_length=10485760,
                                validators=[FileExtensionValidator(allowed_extensions=['pdf','doc','docx','txt'])])
    name=models.CharField(max_length=256)
    of_class=models.ForeignKey(Class,on_delete=models.CASCADE,related_name='cheat_sheet_class')
    chapter=models.ForeignKey(Chapter,on_delete=models.CASCADE,null=True,blank=True)
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE,null=True,blank=True)
