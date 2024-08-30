from faker import Faker

from datetime import date
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings') # this should be done first.

# Import settings
django.setup()

from tasks.models import Task
from django.contrib.auth.models import User

fake = Faker()
users_login=[]

# Cadastra 10 usuários comuns
for _ in range(10):
    try:
        username= fake.user_name
        password=fake.password
        user = User(username=username, password=password, first_name=fake.first_name,last_name=fake.last_name)
        user.save()
        users_login.append({
            "username": username,
            "password": password
        })
    except Exception as error:
        print(str(error))
# Salva os logins dos usuários cadastrados em um arquivo
try:
    with open("export_users.txt", "a") as text_file:
        for line in users_login:
            text_file.write(" ".join(line) + "\n")
except Exception as error:
    print(str(error))

# Cadastra 250 tarefas distribuidas entre os 10 usuários cadastrados
for _ in range(250):
    try:
        task = Task(
            title=fake.text(max_nb_chars=150),
            description=fake.text(),
            due_date=fake.date_between_dates(date_start=date(2024, 8, 30), date_end=date(2024, 12, 31)),
            completed=fake.boolean(35),
            user_id=fake.random_int(1,10)
        )
        task.save()
    except Exception as error:
        print(str(error))
    