
from django.db import models
from django.contrib.auth.models import User

class MyUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ... other fields.  i.e. imagefield, date of birth (dob), etc ..
    # example:
    phone = models.DateField()