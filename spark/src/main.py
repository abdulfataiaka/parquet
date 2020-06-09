import sys
from schemas import Schemas
from converter import Converter

tbnames = sys.argv[1:]
csvdir = '/tmp/exports'
destdir = '/tmp/imports'

schemas = Schemas()
print(f"\n[*] Registered schemas: {'<Empty>' if not len(schemas.tbnames) else ''}")
for stbname in schemas.tbnames:
  print(f'     * {stbname}')
print('')

print(f"\n[*] Tables to import: {'<Empty>' if not len(tbnames) else ''}")
for tbname in tbnames:
  print(f'     * {tbname}')
print('')

converter = Converter(tbnames, schemas, csvdir, destdir)
converter.perform()
