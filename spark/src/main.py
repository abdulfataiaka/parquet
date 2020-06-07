import sys
# from csv_to_parquet import CsvToParquet

rootdir = sys.argv[1]
names = sys.argv[2:]

print(f"\n[*] Rootdir: {rootdir}")
print(f"\n[*] Names:")
for name in names:
  print(f"     * {name}")
print("")

# CsvToParquet.call(names, rootdir)
