from typing import Optional
import requests
from image_depot import DepotType
from .base import Depot


class PomfSe(Depot):
    @classmethod
    def depot_type(cls) -> DepotType:
        return DepotType.PomfSe

    def _upload_file(self, upload_url: str, file_name: str, content):
        files = {
            'files[]': (file_name, content),
        }
        try:
            response = requests.post(upload_url, files=files)
        except Exception as e:
            # 因为这里会访问多个上传地址, 这次失败了继续下一个
            # 所以要把异常自己消化掉
            return self._set_error(e)

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

    def _upload(self, content) -> Optional[str]:
        conf = self._config.pomf_se
        if len(conf.upload_url_list) <= 0:
            return self._set_error('No service is available')
        file_name = self._random_file_name(content)
        if not file_name:
            return None
        for upload_url in conf.upload_url_list[:]:
            url = self._upload_file(upload_url, file_name, content)
            if url:
                return url
            else:  # 上传失败, 从列表中去掉, 下次上传可以跳过
                conf.upload_url_list.remove(upload_url)
        return None
