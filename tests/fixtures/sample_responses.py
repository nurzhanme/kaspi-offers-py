"""Mock API response data for testing."""

# Valid offer with all fields populated
SAMPLE_OFFER_FULL = {
    "masterSku": "123456789",
    "merchantId": "987654321",
    "merchantName": "Test Electronics Store",
    "merchantSku": "SKU-TEST-001",
    "title": "iPhone 15 Pro Max 256GB",
    "price": 599990.0,
    "merchantRating": 4.8,
    "merchantReviewsQuantity": 1523,
    "deliveryType": "EXPRESS",
    "deliveryDuration": "1-2 дня",
    "kaspiDelivery": True,
    "preorder": 0,
    "delivery": "Бесплатно",
    "pickup": "Доступен самовывоз",
}

# Offer with optional fields missing
SAMPLE_OFFER_MINIMAL = {
    "masterSku": "111222333",
    "merchantId": "555666777",
    "merchantName": "Budget Store",
    "merchantSku": "SKU-MIN-001",
    "title": "Basic Phone Case",
    "price": 1990.0,
    "merchantRating": 3.5,
    "merchantReviewsQuantity": 42,
    "deliveryType": "STANDARD",
    "deliveryDuration": None,
    "kaspiDelivery": False,
    "preorder": 0,
}

# Offer with special characters and edge cases
SAMPLE_OFFER_EDGE_CASE = {
    "masterSku": "999888777",
    "merchantId": "111000111",
    "merchantName": "Магазин \"Электроника\" & Co.",
    "merchantSku": "СПЕЦ-СКЮ-001",
    "title": "Товар с спец. символами! @#$%",
    "price": 0.0,  # Zero price edge case
    "merchantRating": 5.0,  # Perfect rating
    "merchantReviewsQuantity": 0,  # No reviews yet
    "deliveryType": "PICKUP_ONLY",
    "deliveryDuration": "Сразу",
    "kaspiDelivery": False,
    "preorder": 1,  # Preorder item
    "delivery": None,
    "pickup": "Только самовывоз",
}

# Complete API response with multiple offers
SAMPLE_RESPONSE_MULTIPLE = {
    "offers": [
        SAMPLE_OFFER_FULL,
        SAMPLE_OFFER_MINIMAL,
        SAMPLE_OFFER_EDGE_CASE,
    ],
    "total": 150,
    "offersCount": 3,
}

# Empty offers response
SAMPLE_RESPONSE_EMPTY = {
    "offers": [],
    "total": 0,
    "offersCount": 0,
}

# Single offer response
SAMPLE_RESPONSE_SINGLE = {
    "offers": [SAMPLE_OFFER_FULL],
    "total": 1,
    "offersCount": 1,
}

# Response with pagination (more total than current offers)
SAMPLE_RESPONSE_PAGINATED = {
    "offers": [SAMPLE_OFFER_FULL, SAMPLE_OFFER_MINIMAL],
    "total": 250,
    "offersCount": 2,
}
