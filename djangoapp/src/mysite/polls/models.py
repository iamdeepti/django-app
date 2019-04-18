from django.db import models

# Create your models here.
class Question(models.Model):
	"""docstring for Questions"models.modelf __init__(self, arg):
		super(Questions,models.model.__init__()
		self.arg = arg"""
	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):

	question = models.ForeignKey(Question, on_delete = models.CASCADE)	
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)