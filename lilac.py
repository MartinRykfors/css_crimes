import random
import lib.cohost as cohost


def body(a):
    description = (
        "A grid of blurry colored dots can be seen. The dots are animated "
        "so that they periodically disappear and reappear quickly. A small black dot "
        "is present in the center of the grid. By staring on the black dot "
        "the colored dots seem to vanish and are replaced by a dot that periodically "
        "flashes with the opposite color of the original dot."
    )
    cohost.with_description(a, illusions, description, "lilac")
    a("Alternative variants under the fold for browsers that do not support the animations above:")
    a("")
    a("---")
    a("")
    illusion(a, "#d2d2d2", "cubic-bezier(.07,-0.41,0,1.65)")
    illusion(a, "#707070", "cubic-bezier(.07,-0.41,0,1.65)")


def illusions(a):
    with a.div(
        style=cohost.style({"border": "1px solid", "background-color": "orange"})
    ):
        a(
            (
                "⚠️ This CSS crime uses easing functions not supported by some browsers. "
                "If the black square below does not move, please expand the post to see "
                "an alternative version that should work with all browsers."
            )
        )

        a.div(
            style=cohost.style(
                {
                    "animation": "1s linear(0, 0, 1, 1) infinite alternate none running spin",
                    "transform": "translateX(40px)",
                    "width": "20px",
                    "height": "20px",
                    "background-color": "black",
                    # 'margin': 'auto',
                }
            )
        )
    a.br()
    a(
        (
            "Stare at the dot in the center without shifting your gaze. Eventually "
            "the colored dots should seem to vanish and be replaced by "
            "periodic flashing of the original dot's opposite color."
        )
    )
    a.br()
    a(
        (
            "I find it that the illusion appears quicker and more reliably if I view it "
            "with one eye closed. Your mileage may vary."
        )
    )
    a.div(style=cohost.style({"height": "50px"}))
    illusion(a, "#d2d2d2", "linear(0, 0 10%, 1 1%, 1)")
    a(
        (
            "In the dark variant, the dots end up losing their color and "
            "start flashing with a dark color. The RGB values of the dots are "
            "the same as in the light version."
        )
    )
    a.div(style=cohost.style({"height": "50px"}))
    illusion(a, "#707070", "linear(0, 0 10%, 1 1%, 1)")


def illusion(a, background, curve):
    blur = 8
    with a.div(
        style=f"display:grid; grid-template-columns: 1fr; grid-template-rows: 1fr;margin:auto; margin-bottom: 50px; max-width: 500px"
    ):
        with a.div(
            style=(
                f"grid-column: 1/span 1; grid-row: 1/span 1; z-index: 3;"
                f"display: flex; justify-content: center; align-items: center"
            )
        ):
            with a.p(style=f"text-align: center"):
                a(".")

        with a.div(
            style=(
                f"filter: blur({blur}px); background-color: {background}; grid-column: 1/span 1; grid-row: 1/span 1;"
                f"width: 100%; "
                f"aspect-ratio: 1 / 1;"
                f"display: flex;"
            )
        ):
            with a.div(
                style=(
                    f"display: grid; "
                    f"grid-template-columns: repeat(11, 1fr); "
                    f"grid-template-rows: repeat(11, 1fr);"
                    f"grid-gap: 0px;"
                    f"flex-grow: 1;"
                )
            ):
                for i in range(2, 11, 2):
                    for j in range(2, 11, 2):
                        if i == 6 and j == 6:
                            continue
                        dot(a, curve, i, j)


def dot(a, curve, i, j):
    # curve = "cubic-bezier(.08,1.05,0,1.03)"
    # curve = "linear(0, 0 10%, 1 1%, 1)"
    duration = 1 + random.random() * 1
    duration = duration * 2
    delay = random.random() * duration - 4
    animation = f"animation: {duration}s {curve} {delay}s infinite none running spin; transform: scale(1%);"
    colors = ["#6bbbd6", "#f59ddf", "#79cf70", "#cfb470"]
    color = colors[int(random.random() * len(colors))]
    color = colors[(i + j) // 2 % len(colors)]
    with a.div(style=f"grid-column: {j}/span 1; grid-row: {i}/span 1; display: flex;"):
        a.div(
            style=(
                f"{animation} background-color: {color};"
                f"flex-grow:1; border-radius: 100px"
            )
        )


cohost.create_document(body, "post.html")
