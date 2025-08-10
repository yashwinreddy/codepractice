from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.github_api import fetch_github_profile, fetch_repos
from app.analytics import compute_metrics

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/profile/{username}", response_class=HTMLResponse)
async def profile(request: Request, username: str):
    try:
        user = await fetch_github_profile(username)
        repos = await fetch_repos(username)
        metrics = compute_metrics(repos)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"User not found or API error: {str(e)}")

    return templates.TemplateResponse("profile.html", {
        "request": request,
        "user": user,
        "metrics": metrics,
        "repos": repos[:5]  # show top 5 repos
    })
