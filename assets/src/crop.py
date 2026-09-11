#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""只裁掉 PNG 上下的多余白边，宽度保持不变（保证所有图统一宽度）。

用亮度阈值 + LUT 找"真正有内容"的行，避免极淡的 box-shadow 像素把 bbox 撑大。
"""
import glob
import os

from PIL import Image

KEEP = 56    # 上下各保留的边距（像素，2x 渲染下 = 视觉 28px）
THRESH = 238  # 暗于此亮度才算"有内容"
LUT = [255] * THRESH + [0] * (256 - THRESH)  # 暗像素 -> 255（非零，bbox 才认）


def trim(path: str) -> None:
    im = Image.open(path).convert("L")
    w, h = im.size
    bbox = im.point(LUT).getbbox()
    if not bbox:
        return
    top = max(0, bbox[1] - KEEP)
    bottom = min(h, bbox[3] + KEEP)
    if bottom - top < h:
        Image.open(path).crop((0, top, w, bottom)).save(path, optimize=True)
        print(f"  crop {os.path.basename(path)}: {h} -> {bottom - top}")


if __name__ == "__main__":
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    for p in sorted(glob.glob(os.path.join(root, "*.png"))):
        if os.path.basename(p).startswith("_"):
            continue
        trim(p)
