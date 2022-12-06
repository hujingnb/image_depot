from typing import Optional
import requests
from image_depot import DepotType
from .base import Depot


class Tucang(Depot):
    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.Tucang

    # 上传图片, 二进制内容
    def _upload(self, content) -> Optional[str]:
        conf = self._config.tucang
        if not conf.token:
            return self._set_error('token is empty')
        tmp_filename = self._random_file_name(content)
        if not tmp_filename:
            return None
        data = {
            'token': conf.token,
        }
        if conf.folder_id:
            data['folderId'] = conf.folder_id
        files = {
            "file": (tmp_filename, content)
        }
        response = requests.post("https://tucang.cc/api/v1/upload", files=files, data=data)
        if response.status_code != 200:
            return self._set_error(f'request fail. code: {response.status_code}')
        #  检查返回数据
        data = response.json()
        url = data.get('data', {}).get('url')
        if not data.get('success') or not url:
            return self._set_error(f'server return error. {response.text}')
        return url
