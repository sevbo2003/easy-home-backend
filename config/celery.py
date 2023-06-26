import os
import dotenv

from celery import Celery


dotenv.load_dotenv(dotenv.find_dotenv(), override=True)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.config")
os.environ.setdefault("DJANGO_CONFIGURATION", "Local")

import configurations
configurations.setup()

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()