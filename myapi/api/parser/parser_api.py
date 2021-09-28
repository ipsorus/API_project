import django
import os
from requests.exceptions import HTTPError
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapi.settings")
django.setup()

from api.models import Poverka
#from django.db.models import *


def get_api_data():
    vri_url = 'https://fgis.gost.ru/fundmetrologytest/eapi/vri'
    params = {
        'year': 2021,
        'start': 2,
        'rows': 5
    }
    #print(requests.codes.ok)
    try:
        response = requests.get(vri_url, params=params)
        # если ответ успешен, исключения задействованы не будут
        response.raise_for_status()
        result = response.json()
        #print(response.json(), response.status_code, response.headers)

        for item in range(result['result']['rows']):
            #print('Number: ', item)
            res = result['result']['items'][item]
            save_data = db_item_create(res)
            # for key, value in res.items():
            #     print('ключ: ', key, ', значение: ', value)
        return save_data

    except (requests.RequestException, ValueError) as err:
        print(f'HTTP error occurred: {err}')
        print(response.status_code)
        return err
    except Exception as other_err:
        print(f'Other error occurred: {other_err}')
        return other_err

        # print(res['org_title'])

    # if response.status_code == 200:
    #     print('test')


def db_item_create(poverki_list):

    item_add = Poverka.objects.create(org_title=poverki_list['org_title'], mit_number=poverki_list['mit_number'], mit_title=poverki_list['mit_title'], mit_notation=poverki_list['mit_notation'], mi_modification=poverki_list['mi_modification'],
                                      mi_number=poverki_list['mi_number'], verification_date=poverki_list['verification_date'], valid_date=poverki_list['valid_date'], result_docnum=poverki_list['result_docnum'], applicability=poverki_list['applicability'])
    return 'Данные внесены в БД'


if __name__ == '__main__':

    parsing = get_api_data()
    print(parsing)
