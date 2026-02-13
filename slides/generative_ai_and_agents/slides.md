Where are we located during the lecture?

<img
  src="../assets/generative_ai_and_agents/imgs/imgs.001.png"
  alt="Overview"
  style="
    width: 800px;
    margin: 0 auto 4rem auto;
    background: transparent;
  "
/>

---

One more class of machine learning models:

<img
  src="../assets/generative_ai_and_agents/imgs/imgs.002.png"
  alt="Overview"
  style="
    width: 800px;
    margin: 0 auto 4rem auto;
    background: transparent;
  "
/>

--

#### What is generative AI?

- synthetic data / content creation
- probabilistic modeling
  - given data, generative models learn to imitate data / to sample data

--

#### Generative Adversarial Networks (GANs)

<img
  src="../assets/generative_ai_and_agents/imgs/imgs.003.png"
  alt="Overview"
  style="
    width: 800px;
    margin: 0 auto 4rem auto;
    background: transparent;
  "
/>

--

### Encoder - Decoder Models

<img
  src="../assets/generative_ai_and_agents/imgs/imgs.004.png"
  alt="Overview"
  style="
    width: 800px;
    margin: 0 auto 0rem auto;
    background: transparent;
  "
/>

<span style="color: lightgreen;">How does the training data look like?</span>

---

https://www.lakera.ai/blog/large-language-models-guide#how-are-large-language-models-trained

Large Language Models (LLMs) — abstract view

- Buzzwords: next-token prediction, probability distribution
- Prepare: tiny next-word example with probabilities

--

#### What is different from latest LLM (> 2017) compared to preview architectures

transformer architecture image

- transformer architecture allows for efficient large scale computation
- attention mechanism allows the model to focus on relevant part whlie disregarding the reest
- attention mechanism captures dependencies between words and therefore improve context understanding

--

#### Inference / Prediction

<img
  src="../assets/generative_ai_and_agents/imgs/imgs.005.png"
  alt="Overview"
  style="
    width: 800px;
    margin: 0 auto 0rem auto;
    background: transparent;
  "
/>

--

#### <span style="color: orange;">Wait what is the LLM predicting exactly, is it a token?</span>

--

<img
  src="../assets/generative_ai_and_agents/imgs/imgs.006.png"
  alt="Overview"
  style="
    width: 800px;
    margin: 0 auto 0rem auto;
    background: transparent;
  "
/>

--

#### A detour into the training phase

--

<img
  src="../assets/generative_ai_and_agents/animations/llm_training_step_0.gif"
  alt="Overview"
  style="
    width: 800px;
    margin: 0 auto 0rem auto;
    background: transparent;
  "
/>

---

Upscaling upscaling upscaling

show evolution of number of parameters over time

TODO for students: calculate memory and number of graphic cards needed to run such a model based on number of parameters

---

How LLMs learn

- Buzzwords: massive text corpora, self-supervision, loss
- Prepare: "predict next word" training loop sketch

---

Words as numbers

- Buzzwords: tokens, embeddings, vectors
- Prepare: simple tokenization + embedding visualization

---

Context vs. world knowledge

- Buzzwords: prompt, context window, memorization vs. generalization
- Prepare: show "grounded info" vs. "model memory"

---

Limitations of LLMs

- Buzzwords: hallucinations, stale knowledge, context limits
- Prepare: 2-3 failure examples (fabricated citation, outdated fact)

---

---

Vector databases: why they exist

- Buzzwords: semantic search, similarity, nearest neighbors
- Prepare: contrast keyword search vs. semantic search

---

What is a vector?

- Buzzwords: high-dimensional point, embedding space
- Prepare: 2D sketch showing similar points close together

---

How vector search works

- Buzzwords: cosine similarity, k-NN, indexing
- Prepare: small diagram of query vector → nearest matches

---

Grounding with vector search (RAG)

- Buzzwords: retrieve, augment, generate
- Prepare: pipeline diagram: query → retrieve → prompt → answer

---

Agents: from models to actions

- Buzzwords: goal, plan, tools, feedback loop
- Prepare: simple agent loop diagram

---

AI Agent + Tools

- Buzzwords: tool calls, function interfaces, safety bounds
- Prepare: example tool list (search, calendar, DB)

---

MCP (Model Context Protocol)

- Buzzwords: standardization, tool discovery, connectors
- Prepare: simple client ↔ MCP server ↔ tool diagram
- USB C picture: from many standards to just one (https://www.faz.net/pro/digitalwirtschaft/kuenstliche-intelligenz/model-context-protocol-was-hinter-dem-neuen-standard-steckt-accg-200509814.html?premium=0xf96cbe2e76e7b601506905a135ed225333d725af0ec8d8cfde2e0ebb68da798c&share=androidfaznativeshare&gift)

---

ReAct agent

- Buzzwords: reasoning + acting, trace, iterate
- Prepare: 3-step thought/action/observation sequence

---

Deep Agent

- Buzzwords: subagents, delegation, parallel tasks
- Prepare: supervisor + workers diagram

---

ACP (Agent Communication Protocol)

- Buzzwords: inter-agent messaging, coordination
- Prepare: multi-agent message flow sketch

---
