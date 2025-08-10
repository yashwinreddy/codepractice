import httpx

GITHUB_API_URL = "https://api.github.com"

async def fetch_github_profile(username: str):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{GITHUB_API_URL}/users/{username}")
        resp.raise_for_status()
        return resp.json()

async def fetch_repos(username: str):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{GITHUB_API_URL}/users/{username}/repos?per_page=100")
        resp.raise_for_status()
        return resp.json()
