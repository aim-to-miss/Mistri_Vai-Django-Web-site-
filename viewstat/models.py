from django.db import models

# Create your models here.
class homestat(models.Model):
	number_of_customer = models.TextField()
	number_of_worker = models.TextField()
	number_of_supplier = models.TextField()
	slug = models.SlugField(default = "homestat")
class comments(models.Model):
	comenter_name = models.TextField()
	service_rating = models.TextField()
	comment_head = models.TextField()
	comment_content = models.TextField()
class mistri(models.Model):
	mistri_img = models.TextField(null = True)
	mistri_name = models.TextField(null = True)
	mistri_catagory = models.TextField(null = True)
	mistri_experiece = models.TextField(null = True)
	mistri_job_completed = models.TextField(null = True)
	mistri_special_ability = models.TextField(null = True)
	mistri_rating = models.TextField(null = True)
	mistri_fee = models.TextField(null = True)
	mistri_status = models.TextField(null = True)
	mistri_address = models.TextField(null = True)
	mistri_job_assigned_date = models.TextField(null = True)
	mistri_job_finishing_date = models.TextField(null = True)
	mistri_contact_number = models.TextField(null = True)
	mistri_money_to_be_paid = models.TextField(null = True)
	mistri_benifit = models.TextField(null = True)
