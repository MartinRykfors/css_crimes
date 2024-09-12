import random
from airium import Airium
import lib.cohost as cohost


def body(a):
    description = """Description"""
    cohost.with_description(a, content, description, "crime")


def content(a):
    with a.div(style=cohost.style({"height": "580px"})):
        with a.div(
            style=cohost.style(
                {
                    "position": "absolute",
                    "top": "100px",
                    "height": "0px",
                }
            )
        ):
            gadget(a)


def gadget(a):
    with a.div(
        style=cohost.style(
            {
                "position": "absolute",
                "height": "400px",
                "width": "400px",
                "background-color": "black",
                "padding": "40px",
            }
        )
    ):
        with a.div(
            style=cohost.style(
                {
                    "height": "100%",
                    "width": "100%",
                    "background-color": "#880000",
                    "border-radius": "20px",
                    "display": "grid",
                    "grid-template-columns": "1fr",
                    "grid-template-rows": "1fr",
                }
            )
        ):
            with a.div(
                style=cohost.style(
                    {
                        "grid-column": "1 / span 1",
                        "grid-row": "1 / span 1",
                        "display": "flex",
                        "justify-content": "center",
                        "align-items": "center",
                        "font-size": "2rem",
                        "color": "hsl(60 80% 70%)",
                        "filter": """
                            drop-shadow(0px  2px 10px hsl(20 100% 35%))
                            drop-shadow(0px -2px 10px hsl(20 100% 35%))
                            drop-shadow(2px  0px 10px hsl(20 100% 35%))
                            drop-shadow(-2px 0px 10px hsl(20 100% 35%))
                            """,
                    }
                )
            ):
                with a.div(style=cohost.style({'transform': 'scale(0)'} | cohost.animation(easing='steps(2, jump-none)'))):
                    with a.div(style=cohost.style({"display": "flex", 'flex-direction': 'column', 'gap': '5px'})):
                        with a.div(style=cohost.style({"display": "flex", 'gap': '5px'})):
                            for d in ["bcd", "bcdef", "afgcd", "fged"]:
                                directive = segment_display_directive(d, 60, 100)
                                with a.div(
                                    style=cohost.style(
                                        {
                                            # "border": "1px solid hsl(60 80% 80%)",
                                        }
                                    )
                                ):
                                    with a.div(
                                        style=cohost.style(
                                            {
                                                "height": "100px",
                                                "width": "60px",
                                                "background-color": "hsl(60 80% 70%)",
                                                "clip-path": f"path('{directive}')",
                                                "color": "2px solid hsl(60 80% 80%)",
                                                "font-family": "monospace",
                                            }
                                        )
                                    ):
                                        pass
                                        # a('hello')
                        with a.div(style=cohost.style({"display": "flex", 'gap': '5px'})):
                            for d in ["afbeg", "abcdef", "afgcd", "fged"]:
                                directive = segment_display_directive(d, 60, 100)
                                with a.div(
                                    style=cohost.style(
                                        {
                                            # "border": "1px solid hsl(60 80% 80%)",
                                        }
                                    )
                                ):
                                    with a.div(
                                        style=cohost.style(
                                            {
                                                "height": "100px",
                                                "width": "60px",
                                                "background-color": "hsl(60 80% 70%)",
                                                "clip-path": f"path('{directive}')",
                                                "color": "2px solid hsl(60 80% 80%)",
                                                "font-family": "monospace",
                                            }
                                        )
                                    ):
                                        pass
                                        # a('hello')
            with a.div(
                style=cohost.style(
                    {
                        "grid-column": "1 / span 1",
                        "grid-row": "1 / span 1",
                        "box-shadow": "inset 0px 0px 50px hsl(0 50% 20%)",
                        "mix-blend-mode": "multiply",
                        "pointer-events": "none",
                    }
                )
            ):
                pass


def segment_display_directive(segments, ww, hh, ss=0.2):
    s = 0.3
    h = 8
    w = 8
    sf = vertical_segment_points(0, 1 + s, 2, h - s * 2)
    sb = vertical_segment_points(w, 1 + s, 2, h - s * 2)
    se = vertical_segment_points(0, h + 1 + s, 2, h - s * 2)
    sc = vertical_segment_points(w, h + 1 + s, 2, h - s * 2)

    sa = horizontal_segment_points(1 + s, 0, w - s * 2, 2)
    sg = horizontal_segment_points(1 + s, h * 1, w - s * 2, 2)
    sd = horizontal_segment_points(1 + s, h * 2, w - s * 2, 2)
    d = {"a": sa, "b": sb, "c": sc, "d": sd, "e": se, "f": sf, "g": sg}
    ps = map(lambda c: d[c], segments)
    trf = lambda p: (p[0] * ww / (w + 2 + s * 2), p[1] * hh / (2 * h + 2 + s * 2))
    return "{}z".format(" ".join([make_directive(s, trf) for s in ps]))


def make_directive(points, trf):
    return "M {} ".format(
        " L ".join(["{:.0f} {:.0f}".format(x, y) for (x, y) in map(trf, points)])
    )


def vertical_segment_points(l, t, w, h):
    points = [
        (w / 2, 0),
        (w, w / 2),
        (w, h - w / 2),
        (w / 2, h),
        (0, h - w / 2),
        (0, w / 2),
    ]
    return [(x + l, y + t) for (x, y) in points]


def horizontal_segment_points(l, t, w, h):
    points = [
        (0, h / 2),
        (h / 2, h),
        (w - h / 2, h),
        (w, h / 2),
        (w - h / 2, 0),
        (h / 2, 0),
    ]
    return [(x + l, y + t) for (x, y) in points]


cohost.create_document(body, "post.html")
