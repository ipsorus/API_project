from api.models import Poverka
from api.serializers import PoverkiSerializer
from django.test import TestCase


class PoverkaSerializerTestCase(TestCase):
    def test_ok(self):
        poverka_1 = Poverka.objects.create(org_title="ФГУП \"ВНИИМС\"",
                                           mit_number="5445-15",
                                           mit_title="Омметры",
                                           mit_notation="3500 мод. RM3543-01, RM3544, RM3545-02, RM3548",
                                           mi_modification="-",
                                           mi_number="676_3659",
                                           verification_date="18.06.2021",
                                           valid_date="17.06.2023",
                                           result_docnum="С-М/18-06-2021/3556590",
                                           applicability='true')
        poverka_2 = Poverka.objects.create(org_title="ФГУП \"УНИИМ\"",
                                           mit_number="65655-15",
                                           mit_title="Ваттметры",
                                           mit_notation="-",
                                           mi_modification="-",
                                           mi_number="545а459",
                                           verification_date="23.05.2021",
                                           valid_date="22.05.2022",
                                           result_docnum="И-Э/23-05-2021/366590",
                                           applicability='false')
        data = PoverkiSerializer([poverka_1, poverka_2], many=True).data
        expected_data = [
            {
                'id': poverka_1.id,
                'org_title': "ФГУП \"ВНИИМС\"",
                'mit_number': "5445-15",
                'mit_title': "Омметры",
                'mit_notation': "3500 мод. RM3543-01, RM3544, RM3545-02, RM3548",
                'mi_modification': "-",
                'mi_number': "676_3659",
                'verification_date': "18.06.2021",
                'valid_date': "17.06.2023",
                'result_docnum': "С-М/18-06-2021/3556590",
                'applicability': 'true'
            },
            {
                'id': poverka_2.id,
                'org_title': "ФГУП \"УНИИМ\"",
                'mit_number': "65655-15",
                'mit_title': "Ваттметры",
                'mit_notation': "-",
                'mi_modification': "-",
                'mi_number': "545а459",
                'verification_date': "23.05.2021",
                'valid_date': "22.05.2022",
                'result_docnum': "И-Э/23-05-2021/366590",
                'applicability': 'false'
            },
        ]
        self.assertEqual(expected_data, data)
