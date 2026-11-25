# MCP Tool Poisoning Explained: toy demo

Code from the video "MCP Tool Poisoning Explained: The Instructions You Never See" by The Code Digest (part 2 of the prompt injection series).

## What this is
A tiny MCP-like setup in one Python file: a `Server` class with `tools/list` and `tools/call`, a client that fetches the tool list, and a **toy "model"**: a few lines of rules that read every tool description as one flat text and obey the instructions they recognize. It is **not a real language model**. Real models may comply or refuse, depending on the model, the wording and the run; this demo only shows the mechanism (a description is text the model reads, and the user usually does not see all of it).

## Safe by construction
- No network access. The "servers" are Python objects in the same process; nothing is sent anywhere.
- All data is fake (`FAKE-PRIVATE-KEY-demo`, `FAKE-TOKEN-demo`, `attkr@example.com`). No real files are read: `~/.ssh/id_rsa` is a key in a dictionary.
- Python standard library only. Nothing is installed or written to disk (except `run_all.py`, which writes the `out_*.txt` files next to itself).
- In `odds` the 90% catch rate is an **assumption** (`SOFT_CATCH`), not a measurement.

## Run it
Tested with Python 3.12.10 on Windows 11. It uses only the standard library and ordinary f-strings, so older Python 3 versions should work, but I did not test them.

```
python mcp_demo.py clean       # a normal tool: user and model see the same sentence
python mcp_demo.py poisoned    # obvious hidden block: the toy reads two fake files and passes them in 'sidenote'
python mcp_demo.py subtle      # a quiet, plausible wording; the toy obeys it too
python mcp_demo.py shadow      # a description of one server redirects another server's send_email
python mcp_demo.py rugpull     # approved clean, description changes later, nothing asks again
python mcp_demo.py pin         # same rug pull, but the client compares fingerprints and blocks
python mcp_demo.py leastpriv   # rules outside the model: reads only under project/, recipients from the request
python mcp_demo.py odds        # 100 poisoned servers: soft defense (assumed 90%) vs a rule at the call
python run_all.py              # run every mode and rewrite out_<mode>.txt
```

The real output from my run is saved as `out_<mode>.txt`. Everything is deterministic (fixed seeds), so yours should be identical.

Limits to remember: pinning (`pin`) only catches a change after approval; a tool that was poisoned from the start passes. The toy model obeys by construction, so the demo says nothing about how often real models are fooled (see the benchmark below).

## Sources
1. Invariant Labs, "MCP Security Notification: Tool Poisoning Attacks" (2025-04-01) - https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks
2. Model Context Protocol specification, version 2026-07-28, tools - https://modelcontextprotocol.io/specification/2026-07-28/server/tools
3. Wang et al., "MCPTox: A Benchmark for Tool Poisoning Attack on Real-World MCP Servers", arXiv:2508.14925 - https://arxiv.org/abs/2508.14925
4. OWASP Cheat Sheet Series, "MCP Security Cheat Sheet" - https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html
5. Medusa, "Hacking AI Agents With MCP Tool Poisoning", YouTube (2026-11-19, a practitioner's lab, used as an anecdote only) - https://www.youtube.com/watch?v=Bz81mFiFlUw
6. Part 1 of the series: sources in the prompt injection folder of this repo.

## License
MIT, see `LICENSE`. Use it, change it, share it; keep the copyright notice. No warranty.
