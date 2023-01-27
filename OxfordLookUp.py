import requests





app_id = 'e210e241'
app_key = "4402047b5562828b52faeee6403f08d3"
language = "en-gb"

def get_def(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    r_js = r.json()
    if 'error' in r_js.keys():    # AGAR , ERROR BO'LIN CHIQSA , YA'NI KEYERROR BO'LIB DIC ICHIDA CHIQARKAN 1!>.......
        return False



    output = {}    # dic
    senses =r_js['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions = []   # list
    for sense in senses:
        definitions.append(f"➸ {sense['definitions'][0]}")   # EACH HAR BIR SENSE ICHIDAGI DEFINITIONS EKAN 1!>......
    output['definitions'] = '\n'.join(definitions)   # JOIN()  # ALL HAMMA DEFINITIONSLARNI OUTPUTNI ICHIGA DEFINITIONS KO'RINISHIDAGI KEY GA SAQLAYMIZ 1!>.......
    # BUNDAY O'YLAB QARASA, BITTA KALITGA , BIR NECHTA , VALUES KIRITISH EKAN 1!>>>>>......
    ####  1 -METHOD FOR ADDING , AUIDIOOS FILES
    if r_js['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):     # AGAR , IF , AUDIO FILE EXIST BO'LSA, GET YORDAMIDA OLA OLSA ,
        output['audio'] = r_js['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
    ###### 2 - METHOD AUDIO FILES ADDS    1!>.......
    # if r_js['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']:
    #     output['AudioFiles'] = ''.join(f"{r_js['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']}")
    #


    return output   # FIINISH RESULT 1!>........


    # TEST QILISH 1!>.......

# if __name__ == '__main__':
#     from pprint import pprint
#     pprint(get_def('America'))
#     pprint(get_def('Apple'))
#     pprint('asdkjbashfb')


