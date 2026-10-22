# MLVehicle: Vehicle Machine Learning Dashboard

A Django web dashboard that reads a vehicle sales dataset and displays grouped data and charts. Built with Django, pandas, Plotly and Bootstrap 5.

## Features

- One-way frequency table of vehicles by manufacturer
- Bar chart of average profit by manufacturer (selling price minus wholesale price)
- Bootstrap-styled layout with a sidebar and scrollspy navigation

## Tech Stack

- Python 3
- Django
- pandas
- Plotly
- Bootstrap 5

## Project Structure

```
MLVehicle/
├── config/              # Project settings and main URLs
├── vehicles/            # Dashboard app
│   ├── dashboard.py     # Table and chart functions
│   ├── views.py         # Loads the CSV and renders the page
│   ├── urls.py          # App routes
│   └── templates/vehicles/index.html
├── dummy_data/          # CSV dataset
├── manage.py
└── requirements.txt
```

## Setup

1. Clone the repository:
```bash
   git clone https://github.com/CYUZUZO010/MLVehicle.git
   cd MLVehicle
```
2. Create and activate a virtual environment:
```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # Mac/Linux
```
3. Install dependencies:
```bash
   pip install -r requirements.txt
```
4. Apply migrations:
```bash
   python manage.py migrate
```
5. Run the server:
```bash
   python manage.py runserver
```
6. Open http://127.0.0.1:8000/

## Dataset

`dummy_data/vehicles_ml_dataset.csv` contains vehicle details (manufacturer, year, body type, fuel type, prices, kilometers driven) and client details (age, gender, country, profession, income).

## Author

CYUZUZO010
