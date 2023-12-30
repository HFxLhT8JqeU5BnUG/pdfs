import argparse

from tests.central import test_dict

parser = argparse.ArgumentParser(description='Welcome to the PDF thing')

parser.add_argument('-t', '--test', help='Run tests', default=False)
# parser.add_argument('-f', '--file', help='Specify input file')

args = parser.parse_args()

if args.test:
    functions = test_dict.values()


for function_to_call in functions:
    function_to_call()