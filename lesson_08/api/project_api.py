import requests

from config import BASE_URL, HEADERS


class ProjectAPI:

    def create_project(self, title):
        body = {
            "title": title
        }

        response = requests.post(
            f"{BASE_URL}/projects",
            json=body,
            headers=HEADERS
        )

        return response

    def get_project(self, project_id):
        response = requests.get(
            f"{BASE_URL}/projects/{project_id}",
            headers=HEADERS
        )

        return response

    def update_project(self, project_id, title):
        body = {
            "title": title
        }

        response = requests.put(
            f"{BASE_URL}/projects/{project_id}",
            json=body,
            headers=HEADERS
        )

        return response
