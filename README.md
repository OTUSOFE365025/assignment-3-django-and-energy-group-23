# Assignment 3 - Django & Energy Usage Application
**Group 23 - CRN 43510**

## Overview 
This project uses the Django ORM framework to build a simple **Cash Register / Product Lookup System**. It stores product information (UPC, name, price) and allows the user to retrieve product details either:

- Through a web interface
- Or directly via a console (terminal) script

The project also includes access to Django's built-in **Admin Dashboard** for managing product records. SQLite is used as the backend database.


---

## Key Features

- **Django ORM** for database modeling and query operations.
- **User Input UI** for entering/scanning UPCs and displaying product details.
- **Fixture Support** using a `product.json` to quickly load product data.
- **Django Admin Panel** for editing and managing stored product entries.
- **Two ways to run** the application: Web mode or Console mode.

--- 

## Project Structure
assignment-3-django-and-energy-group-23-crn-43510/
│
├── db/
│ ├── models.py # Defines Product model (UPC, name, price)
│ └── fixtures/products.json
│

│
├── main.py # Console-based product lookup script
├── manage.py # Django management tool
├── settings.py # Django configuration (apps, DB, templates)
├── urls.py # URL routing file
└── README.md

---

## Running the Application (Windows)
1. Clone the repository:
   git clone https://github.com/OTUSOFE365025/assignment-3-django-and-energy-group-23-crn-43510.git

2. Create and activate a virtual environment:
   python -m venv venv
   venv\Scripts\activate

3. Install requirements:
   pip install django

4. Run migrations to create database tables:
   python manage.py makemigrations
   python manage.py migrate

5. Run the application:
   python main.py

6. Follow the prompts to enter a UPC code or type exit to quit.


## Cash Register Application - Sample Console Output
Below is an example of the application running in Cash Register Scan Mode, showing system users, loaded products, and UPC lookup in action:
Users in Systems:
1 - Dan
2 - Robert

Products Loaded:
| UPC | Item  | Price |
|-----|-------|-------|
| 111 | Apple | $0.99 |
| 222 | Milk  | $3.49 |
| 333 | Bread | $2.25 |

--- Cash Register Scan Mode ---
Enter UPC code (or 'exit'): 111
Item Found: Apple - $0.99
Enter UPC code (or 'exit'):


