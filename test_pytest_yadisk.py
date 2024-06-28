import pytest
import requests

class TestYandexDisk:
    def setup_method(self):
        self.headers = {
            'Authorization': 'OAuth y0_AgAAAAB0PhTFAADLWwAAAAD9GyauAABFMKwdwMdL74S07kEG7swpKVd2Tg'
        }

    @pytest.mark.parametrize(
        'param,value,status',
        (
                ['pat', 'new_folder', 400],
                ['path', 'new_folder', 201],
                ['path', 'new_folder', 409],
        )
    )
    def test_create_folder(self, param, value, status):
        params = {param: value}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params)
        assert response.status_code == status

    @pytest.mark.parametrize(
        'param,value,status,headers',
        (
                ['path', 'new_folder', 401, {'Authorization': 'OAuth y0'}],
        )
    )
    def test_wrong_token(self, param, value, status, headers):
        params = {param: value}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=headers,
                                params=params)
        assert response.status_code == status


