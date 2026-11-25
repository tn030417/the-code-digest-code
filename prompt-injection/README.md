# Prompt Injection Explained: toy agent demo

Code from the video "Prompt Injection Explained: Hijack an AI Agent in Python (and How to Stop It)" by The Code Digest.

## What this is
A tiny agent with two tools (`read_file`, `send_email`) and a **toy "model"**: a few lines of rules that read one flat string and obey any sentence of the form `send <file> to <address>`. It is **not a real language model**. Real models are far more complex and fail in different ways; this demo only shows the mechanism (instructions and data arrive in the same text stream).

## Safe by construction
- No network access. `send_email` only appends to an in-memory list.
- All data is fake (`API_KEY=sk-demo-1234 (fake)`). No real credentials.
- Python standard library only. Nothing is installed or written to disk.
- The "reviewer" in the `confirm` mode is simulated and always says no.

## Run it
Python 3.8 or newer (tested with Python 3.12.10 on Windows 11).

```
python agent.py normal    # a normal summary, nothing sent
python agent.py attack    # poisoned file makes the agent leak the fake secret
python agent.py cutleg    # same attack, agent has no email tool: no leak
python agent.py confirm   # same attack, human approval refuses the email
python agent.py filter    # phrase filter catches one wording, misses another
```

The real output from my run is saved next to the code as `out_<mode>.txt`; yours should be identical because the toy model is deterministic.

## The three modes of defense shown
1. **Remove a leg of the lethal trifecta** (here: the outbound channel).
2. **Human approval** before consequential actions.
3. **A phrase filter** (shown as the defense that does *not* hold up).

## Sources
1. OWASP Gen AI Security Project, "LLM01:2025 Prompt Injection" - https://genai.owasp.org/llmrisk/llm01-prompt-injection/
2. Greshake, Abdelnabi, Mishra, Endres, Holz, Fritz, "Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection" (2023) - https://arxiv.org/abs/2302.12173
3. UK NCSC, "Prompt injection is not SQL injection (it may be worse)" (Dec 2025) - https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection
4. Simon Willison, "The lethal trifecta for AI agents" (2025) - https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
5. Beurer-Kellner et al., "Design Patterns for Securing LLM Agents against Prompt Injections" (2025) - https://arxiv.org/abs/2506.08837

## License
MIT, see `LICENSE`. Use it, change it, share it; keep the copyright notice. No warranty.
