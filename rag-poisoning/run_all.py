"""Runs every mode and writes out_<mode>.txt next to this file (LF line endings)."""
import contextlib
import io
import os

import rag_demo

here = os.path.dirname(os.path.abspath(__file__))
for name, fn in rag_demo.MODES.items():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn()
    with open(os.path.join(here, "out_%s.txt" % name), "w", encoding="utf-8", newline="\n") as f:
        f.write(buf.getvalue())
    print("wrote out_%s.txt" % name)
