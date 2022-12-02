import random
from typing import Optional

import requests

from image_depot import DepotType
from .base import Depot

TOKEN = ''
EMAIL = ''
PASSWORD = ''


def set_config(email: str, password: str):
    """
    :param email:
    :param password:
    :return:
    """
    global EMAIL, PASSWORD
    EMAIL = email
    PASSWORD = password


class Xywm(Depot):
    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.Xywm

    def upload(self, content) -> Optional[str]:
        global TOKEN
        # 若存在用户名和密码, 获取 token
        if not TOKEN and EMAIL and PASSWORD:
            data = {
                'email': EMAIL,
                'password': PASSWORD
            }
            response = requests.post("https://pic.xywm.ltd/api/v1/tokens", data=data)
            if response.status_code == 200:
                TOKEN = response.json().get('data', {}).get('token')

        # 上传图片
        tmp_filename = self._random_file_name(content)
        if not tmp_filename:
            return None
        files = {
            "file": (tmp_filename, content)
        }
        headers = {
            "Accept": "application/json",
        }
        if TOKEN:
            headers['Authorization'] = f'Bearer {TOKEN}'
        response = requests.post("https://pic.xywm.ltd/api/v1/upload", headers=headers, files=files)
        if response.status_code != 200:
            return self._set_error(f'upload fail. code: {response.status_code}')
        data = response.json()
        if not data.get('status'):
            return self._set_error(f'upload fail. {response.text}')
        url = data.get('data', {}).get('links', {}).get('url')
        if not url:
            return self._set_error(f'response error. {response.text}')
        return url
