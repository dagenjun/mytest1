from django.db import models

class author(models.Model):
	authorid = models.AutoField(primary_key = True)
	name = models.CharField(max_length=50)
	age = models.IntegerField(default = 18)
	country = models.CharField(max_length=50, default = 'CHINA')
	class Meta:
		db_table = "author"
 
	def __unicode__(self):
		return self.name

class book(models.Model):
	isbn = models.CharField(max_length=50, primary_key = True)
	title = models.CharField(max_length=50)
	author = models.ForeignKey(author)
	publisher = models.CharField(max_length=50)
	publishdate = models.DateField(max_length=50)
	price = models.FloatField(max_length=50)
	class Meta:
		db_table = "book"
	def __unicode__(self):
		return self.title


    
