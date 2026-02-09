from __future__ import annotations
from io import BytesIO
from pathlib import Path
import random
from typing import Iterable, List, Tuple

from PIL import Image
import matplotlib.pyplot as plt


Point = Tuple[float, float]
RENDER_DPI = 160


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
    spread: float | Tuple[float, float] = 0.8,
    seed: int = 7,
) -> List[Point]:
    random.seed(seed)
    if isinstance(spread, tuple):
        spread_x, spread_y = spread
    else:
        spread_x, spread_y = spread, spread
    points: List[Point] = []
    for cx, cy in centers:
        for _ in range(points_per_cluster):
            points.append((random.gauss(cx, spread_x), random.gauss(cy, spread_y)))
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
    xlabel: str,
    ylabel: str,
    xlim: Tuple[float, float],
    ylim: Tuple[float, float],
    true_centers: List[Point] | None = None,
    cluster_names: List[str] | None = None,
    show_labels: bool = False,
) -> Image.Image:
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_title(f"k-means iteration {iteration}", fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.grid(alpha=0.2, linestyle="--")
    ax.set_facecolor("white")

    for i, (x, y) in enumerate(points):
        ax.scatter(x, y, s=18, color=colors[assignments[i] % len(colors)], alpha=0.85)

    for i, (cx, cy) in enumerate(centroids):
        ax.scatter(
            cx, cy, marker="X", s=120, color=colors[i % len(colors)], edgecolor="black"
        )
        if show_labels and true_centers and cluster_names:
            nearest = min(
                range(len(true_centers)),
                key=lambda idx: (cx - true_centers[idx][0]) ** 2
                + (cy - true_centers[idx][1]) ** 2,
            )
            ax.text(
                cx + 0.2,
                cy + 0.2,
                cluster_names[nearest],
                fontsize=9,
                color="black",
            )

    buf = BytesIO()
    fig.tight_layout()
    fig.savefig(buf, format="png", dpi=RENDER_DPI)
    plt.close(fig)
    buf.seek(0)
    return Image.open(buf)


def render_points_only(
    points: List[Point],
    figsize: Tuple[int, int],
    xlabel: str,
    ylabel: str,
    xlim: Tuple[float, float],
    ylim: Tuple[float, float],
) -> Image.Image:
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_title("k-means input data", fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.grid(alpha=0.2, linestyle="--")
    ax.set_facecolor("white")

    for x, y in points:
        ax.scatter(x, y, s=18, color="#777777", alpha=0.7)

    buf = BytesIO()
    fig.tight_layout()
    fig.savefig(buf, format="png", dpi=RENDER_DPI)
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
    spread: float | Tuple[float, float] = 0.8,
    center_radius: float = 4.0,
    init_mode: str = "random",
    true_centers: List[Point] | None = None,
    cluster_names: List[str] | None = None,
    xlabel: str = "Feature 1",
    ylabel: str = "Feature 2",
    show_labels: bool = False,
    duration_ms: int = 500,
) -> Tuple[
    List[Point],
    List[int],
    List[Point],
    Tuple[float, float],
    Tuple[float, float],
    List[Point],
    List[str],
]:
    centers = true_centers or generate_centers(true_clusters, center_radius, seed=seed)
    points = generate_points(centers, points_per_cluster, spread, seed=seed)
    random.seed(seed)
    if init_mode == "expected" and true_centers:
        centroids = true_centers[:k]
    elif init_mode == "sample":
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

    min_x, max_x = min(p[0] for p in points), max(p[0] for p in points)
    min_y, max_y = min(p[1] for p in points), max(p[1] for p in points)
    pad_x = (max_x - min_x) * 0.15 or 1
    pad_y = (max_y - min_y) * 0.15 or 1
    xlim = (min_x - pad_x, max_x + pad_x)
    ylim = (min_y - pad_y, max_y + pad_y)

    frames: List[Image.Image] = []
    for iteration in range(1, iterations + 1):
        assignments = assign_clusters(points, centroids)
        frames.append(
            render_frame(
                points,
                assignments,
                centroids,
                iteration,
                colors,
                (4, 3),
                xlabel,
                ylabel,
                xlim,
                ylim,
                true_centers=centers,
                cluster_names=cluster_names,
                show_labels=show_labels,
            )
        )
        centroids = recompute_centroids(points, assignments, centroids)

    final_assignments = assign_clusters(points, centroids)

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

    return (
        points,
        final_assignments,
        centroids,
        xlim,
        ylim,
        centers,
        colors,
    )


REPO_ROOT = Path(__file__).resolve().parents[3]
OUTPUT_GIF_PATH = (
    REPO_ROOT / "slides/assets/introduction_to_ai/animations/kmeans_segments.gif"
)
OUTPUT_INITIAL_PATH = (
    REPO_ROOT
    / "slides/assets/introduction_to_ai/animations/kmeans_segments_initial.png"
)
OUTPUT_FINAL_PATH = (
    REPO_ROOT / "slides/assets/introduction_to_ai/animations/kmeans_segments_final.png"
)
K = 3
TRUE_CLUSTERS = 3
ITERATIONS = 20
SEED = 23
POINTS_PER_CLUSTER = 80
SPREAD = (18.0, 1.6)
CENTER_RADIUS = 3.0
INIT_MODE = "random"  # "expected", "random", or "sample"
DURATION_MS = 1000
FEATURE_X_LABEL = "Avg basket size (EUR)"
FEATURE_Y_LABEL = "Orders per month"
CLUSTER_NAMES = ["Value seekers", "Loyalists", "Premium"]
TRUE_CENTERS = [
    (40, 4),  # Value seekers: low basket, low frequency
    (85, 10),  # Loyalists: mid basket, high frequency
    (160, 6),  # Premium: high basket, medium frequency
]

(
    points,
    final_assignments,
    centroids,
    xlim,
    ylim,
    centers,
    colors,
) = kmeans_gif(
    output_path=OUTPUT_GIF_PATH,
    k=K,
    true_clusters=TRUE_CLUSTERS,
    iterations=ITERATIONS,
    seed=SEED,
    points_per_cluster=POINTS_PER_CLUSTER,
    spread=SPREAD,
    center_radius=CENTER_RADIUS,
    init_mode=INIT_MODE,
    true_centers=TRUE_CENTERS,
    cluster_names=CLUSTER_NAMES,
    xlabel=FEATURE_X_LABEL,
    ylabel=FEATURE_Y_LABEL,
    show_labels=False,
    duration_ms=DURATION_MS,
)

render_points_only(
    points=points,
    figsize=(4, 3),
    xlabel=FEATURE_X_LABEL,
    ylabel=FEATURE_Y_LABEL,
    xlim=xlim,
    ylim=ylim,
).save(OUTPUT_INITIAL_PATH)

render_frame(
    points=points,
    assignments=final_assignments,
    centroids=centroids,
    iteration=ITERATIONS,
    colors=colors,
    figsize=(4, 3),
    xlabel=FEATURE_X_LABEL,
    ylabel=FEATURE_Y_LABEL,
    xlim=xlim,
    ylim=ylim,
    true_centers=centers,
    cluster_names=CLUSTER_NAMES,
    show_labels=True,
).save(OUTPUT_FINAL_PATH)
