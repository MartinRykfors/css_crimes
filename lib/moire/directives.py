import math
import numpy as np
from scipy.spatial.transform import Rotation as R


def to_fun(f):
    if isinstance(f, (int, float, str, list, tuple, np.ndarray)):
        return lambda _: f
    return f


class Scale:
    def __init__(self, scale_x, scale_y, directive):
        self.scale_x = to_fun(scale_x)
        self.scale_y = to_fun(scale_y)
        self.directive = directive

    def color(self, x, y, f):
        if not self.scale_x(f) or not self.scale_y(f):
            return False

        x = x / self.scale_x(f)
        y = y / self.scale_y(f)

        return self.directive.color(x, y, f)


class Clone:
    def __init__(self, dx, dy, directive):
        self.dx = to_fun(dx)
        self.dy = to_fun(dy)
        self.directive = directive

    def color(self, x, y, f):
        if self.dx(f):
            x = x % self.dx(f)
        if self.dy(f):
            y = y % self.dy(f)
        return self.directive.color(x, y, f)


class Background:
    def __init__(self, color):
        self._color = to_fun(color)

    def color(self, x, y, f):
        return self._color(f)


class Circle:
    def __init__(self, center_x, center_y, radius, color=0):
        self.center_x = to_fun(center_x)
        self.center_y = to_fun(center_y)
        self.radius = to_fun(radius)
        self._color = to_fun(color)

    def color(self, x, y, f):
        dx = self.center_x(f) - x
        dy = self.center_y(f) - y
        inside = (dx * dx) + (dy * dy) < (self.radius(f) * self.radius(f))
        return self._color(f) if inside else None


class Translate:
    def __init__(self, dx, dy, directive):
        self.dx = to_fun(dx)
        self.dy = to_fun(dy)
        self.directive = directive

    def color(self, x, y, f):
        x = x - self.dx(f)
        y = y - self.dy(f)
        return self.directive.color(x, y, f)


class Subtract:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def color(self, x, y, f):
        if self.b.color(x, y, f) is not None:
            return None
        return self.a.color(x, y, f)


class WithColor:
    def __init__(self, color, directive):
        self.directive = directive
        self.color = color

    def color(self, x, y, f):
        return self.directive.color(x, y, f)


class Twist:
    def __init__(self, amount, directive):
        self.amount = to_fun(amount)
        self.directive = directive

    def color(self, x, y, f):
        distance = math.sqrt(x * x + y * y)
        angle = self.amount(f) * distance
        sa = math.sin(angle)
        ca = math.cos(angle)
        new_x = ca * x - sa * y
        new_y = ca * y + sa * x
        return self.directive.color(new_x, new_y, f)


class Rotate:
    def __init__(self, angle, directive):
        self.angle = to_fun(angle)
        self.directive = directive

    def color(self, x, y, f):
        sa = math.sin(self.angle(f))
        ca = math.cos(self.angle(f))
        new_x = ca * x - sa * y
        new_y = ca * y + sa * x
        return self.directive.color(new_x, new_y, f)


class Box:
    def __init__(self, start_x, start_y, end_x, end_y, color):
        self.start_x = to_fun(start_x)
        self.start_y = to_fun(start_y)
        self.end_x = to_fun(end_x)
        self.end_y = to_fun(end_y)
        self._color = to_fun(color)

    def color(self, x, y, f):
        if self.start_x(f) <= x < self.end_x(f) and self.start_y(f) <= y < self.end_y(
            f
        ):
            return self._color(f)
        return None


class PositiveYPlane:
    def __init__(self, color):
        self._color = to_fun(color)

    def color(self, x, y, f):
        if x <= 0:
            return None
        return self._color(f)


class Radial:
    def __init__(self, num_sectors, color):
        self.num_sectors = num_sectors
        self._color = to_fun(color)

    def color(self, x, y, f):
        inside = (math.atan2(y, x) + math.pi) * self.num_sectors / (
            math.pi * 2
        ) % 1.0 < 0.5
        if inside:
            return self._color(f)

        return None


class Union:
    def __init__(self, *directives):
        self.directives = directives

    def color(self, x, y, f):
        result = None
        for directive in self.directives:
            color = directive.color(x, y, f)
            if color is not None:
                result = color
        return result


class ColorMap:
    def __init__(self, color_map, directive):
        self.color_map = color_map
        self.directive = directive

    def color(self, x, y, f):
        c = self.directive.color(x, y, f)
        if c is None:
            return None
        return self.color_map(x, y, f)


def lin_lin(domain_start, domain_end, range_start, range_end, t):
    s = (t - domain_start) / (domain_end - domain_start)
    return (1 - s) * range_start + range_end * s


class Perspective:
    def __init__(self, z, top_right_x, top_right_y, width, height, *planes):
        self.z = z
        self.top_right_x = top_right_x
        self.top_right_y = top_right_y
        self.width = width
        self.height = height
        self.planes = planes

    def color(self, x, y, f):
        log = x % 100 == 0 and y % 100 == 0
        log = (x == 1 or x == self.width - 1) and (y == 1 or y == self.height - 1)
        log = False
        if log:
            print("")
        origin = np.array([0, 0, self.z])
        target = np.array(
            [
                lin_lin(0, self.width, -self.top_right_x, self.top_right_x, x),
                lin_lin(0, self.height, -self.top_right_y, self.top_right_y, y),
                0,
            ]
        )
        direction = target - origin
        direction = direction / np.linalg.norm(direction)
        if log:
            print(direction)
        t_min = 1000000
        result_color = None
        for plane in self.planes:
            if log:
                print("evaluating at", x, y)
                print("target", target)
                print("plane", plane.a(f), plane.b(f), plane.c(f))
            result = self.intersect(plane, origin, direction, f)
            if result is None:
                if log:
                    print("no result")
                continue
            if result.t > t_min:
                continue
            color = plane.color(result.u, result.v, f)
            if color is None:
                continue
            # we have a color and it is closer than any prior color
            if log:
                print("result", result.u, result.v, result.t)
            t_min = result.t
            result_color = color
        return result_color

    def intersect(self, plane, origin, direction, f):
        pa = np.array(plane.a(f))
        pb = np.array(plane.b(f))
        pc = np.array(plane.c(f))
        e1 = pb - pa
        e2 = pc - pa
        ray_cross_e2 = np.cross(direction, e2)
        det = np.dot(e1, ray_cross_e2)
        if abs(det) < 0.0001:
            return None

        inv_det = 1.0 / det
        s = origin - pa
        v = inv_det * np.dot(s, ray_cross_e2)
        if v < 0 or v > 1:
            return None

        s_cross_e1 = np.cross(s, e1)
        u = inv_det * np.dot(direction, s_cross_e1)
        if u < 0 or u > 1:
            return None

        t = inv_det * np.dot(e2, s_cross_e1)
        if t > 0.0001:
            return Intersection(v, u, t)


class Intersection:
    def __init__(self, u, v, t):
        self.u = u
        self.v = v
        self.t = t


class Plane:
    def __init__(self, a, b, c, width, height, directive):
        self.a = to_fun(a)
        self.b = to_fun(b)
        self.c = to_fun(c)
        self.width = width
        self.height = height
        self.directive = directive

    def color(self, u, v, f):
        x = lin_lin(0, 1, 0, self.width, u)
        y = lin_lin(0, 1, 0, self.height, v)
        return self.directive.color(x, y, f)


class PTranslate:
    def __init__(self, t, plane):
        self.t = to_fun(t)
        self.plane = plane

    def a(self, f):
        return np.array(self.plane.a(f)) + np.array(self.t(f))

    def b(self, f):
        return np.array(self.plane.b(f)) + np.array(self.t(f))

    def c(self, f):
        return np.array(self.plane.c(f)) + np.array(self.t(f))

    def color(self, u, v, f):
        return self.plane.color(u, v, f)


class PRotate:
    def __init__(self, axis, angle, plane):
        self.axis = np.array(axis) / np.linalg.norm(axis)
        self.angle = to_fun(angle)
        self.plane = plane

    def a(self, f):
        r = R.from_rotvec(self.angle(f) * self.axis)
        return r.apply(np.array(self.plane.a(f)))

    def b(self, f):
        r = R.from_rotvec(self.angle(f) * self.axis)
        return r.apply(np.array(self.plane.b(f)))

    def c(self, f):
        r = R.from_rotvec(self.angle(f) * self.axis)
        return r.apply(np.array(self.plane.c(f)))

    def color(self, u, v, f):
        return self.plane.color(u, v, f)


class PScale:
    def __init__(self, scales, plane):
        self.scales = to_fun(scales)
        self.plane = plane

    def a(self, f):
        return self.plane.a(f) * np.array(self.scales(f))

    def b(self, f):
        return self.plane.b(f) * np.array(self.scales(f))

    def c(self, f):
        return self.plane.c(f) * np.array(self.scales(f))

    def color(self, u, v, f):
        return self.plane.color(u, v, f)
