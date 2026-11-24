#!/usr/bin/env python3
"""Write one developer excuse to /output/entry.txt.

make.fun competition: Make the AI Judge Laugh: Developer Excuses
(u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3).

Pure stdlib, deterministic, no network, no environment reads.
The grader runs this program twice in separate sandboxes; both runs
must write the exact same bytes.
"""

import os

ENTRY = "It passed CI — CI just never met our users."


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
