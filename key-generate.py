import boto3

ec2 = boto3.resource('ec2')

key_pair = ec2.create_key_pair(KeyName='python3_aws')

output = open('python3_aws.pem','w')
key_data = str(key_pair.key_material)
output.write(key_data)
