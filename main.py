from flask import Flask
from pornhub_api import PornhubApi
from pornhub_api.backends.aiohttp import AioHttpBackend

app = Flask(__name__)


@app.route("/ph/videos")
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
                    # "name": vid.title,
                    # "categories": [x.category for x in vid.categories],
                    # "thumb": vid.thumb,
                    "title": vid.title,
                    "duration": vid.duration,
                    "views": vid.views,
                    "video_id": vid.video_id,
                    "rating": vid.rating,
                    "ratings": vid.ratings,
                    "url": vid.url,
                    "default_thumb": vid.default_thumb,
                    "thumb": vid.thumb,
                    "publish_date": vid.publish_date,
                    "segment": vid.segment,
                    "thumbs": [th.src for th in vid.thumbs],
                    "tags": [t.tag_name for t in vid.tags],
                    "categories": [c.category for c in vid.categories],
                    "pornstars": [p.pornstar_name for p in vid.pornstars],
                }
            )

        return result


if __name__ == "__main__":
    app.run(host="0.0.0.0")
