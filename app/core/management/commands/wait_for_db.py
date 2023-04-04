"""
Custom Django command:
Wait for database application to be available after service is ready.
"""
import time
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OpError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_ready = False

        while db_ready is False:
            try:
                self.stdout.write('Checking database... ')
                self.check(databases=['default'])
                db_ready = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database is not ready, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database ready.'))
