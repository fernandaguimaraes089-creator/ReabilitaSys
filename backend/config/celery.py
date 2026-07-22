import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('reabilita_sys')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check-medication-expiry': {
        'task': 'apps.medications.tasks.check_medication_expiry',
        'schedule': crontab(hour=6, minute=0),
    },
    'generate-daily-reports': {
        'task': 'apps.dashboard.tasks.generate_daily_reports',
        'schedule': crontab(hour=23, minute=59),
    },
    'backup-database': {
        'task': 'apps.audit.tasks.backup_database',
        'schedule': crontab(hour=2, minute=0),
    },
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
