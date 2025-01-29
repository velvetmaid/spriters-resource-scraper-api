# Spriters Resource Scraper API

<div align="center">
  <img src="https://www.spriters-resource.com/resources/images/light/header/logo.png">
  <p>
  This API allows you to scrape different resources such as menus, categories, and search results from <a href="https://www.spriters-resource.com">Spriters Resource</a>. It provides the following endpoints to interact with the data </p>
</div>

<p align="center">
  <a href="https://spriters-resource-scraper-api-production.up.railway.app/docs" target="_blank"><strong>API Documentation</strong></a>
</p>

## Installation

To get started, clone this repository and install the required dependencies:

```bash
git clone https://github.com/username/spriters-resource-scraper-api.git
cd spriters-resource-scraper-api
pip install -r requirements.txt
```
Running Locally
```bash
uvicorn src.api.index:app --host 0.0.0.0 --port 8000 --reload
```