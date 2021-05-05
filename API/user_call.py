import json
import requests
from requests.structures import CaseInsensitiveDict



class user_API:
    def get_jwt(self, my_id):
        url = 'https://api-dw.heysingles.com/v2/app/getJWT/' + my_id
        response = requests.get(url).json()
        return response['accessToken']

    def get_init_data(self, my_id):
        access_token = self.get_jwt(my_id)
        url = "https://api-dw.heysingles.com/v2/auth/init"
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = "Bearer " + access_token
        response = requests.post(url=url, data={}).json()
        return response

    def get_users(self, my_id, user_id):
      access_token = self.get_jwt(my_id)
      print(access_token)
      url = "https://api-dw.heysingles.com/v2/users"
      headers = CaseInsensitiveDict()
      headers["Accept"] = "application/json"
      headers["Authorization"] = "Bearer " + access_token
      data = json.dumps({
        'userId': user_id})
      print(data)
      response = requests.post(url=url, data=data, headers=headers).json()
      return response

    def get_users_gender(self, my_id, user_id):
      access_token = self.get_jwt(my_id)
      print(access_token)
      url = "https://api-dw.heysingles.com/v2/users"
      headers = CaseInsensitiveDict()
      headers["Accept"] = "application/json"
      headers["Authorization"] = "Bearer " + access_token
      data = json.dumps({
        'userId': user_id})
      print(data)
      response = requests.post(url=url, data=data, headers=headers).json()
      return response['user']['gender']

