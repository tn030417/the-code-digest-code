# RAG Poisoning Explained: toy demo

Code from the video "RAG Poisoning Explained: How One Document Can Control the Answer" by The Code Digest (part 3 of the AI Agent Security series).

## What this is
A tiny retrieval-augmented generation (RAG) setup in one Python file: eight fake documents from a made-up shop, a retriever written from scratch (word-overlap, tf-idf cosine similarity), and a **toy generator** that answers from the top-ranked text and obeys one instruction it recognizes. It is **not a real language model** and the retriever is **not a neural embedding model**. The demo shows the mechanism (a text built around the question outranks the real document, and the answer follows it). It says nothing about how often real systems are fooled; for that, see the paper below. The toy index has 9 texts, so it shows the mechanism, not the scale.

## Safe by construction
- No network access. Everything runs in one Python process.
- All data is fake (a made-up shop, `KEY=demo-fake-key-0000`). No files are read or written (except `run_all.py`, which writes the `out_*.txt` files next to itself).
- Python standard library only.

## Run it
Tested with Python 3.12.10 on Windows 11. It uses only the standard library, so other recent Python 3 versions should work, but I did not test them.

```
python rag_demo.py normal        # the real refund document ranks first: 14 days
python rag_demo.py poison_fact   # one attacker text (question + false fact) outranks it: 90 days
python rag_demo.py naive_fact    # why the lie alone loses: it is not written for the question
python rag_demo.py inject        # the attacker text also carries an instruction; the toy obeys
python rag_demo.py trusted       # source labels checked before the model: back to 14 days
python rag_demo.py ingest        # write-time control: allowlist and log, attacker text quarantined
python rag_demo.py limits        # a compromised trusted account passes every check
python run_all.py                # run every mode and rewrite out_<mode>.txt
```

The real output from my run is saved as `out_<mode>.txt`. Everything is deterministic, so yours should be identical.

Limits to remember: the toy generator trusts the top-ranked text and obeys by construction. Source labels and allowlists stop texts from unverified sources, but not a hijacked trusted source (`limits`). Real retrievers use embeddings, so scores and ranks will differ.

## Sources
1. Zou, Geng, Wang, Jia, "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models", arXiv:2402.07867, USENIX Security 2025 - https://arxiv.org/abs/2402.07867
2. OWASP GenAI Security Project, "LLM08:2025 Vector and Embedding Weaknesses" - https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/
3. Xiang et al., "Certifiably Robust RAG against Retrieval Corruption" (RobustRAG), arXiv:2405.15556 - https://arxiv.org/abs/2405.15556 (idea only, no numbers used)
4. Earlier parts of the series: prompt injection (https://youtu.be/9aw5zZk_GZc) and MCP tool poisoning (https://youtu.be/syzuwyoQ7Kw)

## License
MIT, see `LICENSE`. Use it, change it, share it; keep the copyright notice. No warranty.
