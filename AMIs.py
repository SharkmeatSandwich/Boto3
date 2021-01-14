import boto3

ec2 = boto3.resource('ec2')
# Get a list of all AMIs owned by this account_id
client = boto3.client('ec2', region_name='ap-southeast-2')

ami_filter = [{"Name": "is-public", 'Values': ['false']}]

image_count = []
untagged_images = []
tagged_images = []

amis_total = []
ec2_attached_amis = []

results = client.describe_images(Filters=ami_filter)

if 'Images' in results:
    for img in results['Images']:
        image_count.append(img)
        #print(img['Name'])        
        amis_total.append(img['ImageId'])
        
   
instance_counter = 0

instances = ec2.instances.all()
for instance in instances :
    instance_counter = instance_counter +1
    ec2_attached_amis.append(instance.image_id)

amis_total_set = set(amis_total) #Python Sets do not allow duplicates, so we are relieved of having to code their removal.
ec2_attached_amis_set = set(ec2_attached_amis)

amis_unattached = amis_total_set - ec2_attached_amis_set 

print("There are :\033[96m" + str(len(image_count)) , "\033[0mImages in this region")
print("There are :\033[96m" , instance_counter , "\033[0mRunning Instances")
print("There are:\033[93m" , len(amis_unattached) , "\033[0mImages NOT attached to Instances")
print("--------------------------------------------------------------------------------------")

prompt_1 = " "          #A very simplistic means of allowing only desired input
  
while prompt_1 != "no" or "yes" :
    prompt_1 = input("Would you like to see a list of the unattached images? (yes or no)")
    if prompt_1 == "no" or prompt_1 == "n":
        quit()
    if prompt_1 == "yes" or prompt_1 == "y":
        print("\033[93m" , amis_unattached)
        break

#print(ec2_attached_amis)
#print(amis_total)
