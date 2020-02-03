import os
import requests #package to help make HTTP request

#This is me getting my Hapikey from a .env file I have. I did this to protect my hapikey so I can make demos without exposing it
hapikey = os.getenv("HAPIKEY")

r = requests.get('https://api.hubapi.com/properties/v1/contacts/properties?hapikey={}'.format(hapikey))
i = 0

#Assign the response body to a variable for later usage.
properties=r.json()

#Iterates through each property object within the JSON to get the value of the key "name" if the property is NOT HubSpot defined
for prop in properties:
  try: 
    if prop.get('hubspotDefined') != True:
      propName = prop.get('name');
      print(propName); #prints the property names out to the console
      i = i + 1
  except TypeError:
    pass 

print("------------")  
print(("Total number of custom properties: {}").format(i))


  

   