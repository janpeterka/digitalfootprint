from random import randrange
from datetime import datetime, timedelta


def random_datetime(start, end):
    """
    This function will return a random datetime between two datetime objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)  # nosec
    return start + timedelta(seconds=random_second)


def datetime_days_ago(amount=14):
    """
    """
    return datetime.now() - timedelta(days=amount)
