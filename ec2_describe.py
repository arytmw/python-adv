import boto3

ec2 = boto3.resource('ec2')

for instance in ec2.instances.all():
    print("Instance ID: {}\nPublic IPv4: {}\nAMI: {}\nCurrent State: {}\n".format(instance.id,instance.public_ip_address,instance.image_id,instance.state['Name']))
