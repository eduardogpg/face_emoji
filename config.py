import os

class Config(object):
	SECRET_KEY = 'my_secret_key'
	PAGE_ACCESS_TOKEN = 'EAAaNhMt4ZAvABAL9oTdpjb0W93URZBRDYKmnvosyD8MqBL3EZBwmAkszSuwyZBE7RLZAs9EGmwFUOsj1rPuHuvsmkGEeMotssabggMP0mcOlhUY7quNok9JATvwKHQqfCp4xSZCC0fvgGvbs9rDOynBJq8c1UZCejhYiRD27Ks0bMzSHsTN6jp6'
	
class DevelopmentConfig(Config):
	DEBUG = True	
