from flask import Flask, render_template, request, send_file

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
        image_name = f'/static/defaults/DEFAULT_IMAGE_{is_show_line}_{is_show_label}.png'
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
                if center is None or radius is None or radius < 0:
                    continue
                circle_repository.add(Circle(center, radius))

        image_name = create_graph(
            is_show_line,
            is_show_label,
            point_repository,
            segment_repository,
            polygon_repository,
            circle_repository)
        return send_file(
            image_name,
            mimetype='image/png',
            download_name='plot.png')


if __name__ == '__main__':
    app.run()
