import boto3

# Créer un client S3
s3_client = boto3.client('s3')

# Lister les buckets
response = s3_client.list_buckets()
print("List of S3 Buckets:")
for bucket in response['Buckets']:
    print(bucket['Name'])
