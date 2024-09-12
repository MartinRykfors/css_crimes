import random
from airium import Airium
import lib.cohost as cohost

images = [
    "https://staging.cohostcdn.org/attachment/c7184d64-1572-45e0-8c15-c68106c10458/C21D96D7-C83D-4DB0-A1E4-B7B793AB0C30.jpeg",
    "https://staging.cohostcdn.org/attachment/b4ed94f8-8feb-4ba6-a8b4-c40447c74dc2/F5E405D7-201F-4F2F-8046-DF2B10AF5C7A.jpeg",
    "https://staging.cohostcdn.org/attachment/8632d9c0-f50d-476e-86bb-d865d658c2e1/C9F993CA-56C4-4018-9633-1974A9DD5B06.jpeg",
    "https://staging.cohostcdn.org/attachment/89d2648b-7d74-424f-9a74-b8a7f771ad82/91C6DC90-ECD8-44EE-8B8E-8A53AB288850.jpeg",
    "https://staging.cohostcdn.org/attachment/92f8ab0d-002f-43c2-aada-fa11808341a0/F5C0592F-3CD0-4653-981F-9D0D40DBA154.jpeg",
]


def body(a):
    description = """An interactive slideshow of images, showing a sequence of me opening the case for my old clarinet for the first time in a long time."""
    cohost.with_description(a, content, description, "crime")
    a("")
    a("---")
    a("")
    a(
        """
Doing a little side programming project involving digital signal processing, so I decided to record my clarinet in order to have some input data.

I have not touched this thing for 12 years. Hello old friend! I sure liked stickers back then!

GOOD LORD AM I RUSTY :eggbug-nervous:
"""
    )


def content(a):
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
                    "opacity": "0",
                    "pointer-events": "none",
                }
            )
        ):
            a.img(src=images[4], style=cohost.style({'margin': '0px'}))
        with a.div(
            style=cohost.style({"grid-column": "1 / span 1", "grid-row": "1 / span 1"})
        ):
            with a.details():
                with a.summary(style=cohost.style({"font-size": 0})):
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
                                {"grid-column": "1 / span 1", "grid-row": "1 / span 1"}
                            )
                        ):
                            a.img(src=images[0], style=cohost.style({'margin': '0px'}))
                        with a.div(
                            style=cohost.style(
                                {"grid-column": "1 / span 1", "grid-row": "1 / span 1"}
                            )
                        ):
                            with a.div(
                                style=cohost.style(
                                    {
                                        "font-size": "1rem",
                                        "color": "black",
                                        "border": "2px solid black",
                                        "background-color": "white",
                                        'width': '150px',
                                        'display': 'flex',
                                        'justify-content': 'center',
                                        'align-items': 'center',
                                        'transform': 'translateY(10px)'
                                    } | cohost.animation(easing='cubic-bezier(.51,.01,1,.69)', duration='0.5')
                                )
                            ):
                                a("Keep clicking me! >>>")

                with a.details(style=cohost.style({"height": "0px"})):
                    with a.summary(style=cohost.style({"font-size": 0})):
                        with a.div(
                            style=cohost.style({"transform": "translateY(calc(-100%))"})
                        ):
                            a.img(src=images[1], style=cohost.style({'margin': '0px'}))

                    with a.details():
                        with a.summary(style=cohost.style({"font-size": 0})):
                            with a.div(
                                style=cohost.style(
                                    {"transform": "translateY(calc(-100% * 2))"}
                                )
                            ):
                                a.img(src=images[2], style=cohost.style({'margin': '0px'}))

                        with a.details():
                            with a.summary(style=cohost.style({"font-size": 0})):
                                with a.div(
                                    style=cohost.style(
                                        {"transform": "translateY(calc(-100% * 3))"}
                                    )
                                ):
                                    a.img(src=images[3], style=cohost.style({'margin': '0px'}))

                            with a.details():
                                with a.summary(style=cohost.style({"font-size": 0})):
                                    with a.div(
                                        style=cohost.style(
                                            {
                                                "transform": "translateY(calc(-100% * 3  * 3024 / 4032))"
                                            }
                                        )
                                    ):
                                        a.img(src=images[4], style=cohost.style({'margin': '0px'}))


cohost.create_document(body, "post.html")
