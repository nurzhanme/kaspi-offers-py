# Kaspi Offers API

Python client for Kaspi.kz offers API

## Installation
```bash
pip install kaspi-offers-api
```

## Usage
```python
import asyncio
from kaspi_offers_api import KaspiClient

async def main():
    client = KaspiClient()
    
    # Get offers for a product
    response = await client.get_offers("123728177")
    
    print(f"Found {response.total} offers")
    
    # Iterate through offers
    for offer in response.offers:
        print(f"{offer.merchantName}: {offer.price} ₸")
        print(f"Rating: {offer.merchantRating} ({offer.merchantReviewsQuantity} reviews)")
        print(f"Delivery: {offer.deliveryType}")
        print("---")

asyncio.run(main())
```

## Parameters
```python
response = await client.get_offers(
    product_id="123728177",
    city_id="750000000",  # Almaty by default
    limit=64,
    page=0
)
```

## Data Models

### Offer
- `merchantName` - merchant name
- `price` - price
- `merchantRating` - merchant rating
- `merchantReviewsQuantity` - number of reviews
- `deliveryType` - delivery type (EXPRESS, TO_DOOR, PICKUP, POSTOMAT)
- `kaspiDelivery` - Kaspi delivery available
- `delivery` - delivery date
- `pickup` - pickup date

### OffersResponse
- `offers` - list of offers
- `total` - total count
- `offersCount` - count in response

## Requirements

- Python >= 3.8
- httpx >= 0.27.0