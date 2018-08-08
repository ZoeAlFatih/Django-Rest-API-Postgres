from django.db import models

class Clients(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Senders(models.Model):
    title = models.CharField(max_length=50)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    from_phone = models.CharField(max_length=15)
    from_email = models.EmailField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.title
        
class Message(models.Model):
    title = models.CharField(max_length=50)
    from_phone = models.CharField(max_length=15)
    to_phone = models.CharField(max_length=15)
    from_email = models.EmailField(max_length=50)
    to_email = models.EmailField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.title
    
