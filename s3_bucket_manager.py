from secret import AWS_KEY, AWS_SECRET

import boto3
import os

bucket_name = 'on-chain-bitcoin-analysis'
key_file = 'hello_world.csv'


# This is really basic, probably the most unsafe way to access with credential
# Will secure later
s3 = boto3.resource('s3', aws_access_key_id = AWS_KEY, aws_secret_access_key = AWS_SECRET)

# for bucket in s3.buckets.all():
#     print(bucket.name)

#proper and safe way to download a file from a bucket
# too wordy for me, hope we don't really need to do that everytime
try:
    s3.Bucket(bucket_name).download_file(key_file, 'my_hello_world.csv')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise



#basic function to upload a file to a bucket
# s3.Bucket(bucket_name).upload_file('my_test.txt', 'test.txt')
