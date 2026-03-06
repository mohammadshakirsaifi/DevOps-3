# flask-mongo-app
# Flask MongoDB Atlas Form Application

## Project Overview
This project is a simple **Flask web application** that demonstrates:

- Creating an **API endpoint** that reads data from a backend file and returns it as JSON.
- A **frontend form** that inserts user data into **MongoDB Atlas**.
- Redirecting to a **success page** after successful data submission.
- Displaying **error messages on the same page** if submission fails.

---

## Technologies Used

- Python
- Flask
- MongoDB Atlas
- PyMongo
- HTML
- GitHub

---

## Project Structure
```bash
flask-mongo-app
│
├── app.py
├── data.json
├── requirements.txt
│
├── templates
│ ├── index.html
│ └── success.html
│
└── static
```

---

## Features

### 1. API Endpoint

- Route: `/api`
- Reads data from a backend JSON file (`data.json`)
- Returns data as a JSON response

Example Response:

```json
[
  {
    "id": 1,
    "name": "John",
    "role": "Developer"
  },
  {
    "id": 2,
    "name": "Sara",
    "role": "Designer"
  }
]
```
### 2. Frontend Form

The application contains a form where users can submit:
- Name
- Email
When the form is submitted:
- Data is inserted into MongoDB Atlas
- On success → user redirected to success page
- On error → error displayed on the same page

###### Installation
###### Clone Repository
```bash
git clone https://github.com/yourusername/flask-mongo-app.git
cd flask-mongo-app
```
###### Create Virtual Environment
```bash
python -m venv venv
```
Activate environment
**Windows**
```txt
venv\Scripts\activate
```
**Linux / Mac**
```bash
source venv/bin/activate
```
**Install Dependencies**
```bash
pip install -r requirements.txt
```
###### MongoDB Atlas Setup

###### 1. Create an account at
https://cloud.mongodb.com
###### 2. Create a Cluster
###### 3. Create Database User
###### 4. Allow Network Access (0.0.0.0/0)
###### 5. Copy the connection string
Example:
```txt
mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority
```
Replace it inside app.py
```txt
MONGO_URI = "your_connection_string"
```
**Running the Application**
Run the Flask server:
```txt
python app.py
```
**Application will start at:**
```txt
http://127.0.0.1:5000
```
**API Endpoint**
Access API:
```txt
http://127.0.0.1:5000/api
```
This endpoint reads data from data.json and returns JSON.
**Form Page**
Open:
```txt
http://127.0.0.1:5000
```
Fill the form and submit data.

**Success Page**

If submission is successful:
```txt
Data submitted successfully
```
**Error Handling**
If any error occurs during MongoDB insertion:
- Error message is displayed on the same form page
- User is not redirected
  
**Screenshots (Add in your submission)**
Include the following screenshots:

###### 1. Project Folder Structure
<img width="857" height="297" alt="image" src="https://github.com/user-attachments/assets/d1b51c20-5c3e-4363-a42f-2ac9e358ea75" />
###### 2. Running Flask Server
<img width="1449" height="357" alt="image" src="https://github.com/user-attachments/assets/d7f6ef4e-f667-4d2c-8976-82ad1a4aaf60" />

<img width="1460" height="312" alt="image" src="https://github.com/user-attachments/assets/98aedea3-287d-4251-9b8e-dbe9d19a001e" />

###### 3. API Response (/api)
<img width="351" height="454" alt="image" src="https://github.com/user-attachments/assets/d615b132-f806-4471-824f-880c8dfe0aa2" />

###### 4. Form Page
<img width="339" height="338" alt="image" src="https://github.com/user-attachments/assets/868f15a9-b22f-46ad-9230-3185357067d9" />

###### 5. Successful Submission Page
<img width="522" height="176" alt="image" src="https://github.com/user-attachments/assets/b045a132-5d32-4b8e-b329-d2ffaef868af" />

###### 6. MongoDB Atlas Collection Data
<img width="1919" height="618" alt="image" src="https://github.com/user-attachments/assets/9aebe296-8fa5-410a-ba97-f75541749928" />


###### Requirements

Example requirements.txt
```txt
Flask
pymongo
dnspython
GitHub Repository
```
Example repository link:

https://github.com/mohammadshakirsaifi/DevOps-3.git
###  Author
Mohammad Shakir
