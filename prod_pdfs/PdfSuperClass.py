from db_submod.DB import Db
from env_submod.ENV import Env
from pdf.PDF import Pdf


class PdfSuperClass:
    '''superclass for generating PDFs\n
    pass table/view and template file name (including .pdf extension) in overwritten initialize()\n
    mapping and naming are optional. naming is HIGHLY recommended, mapping is not'''

    def __init__(self):
        self.env_interface = Env()
        DB_AUTH = self.env_interface.get_db_auth()
        self.db_interface = Db(RDBMS='postgres', AUTH = DB_AUTH)
        self.schema = None

        self.attrs = ["table", "template"]
        
        assert self.initialize(), 'Please remember to override the initialize() function'
        
        for attr in self.attrs:
            assert getattr(self, attr, False), f'Necessary PDF attribute {attr} not set in initialize()'

        pdf_params = ["TEMPLATE_DIR", "OUTPUT_DIR"]
        pdf_config = self.env_interface.get(pdf_params)

        PDF_TEMPLATE = pdf_config["TEMPLATE_DIR"] + self.template
        OUTPUT_DIR = pdf_config["OUTPUT_DIR"]

        self.pdf_interface = Pdf(PDF_TEMPLATE, OUTPUT_DIR)
        self.generate()

    
    def initialize(self) -> bool:
        '''MUST be overwritten. set template, schema, table/view, mapping, naming here'''
    # def initialize(self, table: str, template: str, schema: str = None, mapping: dict = None, naming: dict = None) -> bool:
        # self.schema = schema
        # self.table = table
        # self.template = template
        # self.pdf_mapping = mapping
        # self.naming = naming

        return False


    def generate(self):
        '''get DB data, apply transformation, write PDFs'''
        self.rows = self.db_interface.get_all(self.table, self.schema)
        self.transform()
        self.pdf_interface.write(rows = self.rows, map = self.mapping, naming = self.naming)


    def transform(self):
        '''Optional. Transform data here if desired. You're accessing self.rows (list[dict[str, Any]]) before mapping is applied.'''
        pass