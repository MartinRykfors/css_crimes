import random
from airium import Airium
import lib.cohost as cohost


image_map_local = {
    "off": "interface/0001.png",
    "radar": "interface/0002.png",
    "radar_blip": "interface/0003.png",
    "numbers": "interface/0004.png",
    "numbers_1": "interface/0005.png",
    "numbers_2": "interface/0006.png",
    "numbers_3": "interface/0007.png",
    "eggbug": "interface/0008.png",
    "eggbug_1": "interface/0009.png",
    "eggbug_2": "interface/0010.png",
    "eggbug_3": "interface/0011.png",
}
image_map_web = {
    "off": "https://staging.cohostcdn.org/attachment/1f15b219-3e9d-425b-8ea7-2a1df12f259a/0001.png",
    "radar": "https://staging.cohostcdn.org/attachment/e52c805e-8986-453a-b4f9-06a962abb3c5/0002.png",
    "radar_blip": "https://staging.cohostcdn.org/attachment/5c570c10-7482-449c-9f4c-87b6f7190427/0003.png",
    "numbers": "https://staging.cohostcdn.org/attachment/294b74ab-29b6-42c3-8a37-98b7370b8d0c/0004.png",
    "numbers_1": "https://staging.cohostcdn.org/attachment/1645f523-1c3d-46df-84d4-7c98b7a050dd/0005.png",
    "numbers_2": "https://staging.cohostcdn.org/attachment/131a4cc9-6a9f-4d0c-aebe-2635dff75b2c/0006.png",
    "numbers_3": "https://staging.cohostcdn.org/attachment/b01d25b3-dd2b-48ae-96e0-ef94e66c1a41/0007.png",
    "eggbug": "https://staging.cohostcdn.org/attachment/bd8b5897-4ee0-40ad-9d43-0b9f5165fc13/0008.png",
    "eggbug_1": "https://staging.cohostcdn.org/attachment/e2b8aab6-3a33-4326-b6af-9d45dd0c7918/0009.png",
    "eggbug_2": "https://staging.cohostcdn.org/attachment/b61ac097-4226-469a-b852-84ed15745f89/0010.png",
    "eggbug_3": "https://staging.cohostcdn.org/attachment/5d032fa7-1259-4025-aa2f-b231d07974b5/0011.png",
}

image_map = image_map_web


def body(a):
    with a.div(
        style="isplay:flex; flex-direction:row; background-color: rgb(250 216 214); border-radius:0.5rem; color:rgb(34 0 16); padding: 0.75rem; gap: 1rem; align-items:center;align-self:stretch;box-sizing:border-box; width:100%; margin-top:0.75rem; margin-bottom:0.75rem; line-height:1.5"
    ):
        with a.div(
            style="width: 1.5rem; height: 1.5rem; flex-shrink:0; align-self:flex-start; background-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdCb3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0icmdiKDIyOSwgMTA3LCAxMTEpIiBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InctNiBzZWxmLXN0YXJ0IHRleHQtc3RyYXdiZXJyeSI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNMTIgOXYzLjc1bS05LjMwMyAzLjM3NmMtLjg2NiAxLjUuMjE3IDMuMzc0IDEuOTQ4IDMuMzc0aDE0LjcxYzEuNzMgMCAyLjgxMy0xLjg3NCAxLjk0OC0zLjM3NEwxMy45NDkgMy4zNzhjLS44NjYtMS41LTMuMDMyLTEuNS0zLjg5OCAwTDIuNjk3IDE2LjEyNnpNMTIgMTUuNzVoLjAwN3YuMDA4SDEydi0uMDA4eiI+PC9wYXRoPjwvc3ZnPgo=)"
        ):
            pass
        with a.div():
            with a.p(style="margin:0"):
                a('Requires a full width display to work properly.')
    description = """
    An interactive retro display showing graphics in amber.
    Three buttons can be seen below it, labeled Radar, Numbers, Eggbug.
    Clicking those buttons change what graphics are shown on the display.
    Three buttons on the side of the display allow choosing a sub-mode for the current mode selected.
    """
    cohost.with_description(a, content, description, "crime")


def content(a):
    pass

    with a.div(
        style=cohost.style(
            {"position": "relative", "height": "500px", "width": "500px"}
        )
    ):
        with a.div(style=cohost.style({"position": "absolute"})):
            image(a, "off")

        radar(a)

        numbers(a)

        eggbug(a)


def radar(a):
    with a.details(name="mode"):
        with a.summary(style=cohost.style({"font-size": 0})):
            with a.div(
                style=cohost.style(
                    {
                        "position": "absolute",
                        "top": "425px",
                        "left": "50px",
                        "width": "100px",
                        "height": "50px",
                        'cursor': 'pointer',
                    }
                )
            ):
                pass
        with a.div(
            style=cohost.style(
                {
                    "position": "absolute",
                    "pointer-events": "none",
                    "display": "grid",
                    "grid-template": "1fr / 1fr",
                }
            )
        ):
            with a.div(
                style=cohost.style(
                    {"grid-row": "1 / span 1", "grid-column": "1 / span 1"}
                )
            ):
                image(a, "radar")
            with a.div(
                style=cohost.style(
                    {
                        "grid-row": "1 / span 1",
                        "grid-column": "1 / span 1",
                        "transform": "scale(0)",
                    }
                    | cohost.animation(easing="steps(2, jump-none)", duration=3)
                )
            ):
                image(a, "radar_blip")


def numbers(a):
    mode(a, 200, "numbers_mode", "numbers", "numbers_1", "numbers_2", "numbers_3")


def eggbug(a):
    mode(a, 350, "eggbug_mode", "eggbug","eggbug_1", "eggbug_2", "eggbug_3")


def mode(a, left, sub_mode_name, key0, key1, key2, key3):
    with a.details(name="mode"):
        with a.summary(style=cohost.style({"font-size": 0})):
            with a.div(
                style=cohost.style(
                    {
                        "position": "absolute",
                        "top": "425px",
                        "left": f"{left}px",
                        "width": "100px",
                        "height": "50px",
                        'cursor': 'pointer',
                    }
                )
            ):
                pass
        with a.div(
            style=cohost.style(
                {
                    "position": "absolute",
                    "pointer-events": "none",
                    "display": "grid",
                    "grid-template": "1fr / 1fr",
                }
            )
        ):
            with a.div(
                style=cohost.style(
                    {
                        "grid-row": "1 / span 1",
                        "grid-column": "1 / span 1",
                    }
                )
            ):
                image(a, key0)
            sub_mode(a, 100, key1, sub_mode_name)
            sub_mode(a, 200, key2, sub_mode_name)
            sub_mode(a, 300, key3, sub_mode_name)


def sub_mode(a, top, key, mode):
    with a.div(
        style=cohost.style(
            {
                "grid-row": "1 / span 1",
                "grid-column": "1 / span 1",
            }
        )
    ):
        with a.details(name=mode):
            with a.summary(style=cohost.style({"font-size": 0})):
                with a.div(
                    style=cohost.style(
                        {
                            "position": "absolute",
                            "top": f"{top}px",
                            "left": "405px",
                            "width": "50px",
                            "height": "50px",
                            "pointer-events": "auto",
                            'cursor': 'pointer',
                        }
                    )
                ):
                    pass
            image(a, key)


def image(a, key):
    a.img(src=image_map[key], style=cohost.style({"margin": "0px"}))


cohost.create_document(body, "post.html")
