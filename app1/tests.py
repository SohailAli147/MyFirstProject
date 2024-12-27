from django.test import TestCase
from .models import Student

# Create your tests here.

s1=Student(name="sohail",age=22,address="mumbai")
s1.save()