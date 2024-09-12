from airium import Airium
import lib.cohost as cohost

a = Airium(base_indent="")

num_bars = 60
element_width = 10
duration = 10
translate = 400


def body(a):
    cohost.promo_tag(a)
    a(
        (
            "The blue and yellow blocks seem to move forward in a stepping motion, "
            "but they are in fact moving side by side with a constant speed."
        )
    )
    a.br()
    a(
        (
            "The effect becomes stronger if you focus on a fixed point (the + sign) instead of following "
            "the blocks with your eyes."
        )
    )
    cohost.with_description(
        a,
        illusion,
        (
            "A series of vertical black and white bars can be seen. "
            "A blue and yellow rectangle are moving back and forth across the bars. "
            "This creates an optical illusion that the two blocks are moving like two stepping feet, "
            "but they are in fact moving with a constant speed."
        ),
        "lockstep",
    )


def illusion(a):
    with a.div(
        style=cohost.style(
            {
                "display": "inline-grid",
                "grid-template-columns": "1fr",
                "grid-template-rows": "1fr",
            }
        )
    ):
        with a.div(
            style=cohost.style({"grid-column": "1 / span 1", "grid-row": "1 / span 1"})
        ):
            bars(a, num_bars)
        with a.div(
            style=cohost.style({"grid-column": "1 / span 1", "grid-row": "1 / span 1"})
        ):
            feet(a, num_bars)


def bars(a, num_bars):
    with a.div(
        style=cohost.style(
            {
                "display": "grid",
                "grid-template-columns": f"repeat({num_bars} {element_width}px)",
                "grid-template-rows": "1fr",
                "height": "100px",
            }
        )
    ):
        for i in range(1, num_bars + 1):
            color = "black" if i % 2 else "white"
            a.div(
                style=cohost.style(
                    {
                        "background-color": color,
                        "grid-column": f"{i} / span 1",
                        "grid-row": "1 / span 1",
                        "width": f"{element_width}px",
                    }
                )
            )
        with a.div(
            style=cohost.style(
                {
                    "background-color": "gray",
                    "grid-column": "14 / span 3",
                    "grid-row": "1 / span 1",
                    'display': 'flex',
                    'justify-content': 'center',
                    'align-items': 'center'
                }
            )
        ):
            with a.p(style=f"text-align: center"):
                a("+")


def feet(a, num_bars):
    with a.div(
        style=cohost.style(
            {"transform": f"translateX({translate}px)"}
            | cohost.animation(duration=duration)
        )
    ):
        with a.div(
            style=cohost.style(
                {
                    "display": "grid",
                    "grid-template-columns": f"repeat({num_bars} {element_width}px)",
                    "grid-template-rows": "repeat(5 1fr)",
                    "height": "100px",
                }
            )
        ):
            a.div(
                style=cohost.style(
                    {
                        "background-color": "blue",
                        "grid-column": "2 / span 2",
                        "grid-row": "2 / span 1",
                    }
                )
            )
            a.div(
                style=cohost.style(
                    {
                        "background-color": "yellow",
                        "grid-column": "2 / span 2",
                        "grid-row": "4 / span 1",
                    }
                )
            )
            a.div(
                style=cohost.style(
                    {
                        "grid-column": f"1 / span {num_bars}",
                        "grid-row": "1 / span 5",
                    }
                )
            )


cohost.create_document(body, "post.html")
