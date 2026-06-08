import time
import random
import string

def generate_unique_email():
    timestamp = int(time.time())
    random_str = ''.join(random.choices(string.ascii_lowercase, k=4))
    return f"user_{timestamp}_{random_str}@yandex.ru"