import requests

from utils.config import YANDEX_DISK_API_URL


class YandexDiskPage:
    def get_files_and_folders(self, token):
        headers = {
            "Authorization": f"OAuth {token}"
        }
        response = requests.get(YANDEX_DISK_API_URL, headers=headers)
        return response