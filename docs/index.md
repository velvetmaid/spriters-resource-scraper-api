# Spriters Resource Scraper API

<div align="center">
  <img src="https://www.spriters-resource.com/resources/images/light/header/logo.png">
  <p>
  This API allows you to scrape different resources such as menus, categories, and search results from <a href="https://www.spriters-resource.com">Spriters Resource</a>. It provides the following endpoints to interact with the data </p>
</div>

---

#### GET `ROOT` → `/`
```bash
http://localhost:8000
```

**Description:**  
The home endpoint. Checks if the Spriters Resource base URL is reachable.

**Response Example:**

```json
{
  "status": "success",
  "message": "Base URL is reachable"
}
```

---

#### GET `Menus` → `/menus`
```bash
http://localhost:8000/menus
```

**Description:**  
Returns available top-level menu categories.

**Response Example:**

```json
{
  "status": "success",
  "success": true,
  "data": [
    {
      "menu": "Consoles"
    },
    {
      "menu": "Genres"
    },
    {
      "menu": "Advertisement"
    }
  ]
}

```
---

#### GET `Menu Items` → `/menu_items/{item}`
```bash
http://localhost:8000/menu_items/consoles
```

**Description:**  
Returns a list of sub-categories for the given menu.

**Response Example:**

```json
{
  "status": "success",
  "success": true,
  "param": "consoles",
  "data": [
    { "title": "3DS", "link": "/3ds/" },
    { "title": "Arcade", "link": "/arcade/" },
    { "title": "Browser Games", "link": "/browser_games/" }
  ]
}

```

---

#### GET `Category Info` → `/category_info/{category}`
```bash
http://localhost:8000/category_info/nintendo_64
```

**Description:**  
Returns category stats and metadata.

**Response Example:**

```json
{
  "status": "success",
  "success": true,
  "param": "nintendo_64",
  "data": {
    "category": "Nintendo 64 Stats",
    "rss_feed_url": "https://www.spriters-resource.com/uploads.php?cid=17",
    "sheets": "1,626",
    "games": "245",
    "biggest_game": "Paper Mario(298 sheets)",
    "biggest_submitter": "Mr. C(526 sheets)"
  }
}

```

---

#### GET `Category Sections` → `/category_sections/{category}`
```bash
http://localhost:8000/category_sections/nintendo_64
```

**Description:**  
Returns category sections like popular games, recent uploads, etc.

**Response Example:**

```json
{
  "status": "success",
  "success": true,
  "param": "nintendo_64",
  "data": [
    {
      "section_title": "Most Popular Games (All Time)",
      "items": [
        {
          "id": 1,
          "title": "Paper Mario",
          "url": "https://www.spriters-resource.com/nintendo_64/pm/",
          "image": "https://...968.png"
        }
        // ...
      ]
    }
    // More sections
  ]
}

```

---

#### GET `Category Info + Sections` → `/category_info_sections/{category}`
```bash
http://localhost:8000/category_info_sections/nintendo_64
```

**Description:**  
Combines category info with its sections.

**Response Example:**

```json
{
  "status": "success",
  "success": true,
  "param": "nintendo_64",
  "data": {
    "category": "Nintendo 64 Stats",
    "rss_feed_url": "...",
    "sheets": "1,626",
    "games": "245",
    "biggest_game": "...",
    "biggest_submitter": "...",
    "sections": [
      {
        "section_title": "...",
        "items": [
          {
            "id": 1,
            "title": "...",
            "url": "...",
            "image": "..."
          }
        ]
      }
    ]
  }
}

```

---

#### GET `Search` → `/search/?keyword={keyword}`
```bash
http://localhost:8000/search/?keyword=dummy
```

**Description:**  
Search for matching sprites and games.

**Response Example:**

```json
{
  "status": "success",
  "success": true,
  "keyword": "dummy",
  "data": {
    "sheet_results": {
      "title": "Sheet Results (33)",
      "count": 33,
      "items": [[
        {
          "id": 1,
          "title": "Crash Test, Dummy!",
          "link": "...",
          "image_url": "..."
        }
        // ...
      ]]
    },
    "game_results": {
      "title": "Game Results (2)",
      "count": 2,
      "items": [[
        {
          "id": 1,
          "title": "CID The Dummy",
          "link": "...",
          "image_url": "..."
        }
        // ...
      ]]
    }
  }
}
```

---

#### GET `Item Details` → `/items/?selected_item={item}`
```bash
http://localhost:8000?selected_item=mobile/touhoulostword/
```

**Description:**  
Returns detailed info and sections of a specific game.

**Response Example:**

```json
{
  "status": "success",
  "success": true,
  "param": "mobile/touhoulostword/",
  "data": {
    "title": "Touhou LostWord",
    "thumbnail_image_title": "...",
    "thumbnail_image_url": "...",
    "rss_feed_url": "...",
    "category": "Mobile",
    "sheets": "964",
    "hits": "1,038,691",
    "comments": "171",
    "sections": [
      {
        "section_title": "Battle Sprites",
        "items": [
          {
            "id": 1,
            "title": "Aya Shameimaru",
            "url": "...",
            "image": "..."
          }
          // ...
        ]
      }
      // More sections
    ]
  }
}

```
---

#### GET `Sheet Details` → `/sheet/?selected_sheet={item}`
```bash
http://localhost:8000/sheet/?selected_sheet=mobile/touhoulostword/sheet/192701/
```

**Description:**  
Returns detailed information about a specific sheet. 

**Response Example:**

```json
{
    "status": "success",
    "success": true,
    "param": "mobile/touhoulostword/sheet/192701/",
    "data": {
        "title": "Touhou LostWord",
        "category": "Mobile",
        "game": "Touhou LostWord",
        "section": "★5 Story Cards",
        "submitter": "KanaKonpaku",
        "size": "2.43 MB (2048x1485)",
        "format": "PNG (image/png)",
        "hits": "5,735",
        "comments": "0",
        "image_full_view_url": "https://www.spriters-resource.com/fullview/192701/",
        "sheet_image_url": "https://www.spriters-resource.com/resources/sheets/190/192701.png?updated=1677665370"
    }
}

```