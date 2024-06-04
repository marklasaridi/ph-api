from flask import Flask
from pornhub_api import PornhubApi
from pornhub_api.backends.aiohttp import AioHttpBackend

app = Flask(__name__)


@app.route("/videos")
async def execute():
    async with AioHttpBackend() as backend:
        api = PornhubApi(backend=backend)

        videos = await api.search.search_videos(
            "eva elfie",
            category="lesbian",
            thumbsize="large_hd",
            ordering="mostviewed",
        )

        result = []

        for vid in videos:
            result.append(
                {
                    "name": vid.title,
                    "categories": [x.category for x in vid.categories],
                    "thumb": vid.thumb,
                }
            )

        return result


if __name__ == "__main__":
    app.run(host="0.0.0.0")
