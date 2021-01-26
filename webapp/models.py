from django.db import models

class Job(models.Model):
    Sno = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=255)
    job_id = models.IntegerField()
    position = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    package = models.BigIntegerField()
    skills_required = models.CharField(max_length=255)
    experience_required = models.IntegerField()
    

    def __str__(self):
        return self.Sno
    