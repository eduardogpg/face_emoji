def upload_file(path):
	from imgurpython import ImgurClient
	
	client_id = '494404a834dcabb'
	client_secret = 'be3622ab397d1122acb0bdbd589e2c26f40be7dia_aniversario'

	client = ImgurClient(client_id, client_secret)
	response = client.upload_from_path(path)
	return response['link']

def get_all_emojis():
	import os
	return [  "emojis/"+f for f in os.listdir("emojis") if f.endswith(".png") ]
	
def add_emoji_face(image, emojis, faceRectangle, facePosition):
	import random
	from PIL import Image

	path = "new_" + image
	background = Image.open(image)
	foreground = Image.open(random.choice(emojis))
	foreground = foreground.resize( faceRectangle )

	background.paste(foreground, facePosition, foreground)
	background.save(path)
	return path

def get_face(url):
	import json
	import requests


	uri = {'url' : "https://scontent.xx.fbcdn.net/v/t35.0-12/15502853_196089334187097_1763083346_o.png?_nc_ad=z-m&oh=a78e7416bf2cfa7aa166e815780f3874&oe=5852B613"}
	res = requests.post('https://api.projectoxford.ai/face/v1.0/detect',
									params={'returnFaceId' : 'false', 'returnFaceLandmarks': 'true'},
	                data = json.dumps( uri ),
	                headers={'Content-type': 'application/json', 'Host': 'api.projectoxford.ai', 'Ocp-Apim-Subscription-Key': 'a6d271ac0aa14281835d70a538538aba'})

	if res.status_code == 200:
		response = json.loads(res.text)
		image = response[0]
		face = image['faceRectangle']

		return (face['width'], face['height']), (face['left'], face['top'])
		
def create_image(url):
  import urllib
  path = '00000001.jpg'
  f = open(path,'wb')
  f.write(urllib.urlopen(url).read())
  f.close()
  return path

def generate_new_image_emoji(url):
	path = create_image(url)
	faceRectangle, facePosition = get_face(url) #Validar que sea un rostro
	path = add_emoji_face(path, get_all_emojis(), faceRectangle, facePosition)
	return upload_file(path)


if __name__ == '__main__':
	url = "https://scontent.xx.fbcdn.net/v/t35.0-12/15540411_196129220849775_727993538_o.jpg?_nc_ad=z-m&oh=c831d6771942c6ccc9a1f70d0084098f&oe=5852A4F7"
	#url = generate_new_image_emoji(url)
	#print url
	get_face(url)

