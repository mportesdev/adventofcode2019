from itertools import chain

from PIL import Image, ImageDraw

from puzzle_3 import vector_from_string, route_from_vectors, manhattan


def draw_box(draw_obj, x, y, size, color):
    half = size // 2
    draw_obj.rectangle([(x - half - min_x, y - half - min_y),
                        (x + half - min_x, y + half - min_y)],
                       color)


if __name__ == '__main__':
    with open('puzzle_3_input') as f:
        data = f.read()

    vectors_1, vectors_2 = [[vector_from_string(item)
                             for item in line.split(',')]
                            for line in data.splitlines()]

    route_1 = route_from_vectors(vectors_1)
    route_2 = route_from_vectors(vectors_2)

    intersections = (set(route_1) & set(route_2)) - {(0, 0)}
    intersection_1 = min(intersections, key=manhattan)
    intersection_2 = min(intersections,
                         key=lambda i: route_1.index(i) + route_2.index(i))

    min_x = min(t[0] for t in chain(route_1, route_2))
    max_x = max(t[0] for t in chain(route_1, route_2))
    min_y = min(t[1] for t in chain(route_1, route_2))
    max_y = max(t[1] for t in chain(route_1, route_2))

    img_width = max_x - min_x + 1
    img_height = max_y - min_y + 1

    img = Image.new('P', (img_width, img_height))
    img.putpalette([0, 0, 0,
                    255, 0, 0,
                    0, 255, 0,
                    96, 96, 96,
                    96, 0, 96,
                    0, 96, 96])
    draw = ImageDraw.Draw(img)

    # origin
    draw_box(draw, 0, 0, 30, 3)

    # intersection 1
    draw_box(draw, *intersection_1, 30, 4)

    # intersection 2
    draw_box(draw, *intersection_2, 30, 5)

    # red wire
    route_1 = [(x - min_x, y - min_y) for x, y in route_1]
    draw.point(route_1, 1)

    # green wire
    route_2 = [(x - min_x, y - min_y) for x, y in route_2]
    draw.point(route_2, 2)

    # black dot in origin
    draw.point((-min_x, -min_y), 0)

    img.save('puzzle_3.png')
