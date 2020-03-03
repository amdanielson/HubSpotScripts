import os
import requests
import logging
import http.client
hapikey = os.getenv("HAPIKEY") 
key= os.getenv("key")

print("Please enter a contact email address from the HubSpot portal")
email = input()

#gets the two addresses from the contact properties address 1 and address 2

r = requests.get('https://api.hubapi.com/contacts/v1/contact/email/{}/profile?hapikey={}'.format(email, hapikey))
contact=r.json()

    
address1 = contact.get('properties').get('full_address_1').get('value')
address2 = contact.get('properties').get('full_address_2').get('value')
print("Address 1 is: " + address1)
print("Address 2 is: " + address2)


# calls google distance matrix endpoint to get the distance between the two addresses

s = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?origins={}&destinations={}&units=imperial&key={}'.format(address1, address2, key))

distance = s.json()
distance= distance.get('rows')[0].get('elements')[0].get('distance').get('text');
print("The distance between these addresses is: " + distance)

    
# posts the output to a string field in HubSpot on the contact
data = {"properties": [{"property": "distance","value": distance }]}
r = requests.post('https://api.hubapi.com/contacts/v1/contact/email/{}/profile?hapikey={}'.format(email, hapikey), json = data)


#error logging
pastebin_url = r.text 
print(r) 
