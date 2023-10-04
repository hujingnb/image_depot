import random
import re
from typing import Optional
import requests
from image_depot import DepotType
from .base import Depot


class Riyugo(Depot):
    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.Riyugo

    def _upload(self, content) -> Optional[str]:
        file_name = self._random_file_name(content)
        if not file_name:
            return None

        session = requests.session()
        session.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/107.0.0.0 Safari/537.36',
        }
        # 通过首页获取 token
        response = session.get('https://zixiaoyun.com/')
        if response.status_code != 200:
            return self._set_error(f'get token fail. code: {response.status_code}')
        # authToken_today :"FJ932YTHEWOJG94YHEWJGOWEK349"
        # 从结果中通过正则匹配出 token
        matches = re.search(r"authToken_today\s*:\s*\"([0-9A-Za-z]+)\"", response.text)
        if not matches:
            return self._set_error(f'get token fail. content: {response.text}')
        token = matches.group(1)
        data = {
            'uuid': 'o_' + self._random_str(27),
            'nameMode': 'isRenameMode',
            'authToken_today': token,
            'name': file_name,
        }
        files = {
            'file': content,
        }
        headers = {
            'origin': 'https://zixiaoyun.com',
            'referer': 'https://zixiaoyun.com/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/107.0.0.0 Safari/537.36',
        }
        response = session.post('https://s1.wzznft.com/localup.php', data=data, files=files, headers=headers)
        if response.status_code != 200:
            return self._set_error(f'upload fail. code: {response.status_code}. content: {response.text}')
        data = response.json()
        if data.get('result') != 'success' or not data.get('url'):
            return self._set_error(response.text)
        return data.get('url')
