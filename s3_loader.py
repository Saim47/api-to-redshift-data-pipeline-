import boto3
import datetime
from io import StringIO

# AWS credentials (you may use environment variables or other secure methods in production)
AWS_ACCESS_KEY = "*************"
AWS_SECRET_KEY = "***********"
BUCKET_NAME = "************"

# Function to store data into AWS S3
def store_to_s3(df, bucket_name=BUCKET_NAME):
    try:
        # Initialize S3 client with credentials
        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY
        )
        
        # Generate timestamp for filenames
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Store raw data
        raw_key = f"raw/weather_raw_{timestamp}.csv"
        s3.put_object(
            Bucket=bucket_name,
            Key=raw_key,
            Body=df.to_csv(index=False)
        )
        print(f"Raw data saved to s3://{bucket_name}/{raw_key}")
        
        # Store cleaned data
        cleaned_df = clean_weather_data(df)
        processed_key = f"processed/weather_processed_{timestamp}.csv"
        s3.put_object(
            Bucket=bucket_name,
            Key=processed_key,
            Body=cleaned_df.to_csv(index=False)
        )
        print(f"Processed data saved to s3://{bucket_name}/{processed_key}")
        
        return {
            'raw_location': f"s3://{bucket_name}/{raw_key}",
            'processed_location': f"s3://{bucket_name}/{processed_key}",
            'cleaned_data': cleaned_df
        }
        
    except Exception as e:
        print(f"Error storing to S3: {str(e)}")
        return None

# Store the cleaned data to S3
if not weather_df.empty:
    result = store_to_s3(cleaned_weather_df)
    if result:
        print("\nS3 Storage Results:")
        print(f"Raw data location: {result['raw_location']}")
        print(f"Processed data location: {result['processed_location']}")
else:
    print("No data to store")
