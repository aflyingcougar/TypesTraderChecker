#Python code to illustrate parsing of XML files
# importing the required modules
import csv
# import requests
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


def savetoCSV(types, filename):

	# specifying the fields for csv file
	fields = ['name']

	# writing to csv file
	with open(filename, 'w') as csvfile:

		# creating a csv type writer object
		writer = csv.DictWriter(csvfile, fieldnames = fields)

		# writing headers (field names)
		writer.writeheader()

		# writing data rows
		writer.writerows(types)

	
def main():
	# load rss from web to update existing xml file
	# loadRSS()

	# parse Types.xml file
	itemTypes = parseTypes('types.xml')

	# store news items in a csv file
	# savetoCSV(itemTypes, 'parsedTypes.csv')

	for item in itemTypes:
		print(item)
	
	
if __name__ == "__main__":

	# calling main function
	main()
