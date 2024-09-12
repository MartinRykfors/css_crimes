import random
from airium import Airium
import lib.cohost as cohost


def body(a):
    description = """An infinite row of glowing train cars move past while the background flashes at the same
    tempo as Underworld - Dark and Long (Dark Train) plays."""
    cohost.with_description(a, content, description, "crime")
    a("")
    a("---")
    a("")
    a("https://www.youtube.com/watch?v=sHK9usHwxSs")


def content(a):
    with a.div(
        style=cohost.style(
            {
                "width": "100%",
                "height": "400px",
                "background-color": "black",
                "display": "flex",
                "align-items": "center",
            }
        )
    ):
        with a.div(
            style=cohost.style(
                {
                    "display": "grid",
                    "grid-template-columns": "1fr",
                    "grid-template-row": "1fr",
                    "transform": "translateX(-50px)",
                }
            )
        ):

            glow(a, "hsl(200 100% 40%)", 0)
            glow(a, "hsl(230 100% 40%)", 0.25)
            glow(a, "hsl(260 100% 40%)", 0.5)
            glow(a, "hsl(290 100% 40%)", 0.75)

            with a.div(
                style=cohost.style(
                    {
                        "grid-row": "1 / span 1",
                        "grid-column": "1 / span 1",
                        "display": "flex",
                        "align-items": "center",
                        "transform": "scale(120%, 100%)",
                    }
                )
            ):
                for _ in range(18):
                    with a.div(style=cohost.style({"font-size": "2rem"})):
                        with a.div(
                            style=cohost.style(
                                {"transform": "translateX(100%)"}
                                | cohost.animation(direction="normal")
                            )
                        ):
                            with a.div(
                                style=cohost.style(
                                    {
                                        "transform": "translateX(-100%)",
                                        "filter": "drop-shadow(0px 7px 3px black) drop-shadow(0px -5px 3px black) drop-shadow(5px 0px 3px purple)",

                                    }
                                )
                            ):
                                with a.div(
                                    style=cohost.style(
                                        {
                                            # "background": "linear-gradient(to bottom, hsl(240 50% 20%), hsl(0 50% 10%))",
                                            # 'background-color': 'gray',
                                            # "-webkit-background-clip": "text",
                                            # "background-clip": "text",
                                            "color": "rgb(0 0 0 / 50%)",
                                        }
                                    )
                                ):
                                    with a.div(
                                        style=cohost.style(
                                            {"transform": "scale(100%, 100%)"}
                                        )
                                    ):
                                        a("🚃")
                                        # a("A")


def glow(a, color, delay):
    with a.div(
        style=cohost.style(
            {
                "grid-row": "1 / span 1",
                "grid-column": "1 / span 1",
                "width": "200%",
                "height": "100px",
                "overflow": "hidden",
            }
        )
    ):
        duration = 60 / 135.15 * 4
        with a.div(
            style=cohost.style(
                {
                    "background": f"linear-gradient(to bottom, transparent, {color})",
                    "width": "100%",
                    "height": "100px",
                    "transform": "translateY(100%)",
                }
                | cohost.animation(
                    direction="reverse",
                    duration=duration,
                    delay=duration * delay,
                    easing="cubic-bezier(.84,.01,.69,1)",
                )
            )
        ):
            pass


cohost.create_document(body, "post.html")
