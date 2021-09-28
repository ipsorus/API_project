from rest_framework.test import APITestCase
from django.urls import reverse
from api.models import Poverka
from api.serializers import PoverkiSerializer
from rest_framework import status
from django.contrib.auth.models import User

import json


class PoverkiApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_username')

        self.poverka_1 = Poverka.objects.create(org_title="ФГУП \"ВНИИМС\"",
                                          mit_number="5445-15",
                                          mit_title="Омметры",
                                          mit_notation="3500 мод. RM3543-01, RM3544, RM3545-02, RM3548",
                                          mi_modification="-",
                                          mi_number="676_3659",
                                          verification_date="18.06.2021",
                                          valid_date="17.06.2023",
                                          result_docnum="С-М/18-06-2021/3556590",
                                          applicability='true')
        self.poverka_2 = Poverka.objects.create(org_title="ФГУП \"УНИИМ\"",
                                          mit_number="65655-15",
                                          mit_title="Ваттметры",
                                          mit_notation="-",
                                          mi_modification="-",
                                          mi_number="6575-155656",
                                          verification_date="23.05.2021",
                                          valid_date="22.05.2022",
                                          result_docnum="И-Э/23-05-2021/366590",
                                          applicability='false')
        self.poverka_3 = Poverka.objects.create(org_title="ФГУП \"УНИИМС\"",
                                          mit_number="65455-15",
                                          mit_title="Ваттметры",
                                          mit_notation="-",
                                          mi_modification="-",
                                          mi_number="5445-15",
                                          verification_date="23.05.2021",
                                          valid_date="22.05.2022",
                                          result_docnum="И-Э/23-05-2021/5445-15",
                                          applicability='false')


    def test_get(self):
        url = reverse('poverka-list')
        response = self.client.get(url)
        serializer_data = PoverkiSerializer([self.poverka_1, self.poverka_2, self.poverka_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_filter(self):
        url = reverse('poverka-list')
        response = self.client.get(url, data={'mit_title': "Ваттметры"})
        serializer_data = PoverkiSerializer([self.poverka_2, self.poverka_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('poverka-list')
        response = self.client.get(url, data={'search': "5445-15"})
        serializer_data = PoverkiSerializer([self.poverka_1, self.poverka_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_sorting(self):
        url = reverse('poverka-list')
        response = self.client.get(url, data={'ordering': "mit_number"})
        serializer_data = PoverkiSerializer([self.poverka_1, self.poverka_3, self.poverka_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        self.assertEqual(3, Poverka.objects.all().count())
        url = reverse('poverka-list')
        data = {
            "org_title": "ФГУП ВНИИОФИ",
            "mit_number": "55500-21",
            "mit_title": "Термометры",
            "mit_notation": "1СД",
            "mi_modification": "Нет модификации",
            "mi_number": "999999",
            "verification_date": "14.09.2021",
            "valid_date": "13.09.2023",
            "result_docnum": "Свидетельство о поверке 4543",
            "applicability": "true"
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data, content_type='application/json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, Poverka.objects.all().count())

    def test_update(self):
        url = reverse('poverka-detail', args=(self.poverka_1.id,))
        data = {
            "org_title": "ООО Ромашка",
            "mit_number": self.poverka_1.mit_number,
            "mit_title": self.poverka_1.mit_title,
            "mit_notation": self.poverka_1.mit_notation,
            "mi_modification": self.poverka_1.mi_modification,
            "mi_number": "009911",
            "verification_date": self.poverka_1.verification_date,
            "valid_date": self.poverka_1.valid_date,
            "result_docnum": self.poverka_1.result_docnum,
            "applicability": "false"
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.put(url, data=json_data, content_type='application/json')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.poverka_1.refresh_from_db()
        self.assertEqual("ООО Ромашка", self.poverka_1.org_title)
        self.assertEqual("009911", self.poverka_1.mi_number)
        self.assertEqual("false", self.poverka_1.applicability)
