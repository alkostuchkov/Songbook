# -*- mode: python -*-

block_cipher = None

a = Analysis(
  ['main.py'],
  pathex=[
   '/home/alexander/Projects/Python/Songbook/.venv/lib/python3.12/site-packages/PySide6/',
   '/home/alexander/Projects/Python/Songbook/exe'],
  binaries=[],
  datas=[],
  hiddenimports=[],
  hookspath=[],
  runtime_hooks=[],
  excludes=[],
  win_no_prefer_redirects=False,
  win_private_assemblies=False,
  cipher=block_cipher,
  noarchive=False)
pyz = PYZ(
  a.pure, a.zipped_data,
  cipher=block_cipher)
exe = EXE(
  pyz,
  a.scripts,
  a.binaries,
  a.zipfiles,
  a.datas,
  [],
  name='Songbook',
  debug=False,
  bootloader_ignore_signals=False,
  strip=False,
  upx=True,
  runtime_tmpdir=None,
  console=False , version='version.txt' , icon='./icons/songbook.ico')
