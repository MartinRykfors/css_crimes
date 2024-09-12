from airium import Airium
import png
import lib.cohost as cohost

a = Airium(base_indent="")

light_shade = "#aaaaaa"
dark_shade = "#3a3a3a"

shade = 30
alpha = 0.8
size = 8
duration = 15

gradient1 = [
    0,
    35,
    50,
    85,
    100,
]

gradient2 = [
    0,
    48,
    50,
    85,
    87,
]


def body(a):
    cohost.promo_tag(a)
    a(("The squares labeled A and B are both the same shade of gray."))
    a.br()
    illusion(a, gradient1)
    with a.b():
        a("Note:")
    a(
        (
            "I am very much relying on different browsers rendering color blending the same way! "
            "I have verified that the colors are the same on Firefox and Chromium at least."
        )
    )


def illusion(a, gradient):
    with a.div(
        style=cohost.style(
            {
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
                    "max-width": "500px",
                }
            )
        ):
            checkerboard(a, checker)
        with a.div(
            style=cohost.style(
                {
                    "grid-column": "1 / span 1",
                    "grid-row": "1 / span 1",
                    "background": "linear-gradient({})".format(
                        ",".join(
                            [
                                f"rgba({shade}, {shade}, {shade}, 0) {gradient[0]}%",
                                f"rgba({shade}, {shade}, {shade}, 0) {gradient[1]}%",
                                f"rgba({shade}, {shade}, {shade}, {alpha}) {gradient[2]}%",
                                f"rgba({shade}, {shade}, {shade}, {alpha}) {gradient[3]}%",
                                f"rgba({shade}, {shade}, {shade}, 0) {gradient[4]}%",
                            ]
                        )
                    ),
                    "z-index": 1,
                    # "transform": "perspective(300px) rotateY(20deg)",
                    "width": "1000px",
                }
            )
        ):
            pass
        with a.div(
            style=cohost.style(
                {
                    "grid-column": "1 / span 1",
                    "grid-row": "1 / span 1",
                    "max-width": "500px",
                    "z-index": 2,
                }
            )
        ):
            checkerboard(a, annotation)
        with a.div(
            style=cohost.style(
                {
                    "grid-column": "1 / span 1",
                    "grid-row": "1 / span 1",
                    "max-width": "500px",
                    "z-index": 2,
                    "transform": "scale(0%)",
                    "display": "grid",
                    "grid-template-columns": "1fr",
                    "grid-template-rows": "1fr",
                }
                | cohost.animation(
                    easing="steps(2, jump-none)",
                    duration=duration / 2,
                    direction="normal",
                )
            )
        ):
            with a.div(
                style=cohost.style(
                    {
                        "transform": "scale(0%)",
                        "grid-column": "1 / span 1",
                        "grid-row": "1 / span 1",
                        "z-index": 2,
                    }
                    | cohost.animation(
                        easing="steps(2, jump-none)",
                        duration=duration,
                        direction="normal",
                    )
                )
            ):
                checkerboard(a, mask)
            with a.div(
                style=cohost.style(
                    {
                        "transform": "scale(0%)",
                        "grid-column": "1 / span 1",
                        "grid-row": "1 / span 1",
                        "z-index": 2,
                    }
                    | cohost.animation(
                        easing="steps(2, jump-none)",
                        duration=duration,
                        direction="normal",
                        delay=duration / 2,
                    )
                )
            ):
                checkerboard(a, path)




def checkerboard(a, content_fun):
    with a.div(
        style=cohost.style(
            {
                "transform": "rotate(40deg) skew(-0.5rad)",
                "width": "50%",
                "margin": "auto",
            }
        )
    ):
        with a.div(
            style=cohost.style(
                {
                    "display": "grid",
                    "grid-template-columns": f"repeat({size}, 1fr)",
                    "grid-template-rows": f"repeat({size}, 1fr)",
                    "aspect-ratio": 1,
                }
            )
        ):
            for i in range(1, size + 1):
                for j in range(1, size + 1):
                    content_fun(a, i, j)


def checker(a, i, j):
    color = dark_shade if (i + j) % 2 else light_shade
    with a.div(
        style=cohost.style(
            {
                "grid-column": f"{j} / span 1",
                "grid-row": f"{i} / span 1",
                "background-color": color,
            }
        )
    ):
        pass


def annotation(a, i, j):
    with a.div(
        style=cohost.style(
            {
                "grid-column": f"{j} / span 1",
                "grid-row": f"{i} / span 1",
                "display": "flex",
                "justify-content": "center",
                "align-items": "center",
            }
        )
    ):
        if (i, j) == (3, 2):
            with a.span(
                style=cohost.style(
                    {
                        "font-size": "0.7em",
                        "color": "#bbbbbb",
                    }
                )
            ):
                a("A")
        if (i, j) == (6, 6):
            with a.span(
                style=cohost.style(
                    {
                        "font-size": "0.7em",
                        "color": "#bbbbbb",
                    }
                )
            ):
                a("B")


def mask(a, i, j):
    if (i, j) == (3, 2):
        return
    if (i, j) == (6, 6):
        return
    a.div(
        style=cohost.style(
            {
                "grid-column": f"{j} / span 1",
                "grid-row": f"{i} / span 1",
                "background-color": "grey",
            }
        )
    )


def path(a, i, j):
    if (i, j) in [(3, 3), (4, 3), (4, 4), (5, 4), (5, 5), (6, 5)]:
        a.div(
            style=cohost.style(
                {
                    "grid-column": f"{j} / span 1",
                    "grid-row": f"{i} / span 1",
                    "background-color": dark_shade,
                }
            )
        )


cohost.create_document(body, "post.html")
