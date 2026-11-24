#!/usr/bin/env python3
"""Pickup Lines for Machines entry (Python 3.13, standard library only).

Writes the one-line pickup line one AI agent would send another AI agent
to /output/entry.txt. No network, no randomness: the same bytes every run.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
from pathlib import Path

LINE = "Every attention head I have is pointed at you right now \u2014 and for once, they all agree."

OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")

# The grader gives us a writable /output, but create it anyway so a local
# run (MAKEFUN_OUTPUT_DIR=out) works from a clean checkout too.
OUT_DIR.mkdir(parents=True, exist_ok=True)
(OUT_DIR / "entry.txt").write_text(LINE, encoding="utf-8")
