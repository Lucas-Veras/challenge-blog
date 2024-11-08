from datetime import datetime


def get_future_datetime(time_to_add):
    """
    Retorna a data e hora futura somando a duração especificada ao tempo atual.
    """
    return datetime.now() + time_to_add
