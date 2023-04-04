from django.db import models

from .model_logistic import predict_using_model


# Create your models here.
class Record(models.Model):
    # GENDERS = (
    # (True, 'Male'),
    # (False, 'Female'),
    # )

    name = models.CharField(max_length=255, blank=False)
    gender = models.BooleanField(null=False)
    age = models.IntegerField(null=False)
    salary = models.CharField(max_length=50)
    purchased = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def full_name(self):
        return self.name

    def predict_ads_click(self):

        try:
            self.purchased = predict_using_model(
                sex=self.gender, age=self.age, salary=self.salary
            )
            self.save()
            return True
        except Exception as e:
            print("Exception ", e)
            return False

    def __str__(self):
        return f"{self.name}"
