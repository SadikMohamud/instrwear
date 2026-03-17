# Deployment

## Overview

The application is deployed using Heroku.

---

## Database

- SQLite is used during development
- PostgreSQL is used in production via Heroku

---

## Deployment Steps

1. Create Heroku application  
2. Configure environment variables  
3. Add Procfile  
4. Install dependencies  
5. Run migrations  
6. Deploy via Git  

---

## Environment Variables

- SECRET_KEY  
- DATABASE_URL  
- STRIPE_PUBLIC_KEY  
- STRIPE_SECRET_KEY  

---

## Notes

- Static files configured for deployment
- Debug mode disabled in production