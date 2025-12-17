import httpx
import logging
from typing import Optional, Dict, Any
from .models import OffersResponse


class KaspiClient:
    BASE_URL = "https://kaspi.kz"

    def __init__(self, timeout: int = 30, proxy: Optional[str] = None, verbose: bool = False):
        self.timeout = timeout
        self.proxy = proxy
        self.verbose = verbose
        self.headers = {
            "Content-Type": "application/json",
            "Referer": "https://kaspi.kz/shop/search/",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        }

        # Set up logging if verbose mode is enabled
        self.logger = logging.getLogger(__name__)
        if self.verbose:
            if not self.logger.handlers:
                handler = logging.StreamHandler()
                handler.setFormatter(logging.Formatter(
                    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                ))
                self.logger.addHandler(handler)
            self.logger.setLevel(logging.DEBUG)
            self.logger.debug(f"KaspiClient initialized with timeout={timeout}, proxy={proxy}")
        else:
            self.logger.setLevel(logging.WARNING)

    async def test_connection(self) -> Dict[str, Any]:
        """
        Test the connection and proxy configuration.

        Returns:
            Dict containing connection test results including:
            - success: bool
            - proxy: str or None
            - status_code: int
            - error: str (if failed)

        Raises:
            httpx.HTTPError: If the test request fails
        """
        test_url = "https://httpbin.org/get"
        self.logger.debug(f"Testing connection to {test_url}")
        self.logger.debug(f"Using proxy: {self.proxy if self.proxy else 'None (direct connection)'}")

        try:
            async with httpx.AsyncClient(timeout=self.timeout, proxy=self.proxy) as client:
                response = await client.get(test_url)
                response.raise_for_status()
                data = response.json()

                result = {
                    "success": True,
                    "proxy": self.proxy,
                    "status_code": response.status_code,
                    "origin_ip": data.get("origin"),
                    "url_accessed": test_url
                }

                self.logger.debug(f"Connection test successful: {result}")
                return result

        except Exception as e:
            result = {
                "success": False,
                "proxy": self.proxy,
                "error": str(e)
            }
            self.logger.error(f"Connection test failed: {result}")
            raise

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

        self.logger.debug(f"Requesting offers for product_id={product_id}")
        self.logger.debug(f"URL: {url}")
        self.logger.debug(f"Payload: {payload}")
        self.logger.debug(f"Using proxy: {self.proxy if self.proxy else 'None (direct connection)'}")

        async with httpx.AsyncClient(timeout=self.timeout, proxy=self.proxy) as client:
            response = await client.post(url, json=payload, headers=self.headers)
            self.logger.debug(f"Response status: {response.status_code}")
            response.raise_for_status()
            result = OffersResponse.from_dict(response.json())
            self.logger.debug(f"Successfully retrieved {len(result.offers)} offers")
            return result
