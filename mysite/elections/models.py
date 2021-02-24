from django.db import models

# Create your models here.
class Candidate(models.Model):
	name = models.CharField(max_length=10)
	introduction = models.TextField() # 길이 제한 없음
	area = models.CharField(max_length=15)
	party_number = models.IntegerField(default=0)

	def __str__(self):
		return self.name

class Poll(models.Model):
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	area = models.CharField(max_length=15)


class Choice(models.Model):
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE) # 위에서 만든 클래스 사용
	candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
	votes = models.IntegerField(default=0)