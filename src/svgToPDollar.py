from matplotlib import pyplot as plt
from lxml import etree
import argparse
import os


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'svg_file', type=argparse.FileType('r'),
        help="SVG input file")
    return parser.parse_args()


def create_xml(points, name):
    gesture = etree.Element("Gesture")
    gesture.attrib["Name"] = name
    stroke = etree.SubElement(gesture, "Stroke")
    for point in points:
        p = etree.SubElement(stroke, "Point")
        p.attrib["X"] = str(point[0])
        p.attrib["Y"] = str(point[1])
        p.attrib["T"] = "0"
        p.attrib["Pressure"] = "0"
    return etree.ElementTree(gesture)


def write_pdollar_file(points, path=os.getcwd(), name='output'):
    xml_element_tree = create_xml(points, name)
    xml_element_tree.write(
        os.path.join(path, name + '.xml'),
        xml_declaration=True, encoding="utf-8", standalone=True,
        pretty_print=True)


def main(args):
    points = get_point_data_file(args.svg_file)
    if points:
        file_name = os.path.splitext(os.path.basename(args.svg_file.name))[0]
        write_pdollar_file(points, name=file_name)
        display_points(points)


def list_split(listA, n):
    for x in range(0, len(listA), n):
        every_chunk = listA[x: n + x]

        if len(every_chunk) < n:
            every_chunk = every_chunk + \
                          [None for y in range(n - len(every_chunk))]
        yield every_chunk


def get_point_data_file(file):
    xml = etree.parse(file)
    svg = xml.getroot()
    ns = {"svgns": "http://www.w3.org/2000/svg"}
    data = None

    polygon = svg.xpath("//svgns:polygon", namespaces=ns)
    if len(polygon) > 0:
        polygon_points = polygon[0].get("points").split()
        data = list(list_split(polygon_points, 2))
    return data


def display_points(data):
    for i in range(len(data)):
        point = data[i]
        marker = '$' + str(i) + '$'
        marker = 'o'
        yaxis = plt.gca()
        yaxis.invert_yaxis()
        p = plt.plot(float(point[0]), float(point[1]), marker=marker, color="red")
        plt.axis('equal')
    plt.show()


if __name__ == '__main__':
    args = parse()
    main(args)
