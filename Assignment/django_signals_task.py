#Question 1: By default, are Django signals executed synchronously or asynchronously?

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
import time

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler started")
    print("(Sleeping for 5 seconds...)")  # Added this line
    time.sleep(5)  # Simulating a delay
    print("Signal handler finished")

# Simulate creating a new user
print("Creating user...")
user = User.objects.create(username="testuser")
print("User created!")



#Expected Output:

Creating user...
Signal handler started
(Sleeping for 5 seconds...)
(Sleeps for 5 seconds)
Signal handler finished
User created!


#Question 2: Do Django signals run in the same thread as the caller?


import threading
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal running in thread: {threading.current_thread().name}")

# Simulate creating a new user
print(f"Main thread: {threading.current_thread().name}")
user = User.objects.create(username="testuser")

#Expected Output:

Main thread: MainThread
Signal running in thread: MainThread


#Question 3: By default, do Django signals run in the same database transaction as the caller?


from django.db import transaction
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler started")
    raise Exception("Simulated failure")  # This should rollback the transaction

try:
    with transaction.atomic():
        user = User.objects.create(username="testuser")
except Exception as e:
    print(f"Exception: {e}")

# Check if user exists
print("User exists:", User.objects.filter(username="testuser").exists())

#Expected Output:


Signal handler started
Exception: Simulated failure
User exists: False
