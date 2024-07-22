# -*- coding: utf-8 -*-
import os
from PyInstaller.__main__ import run

__version__ = '1.0.0'

icon_dir = os.path.join('src_files', 'logos', 'logo.ico')


def generate_exe():
    opts = [
        '--name=Nova Direita',
        'python_src/main.py',
        '--onefile',
        '--windowed',
        '--hidden-import=pymysql',
        '--hidden-import=pandas',
        '--hidden-import=smtplib',
        '--hidden-import=ssl',
        '--hidden-import=tkcalendar',
        '--hidden-import=babel.numbers',
        '--icon=src_files/logos/logo.ico',
        f'--add-data={icon_dir};icon',
        '--add-data=version.txt;.',
        '--workpath=build',
        '--distpath=dist',
        f'--version-file=version.txt',
    ]
    return opts


if __name__ == '__main__':
    opts = generate_exe()
    run(opts)
