# CI-Online-Data-Catalogue

Filterable catalogue of online data resources applicable to climate risk assessment development with a focus on Irish resources. 

This catalogue is an output from the Climate Change Risk Assessment Methodology work carried out by Climate Ireland.

## Getting Started

Clone the repository, set up env and install dependencies.

```
git clone git@github.com:ClimateIreland/CI-Online-Data-Catalogue.git
cd CI-Online-Data-Catalogue
python3 -m venv ./
source bin/activate 
pip install -r requirements.txt
python dash/app.py

```

The GUI will be running at http://127.0.0.1:8050/

### Deploying


```
docker-compose up
```
The app will be running on localhost:8090.

## Contributing

Camila Tavares Pereira, James Fitton 
