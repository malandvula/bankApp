"""
MQ MALA

readingFiles.py
"""
import csv

def readCSVfile(filename):
	"""
	pre: take a csv file
	post: return list of each line in file
	"""
	fileContents = []
	with open(filename) as csvfile:
		content = csv.reader(csvfile, delimiter='\n')
		for row in content:
			#print('\n'.join(row))
			fileContents.append('\n'.join(row))

	return fileContents

def saveCSVfile(filename, contents):
	"""
	pre: get a file name
	post: reurn file in csv format
	"""
	file = open(filename, 'w')
	for row in contents:
		file.write(row)
		file.write("\n")

def main():
	print(readCSVfile("customer.csv"))
	contents = readCSVfile("customer.csv")
	saveCSVfile("customer1.csv", contents)

if __name__ == '__main__':
	main()