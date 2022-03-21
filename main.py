import logging
from connectors.binance_futures import BinanceFuturesClient
from interface.root_component import Root
import tkinter as tk

logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == '__main__':

    binance = BinanceFuturesClient("57f5560b4991ecdeed954ba8b9a8140231a73846b4775c1d8ba97710e7da9c52",
                                   "fb3dc665d6bbb9b6773bf4e65d508842774ca08e15bba7f3bfc4c439e0687762", True)

    root = Root(binance)
    root.mainloop()
