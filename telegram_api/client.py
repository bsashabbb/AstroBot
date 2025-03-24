import httpx

class TelegramClient:
    def __init__(self, token: str):
        self.base_url = f"https://api.telegram.org/bot{token}/"
        self.client = httpx.AsyncClient()
    
    async def _request(self, method: str, params: dict) -> dict:
        response = await self.client.post(
            f"{self.base_url}{method}",
            json={k: v for k, v in params.items() if v is not None}
        )
        response.raise_for_status()
        return response.json()
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, *exc):
        await self.client.aclose()
