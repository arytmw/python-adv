import boto3

ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
        ImageId='ami-06a0b4e3b7eb7a300',
        InstanceType='t2.micro',
        KeyName='python3_aws',
        MinCount=1,
        MaxCount=2
        )
