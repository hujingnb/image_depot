"""
定义仓库
@author hujing
"""
import traceback


class DepotError:
    def __init__(self, err, back_num=0):
        """
        :param err:
        :param back_num: 堆栈回溯的数量. 在打印堆栈信息的时候去掉最后几个
        """
        self._err = err
        #  最后一个元素是当前构造函数, 去掉
        self._traceback = traceback.extract_stack()[0:-1-back_num]

    def error(self):
        return self._err

    def traceback(self):
        return self._traceback

    def __str__(self):
        return self._err + '\n' + \
               ''.join(traceback.format_list(self._traceback))
