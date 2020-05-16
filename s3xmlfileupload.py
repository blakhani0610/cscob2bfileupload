import os
import boto3
import glob
from botocore.client import Config


ACCESS_KEY_ID = '*****************'
ACCESS_SECRET_KEY = '**********************************'
BUCKET_NAME = '*****************'

#data = open('CloudHomework.jpg', 'rb')

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)


for filename in glob.glob('*.xml'):
    if filename.endswith(".xml"):
        data = open(filename, 'rb') 
        s3.Bucket(BUCKET_NAME).put_object(Key=filename, Body=data)
        print("Uploaded" ,os.path.join(os.getcwd(), filename))
        #os.remove(filename)
        continue
    else:
        print("No more files to upload")

#s3.Bucket(BUCKET_NAME).put_object(Key='CloudHomework.jpg', Body=data)

print ("Done")
