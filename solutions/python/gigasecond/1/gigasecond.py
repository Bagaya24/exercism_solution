"""
The gigasecond module
"""
import datetime

def add(moment: datetime.datetime) -> datetime.datetime:
    """"Add one second to a datetime object.
    :param moment: datetime object
    :return: datetime object with one second added
    """
    moment_second = moment.timestamp() + 1e9
    return datetime.datetime.fromtimestamp(moment_second)