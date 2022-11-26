import random
from typing import Optional

import requests

from image_depot import DepotType
from .base import Depot


class PngCm(Depot):
    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.PngCm

    def upload(self, content) -> Optional[str]:
        data = {
            'uuid': 'o_1g840' + ''.join(random.sample(list('0123456789abcdefghijklmnopqrstuvwxyz') * 21, 21)),
        }
        files = {
            'file': content, 
        }
        response = requests.post('https://png.cm/application/upload.php', data=data, files=files)
        if response.status_code != 200:
            return self._set_error(f'upload fail. code: {response.status_code}. content: {response.text}')
        data = response.json()
        if data.get('code') != 200 or not data.get('url'):
            return self._set_error(response.text)
        return data.get('url')
