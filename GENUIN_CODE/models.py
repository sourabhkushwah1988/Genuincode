from django.db import models

class Ragister(models.Model):  
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

# 🔁 Change model name: Contact → YourCustomName2
class Contact(models.Model):  # 🔁 Change name here
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subject}"

# 🔁 Change model name: CustomUser → YourCustomName3
class CustomUser(models.Model):  # 🔁 Change name here
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

# 🔁 Change model name: LoginAttempt → YourCustomName4
class LoginAttempt(models.Model):  # 🔁 Change name here
    email = models.EmailField()
    password = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.timestamp}"

from django.contrib.auth.models import User

# Profile model to extend the User model with additional information
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_pics/', default='default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'