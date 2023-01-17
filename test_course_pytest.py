import requests


class TestCourses:
    headers = {'Authorization': 'Token 80ab360d3632ee23c24d64cf8abf4363ab80c3aa'}
    url_base_courses = 'http://localhost:8000/api/v1/courses/'

    def test_get_courses(self):
        courses = requests.get(url=self.url_base_courses, headers=self.headers)

        assert courses.status_code == 200

    def test_get_course(self):
        course = requests.get(url=f'{self.url_base_courses}18/', headers=self.headers)

        assert course.status_code == 200

    def test_post_course(self):
        new = {
            "title": "Course DjangoRest",
            "url": "http://www.coursedjangorest.com.br"
        }
        result = requests.post(url=self.url_base_courses, headers=self.headers, data=new)

        assert result.status_code == 201
        assert result.json()['title'] == new['title']

    def test_put_course(self):
        updated = {
            "title": "Course Django_Rest",
            "url": "http://www.djangorestcourse.com.br"
        }

        answer = requests.put(url=f'{self.url_base_courses}18/', headers=self.headers, data=updated)

        assert answer.status_code == 200

    def test_delete_course(self):

        answer = requests.delete(url=f'{self.url_base_courses}18/', headers=self.headers)

        assert answer.status_code == 204 and len(answer.text) == 0
