import xml.etree.ElementTree as ET

def printit():
	tree = ET.parse('samplexml.xml')
	root = tree.getroot()
	print (root.tag)

def main():
	printit()

if __name__ == '__main__':
    main()