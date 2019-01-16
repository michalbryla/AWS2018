from passes import *
import boto3
import os

EC2 = boto3.client('ec2',\
    region_name = REGION_ID,\
    aws_access_key_id=ACCESS_ID,\
    aws_secret_access_key= ACCESS_KEY)

response = EC2.describe_instances()

DNS = response.get('Reservations')[0].get('Instances')[0].get('PublicDnsName')

print("DNS is " + DNS)