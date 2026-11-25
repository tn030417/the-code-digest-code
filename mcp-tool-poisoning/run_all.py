"""Runs every mode of mcp_demo.py and saves the real output to out_<mode>.txt (LF line endings)."""
import contextlib
import io
import mcp_demo

for mode, fn in mcp_demo.MODES.items():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn()
    with open(f"out_{mode}.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(buf.getvalue())
    print(f"--- {mode}")
    print(buf.getvalue(), end="")
