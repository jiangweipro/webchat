# encoding:utf-8

from common import log, const


# 启动通道
def start_process():
    from channel.http.http_channel import HttpChannel
    channel = HttpChannel()
    channel.startup()


if __name__ == '__main__':
    try:
        start_process()
        exit(0)

    except Exception as e:
        log.error("App startup failed!")
        log.exception(e)
