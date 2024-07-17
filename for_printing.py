from api import Regres


gu = Regres()


def for_print():
    result = gu.get_users(1, 6, 12, 0)
    result_second = gu.get_users(1, 6, 12, 0)
    return result, result_second


print(for_print())