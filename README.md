# Netfix

## Project Overview

**Netfix** is a Django-based web platform that allows users to request home services and companies to provide them. Services include carpentry, painting, home cleaning, plumbing, and more. The platform supports **two types of users** with distinct roles:

- **Company**: Can create new services.  
- **Customer**: Can request existing services.  

The system calculates total service costs automatically (`hours × price_per_hour`) and displays them in user profiles.

---

## Objectives

- Implement **user registration and login** for Companies and Customers.
- Ensure **unique emails and usernames** for all users.
- Display **profiles** with relevant information:
  - Customers: personal info + requested services.
  - Companies: personal info + services offered.
- Enable Companies to create services restricted by **field of work**:
  - Allowed fields: Air Conditioner, All in One, Carpentry, Electricity, Gardening, Home Machines, Housekeeping, Interior Design, Locks, Painting, Plumbing, Water Heaters.
  - "All in One" companies can create any service.
- Enable Customers to **request services**, specifying address and hours.
- Show service pages with details, company info, and previously requested services.
- Display service lists:
  - Most requested
  - All services (latest first)
  - By category

---

## Tech Stack

- **Backend**: Python 3, Django 3.1.14  
- **Frontend**: HTML5, CSS3, Django Templates  
- **Database**: SQLite3 (default, can be switched to PostgreSQL)  
- **Version Control**: Git  

---

## Technologies Used

- Django ORM for database management  
- Django Forms for input validation  
- Django Messages framework for success/error notifications  
- Django Authentication system for user login and registration  

---


## Setup Instructions  

1. **Clone the repository**

```bash
git clone https://github.com/helouazizi/netfix.git
cd netfix
```

2. **Create a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create a superuser**

```bash
python manage.py createsuperuser
```

6. **Add .env file**

```bash
echo 'ENVIREMENT="production" \nSECRET_KEY="your server key"' > netfix/.env 
```

7. **Run the development server**

```bash
python manage.py runserver
```

Access the site at `http://127.0.0.1:8000/`.

---


## docker 
1. **Add .env file**

```bash
echo 'ENVIREMENT="production" \nSECRET_KEY="your server key"' > netfix/.env 
```
2. **build an image**
```bash
docker build -t netfix .
```

3. **Run it with .env file**
```bash
docker run --env-file netfix/.env -p 8000:8000 netfix
```

## License

Educational project for Django learning purposes.




## Author

- **Name**: Hassan El ouazizi
- **Email**: ouazizi2code@gmail.com  
- **GitHub**: [https://github.com/helouazizi](https://github.com/helouazizi)

