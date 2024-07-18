# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['NovaDireita.py'],
    pathex=[],
    binaries=[],
    datas=[('../src_files/icon/logo.ico', 'icon'), ('../src_files/version.txt', '.')],
    hiddenimports=['pymysql', 'pandas', 'smtplib', 'ssl', 'tkcalendar', 'babel.numbers'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='NovaDireita',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['..\\src_files\\icon\\logo.ico'],
)
