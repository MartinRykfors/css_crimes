from airium import Airium


def create_document(body, file, source_minify=False):
    a = Airium(base_indent="", source_minify=source_minify)
    a("<!DOCTYPE html>")
    with a.html():
        with a.head():
            a.meta(charset="utf-8")
            a.link(data_chunk="client", rel="stylesheet", href="./cohost.css")
        with a.body():
            body(a)

    with open(file, "wb") as f:
        b = bytes(a)
        print(len(b), "{:.1f}%".format(len(b) / 192000 * 100))
        if len(b) >= 192000:
            print(
                "WARNING: Size likely too big. {} over threshold".format(
                    len(b) - 192000
                )
            )
        f.write(b)


def with_description(a, body, description, tag):
    with a.div(**{"aria-describedby": f"user-content-{tag}"}):
        with a.span(**{"aria-hidden": f"true"}):
            body(a)
        with a.span(
            id=tag,
            style=(
                "clip: rect(0 0 0 0); clip-path: inset(50%);"
                " height: 1px; overflow: hidden; "
                "position: absolute; white-space: nowrap; "
                "width: 1px;"
            ),
        ):
            a(description)


def style(attrs):
    return ";".join([f"{k}:{v}" for k, v in attrs.items()])


def animation(
    duration=1,
    easing="cubic-bezier(0,0,1,1)",
    delay=0,
    direction="alternate",
    count="infinite",
    fill="none",
):
    return {
        "animation": f"{duration}s {easing} {delay}s {count} {direction} {fill} running spin"
    }


def promo_tag(a):
    with a.a(href="https://cohost.org/rykarn/tagged/optical%20illusion"):
        with a.div(
            style=style(
                {
                    "background-color": "rgb(131 37 79)",
                    "color": "rgb(255 249 242)",
                    "padding-top": "0.1rem",
                    "padding-bottom": "0.1rem",
                    "padding-left": "0.5rem",
                    "padding-right": "0.5rem",
                    "border-radius": "999px",
                    "display": "inline-block",
                    "margin-bottom": "1em",
                    "justify-content": "flex-start",
                    "align-items": "center",
                    "z-index": 999,
                }
            )
        ):
            with a.span(style=style({"font-size": "0.8rem"})):
                a("#rykarn's optical illusions")
    a.br()
