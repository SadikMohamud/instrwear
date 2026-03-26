---

# 📁 **docs/API.md**

```markdown
# API Documentation

## Overview

InstrWear uses Django views to provide backend functionality in a REST-like structure.

---

## Base URL

Production:
https://instrwear-8184ce115d49.herokuapp.com/

Local:
http://127.0.0.1:8000/

---

## Authentication

POST /accounts/login/  
POST /accounts/register/shopper/  
POST /accounts/register/merchant/  
GET /accounts/logout/  

---

## Shopper Endpoints

GET /shopper/dashboard/  
GET /shopper/onboarding/  
POST /shopper/onboarding/  

---

## Merchant Endpoints

GET /merchant/dashboard/  
GET /merchant/onboarding/  
POST /merchant/onboarding/  
GET /merchant/products/  
GET /merchant/add-product/  
POST /merchant/add-product/  

---

## Product Endpoints

GET /products/  
GET /products/?category=<id>  
GET /products/<id>/  

---

## Cart Endpoints

GET /cart/  
POST /cart/add/<product_id>/  
POST /cart/remove/<product_id>/  

---

## Checkout Endpoints

GET /checkout/  
POST /checkout/  
GET /checkout/success/  

---

## Orders

GET /orders/  

---

## Permissions

- Anonymous: view products only  
- Authenticated users: cart + checkout  
- Merchants: manage products  
- Admin: full control  

---

## Notes

- Session-based authentication  
- No DRF (yet)  
- Filtering only (no search)  

---

## Future Improvements

- Django REST Framework  
- JWT authentication  
- Pagination  
- Search endpoint