from faker import Faker

from datetime import date
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings') # this should be done first.

# Import settings
django.setup()

from tasks.models import Task

fake = Faker()

for _ in range(100):
    try:
        task = Task(
            title=fake.text(max_nb_chars=150),
            description=fake.text(),
            due_date=fake.date_between_dates(date_start=date(2024, 8, 30), date_end=date(2024, 12, 31)),
            completed=fake.boolean(35),
            user_id=fake.random_int(1,2)
        )
        task.save()
    except Exception as error:
        print(str(error))
    