import requests
from pprint import pprint

TOKEN = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
USER_ID = '552934290'
token_yd = ''

url = 'https://api.vk.com/method/photos.get'
params = {'owner_id':USER_ID,
          'v': '5.77',
          'access_token': TOKEN,
          'album_id':'profile',
          'extended': '1',
          'photo_sizes':'1'}
resp = requests.get(url=url, params=params)
if resp.status_code != 200:
    raise Exception("Unable to get photos")
photos = resp.json()['response']['items']


def get_upload(file, token_yd):
    url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    params = {"path": file, "fields": "json", "overwrite": "true"}
    headers = {'Accept': 'application/json', 'Authorization': f'OAuth {token_yd}'}
    resp = requests.get(url, params=params, headers=headers)
    href = resp.json()['href']
    return href


def get_biggest_px (size_dict):
    if size_dict['width']>= size_dict['height']:
        return size_dict['width']
    else:
        return size_dict['height']

def download_photo(url):
    r = requests.get(url)
    filename = url.split('?')[0].split('/')[-1]
    with open(filename, 'bw') as file:
        for chuk in r.iter_content(4096):
            file.write(chuk)

for photo in photos:

    sizes = photo['sizes']
    max_size_url = max(sizes, key=get_biggest_px)['url']
    max_size_type = max(sizes, key=get_biggest_px)['type']
    file_name = max_size_url.split('?')[0].split('/')[-1]
    download_photo(max_size_url)
    url = get_upload(file_name,token_yd)
    params = {'path': f"Netologe/f'{file_name}'", 'fields': 'json'}
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token_yd}'}
    resp = requests.put(url, data=open(file_name, 'rb'))
    resp.raise_for_status()
    if resp.status_code == 201:
        print('success')





