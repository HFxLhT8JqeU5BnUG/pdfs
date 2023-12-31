from etb_pdf.PDF import Pdf
from etb_env.ENV import Env

def pdf_test():
    env_interface = Env()
    pdf_params = ["OUTPUT_DIR", "TEMPLATE_DIR"]
    params = env_interface.get(pdf_params)

    pdfer = Pdf(params['TEMPLATE_DIR']+'test.pdf', params['OUTPUT_DIR'])
    rows = [{'foo': 'John', 'bar': 25}, {'foo': 'Jane', 'bar': 30}]

    mapping = {'name' : 'foo', 'age' : 'bar'}
    naming = {'static_name' : 'output', 'dynamic_name_key' : 'name'}
    pdfer.write(rows = rows, map = mapping, naming = naming)

# sudo docker run -v ./OUTPUT_DIR:/app/OUTPUT_DIR pdfs