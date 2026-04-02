def clean_products(products):
    seen = set()
    cleaned = []

    for p in products:
        key = p["title"]

        if key in seen:
            continue

        seen.add(key)

        # simple price cleaning
        try:
            p["price"] = float(p["price"])
        except:
            continue

        cleaned.append(p)

    return cleaned