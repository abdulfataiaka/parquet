import sys

srcdir = '/tmp/exports'
destdir = '/tmp/imports'
tbnames = sys.argv[1:]

print(f"\n[*] Tables to import: {'<Empty>' if not len(tbnames) else ''}")
for tbname in tbnames:
  print(f'     * {tbname}')
print('')

print('Start actual conversions')
