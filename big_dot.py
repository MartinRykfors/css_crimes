from airium import Airium
import lib.cohost as cohost

a = Airium(base_indent="")


def body(a):
    description = (
        "An orange dot is surrounded by 6 black dots. The black dots are animated "
        "to periodically change their scale. When the black dots are small, the "
        "orange dot seems to be larger than it is when the surrounding dots "
        "are big."
    )
    cohost.with_description(a, illusion, description, "cafe")


def illusion(a):
    dots(a)
    a(
        (
            "The orange dot appears to be larger when the surrounding black dots are small, "
            "but it is always the same size."
        )
    )
    a.br()
    a(
        (
            "In my opinion, this illusion turned out to be a bit more subtle than other examples of this illusion "
            "that you can find online."
        )
    )


def dots(a):
    with a.div(
        style=cohost.style(
            {
                "display": "flex",
                "max-width": "500px",
                "padding": "50px",
                "margin": "auto",
            }
        )
    ):
        with a.div(
            style=cohost.style(
                {
                    "display": "grid",
                    "grid-template-columns": "1fr 1fr",
                    "grid-template-rows": "1fr",
                    "flex-grow": "1",
                }
            )
        ):
            dot_group(a, 1)
            dot_group(a, 2)


def dot_group(a, instance):
    with a.div(
        style=cohost.style(
            {
                "grid-column": f"{instance}/span 1",
                "grid-row": f"1/span 1",
                "width": "100%",
                "height": "200px",
                "justify-content": "center",
                "align-items": "center",
                "display": "flex",
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
            size = 30
            with a.div(
                style=cohost.style(
                    {
                        "grid-column": f"1/span 1",
                        "grid-row": f"1/span 1",
                        "width": f"{size}px",
                        "height": f"{size}px",
                        "background-color": "orange",
                        "border-radius": f"{size}px",
                        "display": "flex",
                        "justify-content": "center",
                        "align-items": "center",
                    }
                )
            ):
                pass
                # with a.p(style=cohost.style({'text-align':'center'})):
                #     a(':eggbug:')
            for i in range(6):
                angle = i * 360 / 6
                with a.div(
                    style=cohost.style(
                        {
                            "grid-column": f"1/span 1",
                            "grid-row": f"1/span 1",
                            "transform": f"rotate({angle}deg) translateX(60px) scale(2)",
                        }
                    )
                ):
                    curve = "cubic-bezier(.89,0,.2,.99)"
                    duration = 4
                    delay = (instance - 2) * duration
                    animation = f"animation: {duration}s {curve} {delay}s infinite alternate none running spin; transform: scale(1%);"
                    a.div(
                        style=cohost.style(
                            {
                                "width": f"{size}px",
                                "height": f"{size}px",
                                "background-color": "black",
                                "border-radius": f"{size}px",
                                "animation": f"{duration}s {curve} {delay}s infinite alternate none running spin; transform: scale(1%);",
                                "transform": "scale(0.2) translateX(-90px)",
                            }
                        )
                    )


cohost.create_document(body, "post.html")
