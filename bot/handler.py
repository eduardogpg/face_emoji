#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json

from emojis import generate_new_image_emoji

def received_message(event, token):
    sender_id = event['sender']['id']
    message = event['message']

    handler_message(message, sender_id, token)


def handler_message(message, user_id ,token):
	attachments = message.get('attachments', [] )
	send_typing_message(user_id, token) #Typing
	
	if attachments:
		attachment = attachments[0]
		if attachment['type'] == 'image':

			data = text_message(user_id, "Espere, por lo regular esto tarda un por de segundos!")
			call_send_API(data, token)

			send_typing_message(user_id, token) #Typing

			payload = attachment['payload']
			print payload['url']
			url = generate_new_image_emoji(payload['url'], global_path = 'emojis/images/')
			
			send_typing_message(user_id, token) #Typing

			data = image_message(user_id, url)
			call_send_API(data, token)

	else:
		data = text_message(user_id, "Lo siento intenta enviandome una imagen")
		call_send_API(data, token)


def send_typing_message(user_id, token):
	typing = typing_message(user_id)
	call_send_API(typing, token)


def call_send_API(data, token):
  res = requests.post('https://graph.facebook.com/v2.6/me/messages',
					params={ 'access_token': token},
					data= json.dumps( data ),
					headers={'Content-type': 'application/json'})

  if res.status_code == 200:
      print "Mensaje enviado exitosamente!"

def text_message(recipient_id, message_text):
	message_data = {
		'recipient': {'id': recipient_id},
		'message': { 'text': message_text}
	}
	return message_data

def image_message(recipient_id, url):
  message_data = {
      "recipient":{ "id":recipient_id},
      "message":{
      "attachment":{
          "type":"image",
              "payload":{
                  "url":url
              }
          }
      }
  }   
  return message_data


def typing_message(recipient_id):
  message_data = {
		'recipient': {'id': recipient_id},
		'sender_action' : 'typing_on'
  }
  return message_data

