import sys
from converter import Converter

tbnames = sys.argv[1:]

csvdir = '/tmp/exports'
destdir = '/tmp/imports'

print(f"\n[*] Tables to import: {'<Empty>' if not len(tbnames) else ''}")
for tbname in tbnames:
  print(f'     * {tbname}')
print('')

converter = Converter(tbnames, csvdir, destdir)
converter.perform()
