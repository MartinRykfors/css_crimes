import random
from airium import Airium
import lib.cohost as cohost


image_map_local = {"present": "present.png", "present_open": "present_open.png"}
image_map_web = {
    "present": "https://staging.cohostcdn.org/attachment/59aeab03-13de-49cc-906d-5085e68ba55c/present.png",
    "present_open": "https://staging.cohostcdn.org/attachment/f13d5fa8-c10d-454c-82e2-1faa0b43c070/present_open.png",
}

image_map = image_map_web

SIZE = 350


def body(a):
    description = """An interactive birthday gift. Clicking it reveals its contents."""
    cohost.with_description(a, content, description, "crime")


def content(a):
    with a.div(
        style=cohost.style(
            {
                "position": "relative",
                "height": f"{SIZE * 2}px",
                "width": f"{SIZE}px",
            }
        )
    ):

        with a.details():
            with a.summary(style=cohost.style({"font-size": "0"})):
                with a.div(
                    style=cohost.style({"position": "absolute", "cursor": "pointer"})
                ):
                    a.img(
                        src=image_map["present"], style=cohost.style({"margin": "0px"})
                    )
            with a.div(style=cohost.style({"position": "absolute"})):
                with a.div(
                    style=cohost.style(
                        {"display": "grid", "grid-template": "1fr / 1fr"}
                    )
                ):
                    with a.div(
                        style=cohost.style(
                            {"grid-row": "1 / span 1", "grid-column": "1 / span 1"}
                        )
                    ):
                        a.img(
                            src=image_map["present_open"],
                            style=cohost.style({"margin": "0px"}),
                        )
                    with a.div(
                        style=cohost.style(
                            {
                                "grid-row": "1 / span 1",
                                "grid-column": "1 / span 1",
                                "display": "flex",
                                "justify-content": "center",
                                "align-items": "center",
                            }
                        )
                    ):
                        with a.div(
                            style=cohost.style(
                                {"transform": "scale(0.001)"}
                                | cohost.animation(
                                    count=1,
                                    fill="forwards",
                                    delay=1,
                                    duration=2,
                                    easing="cubic-bezier(.17,.67,.48,.99)",
                                )
                            )
                        ):
                            a.img(
                                src="https://staging.cohostcdn.org/avatar/7744-90e2ac93-f936-4293-8394-47d5a70341da-profile.png?dpr=2&width=80&height=80&fit=cover&auto=webp",
                                style=cohost.style({"margin": "0px"}),
                            )


cohost.create_document(body, "post.html")
