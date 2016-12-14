#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from handler import received_message

import json

__author__ = 'Eduardo Ismael García Pérez'
__lastupdated__ = '2016 Diciembre 13'

app = Flask(__name__)

TOKEN = 'EAAJBTt2ITOYBANj2Sc0WX2bi9j8k7HL6LTjsXCz03IYGvWCYw8OHPpSnpV9OwsvYCVxR1NyyaZCzzZCFeh6uc784bS3nwVRqRZAzhZBskpCn9vWHnE7dpBfiFF8Q8N7pmT2es1F5UziR2YCBgZBOKXvOHsZAnaZBkEcjaeaWhlaAZCVMkBa0GlRY'
SECRET_KEY = 'my_secret_key'

  
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
	if request.method == 'GET':
		verify_token = request.args.get('hub.verify_token', '')
		if verify_token == SECRET_KEY:
			return request.args.get('hub.challenge', '')
		return 'Token invalido!'
	
	elif request.method == 'POST':

		print "Entro aqui!"
		
		payload = request.get_data()
		data = json.loads(payload)
		
		for page_entry in data['entry']:
			for message_event in page_entry['messaging']:
				if "message" in message_event:
					received_message(message_event, TOKEN )
				
		return "ok"

if __name__ == '__main__':

	app.run(port = 8000, debug = True)
