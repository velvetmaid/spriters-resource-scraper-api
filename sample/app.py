from flask import Flask, jsonify
from scraper import scrape_touhou

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_scrape_data():
    try:
        data = scrape_touhou()
        return jsonify({"status": "success", "success": True, "data" :data}), 200
    except Exception as e:
        return jsonify({"status": "error", "success": False, "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)
