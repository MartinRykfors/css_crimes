from airium import Airium
import lib.cohost as cohost

a = Airium(base_indent="")


def body(a):
    description = (
        "Four circles made out of hollow squares which alternate between white and black color can be seen. "
        "When the squares all rotate slightly around their own centers, one gets the illusion "
        "that the circles are forming a spiral pattern."
    )
    cohost.with_description(
        a, lambda a: illusion(a, small_version), description, "cafe"
    )
    a(
        "When the squares are tilted, the concentric circles seem to form a spiral pattern."
    )
    a("Version for big screens below the fold:")
    a("")
    a("---")
    a("")
    illusion(a, big_version)


def illusion(a, version):
    with a.div(
        style=cohost.style(
            {
                "max-width": "600px",
                "height": "600px",
                "display": "flex",
                # "aspect-ratio": "1 / 1",
                "margin": "auto",
            }
        )
    ):
        with a.div(
            style=cohost.style(
                {
                    "background-color": "grey",
                    "flex-grow": "1",
                    "display": "flex",
                    "justify-content": "center",
                    "align-items": "center",
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
                # big_version(a)
                # small_version(a)
                version(a)

                with a.div(
                    style=cohost.style(
                        {"grid-column": "1 / span 1", "grid-row": "1 / span 1"}
                    )
                ):
                    with a.p(style=f"text-align: center"):
                        a("+")


def big_version(a):
    for i in range(2, 6):
        r = 12 * ((i % 2) * 2 - 1)
        radius = 50 * i
        count = 14 * i
        spiral(a, radius, count, 18, r)


def small_version(a):
    for i in range(2, 6):
        r = 12 * ((i % 2) * 2 - 1)
        radius = 32 * i
        count = 14 * i
        spiral(a, radius, count, 12, r)


def spiral(a, radius, count, size, rotation):
    for i in range(count):
        color = "white" if i % 2 else "black"
        angle = 360 / count * i
        with a.div(
            style=cohost.style(
                {
                    "margin": "auto",
                    "grid-column": "1 / span 1",
                    "grid-row": "1 / span 1",
                    "transform": f"rotate({angle}deg) translateX({radius}px)",
                }
            )
        ):
            with a.div(
                style=cohost.style(
                    {
                        "border": "1.5px solid {}".format(color),
                        "width": f"{size}px",
                        "height": f"{size}px",
                        "margin": "auto",
                        "transform": f"scale(1) rotate({rotation}deg)",
                    }
                    | cohost.animation2(easing="cubic-bezier(1,-0.06,.54,1)", duration=6)
                )
            ):
                pass


cohost.create_document(body, "post.html")
