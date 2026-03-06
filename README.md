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

**1. Create an account at**
https://cloud.mongodb.com
**2. Create a Cluster**
**3. Create Database User**
**4. Allow Network Access (0.0.0.0/0)**
**5. Copy the connection string**
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

**1. Project Folder Structure**
**2. Running Flask Server**
**3. API Response (/api)**
**4. Form Page**
**5. Successful Submission Page**
**6. MongoDB Atlas Collection Data**


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
