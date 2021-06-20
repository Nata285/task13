import requests
import vk

url = 'https://vk.com/dev/photos.get'
params = {'owner_id':'552934290', 'v': '5.131',
          'access token':
          '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008',
          'album_id':'profile',
          'extended': '1',
          'photo_sizes':'1'}
resp = requests.get(url=url, params=params)
print(resp.json())