import random
from airium import Airium
import lib.cohost as cohost

eggbug_logo = "https://cohost.org/static/41454e429d62b5cb7963.png"


def body(a):
    description = """Description"""
    cohost.with_description(a, content, description, "crime")


def content(a):
    with a.div(
        style=cohost.style(
            {
                "width": "100%",
                "height": "500px",
                "position": "relative",
                "border": "1px solid black",
                "background": "black",
                "overflow": "hidden",
            }
        )
    ):
        with a.div(
            # style=cohost.style({})
            style=cohost.style({"transform": "rotate(-30deg) translateX(-170px) scale(0.8)"})
        ):
            n = 20
            d = 1.2
            for i in range(n):
                particle(
                    a,
                    endx=300 + random.uniform(-20, 20),
                    endy=random.uniform(-30, 30),
                    duration=d,
                    delay=i * d / n,
                    sizex=180,
                    sizey=100,
                    startx=80,
                    starty=150,
                    background="red",
                )

            shake(
                a,
                lambda: static_particle(
                    a,
                    sizex=185,
                    sizey=105,
                    startx=90,
                    starty=150,
                    background="red",
                ),
                factor=0.5,
            )
            n = 20
            for i in range(n):
                particle(
                    a,
                    endx=70 + random.uniform(-20, 90),
                    endy=random.uniform(-15, 15),
                    duration=1,
                    delay=i * 1 / n,
                    sizex=80,
                    startx=80,
                    starty=150,
                    background="orange",
                )
            shake(
                a,
                lambda: static_particle(
                    a,
                    sizex=90,
                    sizey=55,
                    startx=60,
                    starty=150,
                    background="orange",
                ),
                factor=0.2,
            )

            rate = 0.2
            negative(a, 10, rate, starty=60, endy=120)
            negative(a, 9, rate, starty=60, endy=120, offset=0.5)
            negative(a, 10, rate, starty=230, endy=-120)
            negative(a, 9, rate, starty=230, endy=-120, offset=0.5)

            shake(a, lambda: eggbug(a), factor=0.6)


def eggbug(a):
    with a.div(
        style=cohost.style(
            {
                "transform": "translateX(-60px) translateY(15px) scale(0.2) rotate(20deg)",
            }
        )
    ):
        a.img(src=eggbug_logo, style=cohost.style({"margin": "0px"}))


def negative(a, n, rate, offset=0, starty=250, endy=-180):
    for i in range(n):
        particle(
            a,
            endx=400 + random.uniform(-20, 100),
            endy=endy + random.uniform(-60, 60),
            duration=rate * n,
            delay=(i + offset) * rate,
            sizex=90 + random.uniform(-30, 30),
            sizey=40,
            startx=120,
            starty=starty + random.uniform(-20, 20),
            background="black",
            end_scale=0.3,
        )


def particle(
    a,
    startx=0,
    starty=0,
    endx=0,
    endy=0,
    sizex=50,
    sizey=50,
    duration=1,
    delay=0,
    background="white",
    end_scale=0.01,
):
    with a.div(
        style=cohost.style(
            {
                "transform": f"translateX({startx-sizex / 2:.0f}px) translateY({starty - sizey / 2:.0f}px)"
            }
        )
    ):
        with a.div(
            style=cohost.style(
                {
                    "transform": f"translateX({endx:.0f}px) translateY({endy + sizey / 2:.0f}px) scale({end_scale})"
                }
                | cohost.animation(
                    direction="reverse",
                    duration=duration,
                    delay="{:.2f}".format(delay),
                    easing="linear",
                )
            )
        ):
            with a.div(
                style=cohost.style(
                    {
                        "width": f"{sizex}px",
                        "height": f"{sizey}px",
                        "position": "absolute",
                        "clip-path": f"ellipse({sizex / 2}px {sizey / 2}px)",
                        "background": background,
                    }
                )
            ):
                pass


def static_particle(
    a,
    startx=0,
    starty=0,
    sizex=50,
    sizey=50,
    background="white",
):
    with a.div(
        style=cohost.style(
            {
                "transform": f"translateX({startx-sizex / 2:.0f}px) translateY({starty - sizey / 2:.0f}px)"
            }
        )
    ):
        with a.div(
            style=cohost.style(
                {
                    "width": f"{sizex}px",
                    "height": f"{sizey}px",
                    "position": "absolute",
                    "clip-path": f"ellipse({sizex / 2}px {sizey / 2}px)",
                    "background": background,
                }
            )
        ):
            pass


def shake(a, content, factor=1):
    dx1 = 10 * factor
    dy1 = 8 * factor
    with a.div(
        style=cohost.style(
            {"position": "absolute", "transform": f"translateX({dx1}px)"}
            | cohost.animation(
                easing="steps(5, end)", duration=0.023, delay=random.uniform(-1, 0)
            )
        )
    ):
        with a.div(
            style=cohost.style(
                {"transform": f"translateX(-{dx1}px)"}
                | cohost.animation(
                    easing="steps(3, end)", duration=0.01, delay=random.uniform(-1, 0)
                )
            )
        ):
            with a.div(
                style=cohost.style(
                    {"transform": f"translateY({dy1}px)"}
                    | cohost.animation(
                        easing="steps(3, end)",
                        duration=0.027,
                        delay=random.uniform(-1, 0),
                    )
                )
            ):
                with a.div(
                    style=cohost.style(
                        {"transform": f"translateY(-{dy1}px)"}
                        | cohost.animation(
                            easing="steps(3, end)",
                            duration=0.01,
                            delay=random.uniform(-1, 0),
                        )
                    )
                ):
                    content()


cohost.create_document(body, "post.html")
