# -*- coding=utf-8 -*-

from typing import Tuple

from ssns.core.session_maker import _loop, _close_session


class MonetikController:

    def __init__(self, request, models, url):
        self.request = request
        self.models = models
        self.url = url

    def __call__(self):
        return self.date_for_parse()

    def date_for_parse(self) -> Tuple[int, str]:
        """
        Method MonetikController

        :return: is now DOM.
        """
        # ToDo Добавить парсинг ДОМа.
        dom = _loop(url=self.url)

        _close_session(workflow_runtime=True, time_close=1)
        return dom


if __name__ == '__main__':
    date = MonetikController(1, 2, 'https://www.numizmatik.ru/')
    date.date_for_parse()
