from datetime import datetime, timedelta


def datetime_days_ago(amount=14):
    """
    """
    return datetime.now() - timedelta(days=amount)
