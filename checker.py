import lib.cohost as cohost


def body(a):
    description = (
        "A checkerboard of pink and purple squares. In every corner between the squares "
        "a smaller 2 by 2 checkerboard is present, rotated 45 degrees. This creates the impression "
        "that the checkerboard is divided into square regions that are counter-rotated "
        "with respect to one another. "
    )
    cohost.with_description(a, illusion, description, "lilac")


def illusion(a):
    checker(a)
    a(
        (
            "The checkerboard is made out of straight rows and columns, yet they appear crooked."
        )
    )


big_colors = ["#f792fc", "#51026e"]
small_colors = ["white", "black"]


def checker(a):
    n = 13
    with a.div(
        style=cohost.style(
            {
                "max-width": "400px",
                "display": "flex",
                "aspect-ratio": "1 / 1",
                "filter": "blur(1px)",
                "margin": "auto",
            }
        )
    ):
        with a.div(
            style=(
                f"display: grid; "
                f"grid-template-columns: repeat({n}, 1fr 3fr 1fr); "
                f"grid-template-rows: repeat({n}, 1fr 3fr 1fr);"
                f"grid-gap: 0px;"
                f"flex-grow: 1;"
            )
        ):
            for i in range(1, n * 3, 3):
                for j in range(1, n * 3, 3):
                    color = big_colors[(i + j) % 2]
                    background = f"background-color: {color};"
                    if i in [1, n * 3 - 2] or j in [1, n * 3 - 2]:
                        background = ""
                    a.div(
                        style=(
                            f"grid-row: {i} / span 3;"
                            f"grid-column: {j} / span 3;"
                            f"flex-grow: 1;"
                            f"{background}"
                        )
                    )

            for i in range(3, n * 3, 3):
                for j in range(3, n * 3, 3):
                    p = ((i - 3) // 12) % 2
                    q = ((j - 3) // 12) % 2
                    rot = 45 if (((i + j) // 3) + p + q) % 2 else -45
                    with a.div(
                        style=(
                            f"grid-row: {i} / span 2;"
                            f"grid-column: {j} / span 2;"
                            f"display: flex;"
                        )
                    ):
                        duration = 2
                        delay = 0.008 * j
                        curve = "cubic-bezier(.97,-0.07,.06,1.09)"
                        angle = 90 if (p + q) % 2 else -90
                        animation = (
                            f"animation: {duration}s {curve} {delay}s infinite alternate none running spin;"
                            f"transform: scale(-1, -1) rotate({angle}deg);"
                        )
                        with a.div(
                            style=(f"display: flex;" f"flex-grow: 1;" f"{animation}")
                        ):
                            with a.div(
                                style=(
                                    f"display: grid; "
                                    f"grid-template-columns: 1fr 1fr; "
                                    f"grid-template-rows: 1fr 1fr"
                                    f"grid-gap: 0px;"
                                    f"flex-grow: 1;"
                                    f"transform: rotate({rot}deg)"
                                )
                            ):
                                small_checker(a)


def small_checker(a):
    for k in [1, 2]:
        for l in [1, 2]:
            color = small_colors[(k + l) % 2]
            a.div(
                style=(
                    f"grid-row: {k} / span 1;"
                    f"grid-column: {l} / span 1;"
                    f"height: 100%; width: 100%;"
                    f"background-color: {color};"
                )
            )


cohost.create_document(body, "post.html")
