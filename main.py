import sqlInterface as sql
import utils 
import json

<<<<<<< HEAD
deviceModel = 'iPhone6s.m4a'
=======


deviceModel = 'GalaxyS4.m4a'
>>>>>>> 5533a7b779510cc816b8dacff2c3722a8696ff21
file = ["Samples/"+deviceModel]					
row = utils.extractRow(file, deviceModel)
sql.insertFromDic(row)
	

