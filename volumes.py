import boto3

ec2 = boto3.resource('ec2', region_name='ap-southeast-2')

volumes = ec2.volumes.all() # If you want to list out all volumes

#volumes = ec2.volumes.filter(Filters=[{'Name': 'status', 'Values': ['in-use']}]) # if you want to list out only attached volumes
volume_counter = 0
volume_in_use_counter = 0
volume_created_from_snapshots = 0
volume_untagged = 0

untagged_volumes = []

for volume in volumes :
    volume_counter = volume_counter + 1
    #print(volume)
    #print(volume.snapshot_id)
    #print(volume.state)    
    #print(volume.tags)
    
    if len(volume.snapshot_id) > 1 : #To determine if Volume has been created from snapshot
        volume_created_from_snapshots = volume_created_from_snapshots + 1

    if volume.state == 'in-use' :
        volume_in_use_counter = volume_in_use_counter + 1
    
    if volume.tags == None :
        volume_untagged = volume_untagged + 1
        untagged_volumes.append(volume.id)

print("There are :\033[96m" , volume_counter , "\033[0mVolumes in total")
print("There are :\033[92m" , volume_in_use_counter, "\033[0mVolumes in use")
print("There are :\033[96m" , volume_created_from_snapshots , "\033[0mVolumes created from Snapshots")
print("There are :\033[93m" , volume_untagged , "\033[0mUntagged Volumes\033[93m" , untagged_volumes)
