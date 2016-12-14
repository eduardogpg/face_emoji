#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

def upload_file(path):
	from imgurpython import ImgurClient
	client_id = '494404a834dcabb'
	client_secret = 'be3622ab397d1122acb0bdbd589e2c26f40be726'

	client = ImgurClient(client_id, client_secret)
	response = client.upload_from_path(path)
	return response['link']

def get_all_emojis(path):
	import os
	path = "{}/emojis/".format(path)
	return [ path + f for f in os.listdir(path) if f.endswith(".png") ]

	'emojis/images//news/2016-12-14 11:46:56.001682.jpg/emojis/'


def create_image(url, path):
	"""Generamos una nueva imagen apartir de una url, esta imagen almacenará dentro de nuestro servidor."""
	import urllib
	import datetime

	path = '{}/news/{}.jpg'.format(path, str(datetime.datetime.now()))
	image = open(path,'wb')
	image.write( urllib.urlopen(url).read())
	image.close()

	return path

def add_emoji_face(path, emojis, faces):
	import random
	from PIL import Image

	background = Image.open(path)
	foreground = Image.open(random.choice(emojis))

	for face in faces:
		foreground_copy = foreground.resize( (face['width'], face['height']) )
		background.paste(foreground_copy, (face['left'], face['top']), foreground_copy)

	background.save(path)
	return path
	
def get_face(url):
	import json
	import requests

	res = requests.post('https://api.projectoxford.ai/face/v1.0/detect',
									params={'returnFaceId' : 'false', 'returnFaceLandmarks': 'false'},
	                data = json.dumps( { 'url' : url } ),
	                headers={'Content-type': 'application/json', 'Host': 'api.projectoxford.ai', 'Ocp-Apim-Subscription-Key': 'a6d271ac0aa14281835d70a538538aba'})

	faces = []
	if res.status_code == 200:
		face_list = json.loads(res.text)
		for face in face_list:
			faces.append(face['faceRectangle'])
	return faces			


def generate_new_image_emoji(url, global_path = 'images'):
	path = create_image(url, global_path)
	path = add_emoji_face(path, get_all_emojis(global_path), get_face(url))
	return upload_file(path)
	
if __name__ == '__main__':
	print datetime.datetime.now()
	url = "https://scontent.xx.fbcdn.net/v/t34.0-12/15555788_196571710805526_1055831956_n.jpg?_nc_ad=z-m&oh=17a2b65209972eb5ec6ba8c516ebb7b1&oe=585363AD"
	#url = "https://scontent.xx.fbcdn.net/v/t35.0-12/15502853_196089334187097_1763083346_o.png?_nc_ad=z-m&oh=a78e7416bf2cfa7aa166e815780f3874&oe=5852B613"
	url = generate_new_image_emoji(url)
	print url
	print datetime.datetime.now()




	

