import json
import requests


class Reqres:

    def __init__(self):
        self.base_url = "https://reqres.in/"

    def get_users(self, page, per_page, total, total_pages) -> json:
        """Метод делает GET запрос к API сервера и возвращает статус запроса и результат в формате JSON
                со списком пользователей, в соответствии с параметрами."""
        params = {
            'page': page,
            'per_page': per_page,
            'total': total,
            'total_pages': total_pages
        }
        res = requests.get(self.base_url + 'api/users', params=params)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result



