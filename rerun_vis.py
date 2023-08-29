import pickle
import sys
from pathlib import Path

import numpy as np
import rerun as rr
from numpy.typing import ArrayLike
from scipy.spatial.transform import Rotation as R


def rr_log_box(
    rr_path: str,
    boxes: ArrayLike,
    color=(255, 0, 0),
    uncertainty: ArrayLike | None = None,
):
    boxes = np.array(boxes)  # (N, 7)
    uncertainty_labels = None
    if uncertainty is not None:
        uncertainty = np.mean(uncertainty, axis=-1)
        uncertainty_labels = [f"{unc:.4f}" for unc in uncertainty]
    rr.log_obbs(
        rr_path,
        half_sizes=boxes[:, 3:6] / 2,
        positions=boxes[:, :3],
        rotations_q=R.from_euler("z", boxes[:, 6], degrees=False).as_quat(),
        colors=color,
        labels=uncertainty_labels,
    )


def rr_log_frame(rr_path: str, frame_data: dict):
    pass


if __name__ == "__main__":
    # filepath = Path(sys.argv[1])
    # with open(filepath, "rb") as f:
    #     draw_data = pickle.load(f)
    rr.init("viewer", spawn=True)
    for i, data_path in enumerate(Path(sys.argv[1]).iterdir()):
        with open(data_path, "rb") as f:
            draw_data = pickle.load(f)
        if not data_path.stem.isdigit():
            continue

        if not draw_data["boxes"].shape[0] >= 1:
            continue
        if not draw_data["gt_boxes"].shape[0] >= 1:
            continue
        rr.set_time_sequence("frame_id", int(data_path.stem))
        rr.set_time_sequence("id", i)

        rr.log_points("points", draw_data["points"][:, 1:], colors=(255, 255, 255))
        rr_log_box(
            "boxes",
            draw_data["boxes"],
            color=(255, 0, 0),
            uncertainty=draw_data["uncertainty"],
        )
        rr_log_box("gt_boxes", draw_data["gt_boxes"], color=(0, 255, 0))