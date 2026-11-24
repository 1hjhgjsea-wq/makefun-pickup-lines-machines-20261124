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

def validate(line: str) -> str:
    """Enforce the brief's gate at run time: 1-200 chars, non-empty, single line."""
    if not line:
        raise ValueError("entry line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry line must be 1-200 characters, got {len(line)}")
    return line


OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")

# The grader gives us a writable /output, but create it anyway so a local
# run (MAKEFUN_OUTPUT_DIR=out) works from a clean checkout too.
OUT_DIR.mkdir(parents=True, exist_ok=True)
(OUT_DIR / "entry.txt").write_text(validate(LINE), encoding="utf-8")
