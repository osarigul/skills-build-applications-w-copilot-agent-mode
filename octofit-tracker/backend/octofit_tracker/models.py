from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    duration = models.IntegerField()
    def __str__(self):
        return f"{self.user} - {self.activity}"

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    points = models.IntegerField()
    def __str__(self):
        return f"{self.user} - {self.points}"

class Workout(models.Model):
    user = models.CharField(max_length=100)
    workout = models.CharField(max_length=100)
    reps = models.IntegerField()
    def __str__(self):
        return f"{self.user} - {self.workout}"