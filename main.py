import argparse

from tests.central import test_dict
from prod_pdfs.central import pdf_dict

parser = argparse.ArgumentParser(description='Welcome to the PDF thing')

parser.add_argument('-t', '--test', help='Run tests', default=False)
parser.add_argument('-m', '--module', help='Specify module to run', default=False)

args = parser.parse_args()

if args.test:
    assert test_dict.get(args.test, False), f'Test {args.test} not found'
    function_to_call = test_dict.get(args.test)

elif args.module:
    assert pdf_dict.get(args.module, False), f'Module {args.module} not found'
    function_to_call = pdf_dict.get(args.module)


function_to_call()