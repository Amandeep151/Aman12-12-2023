import os
import boto3
import schedule
import time

# AWS credentials (preferably use IAM roles or environment variables)
AWS_ACCESS_KEY = 'AKIAYZOGYVZSFWH5YC50'
AWS_SECRET_KEY = 'n6xZoF69gkSIifIbLPXu/T4bOqQmM5RuwEjYRkk2'
BUCKET_NAME = 'aman22'

# Local directory to be backed up
LOCAL_DIRECTORY = r'C:\Users\amand\OneDrive\awsbackup'

# Initialize S3 client
s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

def upload_to_s3(local_file, s3_key):
    try:
        s3.upload_file(local_file, BUCKET_NAME, s3_key)
    except Exception as e:
        print(f"Error uploading {local_file} to S3: {e}")

def backup():
    print("Backing up files to S3...")
    for root, dirs, files in os.walk(LOCAL_DIRECTORY):
        for file in files:
            local_file_path = os.path.join(root, file)
            s3_key = os.path.relpath(local_file_path, LOCAL_DIRECTORY)
            upload_to_s3(local_file_path, s3_key)
    print("Backup complete.")

# Schedule the backup to run every day at a specific time (adjust as needed)
schedule.every().day.at("03:00").do(backup)

while True:
    schedule.run_pending()
    time.sleep(1)



