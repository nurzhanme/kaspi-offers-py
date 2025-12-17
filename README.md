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

### Using a Proxy
```python
import asyncio
from kaspi_offers_py import KaspiClient

async def main():
    # HTTP proxy
    client = KaspiClient(proxy="http://proxy.example.com:8080")

    # HTTPS proxy
    # client = KaspiClient(proxy="https://proxy.example.com:8080")

    # SOCKS proxy
    # client = KaspiClient(proxy="socks5://proxy.example.com:1080")

    # Proxy with authentication
    # client = KaspiClient(proxy="http://username:password@proxy.example.com:8080")

    response = await client.get_offers("123728177")
    print(f"Found {response.total} offers")

asyncio.run(main())
```

### Testing Proxy Connection
```python
import asyncio
from kaspi_offers_py import KaspiClient

async def main():
    client = KaspiClient(proxy="http://proxy.example.com:8080")

    try:
        # Test the connection and proxy configuration
        result = await client.test_connection()
        print(f"Connection test successful!")
        print(f"Origin IP: {result['origin_ip']}")
        print(f"Using proxy: {result['proxy']}")
        print(f"Status code: {result['status_code']}")
    except Exception as e:
        print(f"Connection test failed: {e}")

asyncio.run(main())
```

### Debug/Verbose Mode
```python
import asyncio
from kaspi_offers_py import KaspiClient

async def main():
    # Enable verbose logging to see detailed debug information
    client = KaspiClient(verbose=True, proxy="http://proxy.example.com:8080")

    # Test connection first
    try:
        result = await client.test_connection()
        print(f"✓ Proxy is working! Origin IP: {result['origin_ip']}")
    except Exception as e:
        print(f"✗ Proxy connection failed: {e}")
        return

    # Get offers with detailed logging
    response = await client.get_offers("123728177")
    print(f"Found {response.total} offers")

asyncio.run(main())
```

When verbose mode is enabled, you'll see detailed logs like:
```
2025-12-17 10:30:45 - kaspi_offers_py.client - DEBUG - KaspiClient initialized with timeout=30, proxy=http://proxy.example.com:8080
2025-12-17 10:30:45 - kaspi_offers_py.client - DEBUG - Testing connection to https://httpbin.org/get
2025-12-17 10:30:45 - kaspi_offers_py.client - DEBUG - Using proxy: http://proxy.example.com:8080
2025-12-17 10:30:46 - kaspi_offers_py.client - DEBUG - Connection test successful: {...}
2025-12-17 10:30:46 - kaspi_offers_py.client - DEBUG - Requesting offers for product_id=123728177
2025-12-17 10:30:46 - kaspi_offers_py.client - DEBUG - Using proxy: http://proxy.example.com:8080
2025-12-17 10:30:47 - kaspi_offers_py.client - DEBUG - Response status: 200
2025-12-17 10:30:47 - kaspi_offers_py.client - DEBUG - Successfully retrieved 64 offers
```

## Parameters

### Client Initialization
```python
client = KaspiClient(
    timeout=30,   # Request timeout in seconds (default: 30)
    proxy=None,   # Optional proxy URL (default: None)
    verbose=False # Enable debug logging (default: False)
)
```

### Getting Offers
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