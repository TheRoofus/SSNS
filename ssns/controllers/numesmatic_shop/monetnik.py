# -*- coding=utf-8 -*-

from ssns.core.session_maker import _loop, _close_session


class MoneticController:

    def __init__(self, request, models, url):
        self.request = request
        self.models = models
        self.url = url

    def __call__(self, request, models, url):
        self.request = request
        self.models = models
        self.url = url
        return self.date_for_parse(self.url)

    def date_for_parse(self, url: str):
        """

        :return:
        """
        dom = _loop(url=url)

        _close_session(workflow_runtime=True, time_close=10)
        return dom


if __name__ == '__main__':
    date = MoneticController(None, None, None)
    date(1, 2, 'https://www.monetnik.ru/')
