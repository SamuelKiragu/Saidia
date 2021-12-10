from django.db import models

# Create your models here.
class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 40)
    x_coordinate = models.DecimalField(max_digits=23, decimal_places=20)
    y_coordinate = models.DecimalField(max_digits=23, decimal_places=20)

    def __str__(self):
        return f"{self.id},{self.name}"

class Needs(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 40)

    def __str__(self):
        return f"{self.name}"

class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 150)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email'], name="unique_user")
        ]

    def __str__(self):
        return f"{self.id},{self.first_name},{self.last_name},{self.email},{self.datetime}"

class Manager(models.Model):
    user =  models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    password = models.CharField(max_length =  200)

    def __str__(self):
        return f"{self.user}"

class Orphanage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 40)
    manager = models.ForeignKey(Manager, on_delete = models.CASCADE)
    needs = models.ManyToManyField(Needs)
    capacity = models.IntegerField()
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    x_coordinate = models.DecimalField(max_digits=23, decimal_places=20)
    y_coordinate = models.DecimalField(max_digits=23, decimal_places=20)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orphanage = models.ForeignKey(Orphanage, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user},{self.orphanage},{self.message},{self.datetime}"
