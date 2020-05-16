import os
import boto3
import glob
from botocore.client import Config


ACCESS_KEY_ID = '***********'
ACCESS_SECRET_KEY = '*****************'
BUCKET_NAME = '*********************'

#data = open('CloudHomework.jpg', 'rb')

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)



s3=boto3.client('s3')
list=s3.list_objects(Bucket=BUCKET_NAME)['Contents']
for key in list:    
      s3.download_file(BUCKET_NAME, key['Key'], key['Key'])
      print("Downloaded file", key)
      s3.delete_object(Bucket=BUCKET_NAME,Key=key['Key'])
      continue
    

print ("Done") 
