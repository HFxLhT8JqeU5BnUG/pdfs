from sqlalchemy import create_engine, MetaData, select, Table


class Db:
    '''simple class for interacting with databases\n
    currently supports "postgres" and "mysql" RDBMS'''

    def __init__(self, RDBMS: str, AUTH: dict[str, str]):
        auth_params = ["USER", "PASSWORD", "HOST", "PORT", "DATABASE"]

        assert all(param in AUTH for param in auth_params), 'Missing or incorrect AUTH keys'

        if RDBMS.lower() == 'postgres':
            driver = 'postgresql+psycopg2'

        elif RDBMS.lower() == 'mysql':
            driver = 'mysql+mysqlconnector'

        self.engine = create_engine(
        f'{driver}://{AUTH["USER"]}:{AUTH["PASSWORD"]}@{AUTH["HOST"]}:{AUTH["PORT"]}/{AUTH["DATABASE"]}'
        )

        self.meta = MetaData()


    def list_tables(self, schema: str) -> dict:
        '''mostly for internal use (identifying tables passed as args)\n
        but feel free to use it to quickly get a list of all tables in a schema'''

        self.meta.reflect(bind=self.engine, schema=schema, views=True)
        return self.meta.tables


    def get(self, schema: str, table: str, cols: list[str] = ['*']) -> list[dict]:
        '''Simple select function, returns list of rows, each row as dict[column name, value]\n
        "table" can be a table name or a view
        do not qualify table names with schema, those are appended in this function\n
        just specify each\n
        cols arg is optional, defaults to *\n
        depreciated in favor of get_view()'''

        with self.engine.connect() as conn:
            select_table = self.list_tables(schema)[f'{schema}.{table}']

            if cols[0] != '*':
                stmt = select(select_table).with_only_columns()
                for col in cols: stmt = stmt.add_columns(select_table.c[col])
            else: stmt = select(select_table)

            result = conn.execute(stmt)

        return [dict(zip(result.keys(), row)) for row in result]


    def get_all(self, table: str) -> list[dict]:
        '''new function, pushes users to do database stuff on the database side\n
        all you can do with this is select * from <table/view/function>'''

        table = Table(table, self.meta, autoload_with=self.engine)

        select_query = table.select()

        with self.engine.connect() as connection:
            result = connection.execute(select_query)
            rows = [dict(zip(result.keys(), row)) for row in result.fetchall()]

        return rows
    