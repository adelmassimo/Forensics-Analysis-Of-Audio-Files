#http://pymysql.readthedocs.io/en/latest/user/examples.html
import sqlInterface as sql
import exiftool
from pymediainfo import MediaInfo
import json
# with exiftool.ExifTool() as et:
# 	print path+file
# 	metadata = et.get_metadata_batch('/User/adel/Desktop/Samples/GalaxyS5.m4a')

deviceModel = 'LGG6.m4a'

files = ["Samples/"+deviceModel]
#files = ["Samples/GalaxyS5.m4a"]

with exiftool.ExifTool() as et:
    allMetadatas = et.get_metadata_batch(files)
    #print metadata

MI = MediaInfo.parse("Samples/"+deviceModel)
mediaInfo = json.loads(MI.to_json())
#print mediaInfo['tracks']

for metadata in allMetadatas:
	#FORMATO QUERY MYSQL: INSERT INTO myDb.myTable('','') VALUES ('', '')
	metadata['groundtruth'] = deviceModel.split('.')[0]
	# posso aggiungere cosa cazzo voglio 
	sql.insertFromDic(metadata)

for info in mediaInfo:
	#FORMATO QUERY MYSQL: INSERT INTO myDb.myTable('','') VALUES ('', '')
	sql.insertFromDic(mediaInfo)
