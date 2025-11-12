# bushbarcoffee

A simple Flask web application for managing orders at the halfway house of a golf course.


## Project Structure
```
app.py                # Main Flask application
data.py               # Data handling logic
requirements.txt      # Python dependencies
static/css/style.css  # CSS styles
templates/            # HTML templates
    base.html
    index.html
    new_order.html
    orders.html
    thanks.html
```

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/nev1000/bushbarcoffee.git
   cd newgolf
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   flask run
   ```
   Or for production:
   ```bash
   gunicorn app:app
   ```

## License
MIT
