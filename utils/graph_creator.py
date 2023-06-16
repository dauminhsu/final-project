import uuid

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon, Circle


def create_graph(
        show_line,
        show_label,
        point_repository,
        segment_repository,
        polygon_repository,
        circle_repository):
    point_x = point_repository.get_all_x() + segment_repository.get_all_x() + \
        polygon_repository.get_all_x() + circle_repository.get_all_x()
    point_y = point_repository.get_all_y() + segment_repository.get_all_y() + \
        polygon_repository.get_all_y() + circle_repository.get_all_y()
    point_label = point_repository.get_all_label() + segment_repository.get_all_label() + \
        polygon_repository.get_all_label() + circle_repository.get_all_label()

    x_min, x_max = -10, 10
    if len(point_x) == 1:
        x_min = min(point_x) - 5
        x_max = max(point_x) + 5
    elif len(point_x) > 0:
        x_min = min(point_x)
        x_max = max(point_x)
    delta_x = x_max - x_min

    y_min, y_max = -10, 10
    if len(point_y) == 1:
        y_min = min(point_y) - 5
        y_max = max(point_y) + 5
    elif len(point_y) > 0:
        y_min = min(point_y)
        y_max = max(point_y)
    delta_y = y_max - y_min

    ticks_frequency = max(delta_x, delta_y) // 20 + 1

    fig, ax = plt.subplots(figsize=(10, 10))

    # Draw points
    ax.scatter(point_x, point_y, c='black')

    # Draw lines and labels
    for x, y, label in zip(point_x, point_y, point_label):
        if show_line:
            ax.plot([x, x], [0, y], c='#95a5a6', ls='--', lw=1.5, alpha=0.5)
            ax.plot([0, x], [y, y], c='#95a5a6', ls='--', lw=1.5, alpha=0.5)
        if show_label:
            ax.annotate(label, (x + 0.1, y + 0.1))

    # Draw segments
    for segment in segment_repository.get():
        ax.plot(segment.get_x(), segment.get_y(), c='black', lw=0.5)

    # Draw polygons
    for polygon in polygon_repository.get():
        ax.add_patch(
            Polygon(
                polygon.to_points_tuple(),
                color='black',
                fill=False))

    # Draw circles
    for circle in circle_repository.get():
        ax.add_patch(
            Circle(
                circle.center.to_tuple(),
                circle.radius,
                color='black',
                fill=False))

    ax.set(
        xlim=(
            x_min - 1,
            x_max + 1),
        ylim=(
            y_min - 1,
            y_max + 1),
        aspect='equal')

    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
    ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)

    x_ticks = np.arange(x_min, x_max + 1, ticks_frequency)
    y_ticks = np.arange(y_min, y_max + 1, ticks_frequency)
    ax.set_xticks(x_ticks[x_ticks != 0])
    ax.set_yticks(y_ticks[y_ticks != 0])

    ax.set_xticks(np.arange(x_min, x_max + 1), minor=True)
    ax.set_yticks(np.arange(y_min, y_max + 1), minor=True)

    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot(
        (1),
        (0),
        marker='>',
        transform=ax.get_yaxis_transform(),
        **arrow_fmt)
    ax.plot(
        (0),
        (1),
        marker='^',
        transform=ax.get_xaxis_transform(),
        **arrow_fmt)

    image_name = f'static/plots/{uuid.uuid1()}.png'
    plt.savefig(image_name, bbox_inches='tight', pad_inches=0.2)

    return image_name
