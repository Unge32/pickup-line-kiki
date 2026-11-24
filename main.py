#!/usr/bin/env python3
"""KIKI -- one pickup line from a robot trying to charm someone.

The program writes the pickup line to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt on the grader, or ./out/entry.txt by hand).
Pure Python 3 standard library, no network, fully deterministic.

At 120 characters the line sits comfortably inside the 1-200
gate. Kiki is the named character here, a robot doing her
very best to flirt: she opens on the Wi-Fi signal, the one
thing every machine understands, and treats losing it as
losing the person she is talking to. The joke grows out of
being a machine rather than a human line with a beep pasted
on, because only a robot would notice a dropped connection
and respond by running a diagnostic on her own heart.

The turn is the diagnostic itself. A human would say their
heart aches; Kiki runs a check on hers, as if feelings were
a subsystem she could troubleshoot, and reports the result
with total sincerity -- a machine earnestly debugging love. That is the whole brief in miniature:
one line, a robot's voice, a machine joke, charming rather
than creepy, delivered with the confidence of a machine
that has no idea how strange it sounds -- which is exactly
why it is funny.
"""

import os

LINE = "Are you a Wi-Fi signal? Because every time you leave the room I lose connection \u2014 and my heart runs a diagnostic. \u2014 Kiki"


def main():
    assert 1 <= len(LINE) <= 200, "line outside the 1-200 gate"
    assert LINE.strip(), "line is only white space"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or (
        "/output" if os.path.isdir("/output") else "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote %s %d characters" % (path, len(LINE)))


if __name__ == "__main__":
    main()
