from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=30)

class Credential(Users):
    max_len_cred = 26
    login = models.CharField(max_len_cred, unique=True)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20,  default='user')

class Messages(models.Model):
    message = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    id_sender = models.ForeignKey(to=Credential, on_delete=models.CASCADE, related_name='sender')
    id_receiver = models.ForeignKey(to=Credential, on_delete=models.CASCADE, related_name='receiver')


class Bans(models.Model):
    id_user = models.ForeignKey(to=Credential, on_delete=models.CASCADE)
