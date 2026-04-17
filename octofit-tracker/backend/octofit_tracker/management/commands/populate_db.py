from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from django.conf import settings

from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # MongoDB bağlantısı
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Koleksiyonları temizle
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Takımlar
        teams = [
            {"name": "Team Marvel"},
            {"name": "Team DC"}
        ]
        team_ids = db.teams.insert_many(teams).inserted_ids

        # Kullanıcılar
        users = [
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Team Marvel"},
            {"name": "Captain America", "email": "cap@marvel.com", "team": "Team Marvel"},
            {"name": "Batman", "email": "batman@dc.com", "team": "Team DC"},
            {"name": "Superman", "email": "superman@dc.com", "team": "Team DC"}
        ]
        db.users.insert_many(users)

        # Aktiviteler
        activities = [
            {"user": "Iron Man", "activity": "Running", "duration": 30},
            {"user": "Captain America", "activity": "Cycling", "duration": 45},
            {"user": "Batman", "activity": "Swimming", "duration": 25},
            {"user": "Superman", "activity": "Flying", "duration": 60}
        ]
        db.activities.insert_many(activities)

        # Liderlik tablosu
        leaderboard = [
            {"user": "Iron Man", "points": 100},
            {"user": "Captain America", "points": 90},
            {"user": "Batman", "points": 95},
            {"user": "Superman", "points": 110}
        ]
        db.leaderboard.insert_many(leaderboard)

        # Antrenmanlar
        workouts = [
            {"user": "Iron Man", "workout": "Push-ups", "reps": 50},
            {"user": "Captain America", "workout": "Sit-ups", "reps": 60},
            {"user": "Batman", "workout": "Pull-ups", "reps": 40},
            {"user": "Superman", "workout": "Squats", "reps": 70}
        ]
        db.workouts.insert_many(workouts)

        # Kullanıcı koleksiyonunda email alanı için unique index
        db.users.create_index([("email", 1)], unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db test verileri başarıyla yüklendi!'))
