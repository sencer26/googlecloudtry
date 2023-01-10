import mysql.connector
import panel as pn
pn.extension('tabulator',notifications=True)


button = pn.widgets.Button(name = 'query')
table =  pn.widgets.Tabulator()

def on_click(event):
    #pn.state.notifications.info('connect stared')
    print('Started')
    try:
        dataBase = mysql.connector.connect(
          #host ="10.47.160.3",
          host ="104.154.109.128",
          user ="root",
          passwd =">SbEPMLp=e_o[Vb#",
          database = "User_Dashboard"
        )
    except Exception as e:
        print(e)
        #pn.state.notifications.info(f'connect faied: {e}')
        return 


    # preparing a cursor object
    cursorObject = dataBase.cursor()

    query = """
    SELECT * FROM Persons
    """
    
    cursorObject.execute(query)

    myresult = cursorObject.fetchall()

    for x in myresult:
        #pn.state.notifications.info(f'{x}')
        print(x)
    df = pd.DataFrame(myresult)
    table.value = df
    # disconnecting from server
    dataBase.close()
    #pn.state.notifications.success('successful closed')

button.on_click(on_click)
pn.Column(
    button,
    table
).servable();
