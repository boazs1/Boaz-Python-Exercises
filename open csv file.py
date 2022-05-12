import csv
import rook

rook.start(token='7aec038f4253ae4d0056ea75d634db2f5d45a3c885cfeb527b20e0b1bcd4a86f', labels={"service":"service#3","env":"dev"},
host='ROOKOUT_CONTROLLER_HOST',
    port=None,
    debug='ROOKOUT_DEBUG',
    throw_errors=None,
    log_to_stderr=None,
    git_commit='ROOKOUT_COMMIT',
    git_origin='ROOKOUT_REMOTE_ORIGIN',
    fork='ROOKOUT_ENABLE_FORK')

file = open("\\temp\status_update.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()
