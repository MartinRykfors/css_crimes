from airium import Airium
import lib.cohost as cohost

a = Airium(base_indent="")

button_width = 100
button_height = 50
button_top = 50
button_left = 20
button_spacing = 130
illusion_top = 150


def body(a):
    cohost.promo_tag(a)
    with a.div(
        style="isplay:flex; flex-direction:row; background-color: rgb(250 216 214); border-radius:0.5rem; color:rgb(34 0 16); padding: 0.75rem; gap: 1rem; align-items:center;align-self:stretch;box-sizing:border-box; width:100%; margin-top:0.75rem; margin-bottom:0.75rem; line-height:1.5"
    ):
        with a.div(
            style="width: 1.5rem; height: 1.5rem; flex-shrink:0; align-self:flex-start; background-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdCb3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0icmdiKDIyOSwgMTA3LCAxMTEpIiBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InctNiBzZWxmLXN0YXJ0IHRleHQtc3RyYXdiZXJyeSI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNMTIgOXYzLjc1bS05LjMwMyAzLjM3NmMtLjg2NiAxLjUuMjE3IDMuMzc0IDEuOTQ4IDMuMzc0aDE0LjcxYzEuNzMgMCAyLjgxMy0xLjg3NCAxLjk0OC0zLjM3NEwxMy45NDkgMy4zNzhjLS44NjYtMS41LTMuMDMyLTEuNS0zLjg5OCAwTDIuNjk3IDE2LjEyNnpNMTIgMTUuNzVoLjAwN3YuMDA4SDEydi0uMDA4eiI+PC9wYXRoPjwvc3ZnPgo=)"
        ):
            pass
        with a.div():
            with a.p(style="margin:0"):
                with a.b():
                    a('Warning: Flashing imagery.')
                a("Pressing the buttons below will cause a rapidly flashing animation to play.")

    a(
        (
            "When the figure below is spinning, it is possible to start perceiving colors in it, even though it is just a grayscale image. "
            "Press the buttons to spin the figure with different speeds!"
        )
    )

    description = "description"

    with a.div(style=cohost.style({"height": "800px", "max-width": "500px", "width": "100%"})):
        with a.div(
            style=cohost.style(
                {
                    "height": "800px",
                    "position": "absolute",
                    "width": "100%",
                    "max-width": "500px",
                }
            )
        ):
            cohost.with_description(a, illusion, description, "spinny")
    a('')
    a('---')
    a('')
    a(
        (
            (
                "I am interested to hear what colors (if any) you can see. Supposedly this illusion varies quite a bit between how different people perceive it. "
                "It is also possible that this could be caused by some display artifact in the screen you are using, in which case this is not really a true optical illusion. "
                "Ideally, this figure should be printed on paper and spun in real life to make the illusion accurate!"
            )
        )
    )


def illusion(a):
    with a.div(
        style=cohost.style(
            {"position": "absolute", "top": "0px", "width": "100%", "aspect-ratio": 1}
        )
    ):
        player(a, 0.5, 1, "slow")
        player(a, 0.3, 2, "medium")
        player(a, 0.2, 3, "fast")

    with a.div(
        style=cohost.style(
            {
                "position": "absolute",
                "top": f"{illusion_top}px",
                "width": "100%",
                "z-index": -1,
                "aspect-ratio": 1,
            }
        )
    ):
        spinny_disk(a, 60, False)

    # with a.div(style=cohost.style({"height": f"{illusion_top}px"})):
    #     pass
    # with a.div(style=cohost.style({"width": "100%", "aspect-ratio": 1})):
    #     pass
    # a('hello')


def get_button_left(index):
    return button_left + (index - 1) * button_spacing


def player(a, duration, index, name):
    with a.details():
        with a.summary(style=cohost.style({"font-size": 0})):
            left = get_button_left(index)
            with a.a():
                with a.div(
                    style=cohost.style(
                        {
                            "width": f"{button_width}px",
                            "height": f"{button_height}px",
                            "left": f"{left}px",
                            "top": f"{button_top}px",
                            "background-color": "green",
                            "position": "absolute",
                            "font-size": "1.5rem",
                            "z-index": 1,
                            "display": "flex",
                            "justify-content": "center",
                            "align-items": "center",
                        }
                    )
                ):
                    a(name)
        for _index in range(1, 4):
            if _index != index:
                left = get_button_left(_index)
                a.div(
                    style=cohost.style(
                        {
                            "width": f"{button_width}px",
                            "height": f"{button_height}px",
                            "left": f"{left}px",
                            "top": f"{button_top}px",
                            "background-color": "gray",
                            "position": "absolute",
                            "font-size": "1.5rem",
                            "z-index": 2,
                        }
                    )
                )
        left = get_button_left(index)
        with a.a(
            style=cohost.style(
                {
                    "pointer-events": "none",
                    "width": f"{button_width}px",
                    "height": f"{button_height}px",
                    "background-color": "red",
                    "left": f"{left}px",
                    "top": f"{button_top}px",
                    "position": "absolute",
                    "z-index": 2,
                    "display": "flex",
                    "justify-content": "center",
                    "align-items": "center",
                }
            )
        ):
            a("stop")
        with a.div(
            style=cohost.style(
                {"top": f"{illusion_top}px", "position": "absolute", "width": "100%"}
            )
        ):
            spinny_disk(a, duration, True)


def spinny_disk(a, duration, animate):
    with a.div(style=cohost.style({"width": "100%", "background-color": "white"})):
        with a.div(
            style=cohost.style(
                {
                    "width": "100%",
                    "aspect-ratio": 1,
                    "filter": "blur(2px)",
                }
                | (
                    cohost.animation(direction="normal", duration=duration)
                    if animate
                    else {}
                )
            )
        ):
            disc(a, True)


def disc(a, block):
    with a.div(
        style=cohost.style(
            {
                "display": "grid",
                "grid-template": "1fr 1fr / 1fr 1fr",
                "width": "100%",
                "height": "100%",
            }
        )
    ):
        if block:
            blocker(a)

        for i in range(4):
            start_deg = 270 + i * 45
            start_radius = 100 - i * 20
            for j in range(4):
                radius = start_radius - 20 / 4 * j
                arc(a, radius, 45, start_deg, 1.5)


def blocker(a):
    with a.div(
        style=cohost.style(
            {
                "grid-row": "2 / span 1",
                "grid-column": "1 / span 2",
                "overflow": "hidden",
                "position": "relative",
                "z-index": 4,
            }
        )
    ):
        a.div(
            style=cohost.style(
                {
                    "background-color": "black",
                    "border-radius": "100%",
                    "height": "200%",
                    "width": "100%",
                    "position": "absolute",
                    "top": "-100%",
                }
            )
        )


def arc(a, radius, span_deg, start_deg, width):
    start_deg = start_deg % 360
    with a.div(
        style=cohost.style(
            {
                "grid-row": "1 / span 2",
                "grid-column": "1 / span 2",
                "z-index": 2,
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
                    "display": "flex",
                    "align-items": "center",
                    "justify-content": "center",
                }
            )
        ):
            with a.div(
                style=cohost.style(
                    {
                        "width": f"{radius}%",
                        "height": f"{radius}%",
                        "border-radius": "50%",
                        "background": f"conic-gradient(from {start_deg}deg, black {span_deg}deg, white {span_deg}deg)",
                    }
                )
            ):
                pass
        with a.div(
            style=cohost.style(
                {
                    "grid-row": "1 / span 1",
                    "grid-column": "1 / span 1",
                    "display": "flex",
                    "align-items": "center",
                    "justify-content": "center",
                }
            )
        ):
            with a.div(
                style=cohost.style(
                    {
                        "width": f"{radius - width}%",
                        "height": f"{radius - width}%",
                        "background-color": "white",
                        "border-radius": "50%",
                    }
                )
            ):
                pass


cohost.create_document(body, "post.html")
