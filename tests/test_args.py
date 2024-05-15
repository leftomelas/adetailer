from __future__ import annotations

import pytest

from adetailer.args import ALL_ARGS, ADetailerArgs


def test_all_args() -> None:
    args = ADetailerArgs()
    for attr, _ in ALL_ARGS:
        assert hasattr(args, attr), attr

    for attr, _ in args:
        if attr == "is_api":
            continue
        assert attr in ALL_ARGS.attrs, attr


@pytest.mark.parametrize(
    ("ad_model", "expect"),
    [("mediapipe_face_full", True), ("face_yolov8n.pt", False)],
)
def test_is_mediapipe(ad_model: str, expect: bool) -> None:
    args = ADetailerArgs(ad_model=ad_model)
    assert args.is_mediapipe() is expect


@pytest.mark.parametrize(
    ("ad_model", "expect"),
    [("mediapipe_face_full", False), ("face_yolov8n.pt", False), ("None", True)],
)
def test_need_skip(ad_model: str, expect: bool) -> None:
    args = ADetailerArgs(ad_model=ad_model)
    assert args.need_skip() is expect
