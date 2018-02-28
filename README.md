# Vessel Scraper
## About
Vessel Scraper crawls vessel schedule, movement and position from Cochin Port's website.<br> 
<br>
Database: PostgreSQL<br>
ORM: SQLAlchemy<br>
Web: Flask<br>

### Setup
`./setup.sh` <br>
`python manage.py migrate`

### To crawl
`python manage.py crawl`

### To browse data
`python manage.py runserver`

