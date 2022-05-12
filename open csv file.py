import csv
import rook
start(token=None,
    host=None,
    port=None,
    debug=None,
    throw_errors=None,    
    log_to_stderr=None,
    labels=None,
    git_commit=None,
    git_origin=None,
    fork=None,
    **kwargs)
rook.start(token='7aec038f4253ae4d0056ea75d634db2f5d45a3c885cfeb527b20e0b1bcd4a86f', labels={"env":"dev"})
file = open("\\temp\status_update.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()
