# importing the module
import requests

#getting url from user
url= input("ENTER YOUR URL: ")

# create HTTP response object
r=requests.get(url)

#splits up the url into its parts,
filename=url.split('/')[-1]# this will take only -1 splitted part of the url

#it takes only -1 splitted part of the url and writes it out to an output file with open('filename','wb') as output_file.
with open(filename,'wb')as output_file:
    
# send a HTTP request to the server and save
# the HTTP response in a response object called r 
#download the content of the given url and save it in a file.
    output_file.write(r.content)

 #prints msg after downloading file successfully
print('Download Completed!!!')


