from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

    #Any code you write here will run before the form opens

  def generate_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    #Call google colab function
    moodboard = anvil.server.call('generate_moodboard', self.enter_prompt.text)
    #If a category is returned set our species 
    self.Event_Moodboard.source = moodboard
      
    pass

