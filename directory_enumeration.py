import requests 
import sys 

sub_list = open("location_name_of_wordlist").read() 
directories = sub_list.splitlines()

for dir in directories:
    dir_enum = f"http://{sys.argv[1]}/{dir}.html" 
    r = requests.get(dir_enum)
    if r.status_code==404: 
        pass
    else:
        print("Valid directory:" ,dir_enum)

# be sure to then go into terminal, enter python + the enumeration file + IP address you want to gather info about
# e.g. python3 directory_enumeration.py 192.168.1.6