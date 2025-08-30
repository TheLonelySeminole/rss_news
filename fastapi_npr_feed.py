import feedparser
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    rss_url = "https://feeds.npr.org/1001/rss.xml"
    d = feedparser.parse(rss_url)
    return templates.TemplateResponse("index.html", {"feed": d, "request": request})


@app.get("/bulma/", response_class=HTMLResponse)
async def read_bulma(request: Request):
    rss_url = "https://feeds.npr.org/1001/rss.xml"
    d = feedparser.parse(rss_url)
    return templates.TemplateResponse(
        "bulma_child.html", {"feed": d, "request": request}
    )
