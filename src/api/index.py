from fastapi import FastAPI, HTTPException
from src.scraper.scraper import *
from src.scraper.utils import *

description = """
![Spriters Resource](https://www.spriters-resource.com/resources/images/light/header/logo.png)
"""

app = FastAPI(
    title="Spriters-Resource Scraper API",
    description=description,
    summary="API to scrape almost everything from Spriters Resource.",
    terms_of_service="https://www.spriters-resource.com/page/faq/",
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)


@app.get("/", tags=["General"])
def home():
    """Home endpoint"""
    data = check_base_url()
    return data


@app.get("/menus", tags=["Scrape"])
def get_menus():
    """Get all menus"""
    try:
        data = scrape_menu()
        return {"status": "success", "success": True, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/menu_items/{item}", tags=["Scrape"])
def get_menu_item(item: str):
    """Get menu item details"""
    try:
        data = scrape_menu_item(item)
        return {"status": "success", "success": True, "param": item, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/category_info/{category}", tags=["Scrape"])
def get_category_info(category: str):
    """Get category information"""
    try:
        data = scrape_category_info(category)
        return {"status": "success", "success": True, "param": category, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/category_sections/{category}", tags=["Scrape"])
def get_category_sections(category: str):
    """Get category sections"""
    try:
        data = scrape_category_sections(category)
        return {"status": "success", "success": True, "param": category, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/category_info_sections/{category}", tags=["Scrape"])
def get_category_info_sections(category: str):
    """Get category info sections"""
    try:
        data = scrape_category_info_sections(category)
        return {"status": "success", "success": True, "param": category, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/search/", tags=["Scrape"])
def search(keyword: str):
    """Search for a keyword"""
    try:
        data = scrape_search_results(keyword)
        return {"status": "success", "success": True, "keyword": keyword, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/items/", tags=["Scrape"])
def get_selected_item(selected_item: str):
    """Get selected item sections"""
    try:
        data = scrape_selected_item(selected_item)
        return {
            "status": "success",
            "success": True,
            "param": selected_item,
            "data": data,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/sheet/", tags=["Scrape"])
def get_selected_sheet(selected_sheet: str):
    """Get selected item sections"""
    try:
        data = scrape_sheet(selected_sheet)
        return {
            "status": "success",
            "success": True,
            "param": selected_sheet,
            "data": data,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
