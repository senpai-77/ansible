import pandas
import sys

inputFile = str(sys.argv[1])
outputFile = str(sys.argv[2])

print(inputFile)
print(outputFile)

pandas.read_json(inputFile).to_excel(outputFile)