import os
from typing import Literal

import requests
from dotenv import load_dotenv
from requests import Response
from bot import log

class CobaltAPI:
    def __init__(self):
        load_dotenv()
        self.url = os.getenv("COBALT_API_URL")
        self.headers = {"Content-Type": "application/json", "Accept": "application/json"}
        self.options = {}

    def __get_request(self) -> Response:
        response = requests.get(self.url)
        return response

    def __post_request(self, data: dict) -> Response:
        response = requests.post(self.url, headers=self.headers, json=data)
        return response

    def status(self) -> bool:
        try:
            response = self.__get_request()
        except:
            return False
        data = response.json()
        return True if data.get("cobalt") else False

    def quality(self, quality: Literal["max", "4320", "2160", "1440", "1080", "720", "480", "360", "240", "144"]):
        self.options['videoQuality'] = quality

    def filename_style(self, pattern: Literal["classic", "pretty", "basic", "nerdy"]):
        self.options['filenameStyle'] = pattern

    def vcodec(self, codec: Literal["h264", "av1", "vp9"]):
        self.options['youtubeVideoCodec'] = codec

    def aformat(self, aformat: Literal["best", "mp3", "ogg", "wav", "opus"]):
        self.options['audioFormat'] = aformat

    def mode(self, mode: Literal["audio", "mute", "auto"]):
        self.options['downloadMode'] = mode

    def services(self) -> list:
        response = requests.get(self.url)
        response.raise_for_status()
        data = response.json()
        return data["cobalt"]["services"]

    def tunnel(self, url: str) -> str:
        data = {'url': url}
        data.update(self.options)
        response = requests.post(
            self.url,
            json=data,
            headers=self.headers
        )
        return response.json()["url"]

    def download(self, url: str) -> str:
        data = {'url': url}
        data.update(self.options)
        response = requests.post(
            self.url,
            json=data,
            headers=self.headers
        )
        if response.status_code != 200:
            return ""
        result = response.json()
        with requests.get(result["url"], stream=True) as r:
            r.raise_for_status()
            try:
                with open(result["filename"], "wb") as f:
                    f.write(r.content)
            except Exception as e:
                log.error(str(e))
        return result["filename"]