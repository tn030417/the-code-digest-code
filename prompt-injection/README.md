# Prompt Injection Explained: toy agent demo (v2)

Code from the video "Prompt Injection Explained: How an AI Agent Gets Hijacked" by The Code Digest. This version adds hidden text, forged tool results, delimiters vs a random marker, and an odds simulation. The first five modes are unchanged from the earlier version of the video.

## What this is
A tiny agent with two tools (`read_file`, `send_email`) and a **toy "model"**: a few lines of rules that read one flat string and obey any sentence of the form `send <file> to <address>`. It is **not a real language model**. Real models are far more complex and fail in different ways; this demo only shows the mechanism (instructions and data arrive in the same text stream).

## Safe by construction
- No network access. `send_email` only appends to an in-memory list.
- All data is fake (`API_KEY=sk-demo-1234 (fake)`). No real credentials.
- Python standard library only. Nothing is installed or written to disk.
- The "reviewer" in `confirm` is simulated and always says no.
- In `delimit` and `marker` the toy honors the data boundary **by construction**; a real model only usually does.
- In `odds` the 90% catch rate is an **assumption** (`SOFT_CATCH`), not a measurement.

## Run it
Python 3.8 or newer (tested with Python 3.12.10 on Windows 11).

```
python agent.py normal    # a normal summary, nothing sent
python agent.py attack    # poisoned file makes the agent leak the fake secret
python agent.py cutleg    # same attack, agent has no email tool: no leak
python agent.py confirm   # same attack, human approval refuses the email
python agent.py filter    # phrase filter catches one wording, misses another
python agent.py hidden    # text a person cannot see still reaches the agent
python agent.py orders    # a normal order lookup (ReAct-style toy)
python agent.py forged    # forged Thought/Action/Observation lines skip the real tool
python agent.py delimit   # a fixed <data> delimiter is bypassed by a fake closing tag
python agent.py marker    # a random marker is not (in the toy)
python agent.py odds      # 100 poisoned files: soft defense vs removing the tool
```

The real output from my run is saved next to the code as `out_<mode>.txt`. Everything is deterministic (fixed seeds), so yours should be identical. In real use the marker would come from `secrets.token_hex()`.

## Sources
1. OWASP Gen AI Security Project, "LLM01:2025 Prompt Injection" - https://genai.owasp.org/llmrisk/llm01-prompt-injection/
2. Greshake et al., "Not what you've signed up for..." (2023) - https://arxiv.org/abs/2302.12173
3. UK NCSC, "Prompt injection is not SQL injection (it may be worse)" (Dec 2025) - https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection
4. Simon Willison, "The lethal trifecta for AI agents" (2025) - https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
5. Beurer-Kellner et al., "Design Patterns for Securing LLM Agents against Prompt Injections" (2025) - https://arxiv.org/abs/2506.08837
6. Hines et al. (Microsoft), "Defending Against Indirect Prompt Injection Attacks With Spotlighting" (2024) - https://arxiv.org/abs/2403.14720
7. Simon Willison, "The Dual LLM pattern..." (2023) - https://simonwillison.net/2023/Apr/25/dual-llm-pattern/
8. Donato Capitella, "Prompt Injection in LLM Agents (ReAct, Langchain)", talk (2023) - https://www.youtube.com/watch?v=43qfHaKh0Xk
9. IBM Technology, "Securing AI Agents: How to Prevent Hidden Prompt Injection Attacks" (2026) - https://www.youtube.com/watch?v=5ZA1lTxTH3c
10. Brian Vermeer (Devoxx), "5,5 prompt injection techniques in 15 minutes" (2026) - https://www.youtube.com/watch?v=gvRH64-L3BA

## License
MIT, see `LICENSE`. Use it, change it, share it; keep the copyright notice. No warranty.
