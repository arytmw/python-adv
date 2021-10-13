import boto3

ec2 = boto3.client('ec2')

instance_id = input("Enter instance ID to stop: ")

ec2.stop_instances(InstanceIds=[instance_id])
waiter = ec2.get_waiter('instance_stopped')
waiter.wait(InstanceIds=[instance_id])
