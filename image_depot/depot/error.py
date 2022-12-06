"""
定义仓库异常
@author hujing
"""
import traceback


class DepotError:
    def __init__(self, err, tb):
        """
        :param err:
        :param tb: 堆栈信息
        """
        if not tb:
            tb = traceback.extract_stack()[0:-1]
            tb = ''.join(traceback.format_list(tb))
        self._err = err
        self._traceback = tb

    def error(self):
        return self._err

    def traceback(self):
        return self._traceback

    def __str__(self):
        return self.error() + '\n' + \
            self.traceback()
