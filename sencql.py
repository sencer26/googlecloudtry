import mysql.connector

dataBase = mysql.connector.connect(
  host ="104.154.109.128",
  user ="root",
  passwd =">SbEPMLp=e_o[Vb#",
  database = "User_Dashboard"
)

 

print(dataBase)

 

dataBase.close()
