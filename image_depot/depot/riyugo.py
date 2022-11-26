import random
from typing import Optional
import requests
from image_depot import DepotType
from .base import Depot


class Riyugo(Depot):
    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.Riyugo

    def upload(self, content) -> Optional[str]:
        data = {
            'uuid': 'o_1g840' + ''.join(random.sample(list('0123456789abcdefghijklmnopqrstuvwxyz') * 22, 22)),
            'nameMode': 'isRenameMode',
        }
        files = {
            'file': content,
        }
        response = requests.post('https://4ae.cn/localup.php', data=data, files=files)
        if response.status_code != 200:
            return self._set_error('upload fail')
        data = response.json()
        if data.get('result') != 'success' or not data.get('url'):
            return self._set_error(response.text)
        return data.get('url')
