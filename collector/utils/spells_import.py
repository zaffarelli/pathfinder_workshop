"""
 ╔╦╗╔═╗  ╔═╗┌─┐┬  ┬  ┌─┐┌─┐┌┬┐┌─┐┬─┐
  ║║╠═╝  ║  │ ││  │  ├┤ │   │ │ │├┬┘
 ═╩╝╩    ╚═╝└─┘┴─┘┴─┘└─┘└─┘ ┴ └─┘┴└─
 Fading Suns
 Fusion Interlock Custom System v7
 This file contains the export to Google SpreadSheet functions

 Share with: dp-98-126@dramatis-personae-236522.iam.gserviceaccount.com
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.conf import settings
from cryptography.fernet import Fernet
from collector.models.pathfinder_spell import PathfinderSpell

SCOLS_AMOUNT = 52 * 3 + 15
SROWS_AMOUNT = 2906

# key = Fernet.generate_key() #this is your "password"
KEY = b'WAXSue9RLeTPqgdvbfrj2e60Xk6PrRgx6jo-KV8JOIw='


def encrypt(str):
    cipher_suite = Fernet(KEY)
    encoded_text = cipher_suite.encrypt(str.encode('UTF-8'))
    return encoded_text


def decrypt(str):
    cipher_suite = Fernet(KEY)
    decoded_text = cipher_suite.decrypt(str.encode('UTF-8'))
    return decoded_text


def connect():
    print("> Connecting")
    cf = 'collector/creds.json'
    cred_file = settings.STATIC_ROOT + cf
    print(cred_file)
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    print("> Sending Credentials")
    credentials = ServiceAccountCredentials.from_json_keyfile_name(cred_file, scope)
    client = gspread.authorize(credentials)
    return client


def connect_as_source():
    print("> Connecting source")
    source_name = 'spell_full'
    tab = 'Updated 31Mar2020'
    client = connect()
    sheet = client.open(source_name).worksheet(tab)
    return sheet


def rc(row, col):
    x = row * SCOLS_AMOUNT + col
    return x


def get_spells():
    header_line = []
    sheet = connect_as_source()
    matrix = sheet.get_all_values()
    print("Getting row headers/properies...")
    for idx, row in enumerate(matrix):
        if idx > 0:
            break;
        for k, v in enumerate(row):
            header_line.append(v)
    # print(header_line)
    print("Catching data...")
    for idx, row in enumerate(matrix):
        if idx > 0:
            s = PathfinderSpell()
            dismiss = False
            spell_message = ''
            for k, v in enumerate(row):
                if k == 0:
                    spell_message += f'Importing spell [{idx:04}> {v}]'
                # if header_line[k] == "source":
                #     if v not in ['PFRPG Core']:
                #         dismiss = True
                #         spell_message= ""
                if hasattr(s, header_line[k]):
                    type_name = type(getattr(s, header_line[k])).__name__
                    if header_line[k] == 'druid':
                        print(type_name, v)
                    if type_name == "str":
                        value = str(v)
                    elif type_name == "int":
                        if v == "NULL":
                            value = None
                        else:
                            value = int(v)
                    elif type_name == "bool":
                        value = False
                        if v == "1":
                            value = True
                    elif type_name == "NoneType":
                        if v == "NULL":
                            value = None
                            # print("NoneType for ", v, value)
                    setattr(s, header_line[k], value)

            if spell_message:
                print(spell_message)
            if not dismiss:
                s.save()
