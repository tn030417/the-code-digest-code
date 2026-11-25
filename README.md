# the-code-digest-code

Code from the videos of **The Code Digest**, one folder per video. Everything is MIT licensed (see `LICENSE`).

| Folder | Video | What it is |
|---|---|---|
| [`prompt-injection/`](prompt-injection/) | Prompt Injection Explained: Hijack an AI Agent in Python | A toy agent that shows how prompt injection works, plus three defenses. Fake data, no network. |
| [`mcp-tool-poisoning/`](mcp-tool-poisoning/) | MCP Tool Poisoning Explained: The Instructions You Never See | A toy MCP setup that shows hidden instructions in tool descriptions, shadowing and rug pulls, plus pinning and a rule outside the model. Fake data, no network. |
| [`rag-poisoning/`](rag-poisoning/) | RAG Poisoning Explained: How One Document Can Control the Answer | A tiny from-scratch retriever and a toy generator that show how one planted text can win the ranking and change the answer, plus source labels, controlled ingestion and their limit. Fake data, no network. |

Each folder has its own README with exact run commands and the real output from the video.
