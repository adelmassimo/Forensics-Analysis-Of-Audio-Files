#http://pymysql.readthedocs.io/en/latest/user/examples.html
import sqlInterface as sql
import operator
import metric
import sys
import json
import utils 

def perpareToJSON(dic1, dic2, blackListPaht, ignoredListPaht):
	string = '['
	with open( blackListPaht ) as file:
		blackList = file.read().split("\n")
	with open( ignoredListPaht ) as file:
		ignoredList = file.read().split("\n")

	for key in dic1:
		if key not in ignoredList:
			if key in dic2:
				string += "{ 'label':'" + str(key).replace("'",'"') + "', 'alert':'" + str(key in blackList) + "', 'value1':'" + str(dic1[key]).replace("'",'"') + "', 'value2':'" + str(dic2[key]).replace("'",'"') + "'},"
			else:
				string += "{ 'label':'" + str(key).replace("'",'"') + "', 'alert':'" + str(key in blackList) + "', 'value1':'" + str(dic1[key]).replace("'",'"') + "', 'value2':' ABSENT'},"
	
	for key in dic2:
		if key not in ignoredList:
			if key not in dic1 :
				string += "{ 'label':'" + str(key).replace("'",'"') + "', 'alert':'" + str(key in blackList) + "', 'value1':'ABSENT', 'value2':'" + str(dic2[key]).replace("'",'"') + "'},"
	return string+"]"

if len(sys.argv) > 1 and len(sys.argv) < 3:
	file1 = sys.argv[1]
	file2 = sys.argv[2]
	blackList = "helpFiles/tagsBlackList.txt"
	ignoredList = "helpFiles/tagsIgnoredList.txt"
if len(sys.argv) > 3:
	file1 = sys.argv[1]
	file2 = sys.argv[2]
	blackList = sys.argv[3]
	ignoredList = sys.argv[4]
else:
	file1 = "/Users/adel/Desktop/FAOAF/Samples/iphone7.m4a"
	file2 = "/Users/adel/Desktop/FAOAF/Samples/GalaxyS4.m4a"
	blackList = "helpFiles/tagsBlackList.txt"
	ignoredList = "helpFiles/tagsIgnoredList.txt"

matchResult = {}

# with exiftool.ExifTool() as et: 
#     metadata = et.get_metadata_batch(file)[0]

queryElement = utils.extractRow(file1)
galleryElement = utils.extractRow(file2)

qResult = {}
for qKey in queryElement:
	if (qKey not in galleryElement) or not(galleryElement[qKey] == queryElement[qKey]):
		qResult[qKey] = queryElement[qKey]

gResult = {}
for gKey in galleryElement:
	if (gKey not in queryElement) or not(galleryElement[gKey] == queryElement[gKey]):
		gResult[gKey] = galleryElement[gKey]
#add lenght informations
gResult['LUNGHEZZA'] = len(galleryElement)
qResult['LUNGHEZZA'] = len(queryElement)

print "var data = " + perpareToJSON(qResult, gResult, blackList, ignoredList) + ";"
		
