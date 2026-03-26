# Deployment Guide

## Development Environment

- Database: SQLite

Run locally:

python manage.py migrate  
python manage.py runserver  

---

## Production (Heroku)

- Database: PostgreSQL

### Steps

1. Push project to GitHub  
2. Create Heroku app  
3. Connect GitHub repo  
4. Set environment variables (including DATABASE_URL)  
5. Run migrations:

heroku run python manage.py migrate  

6. Collect static files:

heroku run python manage.py collectstatic --noinput  

7. Open app:

https://instrwear-8184ce115d49.herokuapp.com/

---

## Notes

- SQLite used for development  
- PostgreSQL used in production  
- Static files handled via collectstatic