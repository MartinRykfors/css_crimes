import png
import itertools
from pathos.pp import ParallelPool as Pool
from joblib import Parallel, delayed


def to_color_tuple(c):
    r = int(c[1:3], base=16)
    g = int(c[3:5], base=16)
    b = int(c[5:7], base=16)
    return (r, g, b)


def query_point(ij, frames, height, directive):
    i = ij[0]
    j = ij[1]
    f = j % frames
    x = j
    y = height - i
    color = directive.color(x, y, f)
    return (ij, color)


# multi = "pathos"
multi = "joblib"
# multi = None


def draw(directives, width, height, frames):
    image = list([["#000000"] * width for _ in range(height)])
    for directive in directives:
        if multi == "pathos":
            with Pool(6) as p:
                indices = itertools.product(range(height), range(width))
                indices_colors = p.amap(
                    lambda ij: query_point(ij, frames, height, directive), indices
                ).get()
                for ij, color in indices_colors:
                    if color is not None:
                        image[ij[0]][ij[1]] = color
        elif multi == "joblib":
            indices = itertools.product(range(height), range(width))
            indices_colors = Parallel(n_jobs=6)(
                delayed(query_point)(ij, frames, height, directive) for ij in indices
            )
            for ij, color in indices_colors:
                if color is not None:
                    image[ij[0]][ij[1]] = color

        else:
            for i in range(len(image)):
                for j in range(len(image[i])):
                    f = j % frames
                    x = j
                    y = height - i
                    color = directive.color(x, y, f)
                    if color is not None:
                        image[i][j] = color
    for row in image:
        yield list(
            itertools.chain.from_iterable(map(lambda color: to_color_tuple(color), row))
        )


def write(anim, width, height, frames, name, bar_margin):
    out = list(draw(anim(width, height, frames), width, height, frames))
    w = png.Writer(width, height, greyscale=False)
    f = open(name, "wb")
    w.write(f, out)
    f.close()
    write_bars(width + bar_margin, height + bar_margin, frames, name + ".bars.png")


def create_bars(frames, width, height):
    element = [1] * frames
    element[frames // 2] = 0
    row = element * ((width // frames) + 1)
    return [row[:width]] * height


def write_bars(width, height, frames, name):
    bar_palette = [(0x00, 0x00, 0x00, 0x00), (0x00, 0x00, 0x00, 0xFF)]
    s = create_bars(frames, width, height)
    w = png.Writer(len(s[0]), len(s), palette=bar_palette, bitdepth=1)
    f = open(name, "wb")
    w.write(f, s)
    f.close()
