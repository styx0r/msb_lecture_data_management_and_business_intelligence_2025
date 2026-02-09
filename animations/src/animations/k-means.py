from __future__ import annotations
from io import BytesIO
from pathlib import Path
import random
from typing import Iterable, List, Tuple

from PIL import Image
import matplotlib.pyplot as plt


Point = Tuple[float, float]


def generate_centers(count: int, center_radius: float, seed: int = 7) -> List[Point]:
    random.seed(seed)
    centers: List[Point] = []
    for _ in range(count):
        angle = random.uniform(0, 2 * 3.14159)
        radius = random.uniform(center_radius * 0.4, center_radius)
        centers.append(
            (
                radius * random.choice([1, -1]) * random.random(),
                radius * random.random(),
            )
        )
    return centers


def generate_points(
    centers: Iterable[Point],
    points_per_cluster: int = 60,
    spread: float = 0.8,
    seed: int = 7,
) -> List[Point]:
    random.seed(seed)
    points: List[Point] = []
    for cx, cy in centers:
        for _ in range(points_per_cluster):
            points.append((random.gauss(cx, spread), random.gauss(cy, spread)))
    return points


def assign_clusters(points: List[Point], centroids: List[Point]) -> List[int]:
    assignments: List[int] = []
    for x, y in points:
        closest = min(
            range(len(centroids)),
            key=lambda i: (x - centroids[i][0]) ** 2 + (y - centroids[i][1]) ** 2,
        )
        assignments.append(closest)
    return assignments


def recompute_centroids(
    points: List[Point], assignments: List[int], centroids: List[Point]
) -> List[Point]:
    k = len(centroids)
    sums = [(0.0, 0.0, 0) for _ in range(k)]
    for (x, y), idx in zip(points, assignments):
        sx, sy, count = sums[idx]
        sums[idx] = (sx + x, sy + y, count + 1)
    new_centroids: List[Point] = []
    for i, (sx, sy, count) in enumerate(sums):
        if count == 0:
            new_centroids.append(centroids[i])
        else:
            new_centroids.append((sx / count, sy / count))
    return new_centroids


def render_frame(
    points: List[Point],
    assignments: List[int],
    centroids: List[Point],
    iteration: int,
    colors: List[str],
    figsize: Tuple[int, int],
) -> Image.Image:
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_title(f"k-means iteration {iteration}", fontsize=12)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_facecolor("white")

    for i, (x, y) in enumerate(points):
        ax.scatter(x, y, s=18, color=colors[assignments[i] % len(colors)], alpha=0.85)

    for i, (cx, cy) in enumerate(centroids):
        ax.scatter(
            cx, cy, marker="X", s=120, color=colors[i % len(colors)], edgecolor="black"
        )

    buf = BytesIO()
    fig.tight_layout()
    fig.savefig(buf, format="png", dpi=120)
    plt.close(fig)
    buf.seek(0)
    return Image.open(buf)


def kmeans_gif(
    output_path: Path,
    k: int = 3,
    true_clusters: int = 3,
    iterations: int = 8,
    seed: int = 7,
    points_per_cluster: int = 60,
    spread: float = 0.8,
    center_radius: float = 4.0,
    init_mode: str = "random",
    duration_ms: int = 500,
) -> None:
    centers = generate_centers(true_clusters, center_radius, seed=seed)
    points = generate_points(centers, points_per_cluster, spread, seed=seed)
    random.seed(seed)
    if init_mode == "sample":
        centroids = random.sample(points, k)
    else:
        all_x = [p[0] for p in points]
        all_y = [p[1] for p in points]
        min_x, max_x = min(all_x), max(all_x)
        min_y, max_y = min(all_y), max(all_y)
        centroids = [
            (random.uniform(min_x, max_x), random.uniform(min_y, max_y))
            for _ in range(k)
        ]
    colors = ["#55c2ff", "#ff6b6b", "#8bdc65", "#f1c453", "#9b59b6"]

    frames: List[Image.Image] = []
    for iteration in range(1, iterations + 1):
        assignments = assign_clusters(points, centroids)
        frames.append(
            render_frame(points, assignments, centroids, iteration, colors, (4, 3))
        )
        centroids = recompute_centroids(points, assignments, centroids)

    if not frames:
        raise RuntimeError("No frames generated.")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration_ms,
        loop=0,
    )


OUTPUT_PATH = Path("kmeans5-5.gif")
K = 5
TRUE_CLUSTERS = 5
ITERATIONS = 10
SEED = 23
POINTS_PER_CLUSTER = 70
SPREAD = 0.2
CENTER_RADIUS = 3.0
INIT_MODE = "random"  # "random" or "sample"
DURATION_MS = 1600

kmeans_gif(
    output_path=OUTPUT_PATH,
    k=K,
    true_clusters=TRUE_CLUSTERS,
    iterations=ITERATIONS,
    seed=SEED,
    points_per_cluster=POINTS_PER_CLUSTER,
    spread=SPREAD,
    center_radius=CENTER_RADIUS,
    init_mode=INIT_MODE,
    duration_ms=DURATION_MS,
)
