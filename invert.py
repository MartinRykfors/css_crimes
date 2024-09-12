from airium import Airium
import lib.cohost as cohost

a = Airium(base_indent="")

assets_global = {
    "eggbug": "https://staging.cohostcdn.org/attachment/9067aef7-a63a-4b53-ab49-877ab1f452fa/eggbug.png",
    "landscape": "https://staging.cohostcdn.org/attachment/1a342c79-0fa3-450d-93ee-f5e176bbbab9/landscape.jpg",
}
assets_local = {"eggbug": "eggbug.png", "landscape": "landscape.jpg"}
assets = assets_global


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
                    a("Warning: Flashing imagery.")
                a(
                    "Pressing the play button on the image below will cause a rapidly flashing animation to play."
                )
    a(("Imagine Eggbug... flying over a field towards you... forever..."))
    cohost.with_description(
        a,
        play_button,
        (
            "An image of a landscape with an Eggbug overlaid. "
            "The landscape image and eggbug image are made to animate with a short, quick, movement. "
            "When the movement is completed, the colors of the image inverts and the motion restarts. "
            "This creates the illusion that Eggbug is always moving towards the viewer, yet it never actually changes position."
        ),
        "invert",
    )


def play_button(a):
    with a.div(style=cohost.style({"height": "600px"})):
        with a.div(style=cohost.style({"position": "absolute", "width": "100%"})):
            with a.details(open=""):
                with a.summary(style=cohost.style({"font-size": 0})):
                    with a.div(style=cohost.style({"position": "absolute"})):
                        animate(a, image, 0.8)
                with a.div(
                    style=cohost.style(
                        {
                            "display": "flex",
                            "justify-content": "center",
                            "pointer-events": "none",
                            "background-color": "white",
                        }
                    )
                ):
                    with a.div(
                        style=cohost.style(
                            {
                                "z-index": 1,
                            }
                        )
                    ):
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
                                        "grid-row": "1 / span 1",
                                        "grid-column": "1 / span 1",
                                    }
                                )
                            ):
                                animate_not(a)
                            with a.div(
                                style=cohost.style(
                                    {
                                        "grid-row": "1 / span 1",
                                        "grid-column": "1 / span 1",
                                        "display": "flex",
                                        "justify-content": "center",
                                        "align-items": "center",
                                        "z-index": 3,
                                    }
                                )
                            ):
                                play_icon(a)


def play_icon(a):
    with a.div(
        style=cohost.style(
            {
                "width": "74px",
                "height": "74px",
                "box-sizing": "border-box",
                "border-color": "transparent transparent transparent #00ff88",
                "border-style": "solid",
                "border-width": "37px 0px 37px 74px",
                "margin-top": "30px",
            }
        )
    ):
        pass


def animate(a, image, duration):
    with a.div(
        style=cohost.style(
            {
                "display": "inline-grid",
                "grid-template-columns": "20px 20px 1fr 20px 20px",
                "grid-template-rows": "10px 1fr 10px",
                "margin": "20px",
            }
        )
    ):
        with a.div(
            style=cohost.style(
                {
                    "grid-row": "2 / span 1",
                    "grid-column": "2 / span 3",
                    "filter": "invert(1)",
                    # "transform": "scale(0%)",
                    "z-index": -1,
                }
                # | cohost.animation(
                #     easing="steps(2, jump-none)", duration=duration, direction="normal"
                # )
            )
        ):
            image(a, duration, duration / 4)
        with a.div(
            style=cohost.style(
                {
                    "grid-row": "2 / span 1",
                    "grid-column": "2 / span 3",
                    "transform": "scale(0%)",
                }
                | cohost.animation(
                    easing="steps(2, jump-none)",
                    duration=duration,
                    direction="normal",
                    delay=duration / 2,
                )
            )
        ):
            image(a, duration, duration / 2 + duration / 4)
        a.div(
            style=cohost.style(
                {
                    "grid-row": "1 / span 3",
                    "grid-column": "1 / span 2",
                    "background": "rgb(255, 255, 255)",
                    "background": "linear-gradient(90deg, rgba(255,255,255,1) 70%, rgba(255,255,255,0) 100%);",
                    "z-index": 7,
                }
            )
        )
        a.div(
            style=cohost.style(
                {
                    "grid-row": "1 / span 3",
                    "grid-column": "4 / span 2",
                    "background": "rgb(255, 255, 255)",
                    "background": "linear-gradient(270deg, rgba(255,255,255,1) 70%, rgba(255,255,255,0) 100%);",
                    "z-index": 7,
                }
            )
        )


def image(a, duration, delay):
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
            style=cohost.style(
                {
                    "grid-row": "1 / span 1",
                    "grid-column": "1 / span 1",
                    "transform": "translateX(-8px)",
                    "filter": "blur(2px)",
                }
                | cohost.animation(duration, "linear", delay, "normal")
            )
        ):
            a.img(src=assets["landscape"], style=cohost.style({"margin": 0}))
        with a.div(
            style=cohost.style(
                {
                    "grid-row": "1 / span 1",
                    "grid-column": "1 / span 1",
                    "transform": "translateX(1px) translateY(7px) rotate(-2deg) scale(0.92)",
                    "display": "flex",
                    "justify-content": "center",
                    "align-items": "center",
                    "filter": "blur(2px)",
                }
                | cohost.animation(duration, "linear", delay, "normal")
            )
        ):
            with a.div(
                style=cohost.style(
                    {
                        "transform": "rotate(20deg)",
                        "display": "flex",
                        "justify-content": "center",
                        "align-items": "center",
                    }
                )
            ):
                a.img(
                    src=assets["eggbug"],
                    style=cohost.style({"width": "50%", "height": "50%", "margin": 0}),
                )


def static_image(a):
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
            style=cohost.style(
                {
                    "grid-row": "1 / span 1",
                    "grid-column": "1 / span 1",
                    "transform": "translateX(-8px)",
                    "filter": "blur(2px)",
                }
            )
        ):
            a.img(src=assets["landscape"], style=cohost.style({"margin": 0}))

        with a.div(
            style=cohost.style(
                {
                    "grid-row": "1 / span 1",
                    "grid-column": "1 / span 1",
                    "transform": "translateX(1px) translateY(7px) rotate(-2deg) scale(0.92)",
                    "display": "flex",
                    "justify-content": "center",
                    "align-items": "center",
                    "filter": "blur(2px)",
                }
            )
        ):
            with a.div(
                style=cohost.style(
                    {
                        "transform": "rotate(20deg)",
                        "display": "flex",
                        "justify-content": "center",
                        "align-items": "center",
                    }
                )
            ):
                a.img(
                    src=assets["eggbug"],
                    style=cohost.style({"width": "50%", "height": "50%", "margin": 0}),
                )


def animate_not(a):
    with a.div(
        style=cohost.style(
            {
                "display": "inline-grid",
                "grid-template-columns": "20px 20px 1fr 20px 20px",
                "grid-template-rows": "10px 1fr 10px",
                "margin": "20px",
            }
        )
    ):
        with a.div(
            style=cohost.style(
                {
                    "grid-row": "2 / span 1",
                    "grid-column": "2 / span 3",
                }
            )
        ):
            static_image(a)
        a.div(
            style=cohost.style(
                {
                    "grid-row": "1 / span 3",
                    "grid-column": "1 / span 2",
                    "background": "rgb(255, 255, 255)",
                    "background": "linear-gradient(90deg, rgba(255,255,255,1) 70%, rgba(255,255,255,0) 100%);",
                    "z-index": 7,
                }
            )
        )
        a.div(
            style=cohost.style(
                {
                    "grid-row": "1 / span 3",
                    "grid-column": "4 / span 2",
                    "background": "rgb(255, 255, 255)",
                    "background": "linear-gradient(270deg, rgba(255,255,255,1) 70%, rgba(255,255,255,0) 100%);",
                    "z-index": 7,
                }
            )
        )


cohost.create_document(body, "post.html")
