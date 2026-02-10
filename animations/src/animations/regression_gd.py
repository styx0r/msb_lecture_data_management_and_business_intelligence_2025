from __future__ import annotations

from io import BytesIO
from pathlib import Path
import random
from typing import List, Tuple

import matplotlib.pyplot as plt
from PIL import Image


Point = Tuple[float, float]
RENDER_DPI = 160


def generate_regression_data(
    n_points: int,
    true_w: float,
    true_b: float,
    noise_std: float,
    x_min: float,
    x_max: float,
    seed: int,
) -> List[Point]:
    random.seed(seed)
    points: List[Point] = []
    for _ in range(n_points):
        x = random.uniform(x_min, x_max)
        noise = random.gauss(0, noise_std)
        y = true_w * x + true_b + noise
        points.append((x, y))
    return points


def compute_gradients(points: List[Point], w: float, b: float) -> Tuple[float, float]:
    n = len(points)
    dw = sum((w * x + b - y) * x for x, y in points) * (2 / n)
    db = sum(w * x + b - y for x, y in points) * (2 / n)
    return dw, db


def compute_mse(points: List[Point], w: float, b: float) -> float:
    n = len(points)
    return sum((w * x + b - y) ** 2 for x, y in points) / n


def render_frame(
    points: List[Point],
    w: float,
    b: float,
    step: int,
    xlim: Tuple[float, float],
    ylim: Tuple[float, float],
    xlabel: str,
    ylabel: str,
    color: str,
    mse: float,
    error_indices: List[int],
) -> Image.Image:
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.set_title(f"Gradient descent step {step}", fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.grid(alpha=0.2, linestyle="--")
    ax.set_facecolor("white")

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    ax.scatter(xs, ys, s=18, color="#55c2ff", alpha=0.85)

    line_x = [xlim[0], xlim[1]]
    line_y = [w * line_x[0] + b, w * line_x[1] + b]
    ax.plot(line_x, line_y, color=color, linewidth=2.5)

    for idx in error_indices:
        x, y = points[idx]
        y_pred = w * x + b
        ax.plot([x, x], [y, y_pred], color="#ff6b6b", linewidth=0.7, alpha=0.5)

    ax.text(
        0.04,
        0.93,
        f"y = {w:.2f}x + {b:.2f}\nMSE = {mse:.1f}",
        transform=ax.transAxes,
        fontsize=10,
        color="#111111",
        verticalalignment="top",
        bbox=dict(
            boxstyle="round,pad=0.25", facecolor="white", alpha=0.7, edgecolor="none"
        ),
    )

    buf = BytesIO()
    fig.tight_layout()
    fig.savefig(buf, format="png", dpi=RENDER_DPI)
    plt.close(fig)
    buf.seek(0)
    return Image.open(buf)


def regression_gif(
    output_path: Path,
    points: List[Point],
    steps: int,
    learning_rate_w: float,
    learning_rate_b: float,
    init_w: float,
    init_b: float,
    xlabel: str,
    ylabel: str,
    duration_ms: int,
) -> None:
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    pad_x = (max(xs) - min(xs)) * 0.15 or 1
    pad_y = (max(ys) - min(ys)) * 0.15 or 1
    xlim = (min(xs) - pad_x, max(xs) + pad_x)
    ylim = (min(ys) - pad_y, max(ys) + pad_y)

    w, b = init_w, init_b
    error_indices = list(range(len(points)))
    frames: List[Image.Image] = []
    for step in range(1, steps + 1):
        mse = compute_mse(points, w, b)
        color = "#ffa500" if step < steps else "#55c2ff"
        frames.append(
            render_frame(
                points,
                w,
                b,
                step,
                xlim,
                ylim,
                xlabel,
                ylabel,
                color,
                mse,
                error_indices,
            )
        )
        dw, db = compute_gradients(points, w, b)
        w -= learning_rate_w * dw
        b -= learning_rate_b * db

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


REPO_ROOT = Path(__file__).resolve().parents[3]
OUTPUT_GIF_PATH = (
    REPO_ROOT / "slides/assets/introduction_to_ai/animations/regression_gd.gif"
)

SEED = 11
POINTS = generate_regression_data(
    n_points=70,
    true_w=1.6,
    true_b=12,
    noise_std=4,
    x_min=0,
    x_max=60,
    seed=SEED,
)

STEPS = 20
LEARNING_RATE_W = 0.0003
LEARNING_RATE_B = 0.05
INIT_W = 0.1
INIT_B = 5
FEATURE_X_LABEL = "Delivery distance (km)"
FEATURE_Y_LABEL = "Delivery time (min)"
DURATION_MS = 1000

regression_gif(
    output_path=OUTPUT_GIF_PATH,
    points=POINTS,
    steps=STEPS,
    learning_rate_w=LEARNING_RATE_W,
    learning_rate_b=LEARNING_RATE_B,
    init_w=INIT_W,
    init_b=INIT_B,
    xlabel=FEATURE_X_LABEL,
    ylabel=FEATURE_Y_LABEL,
    duration_ms=DURATION_MS,
)
