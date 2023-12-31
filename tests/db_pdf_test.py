from db_submod.DB import Db
from env_submod.ENV import Env
from pdf.PDF import Pdf
from .configs.db_pdf_test_conf import pdf_mapping, pdf_naming


class PdfTester:
    def __init__(self):
        self.env_interface = Env()
        DB_AUTH = self.env_interface.get_db_auth()
        self.db_interface = Db(RDBMS='postgres', AUTH = DB_AUTH)
        

        self.table = 'example_pdf_view'

        pdf_params = ["TEMPLATE_DIR", "OUTPUT_DIR"]
        pdf_config = self.env_interface.get(pdf_params)

        PDF_TEMPLATE = pdf_config["TEMPLATE_DIR"] + 'test.pdf'
        OUTPUT_DIR = pdf_config["OUTPUT_DIR"]

        self.pdf_interface = Pdf(PDF_TEMPLATE, OUTPUT_DIR)
        self.generate()


    def generate(self):
        rows = self.db_interface.get_all(self.table)
        self.pdf_interface.write(rows = rows, map = pdf_mapping, naming = pdf_naming)
