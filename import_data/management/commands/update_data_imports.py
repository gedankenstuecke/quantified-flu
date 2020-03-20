from django.core.management.base import BaseCommand
from import_data.models import OuraMember, FitbitMember
from retrospective.tasks import update_fitbit_data, update_oura_data
import time
import requests


class Command(BaseCommand):
    help = "Updates all data for all members"

    def handle(self, *args, **options):
        # cheat to wake up sleeping worker
        requests.get("https://oh-oura-connect.herokuapp.com/")

        oura_users = OuraMember.objects.all()
        for o in oura_users:
            update_oura_data.delay(o.id)
            print("submitted oura update for {}".format(o.id))
            time.sleep(2)

        fitbit_users = FitbitMember.objects.all()
        for f in fitbit_users:
            update_fitbit_data.delay(f.id)
            print("submitted fitbit update for {}".format(f.id))
            time.sleep(2)
