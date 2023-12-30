import os
from dotenv import load_dotenv

class Env:
    '''provides nice central access to grab ENV vals'''

    def __init__(self):
        load_dotenv()

    def get(self, credentials: list[str]) -> dict:
        '''pass list of env values to get, returns key-value mapping of env val name : value'''
        credential_dict = {}

        for entry in credentials:
            value = os.environ.get(entry, False)
            assert value, f'ENV value {entry} not found'

            credential_dict[entry] = value

        return credential_dict