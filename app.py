from flask import Flask, render_template, request

from model.circle import Circle
from model.point import Point
from model.polygon import Polygon
from model.segment import Segment
from repository.circle import CircleRepository
from repository.point import PointRepository
from repository.polygon import PolygonRepository
from repository.segment import SegmentRepository
from utils.graph_creator import create_graph
from utils.parser import parse_point, parse_number

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    is_show_line = request.args.get('show-line') == 'true'
    is_show_label = request.args.get('show-label') == 'true'

    if request.method == 'GET':
        default_point_repository = PointRepository(
            [Point(-3, 5, 'A'), Point(2, -3, 'B'), Point(-5, -11, 'C'), Point(5, 7, 'D')])
        default_segment_repository = SegmentRepository(
            [Segment(Point(7, 5, 'U'), Point(11, 3, 'V'))])
        default_polygon_repository = PolygonRepository([Polygon(
            [Point(-5, 3, 'G'), Point(2, 8, 'H'), Point(8, 9, 'I'), Point(7, -2, 'J'), Point(-1, -5, 'K')])])
        default_circle_repository = CircleRepository(
            [Circle(Point(3, 3, 'O'), 5)])

        image_name = create_graph(
            is_show_line,
            is_show_label,
            default_point_repository,
            default_segment_repository,
            default_polygon_repository,
            default_circle_repository)
        return render_template('index.html', image_name=image_name)
    else:
        point_repository = PointRepository()
        segment_repository = SegmentRepository()
        polygon_repository = PolygonRepository()
        circle_repository = CircleRepository()

        lines = [line.strip()
                 for line in request.json['text'].split('\n') if line.strip()]
        for line in lines:
            args = [arg.strip() for arg in line.split(' ') if arg.strip()]
            if args[0] == 'point':
                new_point = parse_point(args[1])
                if new_point is None:
                    continue
                point_repository.add(new_point)
            elif args[0] == 'segment':
                points = [parse_point(arg) for arg in args[1:]]
                if None in points:
                    continue
                segment_repository.add(Segment(points[0], points[1]))
            elif args[0] == 'polygon':
                points = [parse_point(arg) for arg in args[1:]]
                if None in points:
                    continue
                polygon_repository.add(Polygon(points))
            elif args[0] == 'circle':
                center = parse_point(args[1])
                radius = parse_number(args[2])
                if center is None or radius is None:
                    continue
                circle_repository.add(Circle(center, radius))

        image_name = create_graph(
            is_show_line,
            is_show_label,
            point_repository,
            segment_repository,
            polygon_repository,
            circle_repository)
        return image_name


if __name__ == '__main__':
    app.run()
