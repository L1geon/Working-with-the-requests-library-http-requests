import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {self.token}"
        }

    def _upload_link(self, file_path: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def upload_file(self, file_path: str, filename: str):
        href_json = self._upload_link(file_path)
        href = href_json["href"]
        resp = requests.put(href, data=filename)
        resp.raise_for_status()
        if resp.status_code == 201:
            print("Good!")
