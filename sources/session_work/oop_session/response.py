import random
import json

with open (r"C:\Users\Maydoum\OneDrive\Desktop\DEPI\projects\Depi_Amit_AI_BNS3\sources\session_work\oop_session\chatbot.json", "r") as file:
  responses = json.load(file)

def get_response(user_input):
 

  for key in responses:
    if key in user_input:
      return random.choice(responses[key])
 
 
  return random.choice(responses["default"])