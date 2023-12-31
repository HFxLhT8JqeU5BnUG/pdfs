from etb_db.DB import Db
from etb_env.ENV import Env

def example_table():
    env_interface = Env()
    DB_AUTH = env_interface.get_db_auth()

    db_interface = Db(RDBMS='postgres', AUTH = DB_AUTH)

    table = 'example_table'
    rows = db_interface.get_all(table)

    print(rows)