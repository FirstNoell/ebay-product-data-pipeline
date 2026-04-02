def extract_product(card):
    try:
        title_el = card.query_selector(".s-card__title span")
        price_el = card.query_selector(".s-card__price")
        link_el = card.query_selector("a.s-card__link")
        img_el = card.query_selector("img")

        title = title_el.inner_text().strip() if title_el else ""
        price = price_el.inner_text().replace("$", "").strip() if price_el else ""
        url = link_el.get_attribute("href") if link_el else ""
        image = img_el.get_attribute("src") if img_el else ""

        if not title or not price:
            return None

        return {
            "title": title,
            "price": price,
            "url": url,
            "image": image,
            "status": "ok"
        }

    except Exception:
        return None