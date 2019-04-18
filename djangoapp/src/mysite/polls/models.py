from django.db import models

# Create your models here.
class Question(models.Model):
	"""docstring for Questions"models.modelf __init__(self, arg):
		super(Questions,models.model.__init__()
		self.arg = arg"""

	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text

class Choice(models.Model):

	question = models.ForeignKey(Question, on_delete = models.CASCADE)	
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)
	def __str__(self):
		return self.choice_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now()-datetime.timedelta(days=1)
	