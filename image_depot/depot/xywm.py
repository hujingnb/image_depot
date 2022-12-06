from typing import Optional
import requests
from image_depot import DepotType
from .base import Depot


class Xywm(Depot):
    def __init__(self):
        super().__init__()
        self._token = None

    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.Xywm

    def _upload(self, content) -> Optional[str]:
        conf = self._config.xywm
        # 若存在用户名和密码, 获取 token
        if not self._token and conf.email and conf.password:
            data = {
                'email': conf.email,
                'password': conf.password
            }
            response = requests.post("https://pic.xywm.ltd/api/v1/tokens", data=data)
            if response.status_code == 200:
                self._token = response.json().get('data', {}).get('token')

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
        if self._token:
            headers['Authorization'] = f'Bearer {self._token}'
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
