import httpx
from typing import Optional
from .models import OffersResponse


class KaspiClient:
    BASE_URL = "https://kaspi.kz"

    def __init__(self, timeout: int = 30):
        self.timeout = timeout
        self.headers = {
            "Content-Type": "application/json",
            "Referer": "https://kaspi.kz/shop/search/",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        }

    async def get_offers(
            self,
            product_id: str,
            city_id: str = "750000000",
            limit: int = 64,
            page: int = 0
    ) -> OffersResponse:
        url = f"{self.BASE_URL}/yml/offer-view/offers/{product_id}"

        payload = {
            "cityId": city_id,
            "id": product_id,
            "limit": limit,
            "page": page
        }

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(url, json=payload, headers=self.headers)
            response.raise_for_status()
            return OffersResponse.from_dict(response.json())
