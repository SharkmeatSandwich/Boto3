import boto3

ec2 = boto3.resource('ec2')
# Get a list of all AMIs owned by this account_id
client = boto3.client('ec2', region_name='ap-southeast-2')

ami_filter = [{"Name": "is-public", 'Values': ['false']}]

image_count = []
untagged_images = []
tagged_images = []

tagged_image_counter = 0
image_counter = 0

results = client.describe_images(Filters=ami_filter)

if 'Images' in results:
    for img in results['Images']:
        image_counter = image_counter + 1
        image_count.append(img)
        #print(img['Name'])
        image_keys = []
        image_keys.append(img['ImageId'])
        #print(image_keys)


#print(image_count)

for img in image_count:                                     #To get tag information from AWS AMI, there is no readily accessible .tag attribute,      
    for x in img :                                          #therefore it is neccessary to pull the tag values from the JSON response which comes 
        if x == 'Tags':                                     #effectively as a dictionary inside a list inside yet another list and that is what this 
            tagged_image_counter = tagged_image_counter +1  #code block is doing with multiple lists for each iteration.
            for y in img['Tags'] :
                image_tags_found = []                       #Make list
                image_tags_found.append(y)
                #print(image_tags_found)
                for z in image_tags_found :                 #Search list
                    image_tags = []
                    image_tags.append(z)                    #Make list
                    #print(z)
                    for w in image_tags :                   #Search Dictionary
                        if w['Key'] == 'Owner':             #Note that the final search is of a dictionary, hence the different syntax to the above list searches.
                            print("Owner Tag Found")
        

untagged_image_counter = image_counter - tagged_image_counter

print("There are :" , str(len(image_count)) , "Images in total" )
print("There are :" , tagged_image_counter , "Tagged Images")
print("There are :" , untagged_image_counter , "Untagged Images")


