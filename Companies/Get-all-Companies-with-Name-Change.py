import os
import requests #package to help make HTTP request
import csv
import time #allows time methods below

hapikey = os.getenv("HAPIKEY")
offset ='' 

# Set intial boolean variable to kick off the 'while' loop
has_more = True 
pages = 0

#Loop through the companies until there are no more in the portal
while has_more == True:
  r = requests.get('https://api.hubapi.com/companies/v2/companies/paged?hapikey={}&limit=100&offset={}&propertiesWithHistory=name'.format(hapikey,offset))

  #Assign the response body to a variable for later usage.
  companies=r.json()

  #Loop each object/dictionary in the 'companies' array.

  for company in companies['companies']:
    #get the name, source, and old name for the specific comapny, assign to variables
    name = company.get('properties').get('name').get('value')
    source = company.get('properties').get('name').get('source')
    #print the old name to the repl console
    oldname= company.get('properties').get('name')['versions']

    #The timestamp of the change. We convert the epoch millis to datetime here. 
    timestamp= company.get('properties').get('name').get('timestamp')
    timestamp = time.strftime('%m-%d-%Y %H:%M:%S', time.localtime(timestamp/1000))

    compid = company.get('companyId')
  
    #Only prints the company information to console if there is more than one historical company name and the change source of the most recent name change is BIDEN
    if (len(oldname) >= 2 and source == 'BIDEN'):
      oldname = oldname[1]['value']
      #adds the three items to an array and prints
      row = [name, source, oldname, timestamp, compid]
      print(row)
      
    #line separator between each company
      print ('*****')
      
      #Writes each source, name, old name, and timestamp to a new row in a CSV file
      with open('test.csv', 'a') as newFile:
        newFileWriter = csv.writer(newFile)
        newFileWriter.writerow([name, source, oldname, timestamp, compid])
     
    
  #Pick off the 'has-more' key from the JSON to see if we need to get the next page of companies  
  if companies.get('has-more')==True:
    offset = companies.get('offset')
    pages +=1
    
    continue

  else:
    #If has-more is not True, set has-more to False, which ends the 'while' loop
    has_more = False
    print ("All done, goodbye")
