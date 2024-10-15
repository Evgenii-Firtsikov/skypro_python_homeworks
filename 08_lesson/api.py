import requests

class ProjectPage:
    BASE_URL = "https://yougile.com/api-v2/projects"
    API_KEY = "# Вставить токен авторизации"

    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {self.API_KEY}",
            "Content-Type": "application/json"
        }

    def create_project(self, data):
        response = requests.post(self.BASE_URL, json=data, headers=self.headers)
        return response

    def get_projects(self):
        response = requests.get(self.BASE_URL, headers=self.headers)
        return response

    def get_project(self, project_id):
        url = f"{self.BASE_URL}/{project_id}"
        response = requests.get(url, headers=self.headers)
        return response

    def delete_project(self, project_id):
        url = f"{self.BASE_URL}/{project_id}"
        response = requests.put(url, json={"deleted": True}, headers=self.headers)
        return response
