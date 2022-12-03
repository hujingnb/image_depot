import random
from typing import Optional

import requests

from image_depot import DepotType
from .base import Depot


class UguuSe(Depot):
    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.UguuSe

    def upload(self, content) -> Optional[str]:
        file_name = self._random_file_name(content)
        if not file_name:
            return None
        files = {
            'files[]': (file_name, content),
        }
        response = requests.post('https://uguu.se/upload.php', files=files)
        if response.status_code != 200:
            return self._set_error(f'upload fail. code: {response.status_code}. content: {response.text}')
        data = response.json()
        url = None
        rep_files = data.get('files', [])
        if len(rep_files) == 1:
            url = rep_files[0].get('url')
        if not data.get('success') != 200 or not url:
            return self._set_error(response.text)
        return url
