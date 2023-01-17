import requests


class TestAssessments:
    headers = {'Authorization': 'Token 80ab360d3632ee23c24d64cf8abf4363ab80c3aa'}
    url_base_assessments = 'http://localhost:8000/api/v1/assessments/'

    def test_get_assessments(self):
        assessments = requests.get(url=self.url_base_assessments, headers=self.headers)

        assert assessments.status_code == 200

    def test_get_assessment(self):
        assessment = requests.get(url=f'{self.url_base_assessments}18/', headers=self.headers)

        assert assessment.status_code == 200

    def test_post_assessment(self):
        new = {
            "course": 3,
            "name": "Alan",
            "email": "alan@gmail.com",
            "comment": "Otimo.",
            "assessment": "4"
        }
        result = requests.post(url=self.url_base_assessments, headers=self.headers, data=new)

        assert result.status_code == 201
        assert result.json()['name'] == new['name']

    def test_put_assessment(self):
        updated = {
            "course": 3,
            "name": "alan2",
            "email":"alan2@gmail.com",
            "comment": "Otimo",
            "assessment": "3"
        }

        answer = requests.put(url=f'{self.url_base_assessments}18/', headers=self.headers, data=updated)

        assert answer.status_code == 200

    def test_delete_assessment(self):

        answer = requests.delete(url=f'{self.url_base_assessments}18/', headers=self.headers)

        assert answer.status_code == 204 and len(answer.text) == 0
