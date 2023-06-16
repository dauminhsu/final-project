import uuid

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon, Circle


def get_min_max(repository):
    """
    Получить максимальное значение, минимальное значение и их разницу в списке
    :param repository: список для продолжения
    :return: максимальное значение, минимальное значение и их разница
    """
    val_min, val_max = -10, 10
    if len(repository) == 1:
        val_min = min(repository) - 5
        val_max = max(repository) + 5
    elif len(repository) > 0:
        val_min = min(repository)
        val_max = max(repository)
    delta = val_max - val_min
    return val_min, val_max, delta


def create_graph(
        show_line,
        show_label,
        point_repository,
        segment_repository,
        polygon_repository,
        circle_repository):
    """
    Создайте изображение png с нанесенными координатами
    :param show_line: Отображение пунктира в координатах - bool
    :param show_label: Отображение пунктира в координатах - bool
    :param point_repository: Репозиторий точек для построения — PointRepository
    :param segment_repository: Репозиторий сегментов для построения — SegmentRepository
    :param polygon_repository: Репозиторий полигонов для построения — PolygonRepository
    :param circle_repository: Репозиторий сегментов для построения — CircleRepository
    :return: Путь к сгенерированному изображению
    """
    point_x = point_repository.get_all_x() + segment_repository.get_all_x() + \
        polygon_repository.get_all_x() + circle_repository.get_all_x()
    point_y = point_repository.get_all_y() + segment_repository.get_all_y() + \
        polygon_repository.get_all_y() + circle_repository.get_all_y()
    point_label = point_repository.get_all_label() + segment_repository.get_all_label() + \
        polygon_repository.get_all_label() + circle_repository.get_all_label()

    x_min, x_max, delta_x = get_min_max(point_x)
    y_min, y_max, delta_y = get_min_max(point_x)

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
    plt.savefig(image_name, bbox_inches='tight', pad_inches=0.2, transparent=True)

    return image_name
