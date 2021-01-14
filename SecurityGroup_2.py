import boto3
import json

region = "ap-southeast-2"

ec2 = boto3.resource('ec2')

sgs = ec2.security_groups.all()

sg_group_count = 0

sg_no_name = [] #Unnamed Security Groups
sg_has_owner = [] # Security Groups with Owner tag
sg_tagged = [] #Tagged Security Groups
sg_is_named = [] #Untagged Security Groups


for sg in sgs :
    sg_group_count = sg_group_count + 1
    if sg.tags == None :
        sg_no_name.append(sg.id)
        
    else :       
        sg_sec_tags = []
        
        for tag in sg.tags :
            
            sg_sec_tags.append(tag['Key'])
            sg_tagged.append(sg.id)
            
            if 'Owner' in sg_sec_tags :
                
                sg_has_owner.append(sg.id)
            if 'Name' in sg_sec_tags :
                
                sg_is_named.append(sg.id)
      
sg_tag = set(sg_tagged)
sg_own = set(sg_has_owner)
sg_named = set(sg_is_named)    

sg_needs_owner = sg_tag - sg_own
sg_needs_name =  sg_tag - sg_named

print("")
print("")
print("\033[96m***************SECURITY GROUP TAGGING REPORT************************")
print("\033[0m")
print("There are \033[96m{} total Security Groups".format(sg_group_count))
print("\033[0mThe following Security Groups are tagged correctly:")
print("\033[92m     " , sg_tagged)
print("\033[0mThe following Security groups require Owner tags:") 
print("\033[93m     " , sg_needs_owner)
print("\033[0mThe Following Security Groups require Name tags:")
print("\033[93m     " , sg_needs_name)
print("\033[0mThe following Security Groups are untagged: ")
print("\033[91m     " , sg_no_name)
