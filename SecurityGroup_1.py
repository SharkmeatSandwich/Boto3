import boto3

#Make some pretty colours for our output
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

ec2 = boto3.resource('ec2') #You have to change this line based on how you pass AWS credentials and AWS config

#Make the neccessary lists
sgs = list(ec2.security_groups.all())
insts = list(ec2.instances.all())

#Create sets to compare
all_sgs = set([sg.group_name for sg in sgs])
all_inst_sgs = set([sg['GroupName'] for inst in insts for sg in inst.security_groups]) #This makes a set from the instance details to compare with the set above (all_sgs)

#Compare the sets
unused_sgs = all_sgs - all_inst_sgs
total_sgs = len(all_sgs) + 1
unused_sgs_total = len(unused_sgs) + 1

#Display the relevant information
print("")
print("")
print("\033[96m-------------------------------------------------------------------")
print("\033[0mSecurity Group information")
print ("\033[0mTotal SGs:{}\033[96m", total_sgs)
print ("\033[0mSGS attached to instances:\033[92m" , len(all_inst_sgs))
print ("\033[0mOrphaned SGs:\033[93m", len(unused_sgs))
print ("\033[0mOrphaned SG names:\033[91m", unused_sgs)
print("\033[96m-------------------------------------------------------------------")
