import csv
import rook

rook.start(token='7aec038f4253ae4d0056ea75d634db2f5d45a3c885cfeb527b20e0b1bcd4a86f', labels={"env":"dev"})
if __name__ == "__main__":
    rook.start(token='[7aec038f4253ae4d0056ea75d634db2f5d45a3c885cfeb527b20e0b1bcd4a86f]',
               labels={"env": "dev"}) # Optional,see Labels page below Projects
    # Your program starts here :)
file = open("\\temp\status_update.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()
