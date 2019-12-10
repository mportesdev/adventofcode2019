from itertools import chain

from PIL import Image, ImageDraw

from puzzle_3 import vector_from_string, route_from_vectors, manhattan

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
    draw.rectangle([(-15 - min_x, -15 - min_y),
                    (15 - min_x, 15 - min_y)],
                   3)

    # intersection 1
    draw.rectangle([(-15 - min_x + intersection_1[0],
                     -15 - min_y + intersection_1[1]),
                    (15 - min_x + intersection_1[0],
                     15 - min_y + intersection_1[1])],
                   4)

    # intersection 2
    draw.rectangle([(-15 - min_x + intersection_2[0],
                     -15 - min_y + intersection_2[1]),
                    (15 - min_x + intersection_2[0],
                     15 - min_y + intersection_2[1])],
                   5)

    # red wire
    for x, y in route_1:
        img.putpixel((x - min_x, y - min_y), 1)

    # green wire
    for x, y in route_2:
        img.putpixel((x - min_x, y - min_y), 2)

    # black dot in origin
    img.putpixel((-min_x, -min_y), 0)

    img.save('puzzle_3.png')
