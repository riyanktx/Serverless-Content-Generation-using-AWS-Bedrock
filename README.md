# 📝 Serverless Content Generation using AWS Bedrock

This project is a **serverless content generation application** built using **AWS Bedrock** and core AWS services. It exposes a REST API that accepts a blog topic, generates a blog using a foundation model hosted on AWS Bedrock, and stores the generated content in Amazon S3.

---

## 🚀 Architecture Overview

The application follows a fully serverless architecture:

- **Amazon API Gateway** – Exposes a REST API endpoint
- **AWS Lambda** – Handles request processing and orchestration
- **AWS Bedrock** – Generates blog content using a foundation model
- **Amazon S3** – Stores generated blog files

---

## 🛠️ AWS Services Used

- Amazon API Gateway  
- AWS Lambda  
- AWS Bedrock  
- Amazon S3  
- AWS IAM (Roles & Policies)

---

## 📂 Application Workflow

1. Client sends a POST request with a blog topic
2. API Gateway triggers the Lambda function
3. Lambda invokes AWS Bedrock with the prompt
4. Bedrock generates a ~200-word blog
5. Lambda stores the blog in Amazon S3
6. API responds with a success message

---

