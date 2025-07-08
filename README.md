# 100-days-of-Java

## Ecommerce Apps

This repository contains two sample ecommerce CMS implementations.

### Spring Boot Version

A minimal Spring Boot based CMS with search and a rule-based chatbot.

Run with:

```bash
mvn -f ecommerce-app/pom.xml spring-boot:run
```

Visit `http://localhost:8080/products` to interact with the Java app.

### Django Version

A similar application implemented with Django.

Run migrations and start the server with:

```bash
python manage.py migrate
python manage.py runserver
```

Then visit `http://localhost:8000/products/` for the Python version.
