import requests
import os
import time

token = os.environ['do_key']

# get a list of all active regiions right now
headers = {"Authorization":"Bearer " + token}
regions = requests.get("https://api.digitalocean.com/v2/regions",headers=headers).json()
region_slugs = []

for r in regions['regions']:
  if r['available'] == True:
    region_slugs.append(r['slug'])


print("Whic slug, Slugs avilable:",region_slugs)
print('\n\n')

use_region = input("prompt")
print(use_region)



counter = 0
for y in range(0,1):

  servernames = []

  for x in range(0,10):
    counter = counter + 1
    print('google-isbn-'+str(counter))
    servernames.append('google-isbn-'+str(counter))


  data = {
    "names": servernames,
    "region": use_region,
    "size": "s-1vcpu-1gb",
    "image": 31936125,
    "ssh_keys": [813340],
    "backups": False,
    "ipv6": False,
    "user_data": None,
    "private_networking": None,
    "tags": [
      "isbn"
    ]
  }

  create = requests.post("https://api.digitalocean.com/v2/droplets",json=data,headers=headers).json()
  time.sleep(10)
  print(create)
# droplet_id = create['droplets'][0]['id']


# sleep_time = 10

# while True:
#   print("looking at the status of ", droplet_id)

#   status = requests.get("https://api.digitalocean.com/v2/droplets/" + str(droplet_id),headers=headers).json()

#   if 'droplet' in status:
#     if status['droplet']['status'] == 'active':
#       print("droplet active, working")
#       sleep_time = 20
#     elif status['droplet']['status'] == 'off':
#       print("droplet off, job done, deleting")
#       status = requests.delete("https://api.digitalocean.com/v2/droplets/" + str(droplet_id),headers=headers)
#       print(status.status_code)   

#       break
#     else:
#       print(status['droplet']['status'])


#   else:
#     print("Resource not found: ",droplet_id)
#   time.sleep(sleep_time)
