from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Create Users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel.name)
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel.name)
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc.name)
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc.name)

        # Create Activities
        Activity.objects.create(user=tony, activity_type='run', duration=30, date='2023-01-01')
        Activity.objects.create(user=steve, activity_type='cycle', duration=45, date='2023-01-02')
        Activity.objects.create(user=bruce, activity_type='swim', duration=60, date='2023-01-03')
        Activity.objects.create(user=clark, activity_type='yoga', duration=20, date='2023-01-04')

        # Create Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='5K Run', description='Run 5 kilometers', difficulty='medium')
        Workout.objects.create(name='HIIT', description='High intensity interval training', difficulty='hard')

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, points=100)
        Leaderboard.objects.create(user=steve, points=90)
        Leaderboard.objects.create(user=bruce, points=110)
        Leaderboard.objects.create(user=clark, points=95)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
