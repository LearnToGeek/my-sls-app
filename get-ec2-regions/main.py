import boto3
import json

ec2Client = boto3.client('ec2')

def GetEC2Regions(event,context):
    regionsList = ec2Client.describe_regions()

    return {
        "statusCode":200,
        "body":json.dumps({"message":regionsList['Regions']})
    }