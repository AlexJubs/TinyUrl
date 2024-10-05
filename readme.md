# TinyURL: URL Shortener Service

## Description
TinyURL is a simple URL shortener service that allows users to convert long URLs into shorter, more manageable links. It uses SQLite as a database to store and retrieve URL mappings.

## Features
- Shorten long URLs
- Redirect users from short URLs to original long URLs
- Persistent storage of URL mappings using SQLite

## Installation
1. Clone the repository
2. Install dependencies using Poetry:
   ```
   poetry install
   ```

## Usage
1. Initialize the database (this will be done automatically when you run the app for the first time)
2. Run the application:
   ```
   poetry run python main.py
   ```
3. Access the service through your web browser at `http://localhost:5000`

## API Endpoints
- POST `/shorten`: Shorten a long URL
  - Request body: `{"url": "https://example.com/very/long/url"}`
  - Response: Short URL
- GET `/<short_url>`: Redirect to the original long URL

## Technologies Used
- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- Poetry (for dependency management)