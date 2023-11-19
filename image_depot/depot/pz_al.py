from typing import Optional

import requests

from image_depot import DepotType
from .base import Depot


class PzAl(Depot):
    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.PzAl

    # 上传图片, 二进制内容
    def _upload(self, content) -> Optional[str]:
        file_name = self._random_file_name(content)
        if not file_name:
            return None
        # 获取上传 token
        token = None
        conf = self._config.pz_al
        if conf.email and conf.password:
            token = self._get_token(conf.email, conf.password)
        # 上传图片
        header = {}
        if token:
            header['token'] = token
        response = requests.post('https://pz.al/api/upload', headers=header, files={
            'image': (file_name, content),
        })
        if response.status_code != 200:
            return self._set_error(f'upload fail. code: {response.status_code}. content: {response.text}')
        code = response.json().get('code')
        if code != 200:
            return self._set_error(f'upload fail. code: {code}. content: {response.text}')
        url = response.json().get('data', {}).get('url')
        if not url:
            return self._set_error(f'response error. {response.text}')
        return url

    def _get_token(self, email, password):
        response = requests.post('https://pz.al/api/token', data={
            'email': email,
            'password': password,
        })
        if response.status_code != 200:
            return self._set_error(f'get token fail. code: {response.status_code}. content: {response.text}')
        code = response.json().get('code')
        if code != 200:
            return self._set_error(f'get token fail. code: {code}. content: {response.text}')
        token = response.json().get('data', {}).get('token')
        if not token:
            return self._set_error(f'get token fail. token is empty')
        return token