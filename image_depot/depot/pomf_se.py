from typing import Optional, List

import requests

from image_depot import DepotType
from .base import Depot

UPLOAD_URL_LIST = [
    # https://fileditch.com/
    'https://up1.fileditch.com/upload.php',
    'https://qu.ax/upload.php',
    'https://midi.moe/upload.php',
    'https://cockfile.com/upload.php',
    'https://imouto.kawaii.su/api/upload',
    'https://safe.waifuhunter.club/api/upload',
    'https://take-me-to.space/api/upload',
    'https://files.htp.sh/api/upload',
    'https://pomf.lain.la/upload.php',
    'https://smutty.horse/upload.php',
    'https://stuff.poxydoxy.com/upload.php',
    # 48小时候自动过期
    'https://uguu.se/upload.php',
    # 24小时过期
    'https://cockfile.com/upload.php',
]


def set_config(upload_url_list: List[str]):
    """
    修改此配置, 请确认您对需要的链接了解
    :param upload_url_list:
    :return:
    """
    global UPLOAD_URL_LIST
    UPLOAD_URL_LIST = upload_url_list


class PomfSe(Depot):
    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.PomfSe

    def _upload_file(self, upload_url: str, file_name: str, content):
        files = {
            'files[]': (file_name, content),
        }
        response = requests.post(upload_url, files=files)
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

    def upload(self, content) -> Optional[str]:
        if len(UPLOAD_URL_LIST) <= 0:
            return self._set_error('No service is available')

        file_name = self._random_file_name(content)
        if not file_name:
            return None
        for upload_url in UPLOAD_URL_LIST[:]:
            url = self._upload_file(upload_url, file_name, content)
            if url:
                return url
            else:  # 上传失败, 从列表中去掉, 下次上传可以跳过
                UPLOAD_URL_LIST.remove(upload_url)
        return None
