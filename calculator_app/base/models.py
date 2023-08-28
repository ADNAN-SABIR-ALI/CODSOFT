from django.db import models

class Calculation(models.Model):
    num1 = models.FloatField()
    num2 = models.FloatField()
    operation = models.CharField(max_length=10)
    result = models.FloatField()

    # def __str__(self):
    #     return f"{self.num1} {self.operation} {self.num2} = {self.result}"
