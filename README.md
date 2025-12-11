# Kaspi Offers API

Python client for Kaspi.kz offers API

## Installation
```bash
pip install kaspi-offers-py
```

## Usage
```python
import asyncio
from kaspi_offers_py import KaspiClient

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

- Python >= 3.9
- httpx >= 0.27.0

## Development

### Install development dependencies

**Using uv (recommended):**
```bash
# Automatically installs dev dependencies
uv sync
```

**Using pip:**
```bash
pip install -e ".[dev]"
```

### Running tests

**Using uv:**
```bash
# Unit tests only (default - fast, no network)
uv run pytest

# Integration tests (real API calls, requires network)
uv run pytest -m integration

# All tests (unit + integration)
uv run pytest -m ""

# With coverage
uv run pytest --cov=kaspi_offers_py --cov-report=html
```

**Using pip/pytest directly:**
```bash
# Unit tests only (default - fast, no network)
pytest

# Integration tests (real API calls, requires network)
pytest -m integration

# All tests (unit + integration)
pytest -m ""

# With coverage
pytest --cov=kaspi_offers_py --cov-report=html
```