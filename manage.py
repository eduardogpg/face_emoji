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

	background = Image.open(image)
	foreground = Image.open(random.choice(emojis))
	foreground = foreground.resize( faceRectangle )

	background.paste(foreground, facePosition, foreground)
	background.save('new.jpg')
	background.show()

def get_face(url):
	import json
	import requests

	SubscriptionKey = 'a6d271ac0aa14281835d70a538538aba'

	res = requests.post('https://api.projectoxford.ai/face/v1.0/detect',
				params={'returnFaceId' : 'false', 'returnFaceLandmarks': 'true'},
				data = json.dumps( {'url' : url} ),
				headers={'Content-type': 'application/json', 'Host': 'api.projectoxford.ai', 'Ocp-Apim-Subscription-Key': SubscriptionKey })

	if res.status_code == 200:
		image = json.loads(res.text)[0]
		face = image['faceRectangle']

		return (face['width'], face['height']), (face['left'], face['top'])

if __name__ == '__main__':
	url = "https://scontent.xx.fbcdn.net/v/t35.0-12/15502853_196089334187097_1763083346_o.png?_nc_ad=z-m&oh=a78e7416bf2cfa7aa166e815780f3874&oe=5852B613"
	#emojis = get_all_emojis()
	#faceRectangle, facePosition = get_face(url)
	#add_emoji_face('test.jpg', emojis, faceRectangle, facePosition)	


	image = 'new.jpg'
	upload_file(image)
	
