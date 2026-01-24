import boto3 
import botocore.config 
import json
from datetime import datetime

def blog_generate_using_bedrock(blogtopic: str) -> str:
    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "messages": [
            {"role": "user", "content": f"Write a 200 word blog on {blogtopic}"}
        ],
        "max_tokens": 500,
        "temperature": 0.5
    }

    try:
        bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

        response = bedrock.invoke_model(
            modelId="us.anthropic.claude-sonnet-4-5-20250929-v1:0",
            body=json.dumps(body),
            accept="application/json",
            contentType="application/json"
        )

        raw_body = response["body"].read()
        model_response = json.loads(raw_body)
        text = model_response["content"][0]["text"]
        print(text)
        return text


    except Exception as e:
        print(f"Error generating the blog: {e}")
        return ""

    
def save_blog_details(s3_key,s3_bucket,generate_blog):
    s3 = boto3.client("s3")

    try:
        s3.put_object(Bucket = s3_bucket, Key = s3_key, Body = generate_blog)
        print("Saved to S3")
    except Exception as e:
        print(f"Error when saving the code to S3:{e}")

    
def lambda_handler(event, context):

    event = json.loads(event["body"])
    blogtopic = event["blog_topic"]

    generate_blog = blog_generate_using_bedrock(blogtopic=blogtopic)

    if generate_blog:
        current_time = datetime.now().strftime("%H%M%S")
        s3_key = f"blog_output/{current_time}.txt"
        s3_bucket = "blog-storage-bucket-14"
        save_blog_details(s3_key,s3_bucket,generate_blog)
    else:
        print("No blog generated")

    return {
        'statusCode': 200,
        'body': json.dumps('Blog generation completed')
    }



