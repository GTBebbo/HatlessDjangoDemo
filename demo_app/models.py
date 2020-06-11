from django.db import models
from django.contrib.auth.models import User
import datetime

class BlogPost(models.Model):
	# Table Columns Defined Here
	title = models.CharField(max_length=50)
	content = models.TextField()
	posted_time = models.DateTimeField(default=datetime.datetime.now())
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.title




