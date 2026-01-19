import math

def area_circumference(radius):
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    result = (
        f"area: {area:.2f}, \n"
        f"circumference: {circumference:.2f}"
    )
    return result

if __name__ == "__main__":
    print(area_circumference(3))
    