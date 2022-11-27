from typing import Optional

import requests

from image_depot import DepotType
from .base import Depot

TOKEN = ''
UID = ''


def set_config(token: str, uid: str):
    """
    :param token: 获取地址: https://www.imgurl.org/vip/manage/mytoken
    :param uid: 与 token 一起获取
    :return:
    """
    global TOKEN, UID
    TOKEN = token
    UID = uid


class ImgUrl(Depot):
    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.ImgUrl

    def upload(self, content) -> Optional[str]:
        if not TOKEN or not UID:
            return self._set_error('token or uid is empty')
        file_name = self._random_file_name(content)
        if not file_name:
            return None
        files = {
            'file': (file_name, content)
        }
        data = {
            'uid': UID,
            'token': TOKEN,
        }
        response = requests.post('https://www.imgurl.org/api/v2/upload', files=files, data=data)
        if response.status_code != 200:
            return self._set_error(f'request fail. code: {response.status_code}')
        data = response.json()
        if not data:
            return self._set_error(f'parse response fail. data: {response.text}')
        # 接口返回错误信息
        code = data.get('code')
        msg = data.get('msg')
        if code != 200 and msg:
            return self._set_error(msg)
        if code != 200:
            return self._set_error(f'response error. {response.text}')
        url = data.get('data', {}).get('url')
        if not url:
            return self._set_error(f'parse url error. {response.text}')
        return url
