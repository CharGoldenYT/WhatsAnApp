# -*- mode: python ; coding: utf-8 -*-
import sys
import os
from PyInstaller.utils.hooks import collect_all

# Collect metadata/binaries for Webview
datas_wv, binaries_wv, hiddenimports_wv = collect_all('webview')

if sys.platform == "win32":
    icon_file = "assets/WhatsAnApp.ico"
else:
    icon_file = "assets/WhatsAnApp.png"

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=binaries_wv,
    datas=[('assets', 'assets')] + datas_wv,
    hiddenimports=[
        'pywebview', 
        'flask', 
        'qtpy', 
        'PyQt5',
        'PyQt5.QtWebEngineWidgets'
    ] + hiddenimports_wv,
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
    name='WhatsAnApp',
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
    icon=icon_file
)