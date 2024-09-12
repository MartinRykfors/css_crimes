import math
import random
import itertools
from airium import Airium
import lib.cohost as cohost
import enum


class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, o):
        return Vec(self.x + o.x, self.y + o.y)

    def __sub__(self, o):
        return Vec(self.x - o.x, self.y - o.y)

    def __mul__(self, r):
        return Vec(self.x * r, self.y * r)

    def __div__(self, r):
        return Vec(self.x / r, self.y / r)

    def normalized(self):
        return self * (1 / self.length)

    @property
    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)


def body(a):
    description = """
    19 hexagons are arranged in a grid.
    Each hexagon has a number of curved paths starting at one side and ending at another side,
    possibly lining up with a path inside a neighboring hexagon.
    The paths come in three different colors.
    By clicking on a hexagon, it rotates 60 degrees."""
    cohost.with_description(a, content, description, "crime")

    a("Rotate the tiles so that the following holds:")
    with a.ul():
        with a.li():
            a(
                "There exists a single loop of line segments that passes through every tile of the grid."
            )
        with a.li():
            a("No other loop exists.")
        with a.li():
            a(
                "Any set of three consecutive line segments on the loop contain each of the three colors."
            )
        with a.li():
            a(
                "The ends of any line segment not on the loop must either line up with a line segment of the same color or line up with the boundary of the grid."
            )

    a("Clarifications:")
    with a.ul():
        with a.li():
            a(
                "The loop may pass through a tile multiple times. It may cross itself doing so."
            )
        with a.li():
            a(
                "The black dots and dashes are only for visual aid in telling the colors apart."
            )

memory_spacing = 999
element_width = 80

memory_width = element_width
line_width = 7
color_blind_width = 2
grid_spacing = 10
SHUFFLE = True


class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


RED = Color.RED
GREEN = Color.GREEN
BLUE = Color.BLUE

tile_background = "#013"
color_map = {Color.BLUE: "#68f", Color.GREEN: "#FB0", Color.RED: "#D27"}
color_blind_map = {Color.BLUE: "dotted", Color.GREEN: "dashed", Color.RED: None}


class Arc(enum.Enum):
    STRAIGHT = 1
    WIDE = 2
    TIGHT = 3


STRAIGHT = Arc.STRAIGHT
WIDE = Arc.WIDE
TIGHT = Arc.TIGHT

# STRAIGHT
# WIDE
# TIGHT

# GREEN
# RED
# BLUE

puzzle_spec = [
    # Row 1
    [(TIGHT, BLUE, 3)],
    [(TIGHT, BLUE, 2), (STRAIGHT, GREEN, 3)],
    [(TIGHT, RED, 4), (TIGHT, RED, 2)],
    # Row 2
    [(WIDE, RED, 3), (TIGHT, GREEN, 1)],
    [(WIDE, GREEN, 1), (WIDE, RED, 0), (TIGHT, RED, 4)],
    [(TIGHT, GREEN, 7), (TIGHT, GREEN, 5), (TIGHT, RED, 3)],
    [(WIDE, BLUE, 3), (WIDE, BLUE, 2), (TIGHT, RED, 0)],
    # Row 3
    [(TIGHT, GREEN, 2)],
    [(WIDE, BLUE, 5), (WIDE, RED, 4), (TIGHT, GREEN, 2)],
    [(STRAIGHT, GREEN, 0), (TIGHT, GREEN, 5)],
    [(WIDE, BLUE, 4), (WIDE, BLUE, 1)],
    [(WIDE, RED, 4)],
    # Row 4
    [(WIDE, RED, 7), (WIDE, RED, 6)],
    [(WIDE, GREEN, 6), (WIDE, BLUE, 5), (TIGHT, GREEN, 3)],
    [(WIDE, GREEN, 3), (STRAIGHT, GREEN, 3)],
    [(STRAIGHT, GREEN, 0), (STRAIGHT, BLUE, 2)],
    # Row 5
    [(TIGHT, BLUE, 7), (STRAIGHT, RED, 8)],
    [(WIDE, RED, 6), (WIDE, RED, 5)],
    [(WIDE, BLUE, 5), (STRAIGHT, GREEN, 5)],
]

print(len(puzzle_spec))


def content(a):
    with a.div(
        style=cohost.style(
            {
                "position": "relative",
                "height": f"{r * 10 * (element_width + grid_spacing) + 10}px",
            }
        )
    ):
        grid(a)


def grid(a):
    num_columns = [3, 4, 5, 4, 3]
    el = element_width + grid_spacing
    i = 0

    for row in range(5):
        for column in range(num_columns[row]):
            if row <= 2:
                x = (column - row) * el * 1.5 * R + 3 * el * R
                y = (column + row) * el * r
            else:
                x = (
                    (column - row) * el * 1.5 * R
                    + 3 * el * R
                    + (row - 2) * el * R * 1.5
                )
                y = (column + row) * el * r + (row - 2) * el * r
            with a.div(
                style=cohost.style(
                    {
                        "display": "inline-flex",
                        "position": "absolute",
                        "padding-right": f"{memory_width}px",
                        "padding-bottom": f"{memory_width}px",
                        "left": f"{x}px",
                        "top": f"{y}px",
                        "filter": "drop-shadow(2px 2px 2px black)",
                    }
                )
            ):
                shuffle = int(random.uniform(1, 6)) if SHUFFLE else 0
                print(shuffle)
                alternative(a, 0, puzzle_spec[i], shuffle=shuffle)
                alternative(a, 1, puzzle_spec[i], shuffle=shuffle)
                alternative(a, 2, puzzle_spec[i], shuffle=shuffle)
                alternative(a, 3, puzzle_spec[i], shuffle=shuffle)
                alternative(a, 4, puzzle_spec[i], shuffle=shuffle)
                alternative(a, 5, puzzle_spec[i], shuffle=shuffle, w=6)
                i += 1


def alternative(a, n, tile_spec, shuffle=0, w=1):
    with a.details(style=cohost.style({})):
        with a.summary(
            style=cohost.style(
                {
                    "left": f"calc({n * memory_spacing}px - calc({memory_spacing*100}% - {memory_spacing*memory_width}px))",
                    "position": "absolute",
                    "font-size": 0,
                }
            )
        ):
            with a.div(
                style=cohost.style(
                    {
                        "position": "absolute",
                    }
                )
            ):
                hexagon(a, tile_spec, n + shuffle)
            with a.div(
                style=cohost.style(
                    {
                        "position": "absolute",
                        "left": f"{(6 - n) * memory_spacing * 2 - memory_spacing}px",
                    }
                )
            ):
                hexagon(a, tile_spec, n + shuffle)

        with a.div(style=cohost.style({"width": f"{w}px"})):
            pass


R = 0.5
r = R * 0.866
corners = [
    Vec(R / 2 + 1 / 2, 1 / 2 - r),
    Vec(1, 1 / 2),
    Vec(R / 2 + 1 / 2, r + 1 / 2),
    Vec(R / 2, r + 1 / 2),
    Vec(0, 1 / 2),
    Vec(R / 2, 1 / 2 - r),
]


def star_corner(i):
    c = corners[i % 6]
    b = corners[(i + 5) % 6]
    return c + (c - b)


def side(i):
    c = corners[i % 6]
    b = corners[(i + 5) % 6]
    return (c + b) * 0.5


def side_tangent(i):
    c = corners[i % 6]
    b = corners[(i + 5) % 6]
    return (c - b).normalized()


star_corners = list([star_corner(i) for i in range(6)])
sides = list([side(i) for i in range(6)])


def hexagon(a, tile_spec, n=0):
    spec = ",".join("{:.0f}%{:.0f}%".format(c.x * 100, c.y * 100) for c in corners)
    with a.div(
        style=cohost.style(
            {
                "height": f"{element_width}px",
                "width": f"{element_width}px",
                "background": tile_background,
                "clip-path": f"polygon({spec})",
                "cursor": "pointer",
                "position": "relative",
            }
        )
    ):
        for arc, color, position in tile_spec:
            position = (position + n) % 6
            if arc == Arc.STRAIGHT:
                cross_line(a, position, color)
            elif arc == Arc.TIGHT:
                tight_arc(a, position, color)
            else:
                wide_arc(a, position, color)


def cross_line(a, side, color):
    side = side % 3

    if side != 2:
        with a.div(
            style=cohost.style(
                {
                    "position": "absolute",
                    "transform": f"rotate({(side + 1) * 60}deg)",
                    "height": "100%",
                    "width": "100%",
                }
            )
        ):
            cross_line_element(a, color_map[color], line_width, "solid")
            if color_blind_map[color]:
                cross_line_element(a, "#000", color_blind_width, color_blind_map[color])
    else:
        cross_line_element(a, color_map[color], line_width, "solid")
        if color_blind_map[color]:
            cross_line_element(a, "#000", color_blind_width, color_blind_map[color])


def cross_line_element(a, color, T, style):
    with a.div(
        style=cohost.style(
            {
                "position": "absolute",
                "height": f"{element_width}px",
                "left": f"{element_width / 2 - T / 2}px",
                "border-left": f"{T}px {style} {color}",
            }
        )
    ):
        pass


def tight_arc(a, corner, color):
    T = line_width
    t = T / element_width
    tight_element(a, corner, T, t, color_map[color], "solid")

    if color_blind_map[color]:
        T = color_blind_width
        t = T / element_width
        css_color = "#000"
        style = color_blind_map[color]
        tight_element(a, corner, T, t, css_color, style)


def tight_element(a, corner, T, t, css_color, style):
    with a.div(
        style=cohost.style(
            {
                "height": f"{(R + t) * 100:.0f}%",
                "width": f"{(R + t) * 100:.0f}%",
                "position": "absolute",
                "top": f"{(corners[corner].y - (R + t) / 2) * 100:.0f}%",
                "left": f"{(corners[corner].x - (R + t) / 2) * 100:.0f}%",
                "border": f"{T}px {style} {css_color}",
                "border-radius": "99px",
            }
        )
    ):
        pass


def wide_arc(a, side, color):
    T = line_width
    t = T / element_width
    rad = R * 3 / 2 + t / 2
    wide_element(a, side, T, rad, "solid", color_map[color])

    if color_blind_map[color]:
        T = color_blind_width
        t = T / element_width
        rad = R * 3 / 2 + t / 2
        style = color_blind_map[color]
        css_color = "#000"
        wide_element(a, side, T, rad, style, css_color)


def wide_element(a, side, T, rad, style, css_color):
    with a.div(
        style=cohost.style(
            {
                "height": f"{rad * 2 * 100:.0f}%",
                "width": f"{rad * 2 * 100:.0f}%",
                "position": "absolute",
                "top": f"{(star_corner(side).y - rad) * 100:.0f}%",
                "left": f"{(star_corner(side).x - rad) * 100:.0f}%",
                "border": f"{T}px {style} {css_color}",
                "border-radius": "99px",
            }
        )
    ):
        pass


cohost.create_document(body, "post.html")
