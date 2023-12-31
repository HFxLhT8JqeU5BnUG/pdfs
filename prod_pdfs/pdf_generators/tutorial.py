from prod_pdfs.PdfSuperClass import PdfSuperClass
from ..configs.tutorial_conf import tutorial_mapping, tutorial_naming

class TutorialPdf(PdfSuperClass):
    '''tutorial PDF class to demonstrate usage'''

    def initialize(self) -> bool:
        self.schema = 'test_schema'
        self.table = 'tutorial_pdf_view'
        self.template = 'pdf_form_example.pdf'
        self.mapping = tutorial_mapping
        self.naming = tutorial_naming
        
        return True


    def transform(self):
        for row in self.rows:
            row["row_num"] = row["varchar_col"].split()[1]
            row['int_col'] = str(int(row['int_col'])/2)
            # ^^idk man, just trying to show that you can do stuff to the data here