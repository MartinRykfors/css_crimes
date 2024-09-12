import random
from airium import Airium
import lib.cohost as cohost


def body(a):
    description = """A grid of circles can be seen. Inside each circle are two glowing, cuved lines.
    The circles are animated to rotate so that the lines inside the circles line up with the ones
    in the neighboring circles, creating an ever shifting geometrical pattern of squiggles."""
    cohost.with_description(a, content, description, "crime")


def content(a):
    n = 6
    with a.div(
        style=cohost.style(
            {
                # "width": "600px",
                "width": "100%",
                "background-color": "hsl(20 100% 5%)",
                "display": "grid",
                "grid-template-columns": f"repeat({n}, 1fr)",
                "grid-template-rows": f"repeat({n}, 1fr)",
            }
        )
    ):
        for i in range(n):
            for j in range(n):
                element(a, i, j)


def element(a, i, j):
    with a.div(
        style=cohost.style(
            {
                "grid-column": f"{i + 1} / span 1",
                "grid-row": f"{j + 1} / span 1",
                "width": "100%",
                "background-color": "black",
                "display": "grid",
                "grid-template-columns": f"1fr",
                "grid-template-rows": f"1fr",
                "border-radius": "100px",
                "transform": "scale(1) rotate(90deg)",
                # "filter": "drop-shadow(0px 0px 6px hsl(200 100% 30%))",
            }
            | cohost.animation(
                easing="cubic-bezier(.84,0,.15,.99)",
                duration=random.uniform(4.6, 5.5),
                delay=random.uniform(0, 8),
            )
        )
    ):
        lines(a, 30, f"hsl({i * 10 + j * 10 + 200} 80% 50%)", 10)
        lines(a, 8, "hsl(180 50% 100%)", 1)


def lines(a, thickness, line_color, blur):
    with a.div(
        style=cohost.style(
            {
                "grid-column": "1 / span 1",
                "grid-row": "1 / span 1",
                "aspect-ratio": "1 / 1",
                "display": "grid",
                "grid-template-columns": f"1fr {thickness}px 1fr",
                "grid-template-rows": f"1fr {thickness}px 1fr",
            }
        )
    ):
        with a.div(
            style=cohost.style(
                {
                    "grid-column": "1 / span 2",
                    "grid-row": "1 / span 2",
                    "width": "100%",
                    "height": "100%",
                    "border-bottom-right-radius": "5000px",
                    "border-bottom-width": f"{thickness}px",
                    "border-bottom-style": "solid",
                    "border-bottom-color": line_color,
                    "border-right-width": f"{thickness}px",
                    "border-right-style": "solid",
                    "border-right-color": line_color,
                    "filter": f"blur({blur}px)",
                }
            )
        ):
            pass
        with a.div(
            style=cohost.style(
                {
                    "grid-column": "2 / span 2",
                    "grid-row": "2 / span 2",
                    "width": "100%",
                    "height": "100%",
                    "border-top-left-radius": "5000px",
                    "border-top-width": f"{thickness}px",
                    "border-top-style": "solid",
                    "border-top-color": line_color,
                    "border-left-width": f"{thickness}px",
                    "border-left-style": "solid",
                    "border-left-color": line_color,
                    "filter": f"blur({blur}px)",
                }
            )
        ):
            pass


cohost.create_document(body, "post.html")
