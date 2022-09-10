import boto3
##created sns topic on melimu aws ##
#ec2 = boto3.resource("ec2")
client = boto3.client("sns")
response = client.create_topic(
    Name="sns-demo")
print(response)


