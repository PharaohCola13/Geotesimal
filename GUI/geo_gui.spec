# -*- mode: python -*-

block_cipher = None


a = Analysis(['geo_gui.py'],
             pathex=['/home/pharaohcola13/PycharmProjects/Research/geometric-models/GUI'],
             binaries=[],
             datas=[],
             hiddenimports=['PIL._tkinter_finder'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='geo_gui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
