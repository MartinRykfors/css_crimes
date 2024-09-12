import random
import math
from airium import Airium
import lib.cohost as cohost


random.seed(6)


def body(a):
    description = """A mesmerizing pattern of strips of colored lights, arranged in a pattern of rotating concentric circles."""
    cohost.with_description(a, content, description, "crime")
    a("")
    a("---")
    a("")
    a(
        "Made this in yesterday's stream! Thanks to everyone who stopped by and had a look!"
    )


def lin_lin(t, t_min, t_max, o_min, o_max):
    return o_min + (o_max - o_min) * ((t - t_min) / (t_max - t_min))


def content(a):
    n = 2
    with a.div(
        style=cohost.style(
            {"display": "grid", "grid": f"repeat({n}, 1fr) / repeat({n}, 1fr)"}
        )
    ):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                with a.div(
                    style=cohost.style(
                        {"grid-column": f"{j} / span 1", "grid-row": f"{i} / span 1"}
                    )
                ):
                    spinny_stack(a, i, j)


def spinny_stack(a, i, j):
    palette = ["#141855", "#141855", "#861677", "#DF2B54", "#DF2B54", "#FCF665"]
    hue = 10 * (i + 2 * j - 3) + 190

    with a.div(
        style=cohost.style(
            {"display": "grid", "grid": "1fr / 1fr", "background": "black"}
        )
    ):
        for i, width in enumerate(range(100, 20, -20)):
            with a.div(
                style=cohost.style(
                    {
                        "grid-column": "1 / span 1",
                        "grid-row": "1 / span 1",
                        "display": "flex",
                        "align-items": "center",
                        "justify-content": "center",
                        "aspect-ratio": "1",
                    }
                )
            ):
                with a.div(
                    style=cohost.style({"width": f"{width}%", "aspect-ratio": "1"})
                ):
                    spinny_group(
                        a,
                        num_bars=int(random.expovariate(0.4)) + 7,
                        glow_hue=hue + int(random.expovariate(0.03)),
                        duration=random.uniform(20, 50),
                        width_percentage=width,
                    )


def spinny_group(a, num_bars, glow_hue, duration, width_percentage):
    with a.div(
        style=cohost.style(
            {
                "display": "grid",
                "grid": "1fr / 1fr",
                "aspect-ratio": "1",
                "width": "100%",
            }
        )
    ):
        glow_circle(a, glow_hue, lin_lin(width_percentage, 0, 100, 60, 78), 100)
        bars(a, num_bars, 0.2, "transparent", "black", duration)
        static_bars(
            a,
            num_bars + 1,
            0.2 + lin_lin(num_bars, 7, 20, 0, 0.2),
            "transparent",
            "black",
            0.1 + lin_lin(num_bars, 7, 20, 0, 0.3),
        )


def bars(a, num_bars, fuzz, color1, color2, duration):
    end_turn = 1 / num_bars
    with a.div(
        style=cohost.style(
            {"grid-column": "1 / span 1", "grid-row": "1 / span 1", "aspect-ratio": "1"}
        )
    ):
        with a.div(
            style=cohost.style(
                cohost.animation(
                    duration=random.uniform(30, 60),
                    easing="cubic-bezier(.44,-0.01,.54,1)",
                )
            )
        ):
            with a.div(
                style=cohost.style(
                    {
                        "aspect-ratio": "1",
                        "background": f"""repeating-conic-gradient(
                                from 0turn,
                                {color1} 0turn {end_turn / 2 - (end_turn * fuzz) / 2}turn,
                                {color2} {end_turn / 2}turn {end_turn - (end_turn * fuzz) / 2}turn,
                                {color1} {end_turn}turn
                            )""",
                        "border-radius": "1000px",
                    }
                    | cohost.animation(
                        duration=duration,
                        direction=random.choice(["normal"]),
                    )
                )
            ):
                pass


def static_bars(a, num_bars, fuzz, color1, color2, bias):
    normalized_bias = bias / num_bars
    end_turn = 1 / num_bars
    with a.div(
        style=cohost.style(
            {
                "grid-column": "1 / span 1",
                "grid-row": "1 / span 1",
                "aspect-ratio": "1",
                "background": f"""repeating-conic-gradient(
                    from 0turn,
                    {color1} 0turn {end_turn / 2 - (end_turn * fuzz) / 2 - normalized_bias}turn,
                    {color2} {end_turn / 2 - normalized_bias}turn {end_turn - (end_turn * fuzz) / 2}turn,
                    {color1} {end_turn}turn
                )""",
                "border-radius": "1000px",
            }
            | cohost.animation(
                duration=random.uniform(100, 200),
                direction=random.choice(["normal"]),
            )
        )
    ):
        pass


def glow_circle(a, hue, start_percentage, end_percentage):
    s2 = math.sqrt(2)
    stops = [
        ("transparent", 0),
        (f"hsl({hue} 100% 50%)", 32),
        (f"hsl({hue} 100% 95%)", 40),
        (f"hsl({hue} 100% 95%)", 60),
        (f"hsl({hue} 100% 50%)", 62),
        ("transparent", 100),
    ]

    def remap(stop):
        return (
            start_percentage + (stop / 100) * (end_percentage - start_percentage)
        ) / s2

    adjusted_stops = [(c, remap(s)) for c, s in stops]
    gradient_spec = ",".join(["{} {}%".format(c, s) for c, s in adjusted_stops])
    with a.div(
        style=cohost.style(
            {
                "aspect-ratio": "1",
                "background": f"""radial-gradient(
                    {gradient_spec}
                )""",
                "grid-column": "1 / span 1",
                "grid-row": "1 / span 1",
                "transform": "scale(1)",
            }
        )
    ):
        pass


cohost.create_document(body, "post.html")
