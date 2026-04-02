from scraper.ebay_scraper import get_products
from cleaner.data_cleaner import clean_products
from utils.csv_exporter import save_to_csv


SEARCH_URL = "https://www.ebay.com/sch/i.html?_nkw=kitchen+accessories"


def main():
    print("🚀 eBay Pipeline Started")

    products = get_products(SEARCH_URL)

    print(f"📦 Raw products: {len(products)}")

    cleaned = clean_products(products)

    print(f"🧹 Cleaned products: {len(cleaned)}")

    save_to_csv(cleaned, "data/products.csv")

    print("✅ Done! Saved to data/products.csv")


if __name__ == "__main__":
    main()