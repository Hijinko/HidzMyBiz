#import os
#os.environ['KIVY_NO_CONSOLELOG'] = '1'
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from hmbmodules import *


class MenuLayout(BoxLayout):
	pass

class AddFormLayout(BoxLayout):
	encode_file = ObjectProperty()
	decode_file = ObjectProperty()
	file_name = ObjectProperty()
	
	def Encode_Message(self):
		try:
			fname = self.file_name.text
			msg = self.file_message.text
			encodeInText(msg ,fname)
			with open(self.file_name.text) as f:
				data = f.read()
			self.file_message.text = data
		except FileNotFoundError:
			self.file_message.text= 'Please enter a file name to encode message to.'
		
	def Decode_Message(self):
		try:
			self.file_message.text = decode(self.file_name.text)
		except FileNotFoundError:
			if self.file_name.text == '':
				self.file_message.text = 'Please enter a file name to decode.'
			else:
				self.file_message.text = 'file named ({}) does not exist'.format(self.file_name.text)
			
class HmbApp(App):
	pass
	
if __name__=='__main__': HmbApp().run()
