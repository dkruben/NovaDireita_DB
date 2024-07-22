# -*- coding: utf-8 -*-


def setup_logging():
    # logs_dir = os.path.join(os.path.dirname(__file__), 'logs')
    # os.makedirs(logs_dir, exist_ok=True)
    # current_date = datetime.now().strftime('%d-%m-%Y')
    # log_filename = f'{logs_dir}/novadireita_{current_date}.log'
    # logging.basicConfig(
    #    level=logging.DEBUG,
    #    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    #    datefmt='%d-%m-%Y %H:%M:%S',
    #    filename=log_filename,
    #    filemode='w'
    # )
    # console = logging.StreamHandler()
    # console.setLevel(logging.INFO)
    # formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    # console.setFormatter(formatter)
    # logging.getLogger('').addHandler(console)
    # return logging.getLogger('NovaDireita')
    pass


logger = setup_logging()
