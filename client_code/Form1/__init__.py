from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    anvil.users.logout()
    # Any code you write here will run before the form opens.
    anvil.users.login_with_form()

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    user = anvil.users.get_user()
    print(user['email'])


    
