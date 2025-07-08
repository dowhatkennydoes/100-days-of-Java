# Fye CBD Ecommerce CMS

Fye is a small sample ecommerce CMS for a CBD business. It is built with **Django**, uses **SQLite** for local storage, and can optionally log chat messages to **Firebase**.  The CMS lets you manage your product catalog and includes a very simple chatbot example.

Run migrations and start the server with:

```bash
pip install django firebase-admin
python manage.py migrate
python manage.py runserver
```

Then visit `http://localhost:8000/products/` to manage products and chat with the bot.

### Firebase Setup

If you want chat logs written to Firebase, create a service account JSON file and place it at `django-app/firebase_credentials.json`.  The app uses `firebase_admin` to write chat transcripts to the `chat_logs` collection.
