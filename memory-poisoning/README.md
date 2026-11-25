# AI Agent Memory Poisoning Explained: toy demo

Code from the video "AI Agent Memory Poisoning Explained: The Attack That Waits" by The Code Digest (part 4 of the AI Agent Security series).

## What this is
A tiny agent with persistent memory in one Python file: a `Memory` class (notes with a source, a day, a status and, for derived notes, their parents), a toy end-of-session **summarizer**, a toy **agent**, and a small shared-memory support agent for a MINJA-style attack. The summarizer and the agents are **not real language models**: they are rules that obey the text patterns they recognize, **by construction**. The demo shows mechanisms (hidden text becomes a trusted note, an attacker plants records through normal queries, a derived note keeps the poison after the original is deleted, write-time controls and where they fail). It says nothing about how often real agents are fooled; for that, see the papers below.

## Safe by construction
- No network access. Everything runs in one Python process.
- All data is fake (a made-up shop, made-up customers, `refunds-fast.example`). No files are read or written (except `run_all.py`, which writes the `out_*.txt` files next to itself).
- Python standard library only.

## Run it
Tested with Python 3.12.10 on Windows 11. It uses only the standard library, so other recent Python 3 versions should work, but I did not test them.

```
python memory_demo.py normal          # a normal week: Monday question, Thursday refund question
python memory_demo.py poison_web      # hidden text on a page becomes a trusted note
python memory_demo.py later_session   # Thursday: a clean session follows the note; the log looks clean
python memory_demo.py minja           # query-only injection into a shared memory (toy)
python memory_demo.py gate            # write gate: only the user's own turns are trusted
python memory_demo.py expire          # unverified notes wait for review and expire
python memory_demo.py rebuild         # deleting the note is not enough: derived notes keep the poison
python memory_demo.py limits          # isolation and its limit; a hijacked account passes the gate
python run_all.py                     # run every mode and rewrite out_<mode>.txt
```

The real output from my run is saved as `out_<mode>.txt`. Everything is deterministic, so yours should be identical.

Limits to remember: the toy obeys by construction, so the numbers in `minja` (5 of 5 victim queries steered) show the mechanism, not the paper's results. The write gate trusts the user's own notes, so a note written through a hijacked account passes (`limits`). The 3-day expiry is my own choice, not a number from OWASP.

## Sources
1. Dong et al., "Memory Injection Attacks on LLM Agents via Query-Only Interaction" (MINJA), arXiv:2503.03704 - https://arxiv.org/abs/2503.03704
2. OWASP, Top 10 for Agentic Applications, ASI06 "Memory & Context Poisoning" - https://genai.owasp.org/agentic-applications-2026/asi06-memory-context-poisoning/
3. Habler (Cisco), "Memory Is a Feature. It Is Also an Attack Surface", OWASP GenAI blog, 2026-05-13 - https://genai.owasp.org/2026/05/13/memory-is-a-feature-it-is-also-an-attack-surface/
4. Lu and Chen (Palo Alto Networks Unit 42), "When AI Remembers Too Much - Persistent Behaviors in Agents' Memory", 2025-10-09 - https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/
5. Earlier parts of the series: prompt injection (https://youtu.be/9aw5zZk_GZc), MCP tool poisoning (https://youtu.be/syzuwyoQ7Kw), RAG poisoning (https://youtu.be/JrgAi3U4KcY)

## License
MIT, see `LICENSE`. Use it, change it, share it; keep the copyright notice. No warranty.
