import mysql.connector
  
dataBase = mysql.connector.connect(
  host ="104.154.109.128",
  user ="root",
  passwd ="root1234",
  database = "Persons.newtable"
)

print(dataBase)

dataBase.close()