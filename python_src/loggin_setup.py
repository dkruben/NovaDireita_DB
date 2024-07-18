# -*- coding: utf-8 -*-
import logging
import os
from datetime import datetime


def setup_logging():
    log_directory = 'logs'
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    current_date = datetime.now().strftime('%d-%m-%Y')
    log_filename = f'{log_directory}/novadireita_{current_date}.log'
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        datefmt='%d-%m-%Y %H:%M:%S',
        filename=log_filename,
        filemode='a'
    )
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    return logging.getLogger('NovaDireita')


logger = setup_logging()
