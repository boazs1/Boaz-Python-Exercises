import csv
import rook

rook.start(token='7aec038f4253ae4d0056ea75d634db2f5d45a3c885cfeb527b20e0b1bcd4a86f',
    labels=None,
    git_commit='bfdd9510bfcbb7c9b990d10a9fb6d3356abad565',
    git_origin='https://github.com/boazs1/Boaz-Python-Exercises'
)

file = open("\\temp\status_update.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()
i = 1
while i < 1000000000:
  print(i)
  i += 1
