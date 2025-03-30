# AWS Project: Customer ID Management System

## Overview

This project is a fully integrated AWS-based system that provides a REST API, a Step Functions workflow, and a React-based frontend to manage customer IDs using DynamoDB. The infrastructure is built using AWS Lambda, API Gateway, S3, CloudFront, and IAM for security.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Architecture](#architecture)
3. [Setup & Deployment Steps](#setup--deployment-steps)
4. [Testing the API](#testing-the-api)
5. [Frontend Deployment](#frontend-deployment)
6. [Step Functions Workflow](#step-functions-workflow)
7. [Security & IAM](#security--iam)
8. [Final Testing](#final-testing)

## Prerequisites

- **AWS Account** (Created a new AWS account)
- **AWS CLI** installed and configured on the local machine
- **Python & Boto3** installed for backend development
- **React.js** for frontend development

## Architecture

### Components Used:

- **DynamoDB**: Stores customer IDs
- **AWS Lambda**: Handles backend logic
- **API Gateway**: Exposes REST API endpoints
- **React (Frontend)**: Provides a UI for adding/checking customer IDs
- **S3 & CloudFront**: Hosts the frontend securely
- **AWS Step Functions**: Automates customer ID management workflow

---

## Setup & Deployment Steps

### 1. AWS Account Setup

- Created an AWS account
- Configured IAM user and assigned necessary permissions

### 2. DynamoDB Setup

- Created a DynamoDB table named `customer_ids`
- Defined **id (String)** as the partition key

### 3. Backend Development

#### Created Two Lambda Functions:

1. **put_customer_id**: Adds a new customer ID to the DynamoDB table
2. **get_customer_id**: Checks if a customer ID exists and returns a JSON response

### 4. API Gateway Configuration

- Created an API Gateway with **REST API endpoints**
- Integrated with the Lambda functions
- Enabled **CORS** for cross-origin access

### 5. React Frontend Development

- Developed a simple React app with **three components**:
  - **AddCustomerID**: Adds an ID to DynamoDB
  - **CheckCustomerID**: Checks if an ID exists
  - **ResponseDisplay**: Shows the results

### 6. Frontend Deployment on AWS S3

- Uploaded the built React app to an S3 bucket
- Configured S3 bucket policy to restrict public access
- Enabled website hosting on S3

### 7. CloudFront Configuration (HTTPS)

- Created a **CloudFront distribution** pointing to the S3 bucket
- Configured an SSL certificate using **AWS Certificate Manager**
- Linked the domain `cloudzoneprojects.info` to CloudFront

### 8. Step Functions Workflow

- Created a **State Machine** with three Lambda functions:
  - **check_customer_id**: Checks if ID exists
  - **log_existing_id**: Logs the existing ID
  - **add_new_id**: Adds a new ID if it doesn’t exist
- Triggered the Step Function using **EventBridge** on API calls

### 9. Security & IAM Setup

- Restricted S3 bucket access to CloudFront only
- Created an IAM **Read-Only User** for AWS resource access
- Ensured minimal permissions for Lambda and API Gateway

### 10. Final Deployment & Testing

- Deployed API Gateway and tested using **Postman & cURL**
- Verified React app interaction with API endpoints
- Monitored **CloudWatch logs** for debugging and performance

---

## Testing the API

To test API endpoints:

### **Add a Customer ID**

```bash
curl -X PUT https://customer-id-app-123.execute-api.region.amazonaws.com/prod/customer -d '{"id": "12345"}' -H "Content-Type: application/json"
```

### **Check if a Customer ID Exists**

```bash
curl -X GET https://customer-id-app-123.execute-api.region.amazonaws.com/prod/customer?id=12345
```

Expected response:

```json
{ "exists": true }
```

---

## Postman Testing

### **PUT Request**

```http
PUT http://customer-id-app-123.s3-website.eu-north-1.amazonaws.com/

{
  "body": "{\"id\": \"2626\"}"
}
```

#### **Response:**

```json
{
  "statusCode": 200,
  "headers": {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Authorization"
  },
  "body": "{\"message\": \"Client updated successfully.\", \"id\": \"2626\"}"
}
```

### **GET Request**

```http
GET https://7firq774sg.execute-api.eu-north-1.amazonaws.com/Prod/customer/1234
```

#### **Response:**

```json
{
  "message": "ID exists",
  "id": "1234"
}
```

---

## Frontend Deployment

- 🚨 **Important Notice:** HTTPS is currently not working for `https://cloudzoneprojects.info`.
- You can access the frontend using HTTP here:
  - 🔗 [http://customer-id-app-123.s3-website.eu-north-1.amazonaws.com/](http://customer-id-app-123.s3-website.eu-north-1.amazonaws.com/)

---

## Step Functions Workflow

- Triggered automatically when a new customer ID is submitted
- Can be monitored in AWS Step Functions console

---

## Security & IAM

- **IAM Role for Lambda**: Minimal permissions for DynamoDB access
- **S3 Bucket Policy**: Restricted to CloudFront only
- **API Gateway Authorization**: Public access for testing (can be restricted later)

---

## AWS Console Sign-In Details

- **Console Sign-In URL**: [AWS Console Sign-In](https://541153896631.signin.aws.amazon.com/console)
- **User Name**: `UserReadOnly`
- **Console Password**: `CloudZoneProject$`

---

## Conclusion

This project successfully implements a **secure, scalable, and fully integrated AWS solution** for managing customer IDs. The infrastructure follows best practices for **cost efficiency, security, and performance**.

🚀 **Note:** I purchased the domain `cloudzoneprojects.info`, but the DNS records are not yet validated. Additionally, the CloudFront trigger and Cloud Zone setup are pending. I truly enjoyed working on this project, but I need a few more hours to finalize everything completely.
