# Test


import sys
import argparse
# import pandas
import os.path
from os import path

class BuildHTML:
	htmlLine = ""
	def __init__(self, bigpain, platform):
		self.lineToEdit = bigpain
		self.platform = args.platform
		print( self.platform, self.lineToEdit)

	def convertToHtml(self):
		print("in convert to html")
		self.htmlLine = self.lineToEdit.replace("\\","</div><div>")
		self.htmlLine = "<div>" + self.htmlLine.strip('\n') + "</div>"
		print(self.htmlLine)
		return (self.htmlLine)


class ImportFile:
	firstTime = True
	fileName = ""
	platform = ""
	def __init__(self, fileName, platform):
		self.fileName = args.fileName
		self.platform = args.platform
		print("in constructor" + self.fileName + self.platform)

	def convertFile(self):
		
		
		with open(self.fileName, "r") as f:
			with open("fixedFile.csv", "w") as f1:
				for line in f:
					if self.firstTime:
						self.firstTime = False
						f1.write("Title,Description\n")
						print("firsttime")
					else:
						strLine = line
						
						splitArray = strLine.split(',')
						
						if len(splitArray) > 3:
							bigpain = splitArray[3]
							bh = BuildHTML(bigpain, self.platform)

							writeLine = splitArray[1] + "," + bh.convertToHtml() +'\n'
							f1.write(writeLine)
							print("other times") 
				f1.close
				f.close 

		

parser = argparse.ArgumentParser(add_help=False)

parser.add_argument('-p', action="store", dest="platform", choices=["jira"],default="jira", help=("only jira suported at this time"))
parser.add_argument('-f', action="store", dest="fileName", required=True)
args = parser.parse_args()

if not path.exists(args.fileName):
	print("file " + str(args.fileName) + "doesn't exist")
	sys.exit(1)


updateFile = ImportFile(args.fileName, args.platform)
print (updateFile.platform)
updateFile.convertFile()
print ("after convert")
