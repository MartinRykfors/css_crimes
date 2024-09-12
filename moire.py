import random
import math
from airium import Airium
import lib.cohost as cohost
import lib.moire.write as w
import lib.moire.directives as d
import cProfile
import time

pi = math.pi
tau = pi * 2

image_map_local = {}
for name in [
    "cube",
    "circlecircle",
    "crossover",
    "piston",
    "spiral",
    "tunnel",
    "flags",
]:
    image_map_local[name] = f"output/{name}.png"
    image_map_local[name + "_bars"] = f"output/{name}.png.bars.png"

image_map_web = {
    "cube": "https://staging.cohostcdn.org/attachment/6ad8075f-9188-4fa0-894b-e91b7e9ec71a/cube.png",
    "cube_bars": "https://staging.cohostcdn.org/attachment/80280615-f523-492e-b2cb-7546828c4331/cube.png.bars.png",
    "circlecircle": "https://staging.cohostcdn.org/attachment/eca2d311-d026-4d37-abc5-b39caf03d01b/circlecircle.png",
    "circlecircle_bars": "https://staging.cohostcdn.org/attachment/21e0a4c6-0922-4887-bb1a-8a1b327c677e/circlecircle.png.bars.png",
    "crossover": "https://staging.cohostcdn.org/attachment/fd2360df-bb1e-4bc7-a531-db2ce1b7c922/crossover.png",
    "crossover_bars": "https://staging.cohostcdn.org/attachment/3bdcffa4-4051-44ee-bfa6-7c9533722572/crossover.png.bars.png",
    "piston": "https://staging.cohostcdn.org/attachment/a7c8c6ad-7cd9-47a6-a98a-dbb7d7834f9e/piston.png",
    "piston_bars": "https://staging.cohostcdn.org/attachment/9f90f52b-d9ff-4e8b-912c-1a671ef79e1c/piston.png.bars.png",
    "spiral": "https://staging.cohostcdn.org/attachment/ff003ca2-4e41-43e2-968c-38f24b8f4102/spiral.png",
    "spiral_bars": "https://staging.cohostcdn.org/attachment/7895e864-534c-48b2-980a-4c99c0cf0f0c/spiral.png.bars.png",
    "tunnel": "https://staging.cohostcdn.org/attachment/786afd75-c5d7-4c7d-8115-80276847c121/tunnel.png",
    "tunnel_bars": "https://staging.cohostcdn.org/attachment/6c6830f9-1977-48f6-b76f-69578415502e/tunnel.png.bars.png",
    "flags": "https://staging.cohostcdn.org/attachment/e67d081b-b406-4a1a-9491-6533edebd951/flags.png",
    "flags_bars": "https://staging.cohostcdn.org/attachment/72f742c6-12a8-4423-a7bb-3c8eb0d52d6c/flags.png.bars.png",
}

image_map = image_map_web

debug = False


def body(a):
    if debug:
        auto_window(a, "output/test.png", "output/test.png.bars.png")
        return
    description = """An interactive moire animation"""
    intro(a)
    content(a)


def intro(a):

    with a.p():
        a("""Scroll the windows below sideways slowly to see the animation.""")
        a(
            """If you find the scrolling tricky, you can click the Autoplay button to see an automated version of each animation."""
        )


def content(a):
    group(a, "spiral", "Two psychedelic spirals", show_hint=True)
    group(a, "tunnel", "Travelling through a rainbow tunnel with checkerboard sides")
    a("")
    a("---")
    a("")
    group(a, "circlecircle", "Several groups of spinning circles")
    group(a, "piston", "A moving piston")
    group(a, "crossover", "Five dots oscillating through the center of the image")
    group(a, "cube", "A spinning cube")
    group(a, "flags", "Several different pride flags spinning in 3D")
    with a.div(style=cohost.style({"margin-top": "2rem"})):
        a(
            "Hey! I hope you enjoyed these animations of mine. I might make more once I gather enough ideas for new ones."
        )
        a(
            "I really like Cohost for being a place I can call my online home, a place that allows for hosting html experiments like these."
        )
        a(
            'If you have the means, please consider subscribing to <a href="https://cohost.org/rc/user/settings#cohost-plus">Cohost plus</a>.'
        )
        a(
            "I would be very grateful if you can help this site thrive and let me keep this little corner on the internet available for me to keep doing fun things like these. Thank you for using Cohost!"
        )


def group(a, prefix, description, show_hint=False):
    def _group(a):
        scroll_window(a, image_map[prefix], image_map[prefix + "_bars"])
        if show_hint:
            hint(a)
        with a.details():
            with a.summary(
                style=cohost.style(
                    {
                        "font-size": "1.5rem",
                        "color": "#00bb00",
                        "background-color": "black",
                        "padding": "0.5rem",
                        "cursor": "pointer",
                    }
                )
            ):
                a("Autoplay")
            auto_window(a, image_map[prefix], image_map[prefix + "_bars"])

    cohost.with_description(a, _group, description, prefix)


def hint(a):
    with a.div(
        style=cohost.style(
            {
                "pointer-events": "none",
                "transform": "translateY(-3rem)",
                "height": "1px",
            }
        )
    ):
        with a.div(
            style=cohost.style(
                {
                    "transform": "translateX(15px)",
                    "color": "black",
                    "font-size": ".8rem",
                    "background-color": "white",
                    "border": "1px solid black",
                    "display": "inline-block",
                }
                | cohost.animation(easing="cubic-bezier(.67,-0.01,.44,.99)")
            )
        ):
            a("⬅️ Scroll me sideways! ➡️")


def auto_window(a, image_url, bar_url):
    with a.div(
        style=cohost.style(
            {
                "width": "100%",
                "overflow": "hidden",
                "border": "2px dashed white",
                "background-color": "gray",
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
                    {"grid-column": "1 / span 1", "grid-row": "1 / span 1"}
                )
            ):
                a.img(src=image_url, style=cohost.style({"margin": "0px"}))
            with a.div(
                style=cohost.style(
                    {
                        "grid-column": "1 / span 1",
                        "grid-row": "1 / span 1",
                        "height": f"{height}px",
                        "transform": f"translateX(-{width + bar_margin}px)",
                    }
                    | cohost.animation(
                        duration=20,
                        easing="cubic-bezier(.16,.01,.83,.99)",
                        direction="alternate",
                    )
                )
            ):
                with a.div(
                    style=cohost.style(
                        {
                            "margin-left": f"{width}px",
                            "width": f"{width + bar_margin}px",
                        }
                    )
                ):
                    a.img(src=bar_url, style=cohost.style({"margin": "0px"}))
                    # pass


def scroll_window(a, image_url, bar_url, show_hint=False):

    with a.div(
        style=cohost.style(
            {
                "width": "100%",
                "overflow": "hidden",
                "border": "2px dashed white",
                "background-color": "gray",
                "margin-top": "3rem",
                "margin-bottom": "0.2rem",
            }
        )
    ):
        with a.div(
            style=cohost.style(
                {
                    "width": "10000px",
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
                a.img(src=image_url, style=cohost.style({"margin": "0px"}))

            with a.div(
                style=cohost.style(
                    {
                        "grid-column": "1 / span 1",
                        "grid-row": "1 / span 1",
                        "overflow-x": "scroll",
                        "overflow-y": "clip",
                        "perspective": "100px",
                    }
                )
            ):
                factor = 2
                with a.div(
                    style=cohost.style(
                        {
                            "width": "calc(100% + 512px)",
                            "transform": f"scale({factor}, 3) translateZ(-{100 * (factor - 1)}px)",
                        }
                    )
                ):
                    with a.div(
                        style=cohost.style(
                            {
                                "margin": f"0px 0px 0px {480 - 100}px",
                                "width": f"{width}px",
                                "height": f"{height}px",
                                "overflow": "hide",
                            }
                        )
                    ):
                        with a.div(
                            style=cohost.style(
                                {"width": f"{width + bar_margin}px", "height": "256px"}
                            )
                        ):
                            a.img(src=bar_url, style=cohost.style({"margin": "0px"}))


def hsl(h, s, l):
    def mix(a, b, t):
        return (1 - t) * a + b * t

    def fract(x):
        return x - math.floor(x)

    def clamp(a, _min, _max):
        return max(min(a, _max), _min)

    p = [
        abs(fract(h + 1) * 6 - 3),
        abs(fract(h + 2 / 3) * 6 - 3),
        abs(fract(h + 1 / 3) * 6 - 3),
    ]
    a = [
        l * mix(1, clamp(p[0] - 1, 0, 1), s),
        l * mix(1, clamp(p[1] - 1, 0, 1), s),
        l * mix(1, clamp(p[2] - 1, 0, 1), s),
    ]

    def to_int(c):
        return f"{int(c * 255):0>2x}"

    return "#" + to_int(a[0]) + to_int(a[1]) + to_int(a[2])


def animation1(w, h, frames):
    yield d.Background("#000000")
    g = 5
    for i in range(g):
        dots = 3
        for j in range(dots):
            yield d.Translate(
                w / 2,
                h / 2,
                d.Rotate(
                    lambda f: 2 * math.pi * (i - f / frames) / g,
                    d.Translate(
                        120,
                        0,
                        d.Rotate(
                            lambda f: 2 * math.pi * f / frames + j * math.pi * 2 / dots,
                            d.Translate(
                                40,
                                0,
                                d.Circle(
                                    0,
                                    0,
                                    30,
                                    lambda f: hsl(
                                        j / (dots + 10) + f / (frames * g) - i / g,
                                        0.5,
                                        1,
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            )


# 20 frames
def animation2(w, h, frames):
    yield d.Background("#222222")
    num_dots = 5
    for i in range(num_dots):
        color = ["#ff00a1", "#ff9400", "#ffee00", "#b4ff2b", "#24dfe2"][i % num_dots]
        yield d.Translate(
            w / 2,
            h / 2,
            d.Rotate(
                math.pi * 2 * i / num_dots,
                d.Translate(
                    lambda f: math.sin(
                        math.pi * 2 * f / frames + math.pi * 2 * (i * 3) / num_dots
                    )
                    * w
                    / 2,
                    0,
                    d.Circle(0, 0, 30, color),
                ),
            ),
        )


# 8 frames
def animation3(w, h, frames):
    yield d.Background("#222222")

    yield d.Translate(
        w / 2,
        h / 2,
        d.Union(
            # subdivided_spiral(frames, 17, "#318fe0"),
            subdivided_spiral(
                frames,
                17,
                lambda f: hsl(0.6 + 0.07 * math.sin(tau * f / frames), 0.5, 1),
            ),
            subdivided_spiral(
                frames,
                17,
                lambda f: hsl(0.7 + 0.07 * math.sin(tau * f / frames), 0.8, 0.6),
                True,
            ),
            d.Rotate(
                math.pi,
                subdivided_spiral(
                    frames,
                    -13,
                    lambda f: hsl(0.05 + 0.04 * math.sin(tau * f / frames), 0.5, 1),
                ),
            ),
            d.Rotate(
                math.pi,
                subdivided_spiral(
                    frames,
                    -13,
                    lambda f: hsl(0.2 + 0.07 * math.sin(tau * f / frames), 0.5, 0.3),
                    True,
                ),
            ),
        ),
    )


def subdivided_spiral(frames, divisions, color, offset=False):
    c = math.pi / divisions if offset else 0
    return d.Subtract(
        d.Twist(0.05, d.PositiveYPlane(color)),
        d.Rotate(
            lambda f: math.pi * 2 * f / frames / divisions + c,
            d.Twist(0.002, d.Radial(divisions, "#888888")),
        ),
    )


def animation4(w, h, frames):
    yield d.Background("#222222")
    yield d.Translate(
        w / 2,
        h / 2,
        d.Union(
            d.Translate(
                lambda f: 50 * math.cos(tau * f / frames),
                lambda f: 50 * math.sin(tau * f / frames) - 80,
                d.Rotate(
                    lambda f: -3 * math.cos(tau * f / frames) / tau,
                    d.Union(
                        d.Box(-15, 0, 15, 140, "#666666"),
                        d.Box(-25, -25, 25, 25, "#bbbbbb"),
                        d.Circle(0, 0, 15, "#000000"),
                    ),
                ),
            ),
            d.Translate(
                0,
                lambda f: 60 + 50 * math.sin(math.pi * 2 * f / frames),
                d.Union(
                    d.ColorMap(
                        lambda x, y, f: hsl(0, 0, d.lin_lin(-40, 40, 0.4, 0.9, x)),
                        d.Box(-40, -40, 40, 60, "#aaaaaa"),
                    ),
                    d.Box(-40, 50, 40, 55, "#333333"),
                    d.Box(-40, 40, 40, 45, "#333333"),
                    d.Circle(0, 0, 10, "#000000"),
                ),
            ),
        ),
    )


def animation5(w, h, frames):
    def cube():
        def face(axis, angle, color_offset, color_rate):
            color_offset += 0.65
            color1 = lambda f: hsl(color_rate * f / frames + color_offset, 0.5, 1)
            color2 = lambda f: hsl(
                color_rate * f / frames + color_offset + 0.05, 0.7, 1
            )
            size = width
            return d.PRotate(
                axis,
                angle * tau / 4,
                d.Plane(
                    [-1, -1, 1],
                    [1, -1, 1],
                    [-1, 1, 1],
                    size,
                    size,
                    d.Union(
                        d.Subtract(
                            d.Background(color1),
                            d.Box(
                                30,
                                30,
                                size - 30,
                                size - 30,
                                "#000000",
                            ),
                        ),
                        d.Box(
                            100,
                            100,
                            size - 100,
                            size - 100,
                            color2,
                        ),
                    ),
                ),
            )

        for axis, angle, color_offset, color_rate in [
            ([0, 1, 0], 0, 0 / 4, 1 / 4),
            ([0, 1, 0], 1, 1 / 4, 1 / 4),
            ([0, 1, 0], 2, 2 / 4, 1 / 4),
            ([0, 1, 0], 3, 3 / 4, 1 / 4),
            ([1, 0, 0], 1, 1 / 4, 0),
            ([1, 0, 0], -1, 3 / 4, 0),
        ]:
            yield d.PTranslate(
                [0, 0, -1.5],
                d.PRotate(
                    [0.2, 0, 1],
                    tau / 12,
                    d.PRotate(
                        [0, 1, 0],
                        lambda f: f * tau / frames / 4,
                        face(axis, angle, color_offset, color_rate),
                    ),
                ),
            )

    yield d.Background("#222222")
    yield d.Perspective(1.2, 1, 1, w, h, *cube())


# tunnel, 8 frames
def animation6(w, h, frames):
    def checkerboard(size, frames):
        return d.Clone(
            size * 2,
            size * 2,
            d.Translate(
                lambda f: -size * 2 * f / frames,
                0,
                d.Union(
                    d.Box(0, 0, size, size, "#ffffff"),
                    d.Box(size, size, size * 2, size * 2, "#ffffff"),
                    d.Box(size * 2, 0, size * 3, size, "#ffffff"),
                    d.Box(size * 3, size, size * 4, size * 2, "#ffffff"),
                ),
            ),
        )

    t = lambda f: f / frames
    size = 90
    color_map = lambda x, y, f: hsl(
        d.lin_lin(0, w * 2, 0.7, 1.7, x),
        d.lin_lin(0, w * 2, 1, 0, x),
        d.lin_lin(0, w * 2, 1, 0, x),
    )
    yield d.Background(hsl(0, 0, 0))

    yield d.Perspective(
        1,
        1,
        1,
        w,
        h,
        d.Plane(
            [-1, -1, 0],
            [-1, -1, -3],
            [-1, 1, 0],
            w * 2,
            size * 4,
            d.Union(
                d.ColorMap(
                    color_map,
                    checkerboard(size, frames),
                ),
            ),
        ),
        d.Plane(
            [1, -1, 0],
            [1, -1, -3],
            [1, 1, 0],
            w * 2,
            size * 4,
            d.Union(
                d.ColorMap(
                    color_map,
                    checkerboard(size, frames),
                ),
            ),
        ),
        d.Plane(
            [-1, -1, 0],
            [-1, -1, -3],
            [1, -1, 0],
            w * 2,
            size * 2,
            d.Union(
                d.ColorMap(
                    color_map,
                    checkerboard(size, frames),
                ),
            ),
        ),
        d.Plane(
            [-1, 1, 0],
            [-1, 1, -3],
            [1, 1, 0],
            w * 2,
            size * 2,
            d.Union(
                d.ColorMap(
                    color_map,
                    checkerboard(size, frames),
                ),
            ),
        ),
    )


def animation7(w, h, frames):
    yield d.ColorMap(
        lambda x, y, f: hsl(
            0,
            0,
            d.lin_lin(0, h, 0, 0.5, y),
        ),
        d.Background("#000000"),
    )
    flags = [
        [("#FF1B8D", 1), ("#FFD900", 1), ("#1BB3FF", 1)],
        [
            ("#4DB0D4", 1),
            ("#D0919D", 1),
            ("#D9D9D9", 1),
            ("#D0919D", 1),
            ("#4DB0D4", 1),
        ],
        [
            ("#E60000", 1),
            ("#FF8E00", 1),
            ("#FFEF00", 1),
            ("#00821B", 1),
            ("#004BFF", 1),
            ("#780089", 1),
        ],
        [
            ("#D62900", 1),
            ("#FF9B55", 1),
            ("#FFFFFF", 1),
            ("#D462A6", 1),
            ("#A50062", 1),
        ],
        [("#B70060", 2), ("#844280", 1.5), ("#002D90", 2)],
        [
            ("#FFF42F", 1),
            ("#FFFFFF", 1),
            ("#9C59D1", 1),
            ("#292929", 1),
        ],
        [
            ("#3AA740", 1),
            ("#A8D47A", 1),
            ("#FFFFFF", 1),
            ("#ABABAB", 1),
            ("#000000", 1),
        ],
        [
            ("#000000", 1),
            ("#A5A5A5", 1),
            ("#FFFFFF", 1),
            ("#810081", 1),
        ],
    ]

    def flag(w, h, bars):
        total = sum(height for _, height in bars)
        y_end = h
        for color, height in bars:
            y_start = y_end - h * height / total
            yield d.Box(0, y_start, w, y_end, color)
            y_end = y_start

    # for b in flag(w, h, flags[-1]):
    #     yield b
    def planes():
        total = len(flags)
        size = 100
        for i, flag_spec in enumerate(flags):
            yield d.PTranslate(
                [0, (i * 2 + 1) / total - 1, -1],
                d.PScale(
                    [1, 0.9 / total, 1],
                    d.PRotate(
                        [0, 1, 0],
                        lambda f, i=i: (f + i * 0.4) * pi / frames,
                        d.Plane(
                            [-1, -1, 0],
                            [1, -1, 0],
                            [-1, 1, 0],
                            size,
                            size,
                            d.Union(*flag(size, size, flag_spec)),
                        ),
                    ),
                ),
            )
        return

    yield d.Perspective(2, 1, 1, w, h, *planes())


width = 340
height = 400
bar_margin = 50


animations = [
    (animation1, width, height, 10, "circlecircle"),
    # (animation2, width, height, 20, "crossover"),
    # (animation3, width, height, 8, "spiral"),
    # (animation4, width, height, 8, "piston"),
    # (animation5, width, height, 12, "cube"),
    # (animation6, width, height, 8, "tunnel"),
    # (animation7, width, height + 100, 7, "flags"),
    # (animation4, width, height, 8, "test"),
]
t_start = time.time()
for animation, width, height, frames, name in animations:
    w.write(
        animation,
        width,
        height,
        frames,
        f"output/{name}.png",
        bar_margin,
    )
t_end = time.time()
print("### TIMING ###")
print(t_end - t_start)

cohost.create_document(body, "post.html")
