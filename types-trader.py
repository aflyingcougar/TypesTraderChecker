#Python code to illustrate parsing of XML files
# importing the required modules
import csv
# import requests
import re
import xml.etree.ElementTree as ET

def parseTypes(xmlfile):

	# create element tree object
	tree = ET.parse(xmlfile)

	# get root element
	root = tree.getroot()

	# create empty list for item types
	types = []

	# iterate item types
	for item in root.findall('./type'):

		typeName = item.attrib['name']

		# append type name item types list
		types.append(typeName)
	
	# return types list
	return types

def parseTrader(txtfile):

	filename = 'TraderConfig.txt'
	pattern = re.compile(r"^\s+(?!Each)(?!You)\w+", re.IGNORECASE)
	traderTypes = []

	# Make sure the file gets closed after being iterated
	with open(filename, 'r') as f:
		# Read the file contents and generate a list with each line
		lines = f.readlines()

	# Iterate each line
	for line in lines:
		match = re.search(pattern, line)

		if match:
			new_line = match.group()
			# print(new_line)
			
			#  Remove tabs
			tabs = re.compile(r"^\s+", re.IGNORECASE)
			new_line = tabs.sub('', new_line)
			
			traderTypes.append(new_line)

	removeDuplicates(traderTypes)

	return traderTypes

def checkIfDuplicates(list):
	# check if given list contains any duplicates
	duplicates = 0
	types = set()
	for item in list:
		if item in types:
			print("Duplicate type: " + str(item))
			duplicates = duplicates + 1

		else:
			types.add(item)

	return str(duplicates)

def removeDuplicates(typesList):
	typesList = list(set(typesList))

def typesNotInTrader(itemTypes, traderTypes):

	missingTypes = []

	for type in itemTypes:
		if not(type.upper() in (traderType.upper() for traderType in traderTypes)):
			missingTypes.append(type)

	return missingTypes

def savetoCSV(types, filename):
  
    # specifying the fields for csv file
	fields = ['Type Name']
  
    # writing to csv file
	with open(filename, 'w', newline='') as csvfile:
  
        # creating a csv dict writer object
		writer = csv.writer(csvfile)
  
        # writing headers (field names)
		writer.writerow(fields)
  
		for item in types:
			writer.writerow([item])
        
def main():
	
	# parse Types.xml file
	itemTypes = parseTypes('types.xml')

	# parse TraderConfig.txt
	traderTypes = parseTrader('TraderConfig.txt')

	savetoCSV(itemTypes, 'types.csv')
	savetoCSV(traderTypes, 'trader.csv')

	print('Number of types in types.xml: ' + str(len(itemTypes)))
	print('Number of unique types in TraderConfig.txt: ' + str(len(traderTypes)))
	print('Checking for duplicates in types.xml... ' + checkIfDuplicates(itemTypes) + ' found')
	
	savetoCSV(typesNotInTrader(itemTypes, traderTypes), 'typesNotInTrader.csv')
	print('Saved types not in trader: typesNotInTrader.csv!')
	

	
	
if __name__ == "__main__":

	# calling main function
	main()
