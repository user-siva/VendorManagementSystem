# VendorManagementSystem

The Vendor Management System is a Django-based application designed to streamline vendor management  
processes, including vendor profile management, purchase order tracking, and vendor performance evaluation.   
This system allows users to efficiently manage vendor information, track purchase orders, and calculate   
various performance metrics to evaluate vendor performance over time.

## Prerequisites

- Python (version 3.12)
- Django (version 5.0.6)

## Installation

# 1. Clone the repository:
   git clone https://github.com/user-siva/VendorManagementSystem.git  
   cd project-directory (VendorManagementSystem)

# 2.Create a virtual environment:
pipenv shell  
pipenv install 

# 4.Database setup:
python manage.py makemigrations    
python manage.py migrate  

# 1.Start the server:
python manage.py runserver  

# 2.Access API endpoints:

## Vendor API: /vendor/
Purchase Order API: /purchase-order/  
Historical Performance API: /vendor/historical_performance  

# Create User and Token based Authentication
POST user/create: Create a User  
A token is given to the user  
Use this token in HTTP Authorization header  
Authorization : Token your_token

## API Endpoints
Vendor API  
● POST /api/vendors/: Create a new vendor.  
● GET /api/vendors/: List all vendors.  
● GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.  
● PUT /api/vendors/{vendor_id}/: Update a vendor's details.  
● DELETE /api/vendors/{vendor_id}/: Delete a vendor  
  
Purchase Order API  
● POST /api/purchase_orders/: Create a purchase order.  
● GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.  
● GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.  
● PUT /api/purchase_orders/{po_id}/: Update a purchase order.  
● DELETE /api/purchase_orders/{po_id}/: Delete a purchase order  
  
Vendor Performance Evaluation  
● GET /api/vendors/{vendor_id}/performance: Retrieve a vendor's performance metrics  

Historical Performance API  
GET /vendor/historical_performance: List historical performance for all vendors.  
GET /vendor/historical_performance/{id}/: Retrieve a specific historical performance.
  
Update Acknowledgment Endpoint:  
● POST /api/purchase_orders/{po_id}/acknowledge for vendors to acknowledge POs.  
