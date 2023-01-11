import panel as pn
import sqlalchemy
import pandas as pd

pn.extension('tabulator') #,notifications=True)


button = pn.widgets.Button(name = 'query')
table =  pn.widgets.Tabulator()


def init_db_connection():
    db_config = {
        'pool_size': 5,
        'max_overflow': 2,
        'pool_timeout': 30,
        'pool_recycle': 1800,
    }
    return init_unix_connection_engine(db_config)

def init_unix_connection_engine(db_config):    
    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername="postgres+pg8000",
            query={"unix_sock": "/cloudsql/jupyter-1-09042020:us-central1:sencql/.s.PGSQL.5432"},
            username="root",
            password=">SbEPMLp=e_o[Vb#",
            database="User_Dashboard",
        ),
        **db_config
    )
    pool.dialect.description_encoding = None
    return pool

db = init_db_connection()


def on_click(event):
   
    print('Started')

    with db.connect() as conn:
        # Execute the query and fetch all results
        myresult = conn.execute(
            "SELECT * FROM Persons "
        ).fetchall()
        
    df = pd.DataFrame(myresult)
    table.value = df
        


button.on_click(on_click)
pn.Column(
    button,
    table
).servable();
##
