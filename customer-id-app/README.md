# AWS Project: Customer ID Management System

## Overview

This project is a fully integrated AWS-based system that provides a REST API, a Step Functions workflow, and a React-based frontend to manage customer IDs using DynamoDB. The infrastructure is built using AWS Lambda, API Gateway, S3, CloudFront, EventBridge, and IAM for security.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Architecture](#architecture)
3. [Setup & Deployment Steps](#setup--deployment-steps)
4. [Testing the API](#testing-the-api)
5. [Frontend Deployment](#frontend-deployment)
6. [EventBridge & Step Functions Workflow](#eventbridge--step-functions-workflow)
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
- **Amazon EventBridge**: Facilitates event-driven communication between services

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

### 8. EventBridge & Step Functions Workflow

#### **EventBridge Setup**

- **Created an Event Bus** named `CustomerIDEventsBus`
- **Defined an Event Rule** to listen for `new-customer-id` events
- **Configured the rule to trigger Step Functions** when an event is received

#### **Step Functions Workflow**

- Created a **State Machine** with three Lambda functions:
  - **check_customer_id**: Checks if ID exists
  - **log_existing_id**: Logs the existing ID
  - **add_new_id**: Adds a new ID if it doesn’t exist
- Triggered the Step Function using **EventBridge** on API calls

#### **Testing EventBridge Workflow**

To manually trigger an event:

```bash
aws events put-events --entries '[
  {
    "Source": "myapp",
    "DetailType": "new-customer-id",
    "Detail": "{\"id\": \"123456\"}",
    "EventBusName": "CustomerIDEventsBus"
  }
]'
```

Expected response:

```json
{
  "FailedEntryCount": 0,
  "Entries": [
    {
      "EventId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
  ]
}
```

Then, verify the execution in **AWS Step Functions**.

---

## Security & IAM Setup

- Restricted S3 bucket access to CloudFront only
- Created an IAM **Read-Only User** for AWS resource access
- Ensured minimal permissions for Lambda and API Gateway
- **Updated IAM permissions** for EventBridge to allow Step Functions execution

---

## Final Deployment & Testing

- Deployed API Gateway and tested using **Postman & cURL**
- Verified React app interaction with API endpoints
- Monitored **CloudWatch logs** for debugging and performance
- Confirmed EventBridge triggers and Step Functions execution

---

## Testing the API

### **Add a Customer ID**

```bash
curl -X PUT "https://api.example.com/Prod/customer" \
     -H "Content-Type: application/json" \
     -d '{"body": "{\"id\": \"2626\"}"}'
```

### **Check if a Customer ID Exists**

```bash
curl -X GET "https://api.example.com/Prod/customer?id=12345"
```

Expected response:

```json
{ "exists": true }
```

---

## Frontend Deployment

- 🚨 **Important Notice:** HTTPS is currently not working for `https://cloudzoneprojects.info`.
- You can access the frontend using HTTP here:
  - 🔗 [http://customer-id-app-123.s3-website.eu-north-1.amazonaws.com/](http://customer-id-app-123.s3-website.eu-north-1.amazonaws.com/)

---

## AWS Console Sign-In Details

- **Console Sign-In URL**: [AWS Console Sign-In](https://signin.aws.amazon.com)
- **User Name**: `UserReadOnly`
- **Console Password**: `CloudZoneProject$`

---

## Conclusion

This project successfully implements a **secure, scalable, and fully integrated AWS solution** for managing customer IDs. The infrastructure follows best practices for **cost efficiency, security, and performance**.

🚀 **Note:** The CloudFront trigger and Cloud Zone setup are pending. I truly enjoyed working on this project, but I need a few more hours to finalize everything completely.
