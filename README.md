# ✅ Serverless To-Do List App on AWS

This project is a fully serverless To-Do List application built using AWS Lambda, DynamoDB, IAM, and Streamlit. Users can **add**, **view**, **update**, and **delete** tasks in real-time.

---

## 📐 Mini Design Document

### Architecture Overview

- **Frontend**: Streamlit App (Python-based UI)
- **Backend**: AWS Lambda Functions
- **Database**: Amazon DynamoDB
- **Security**: IAM roles & policies to manage secure access
- **Communication**: Streamlit app calls AWS Lambda functions via `boto3`

### Core Features

- Create, view, update, and delete tasks
- Tasks stored in DynamoDB with fields:
  - `task_id` (string - UUID)
  - `title` (string)
  - `description` (string)
  - `status` (string: `pending`, `completed`)
  - `created_at` (ISO timestamp)

### Bonus Features (optional ideas)

- Task due date with sorting
- Priority tagging (`low`, `medium`, `high`)
- Auto-delete expired tasks (via DynamoDB TTL)
- Email notification (via SNS or SES)

---

## 🔧 How to Use

### 🖥️ Prerequisites

- Python 3.8+
- Streamlit
- AWS CLI configured
- Boto3 installed

```bash
pip install streamlit boto3
