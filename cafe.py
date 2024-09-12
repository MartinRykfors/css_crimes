from airium import Airium
import lib.cohost as cohost

a = Airium(base_indent="")


def body(a):
    description = (
        "A grid of black and white tiles can be seen. Each row of tiles alternate between "
        "black and white tiles. "
        "When the rows of tiles are shifted horizontally with respect to one another, "
        "so that the pattern looks like zig-zagging columns of black and white tiles, "
        "one gets the illusion that the rows are skewed and no longer perfectly horizontal."
    )
    cohost.with_description(a, illusion, description, "cafe")


def illusion(a):
    with a.div(style="margin:auto"):
        with a.div(style=f"display: flex; flex-direction: column; gap: 0px; padding-left: 20px"):
            for i in range(10):
                row(a, i)
    a(
        (
            "When the rows are shifted to create a zig-zag pattern "
            "it seems like the rows are no longer perfectly horizontal."
        )
    )


def row(a, i):
    size = 26
    gap = "1"
    dx = (i % 2) * 16 * (((i // 2) % 2) * 2 - 1)
    tx = dx * -1
    border = f"border-style: solid; border-color: gray; border-width: {gap}px"
    curve = "cubic-bezier(1,-0.01,0,1.03)"
    animation = f"animation: 4s {curve} 0s infinite alternate none running spin; transform: translateX({tx}px);"
    with a.div(style=animation):
        with a.div(style=f"transform: translateX({dx}px)"):
            with a.div(style=f"display: flex; flex-direction: row; gap: 0px;"):
                for _ in range(5):
                    a.div(
                        style=f"height: {size}px; width: 36px; background-color: black; {border}"
                    )
                    a.div(
                        style=f"height: {size}px; width: 36px; background-color: white; {border}"
                    )


cohost.create_document(body, "post.html")
