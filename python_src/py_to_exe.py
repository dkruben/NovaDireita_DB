# -*- coding: utf-8 -*-
import os
from PyInstaller.__main__ import run

icon_dir = os.path.join('/'.join(['..', 'src_files', 'icon', 'logo.ico']))
vers_dir = os.path.join('/'.join(['..', 'src_files', 'version.txt']))


def generate_exe():
    opts = [
        'NovaDireita.py',
        '--onefile',
        '--windowed',
        '--hidden-import=pymysql',
        '--hidden-import=pandas',
        '--hidden-import=smtplib',
        '--hidden-import=ssl',
        '--hidden-import=tkcalendar',
        '--hidden-import=babel.numbers',
        '--icon=../src_files/icon/logo.ico',
        f'--add-data={os.path.join(icon_dir)};icon',
        f'--add-data={os.path.join(vers_dir)};.',
        f'--workpath=../build',
        f'--distpath=../dist'
    ]
    return opts


if __name__ == '__main__':
    opts = generate_exe()
    run(opts)
