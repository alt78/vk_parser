import csv

import requests



def take_posts(count):

    #token = ''
    version = 5.92
    domain = 'itsmoes'
    count=count
    response = requests.get('https://api.vk.com/method/wall.get',
                            params={'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': count

                                    })

    data = response.json()['response']['items']
    return data

def file_writter(data):
    with open('ff.csv','w') as file:
        a_pen=csv.writer(file)
        a_pen.writerow(['likes','body','url'])
        for post in data:
            try:
                if post['attachments'][0]['type']:
                    img_url=post['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_url='pass'
            except:
                img_url='pass'
            a_pen.writerow((post['likes']['count'],post['text'],img_url))


all_post=take_posts(10)
file_writter(all_post)
print(1)