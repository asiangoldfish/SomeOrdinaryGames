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

    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    @classmethod
    def from_tuple(cls, t: tuple):
        if len(t) != 2:
            raise ValueError("Tuple must have exactly 2 elements for Vec2.")
        return cls(*t)


class Vec3:
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z

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
            self.z - other.z        )

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

    @classmethod
    def from_tuple(cls, t: tuple):
        if len(t) != 3:
            raise ValueError("Tuple must have exactly 3 elements for Vec3.")
        return cls(*t)