from django.db import models

class Company(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    city=models.CharField(max_length=200)
    address=models.CharField(max_length=200)

    def to_json(self):
        return {
            'id':self.id,
            'name':self.name,
            'description':self.description,
            'city':self.city,
            'address':self.address
        }

class Vacancy(models.Model):
    name=models.CharField(max_length=200)
    salary=models.FloatField()
    description=models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default="Apple")
    def to_json(self):
        return {
            'id':self.id,
            'name':self.name,
            'description':self.description,
            'salary':self.salary,
            'company':self.company.__str__()
        }