import random
from airium import Airium
import lib.cohost as cohost
import random


def body(a):
    random.seed(602)
    description = """A mathematical expression that combines addition, multiplication, subtraction and parentheses. However, depending on the width of the device used to view this post, the numbers in the equation change randomly."""
    a("What is the value of this?")
    cohost.with_description(a, content, description, "crime")


def content(a):
    with a.div(
        style=cohost.style(
            {
                "height": "2em",
                "max-width": "602px",
                "position": "relative",
                # "resize": "horizontal",
                # "overflow": "hidden",
            }
        )
    ):
        for i in range(20, 603):
            equation(a, i, random_expression())


def equation(a, index, eqn):
    with a.div(
        style=cohost.style(
            {
                "position": "absolute",
                "left": f"calc((100% - {index}px) * 1000)",
            }
        )
    ):
        a(eqn)


def random_expression():
    global values

    def r():
        return random.randint(2, 6)

    return f"({r()} + {r()}) * {r()} - {r()} * {r()}"


cohost.create_document(body, "post.html")
