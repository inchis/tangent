from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.db import models


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

Gender_Choices = (
    ('M', 'Male'),
    ('F', 'Female'),
)

Race_Choices = (
    ('B', 'Black African'),
    ('C', 'Coloured'),
    ('I', 'Indian or Asian'),
    ('W', 'White'),
    ('N', 'none Dominant')
)

Review_Choices = (
    ('P', 'Performance'),
    ('S', 'Starting Salary'),
    ('A', 'Annual Increase'),
    ('E', 'Expectation Review')
)


class Employee(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    birth_date = models.DateField(blank=False)
    gender = models.CharField(blank=False, max_length=25, choices=Gender_Choices)
    race = models.CharField(blank=False, max_length=25, choices=Race_Choices)
    position = models.CharField(max_length=120, blank=False, default='')
    start_date = models.DateField(blank=False)
    user = models.ForeignKey(User, unique=True)
    email = models.EmailField(blank=False)
    review = models.CharField(blank=False, max_length=25, choices=Review_Choices)

    def __str__(self):
        return ('%s' % self.user).encode('ascii', 'replace')

    def __unicode__(self):
        return u'%s' % self.user

