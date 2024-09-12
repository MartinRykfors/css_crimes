import random
from airium import Airium
import lib.cohost as cohost


def body(a):
    description = (
        """A css animation showing that PRIDE MONTH is an anagram of HERMIT POND"""
    )
    cohost.with_description(a, content, description, "crime")


def content(a):
    with a.div(
        style=cohost.style(
            {
                "display": "inline-flex",
                "height": "10rem",

            }
        )
    ):
        letters = [
            ("P", 7),
            ("R", 1),
            ("I", 2),
            ("D", 7),
            ("E", -3),
            (" ", 0),
            ("M", -3),
            ("O", 1),
            ("N", 1),
            ("T", -4),
            ("H", -10),
        ]
        for i, s in enumerate(letters):
            letter(a, s[0], s[1], i)


def letter(a, l, offset, i):
    with a.div(
        style=cohost.style(
            {
                "font-family": "monospace",
                "font-size": "4rem",
                'color': f'hsl({i * 20} 60% 50%)',
                "width": "2rem",
                "transform": f"translateY(4rem) translateX({offset*2}rem)",
            }
            | cohost.animation(
                direction="alternate-reverse",
                easing="cubic-bezier(.91,-0.05,.06,1.01)",
                duration=10,
                delay=i * -0.2,
            )
        )
    ):
        a(l)


cohost.create_document(body, "post.html")
