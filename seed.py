from faker import Faker

from datetime import date
from random import randint
import os
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings') # this should be done first.

# Import settings
django.setup()

from tasks.models import Task
from django.contrib.auth.models import User

fake = Faker()
users_login={}

# Cadastra 10 usuários comuns
for i in range(10):
    try:
        username= f"{fake.user_name()}.{randint(1,1000)}"
        password=fake.password()
        user = User(username=username, first_name=fake.first_name(),last_name=fake.last_name())
        user.set_password(raw_password=password)
        user.save()
        for _ in range(25):
            try:
                task = Task(
                    title=fake.text(max_nb_chars=150),
                    description=fake.text(),
                    due_date=fake.date_between_dates(date_start=date(2024, 8, 30), date_end=date(2024, 12, 31)),
                    completed=fake.boolean(35),
                    user_id=user.id
                )
                task.save()
            except Exception as error:
                print(str(error))
        users_login[f"user{i}"] = {
            'username': username,
            'password': password
        }
    except Exception as error:
        print(str(error))
# Salva os logins dos usuários cadastrados em um arquivo
try:
    json_object = json.dumps(users_login, indent=4)
    with open("export_users.json", "w") as text_file:
        text_file.write(json_object)
except Exception as error:
    print(str(error))

# Cadastra 250 tarefas distribuidas entre os 10 usuários cadastrados

    