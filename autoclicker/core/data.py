class Vec2:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def __iter__(self):
        yield self.x
        yield self.y

    def __add__(self, other):
        return Vec2(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        return Vec2(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other):
        if type(other) is Vec2:
            return Vec2(
                self.x * other.x,
                self.y * other.y
            )
        elif type(other) is float:
            return Vec2(
                self.x * other,
                self.y * other
            )

    def __truediv__(self, other):
        if type(other) is Vec2:
            return Vec2(
                self.x / other.x,
                self.y / other.y
            )
        elif type(other) is float:
            return Vec2(
                self.x / other,
                self.y / other
            )
        elif type(other) is int:
            return Vec2(
                self.x // other,
                self.y // other
            )
        else:
            raise TypeError(
                f"Argument 'other' has the unsupported type '{type(other)}'")

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __getitem__(self, index):
        return (self.x, self.y)[index]

    @classmethod
    def from_tuple(cls, t: tuple):
        if len(t) != 2:
            raise ValueError("Tuple must have exactly 2 elements for Vec2.")
        return cls(*t)

    def to_tuple(self):
        return (*self,)


class Vec3:
    def __init__(self, *args):
        if len(args) == 0:
            self.x = self.y = self.z = 0.0
        elif len(args) == 1:
            self.x = self.y = self.z = float(args[0])
        elif len(args) == 2:
            self.x, self.y, self.z = float(args[0]), float(args[1]), 0
        elif len(args) == 3:
            self.x, self.y, self.z = args
        else:
            raise TypeError("Vec3 cannot have more than 3 arguments")

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __add__(self, other):
        return Vec2(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __sub__(self, other):
        return Vec2(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z)

    def __mul__(self, other):
        return Vec2(
            self.x * other.x,
            self.y * other.y,
            self.z * other.z
        )

    def __truediv__(self, other):
        return Vec2(
            self.x / other.x,
            self.y / other.y,
            self.z / other.z
        )

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __getitem__(self, index):
        return (self.x, self.y)[index]

    @classmethod
    def from_tuple(cls, t: tuple):
        if len(t) != 3:
            raise ValueError("Tuple must have exactly 3 elements for Vec3.")
        return cls(*t)

    def to_tuple(self):
        return (*self,)
