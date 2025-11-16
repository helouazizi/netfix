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
- **Database**: MYSQL 
- **Version Control**: Git 
- **Containaersation** : docker , docker-compose

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

2. **Make sure Docker installed**

```bash
docker --version 
```




3. **Add .env file in the root project and add this variables**

```bash
# Database
MYSQL_ROOT_PASSWORD=rootpass
MYSQL_DATABASE=netfix_database
MYSQL_USER=your_user
MYSQL_PASSWORD=your_pass
MYSQL_HOST=netfix_db
MYSQL_PORT=3306

# Django
DJANGO_SECRET_KEY=your_secret_key_here
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=*
DJANGO_ENVIREMENT=production
```

4. **Run it with docker**

```bash
docker-compose up --build
```

5. **Apply migrations**

```bash
docker exec -it netfix_app python manage.py migrate
```

Access the site at `http://127.0.0.1:8000/`.

---




## License

Educational project for Django learning purposes.




## Author

- **Name**: Hassan El ouazizi
- **Email**: ouazizi2code@gmail.com  
- **GitHub**: [https://github.com/helouazizi](https://github.com/helouazizi)

