<style>
  /* Keep images inside slide bounds (no cropping in presentation mode) */
  .img-full {
    max-width: 100%;
    max-height: 60vh;
    width: 100%;
    height: auto;
    object-fit: contain;
    margin: 0.25rem auto 0 auto;
    background: transparent;
    display: block;
  }

  .img-medium {
    max-width: 100%;
    max-height: 52vh;
    width: 90%;
    height: auto;
    object-fit: contain;
    margin: 0.25rem auto 0 auto;
    background: transparent;
    display: block;
  }

  .img-small {
    max-width: 100%;
    max-height: 44vh;
    width: 70%;
    height: auto;
    object-fit: contain;
    margin: 0.25rem auto 0 auto;
    background: transparent;
    display: block;
  }

  .img-tall {
    max-width: 100%;
    max-height: 66vh;
    width: 75%;
    height: auto;
    object-fit: contain;
    margin: 0.25rem auto 0 auto;
    background: transparent;
    display: block;
  }

  .two-col {
    display: flex;
    gap: 2rem;
    align-items: center;
    justify-content: space-between;
  }

  .two-col > div {
    flex: 1;
  }

  .three-col {
    display: flex;
    gap: 1.5rem;
    align-items: flex-start;
    justify-content: space-between;
  }

  .three-col > div {
    flex: 1;
  }

  .box {
    border: 2px solid rgba(255, 255, 255, 0.35);
    border-radius: 14px;
    padding: 0.8rem 1rem;
  }

  .muted {
    opacity: 0.85;
  }

  .tiny {
    font-size: 0.6em;
  }

  .section {
    text-align: center;
    padding: 2.5rem 1rem;
    border: 2px solid rgba(255, 255, 255, 0.25);
    border-radius: 18px;
  }

  .section .kicker {
    letter-spacing: 0.2em;
    text-transform: uppercase;
    font-size: 0.65em;
    opacity: 0.85;
  }

  .section .title {
    margin-top: 0.6rem;
    font-size: 1.55em;
  }

  .section .subtitle {
    margin-top: 0.6rem;
    font-size: 0.85em;
    opacity: 0.85;
  }

  table.taskmap {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.82em;
  }
  table.taskmap th,
  table.taskmap td {
    border: 1px solid rgba(255, 255, 255, 0.18);
    padding: 0.35rem 0.5rem;
    text-align: center;
  }
  table.taskmap th {
    color: lightgreen;
    font-weight: 600;
  }
  table.taskmap td:first-child {
    text-align: left;
    color: rgba(255, 255, 255, 0.92);
    font-weight: 600;
  }
</style>

<!-- ========================================================= -->
<!-- 0) Opening -->
<!-- ========================================================= -->

### Agenda (90 min)

- <span style="color: lightgreen;">Where AI comes from</span>: history as a story
- <span style="color: lightgreen;">Foundations</span>: paradigms + representation + first algorithms
- <span style="color: lightgreen;">Learning types</span> (5 buckets)
- <span style="color: lightgreen;">Core task families</span> (what we solve)
- <span style="color: lightgreen;">Why models work (or fail)</span>
- <span style="color: lightgreen;">Classical ML toolbox</span>
- <span style="color: lightgreen;">Deep learning essentials</span> (no transformers today)

Note:
- Format: visual-first slides; speaker notes contain the talk track + sources.
- Thread: we’ll use a recurring BI/Data Science example — an e-commerce company (“ShopNow”).

---

### Why AI matters (especially for BI)

<div class="two-col">
  <div>
    <img
      src="../assets/introduction_to_ai/imgs/ai_hero.jpg"
      alt="Artificial Intelligence illustration"
      class="img-medium"
    />
  </div>
  <div class="box" style="text-align: left; font-size: 0.85em">
    <div style="color: lightgreen; font-size: 0.95em">From dashboards to decisions</div>
    <ul class="muted" style="margin-top: 0.55rem">
      <li><span style="color: orange;">Prediction</span>: demand, churn, delivery delay</li>
      <li><span style="color: orange;">Detection</span>: fraud, anomalies, quality issues</li>
      <li><span style="color: orange;">Automation</span>: summaries, routing, recurring analysis</li>
      <li><span style="color: orange;">Interfaces</span>: “chat with your data”</li>
    </ul>
  </div>
</div>

Note:
- One message: BI becomes more valuable when it drives action, not only reporting.
- ShopNow example: reduce chargebacks, keep inventory healthy, and improve search/recommendations.
Source (image): https://commons.wikimedia.org/wiki/File:Artificial-Intelligence.jpg

---

<!-- ========================================================= -->
<!-- 1) Where AI comes from (history as story) -->
<!-- ========================================================= -->

<div class="section">
  <div class="kicker">1) Where AI comes from</div>
  <div class="title">History as a story</div>
  <div class="subtitle">From rules and search → learning from data</div>
</div>

Note:
- Goal: give a narrative that explains why ML/deep learning took over many tasks.

---

### Timeline overview (big picture)

<div style="position: relative; width: 100%; max-width: 100%">
  <img
    src="../assets/introduction_to_ai/imgs/ai_history_timeline.jpg"
    alt="AI history timeline"
    class="img-full"
  />
  <!-- Hide the “modern GenAI” part: next lecture -->
  <div
    style="
      position: absolute;
      top: 0;
      right: 0;
      width: 26%;
      height: 100%;
      background: rgba(0, 0, 0, 0.72);
      border-left: 2px solid rgba(255, 255, 255, 0.18);
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 0.6rem;
    "
  >
    <div>
      <div style="color: orange; font-weight: 700">Next lecture</div>
      <div class="tiny muted" style="margin-top: 0.35rem">
        Generative AI & Agents
      </div>
    </div>
  </div>
</div>

Note:
- Use as map, then zoom into characters + turning points.
- In this lecture we stop around AlphaGo; the modern GenAI part is next lecture.
Source: https://commons.wikimedia.org/wiki/File:AI-History-Timeline-300dpi.jpg

---

### Alan Turing: the question + the test

<img
  src="../assets/introduction_to_ai/imgs/alan_turing_1936.jpg"
  alt="Alan Turing portrait"
  class="img-small"
/>

<div class="muted" style="margin-top: 0.4rem">
  “Can machines think?” → test behavior, not philosophy
</div>

Note:
- Teaching point: “intelligence” becomes a measurable goal/metric.
- ShopNow analogy: “reduce fraud” becomes a measurable objective (chargebacks, false positives, review rate).
Source: https://commons.wikimedia.org/wiki/File:Alan_Turing_(1912-1954)_in_1936_at_Princeton_University.jpg

---

### Dartmouth / early optimism (term “AI”)

<div class="two-col">
  <div>
    <img
      src="../assets/introduction_to_ai/imgs/dartmouth_1959.jpg"
      alt="Dartmouth College (1959)"
      class="img-small"
      style="width: 85%"
    />
  </div>
  <div>
    <img
      src="../assets/introduction_to_ai/imgs/john_mccarthy_2006.jpg"
      alt="John McCarthy"
      class="img-small"
      style="width: 85%"
    />
  </div>
</div>

Note:
- Dartmouth workshop (1956): “AI” as a named research agenda.
Sources:
- Dartmouth photo: https://commons.wikimedia.org/wiki/File:Buttermilk_Dartmouth_1959_(51180053141).jpg
- McCarthy photo: https://commons.wikimedia.org/wiki/File:John_McCarthy_(computer_scientist)_Stanford_2006_(272020300).jpg

---

### Symbolic era → reasoning with rules and search

<img
  src="../assets/introduction_to_ai/imgs/shakey_robot_1969.jpg"
  alt="Shakey the robot"
  class="img-medium"
/>

Note:
- Symbolic AI: explicit knowledge (logic, rules) + search/planning.
- ShopNow tie-in: rules still matter (compliance/eligibility), but patterns like fraud are “adaptive”.
Source: https://commons.wikimedia.org/wiki/File:SRI_Shakey_robot,_1969,_Computer_History_Museum.jpg

---

### Expert systems (1970s–1980s)

<div class="three-col">
  <div class="box" style="text-align: left">
    <div style="color: orange">Knowledge base</div>
    <div class="muted" style="margin-top: 0.5rem">
      rules + facts
      <br />
      “IF X AND Y THEN Z”
    </div>
  </div>
  <div class="box" style="text-align: left">
    <div style="color: orange">Inference engine</div>
    <div class="muted" style="margin-top: 0.5rem">
      chaining + search
      <br />
      apply rules consistently
    </div>
  </div>
  <div class="box" style="text-align: left">
    <div style="color: orange">Explanation</div>
    <div class="muted" style="margin-top: 0.5rem">
      “why this result?”
      <br />
      trace rule chain
    </div>
  </div>
</div>

Note:
- Successes: MYCIN, XCON. Weakness: brittle + expensive maintenance.
- ShopNow: fraud rules explode as attackers adapt.

---

### AI winters (when hype met reality)

<div class="two-col">
  <div>
    <img
      src="../assets/introduction_to_ai/imgs/ai_winter_landscape.jpg"
      alt="Winter landscape"
      class="img-small"
      style="width: 90%"
    />
  </div>
  <div class="box" style="text-align: left; font-size: 0.95em">
    <div style="color: orange">Two famous slowdowns</div>
    <ul class="muted" style="margin-top: 0.6rem">
      <li><span style="color: lightgreen;">1974–1980</span>: expectations too high, compute too weak</li>
      <li><span style="color: lightgreen;">1987–1993</span>: expert systems under-delivered</li>
    </ul>
  </div>
</div>

Note:
- Teach: hype cycles are normal.
Source (image): https://commons.wikimedia.org/wiki/File:Winter_landscape_4.jpg

---

### Data + compute + algorithms: why ML / DL “won”

<div class="three-col">
  <div class="box" style="text-align: center">
    <div style="color: lightgreen; font-size: 0.95em">Data</div>
    <div class="muted tiny" style="margin-top: 0.4rem">logs, sensors, storage</div>
    <div class="muted" style="margin-top: 0.5rem">more examples</div>
  </div>
  <div class="box" style="text-align: center">
    <div style="color: lightgreen; font-size: 0.95em">Compute</div>
    <div class="muted tiny" style="margin-top: 0.4rem">GPUs + faster hardware</div>
    <div class="muted" style="margin-top: 0.5rem">bigger models</div>
  </div>
  <div class="box" style="text-align: center">
    <div style="color: lightgreen; font-size: 0.95em">Algorithms</div>
    <div class="muted tiny" style="margin-top: 0.4rem">better training tricks</div>
    <div class="muted" style="margin-top: 0.5rem">better accuracy</div>
  </div>
</div>

<div class="tiny muted" style="margin-top: 0.8rem">
  <span style="color: orange;">Key shift:</span> instead of writing rules, we learn from examples.
</div>

Note:
- ShopNow: clickstream + orders + catalog images = data fuel.

--

<img
  src="../assets/introduction_to_ai/imgs/moores_law_transistor_count.png"
  alt="Moore's law transistor count chart"
  class="img-medium"
/>

Note:
- Supporting visual: compute grew exponentially.
Source: https://commons.wikimedia.org/wiki/File:Moore%27s_Law_Transistor_Count_1970-2020.png

---

### Milestone (contrast): Deep Blue (search/symbolic flavor)

<img
  src="../assets/introduction_to_ai/imgs/deep_blue_vs_kasparov.gif"
  alt="Deep Blue vs Kasparov game animation"
  class="img-medium"
/>

Note:
- Deep Blue: search + engineered evaluation (less “learning from data”).
Source: https://commons.wikimedia.org/wiki/File:Deep_Blue_versus_Kasparov,_1997,_Game_6.gif

---

### Milestone (contrast): AlexNet (deep learning comeback)

<img
  src="../assets/introduction_to_ai/imgs/alexnet_block_diagram.svg"
  alt="AlexNet block diagram"
  class="img-medium"
/>

Note:
- AlexNet (2012) + ImageNet + GPUs = deep learning works at scale.
Source: https://commons.wikimedia.org/wiki/File:AlexNet_block_diagram.svg

---

### Milestone (contrast): AlphaGo (learning at scale)

<img
  src="../assets/introduction_to_ai/imgs/alphago_divine_move.jpg"
  alt="AlphaGo vs Lee Sedol divine move visualization"
  class="img-medium"
/>

Note:
- AlphaGo blends deep learning + reinforcement learning + search.
Source: https://commons.wikimedia.org/wiki/File:Lee-sedol-alphago-divine-move.jpg

---

<!-- ========================================================= -->
<!-- 2) Two paradigms + knowledge representation -->
<!-- ========================================================= -->

<div class="section">
  <div class="kicker">2) Paradigms & knowledge</div>
  <div class="title">How do we build AI systems?</div>
  <div class="subtitle">Paradigms, representations, first concrete examples</div>
</div>

Note:
- Now we convert the history into the conceptual toolkit.

---

### Symbolic AI vs. Machine Learning

<div class="two-col">
  <div class="box" style="text-align: left">
    <div style="color: orange; font-size: 0.95em">Symbolic AI</div>
    <ul class="muted" style="margin-top: 0.6rem">
      <li>explicit rules + logic</li>
      <li>search + planning</li>
      <li>great when rules are clear</li>
    </ul>
  </div>
  <div class="box" style="text-align: left">
    <div style="color: lightgreen; font-size: 0.95em">Machine learning</div>
    <ul class="muted" style="margin-top: 0.6rem">
      <li>learn patterns from data</li>
      <li>needs evaluation + iteration</li>
      <li>dominates messy tasks</li>
    </ul>
  </div>
</div>

Note:
- Real systems are hybrid: business rules as guardrails + ML scores.
- ShopNow: “never ship to embargoed regions” (rule) + “fraud risk score” (ML).

---

### Knowledge representation (1/2): rules + graphs

<div class="two-col">
  <div class="box" style="text-align: left">
    <div style="color: orange">Rules / logic</div>
    <div class="muted" style="margin-top: 0.5rem">
      IF (new_customer AND high_amount AND shipping≠billing)
      <br />
      THEN flag_as_risky
    </div>
    <div class="tiny muted" style="margin-top: 0.6rem">
      easy to explain, hard to scale
    </div>
  </div>
  <div class="box" style="text-align: left">
    <div style="color: orange">Graphs / ontologies</div>
    <img
      src="../assets/introduction_to_ai/imgs/rdf_triples.jpg"
      alt="RDF triples graph"
      class="img-small"
      style="width: 100%; max-height: 30vh"
    />
    <div class="tiny muted" style="margin-top: 0.4rem">
      entities + relations (“product → category → brand”)
    </div>
  </div>
</div>

Note:
- ShopNow: catalog knowledge graph (brand ↔ category ↔ product).
RDF triples source: https://commons.wikimedia.org/wiki/File:Fig.3_Graphe_de_trois_triplets_RDF_avec_litt%C3%A9raux.jpg

---

### Knowledge representation (2/2): features + vectors

<div class="two-col">
  <div class="box" style="text-align: left">
    <div style="color: orange">Features</div>
    <ul class="muted" style="margin-top: 0.6rem">
      <li>age, cart_value, #returns</li>
      <li>category, brand, region</li>
      <li>time since last purchase</li>
    </ul>
    <div class="tiny muted" style="margin-top: 0.6rem">
      feed features into a model
    </div>
  </div>
  <div class="box" style="text-align: left">
    <div style="color: orange">Vectors (“embeddings”)</div>
    <svg width="100%" height="240" viewBox="0 0 520 240" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="520" height="240" fill="transparent" />
      <circle cx="90" cy="170" r="7" fill="#9bd" />
      <circle cx="125" cy="130" r="7" fill="#9bd" />
      <circle cx="155" cy="165" r="7" fill="#9bd" />
      <circle cx="210" cy="105" r="7" fill="#9bd" />
      <circle cx="240" cy="130" r="7" fill="#9bd" />
      <circle cx="315" cy="165" r="7" fill="#bd9" />
      <circle cx="345" cy="145" r="7" fill="#bd9" />
      <circle cx="365" cy="175" r="7" fill="#bd9" />
      <circle cx="435" cy="110" r="7" fill="#bd9" />
      <circle cx="455" cy="130" r="7" fill="#bd9" />
      <line x1="70" y1="200" x2="470" y2="200" stroke="rgba(255,255,255,0.35)" stroke-width="2" />
      <line x1="70" y1="200" x2="70" y2="30" stroke="rgba(255,255,255,0.35)" stroke-width="2" />
      <text x="75" y="48" fill="rgba(255,255,255,0.75)" font-size="16">vector space</text>
      <text x="90" y="224" fill="rgba(255,255,255,0.65)" font-size="14">dimension 1</text>
    </svg>
    <div class="tiny muted" style="margin-top: 0.4rem">
      similar items/users end up close together
    </div>
  </div>
</div>

Note:
- Sets up recommenders and embeddings later.

---

### First algorithms (search/pathfinding): BFS vs DFS vs A*

<div class="three-col">
  <div style="text-align: center">
    <div class="muted" style="margin-bottom: 0.4rem">BFS</div>
    <img
      src="../assets/introduction_to_ai/imgs/bfs.gif"
      alt="Breadth-first search animation"
      class="img-small"
      style="width: 95%; max-height: 26vh"
    />
  </div>
  <div style="text-align: center">
    <div class="muted" style="margin-bottom: 0.4rem">DFS</div>
    <img
      src="../assets/introduction_to_ai/imgs/dfs.gif"
      alt="Depth-first search animation"
      class="img-small"
      style="width: 95%; max-height: 26vh"
    />
  </div>
  <div style="text-align: center">
    <div class="muted" style="margin-bottom: 0.4rem">A*</div>
    <img
      src="../assets/introduction_to_ai/imgs/astar_progress.gif"
      alt="A* search animation"
      class="img-small"
      style="width: 95%; max-height: 26vh"
    />
  </div>
</div>

<div class="tiny muted" style="margin-top: 0.6rem">
  BFS explores “in waves”, DFS goes “deep”, A* uses a heuristic to focus.
</div>

Note:
- Visual note: BFS/DFS gifs are on graphs; A* is on a grid. If you want one single “same maze” comparison image, replace with a custom 3-panel maze illustration.
- ShopNow: warehouse picking paths, routing, configuration search.
Sources:
- BFS: https://commons.wikimedia.org/wiki/File:Breadth-First-Search-Algorithm.gif
- DFS: https://commons.wikimedia.org/wiki/File:Depth-First-Search.gif
- A*: https://commons.wikimedia.org/wiki/File:Astar_progress_animation.gif

---

### Rule-based example vs learned classifier

<div class="two-col">
  <div class="box" style="text-align: left">
    <div style="color: orange; font-size: 0.95em">Rule-based</div>
    <div class="muted" style="margin-top: 0.6rem">
      IF order_value &gt; 500
      <br />
      AND new_customer
      <br />
      AND shipping≠billing
      <br />
      THEN review
    </div>
    <div class="tiny muted" style="margin-top: 0.7rem">
      transparent, brittle, easy to evade
    </div>
  </div>
  <div class="box" style="text-align: left">
    <div style="color: lightgreen; font-size: 0.95em">Learned classifier</div>
    <div class="muted" style="margin-top: 0.6rem">
      input features → score
      <br />
      \(x \rightarrow p(\mathrm{fraud}\mid x)\)
    </div>
    <div class="tiny muted" style="margin-top: 0.7rem">
      adapts, needs data + evaluation + monitoring
    </div>
  </div>
</div>

Note:
- In practice: hybrid is common (rules as guardrails + ML score).
- ShopNow: fraud/chargeback detection is a canonical example.

---

<!-- ========================================================= -->
<!-- 3) Learning types -->
<!-- ========================================================= -->

<div class="section">
  <div class="kicker">3) Learning types</div>
  <div class="title">How do models learn?</div>
  <div class="subtitle">Five buckets</div>
</div>

Note:
- Learning type is about what feedback signal you have.

---

### Learning types (overview)

<div class="three-col">
  <div class="box" style="text-align: left">
    <div style="color: lightgreen">Supervised</div>
    <div class="muted" style="margin-top: 0.4rem">labeled examples (x, y)</div>
    <div class="tiny muted">fraud yes/no, demand prediction</div>
  </div>
  <div class="box" style="text-align: left">
    <div style="color: lightgreen">Unsupervised</div>
    <div class="muted" style="margin-top: 0.4rem">no labels (x)</div>
    <div class="tiny muted">segments, compression</div>
  </div>
  <div class="box" style="text-align: left">
    <div style="color: lightgreen">Reinforcement</div>
    <div class="muted" style="margin-top: 0.4rem">reward signal</div>
    <div class="tiny muted">control, bidding</div>
  </div>
</div>

<div class="three-col" style="margin-top: 1rem">
  <div class="box" style="text-align: left">
    <div style="color: lightgreen">Semi-supervised</div>
    <div class="muted" style="margin-top: 0.4rem">few labels + many unlabeled</div>
  </div>
  <div class="box" style="text-align: left">
    <div style="color: lightgreen">Self-supervised</div>
    <div class="muted" style="margin-top: 0.4rem">labels from the data itself</div>
  </div>
  <div></div>
</div>

Note:
- One taxonomy you can reuse across the whole course.

---

### Supervised learning

<div class="box" style="text-align: left">
  <div style="color: lightgreen">You have labels.</div>
  <div class="muted" style="margin-top: 0.6rem">
    learn \(f(x)\) from examples \((x, y)\)
  </div>
</div>

Note:
- ShopNow: fraud detection, churn prediction, delivery delay prediction, demand forecasting.

---

### Unsupervised learning

<div class="box" style="text-align: left">
  <div style="color: lightgreen">No labels.</div>
  <div class="muted" style="margin-top: 0.6rem">
    discover structure in \(x\) (groups, patterns, compression)
  </div>
</div>

Note:
- ShopNow: customer segmentation; explore browsing sessions; learn product/user representations.

---

### Semi-supervised learning

<img
  src="../assets/introduction_to_ai/imgs/semi_supervised_unlabeled.png"
  alt="Semi-supervised learning with unlabeled data"
  class="img-small"
  style="width: 55%"
/>

Note:
- Typical situation: labels are expensive, raw data is abundant.
- ShopNow: only some orders are confirmed fraud; many are unlabeled.
Source: https://commons.wikimedia.org/wiki/File:Example_of_unlabeled_data_in_semisupervised_learning.png

---

### Self-supervised learning

<img
  src="../assets/introduction_to_ai/imgs/autoencoder_structure.png"
  alt="Autoencoder structure diagram"
  class="img-small"
  style="width: 60%"
/>

Note:
- Create training signal from the data.
- ShopNow: learn product representations from images/text without hand labels.
Source: https://commons.wikimedia.org/wiki/File:Autoencoder_structure.png

---

### Reinforcement learning (RL)

<img
  src="../assets/introduction_to_ai/imgs/reinforcement_learning_diagram.svg"
  alt="Reinforcement learning agent-environment diagram"
  class="img-medium"
/>

Note:
- Learn by trial-and-error with rewards.
- ShopNow: bidding/ads (reward = conversion), inventory policy (reward = profit).
Source: https://commons.wikimedia.org/wiki/File:Reinforcement_learning_diagram.svg

---

<!-- ========================================================= -->
<!-- 4) Core task families -->
<!-- ========================================================= -->

<div class="section">
  <div class="kicker">4) Core task families</div>
  <div class="title">What problems do we solve?</div>
  <div class="subtitle">Tasks mapped to learning types</div>
</div>

Note:
- Learning type = feedback. Task family = what output you want.

---

### Task families × learning types (overview)

<table class="taskmap">
  <thead>
    <tr>
      <th>Task family</th>
      <th>Supervised</th>
      <th>Unsupervised</th>
      <th>Self-/semi</th>
      <th>RL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Classification / Regression</td>
      <td>✓</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Clustering / Dim. reduction</td>
      <td></td>
      <td>✓</td>
      <td>✓</td>
      <td></td>
    </tr>
    <tr>
      <td>Anomaly detection</td>
      <td>✓</td>
      <td>✓</td>
      <td>✓</td>
      <td></td>
    </tr>
    <tr>
      <td>Ranking & recommenders</td>
      <td>✓</td>
      <td>✓</td>
      <td>✓</td>
      <td></td>
    </tr>
    <tr>
      <td>Generative modeling</td>
      <td></td>
      <td></td>
      <td>✓</td>
      <td></td>
    </tr>
  </tbody>
</table>

Note:
- Generative modeling is mentioned only; next lecture covers GenAI & agents (no transformers/LLMs today).

---

### Classification / Regression

<div class="two-col">
  <div>
    <h4 style="color: orange; margin-bottom: 0.5rem">Classification</h4>
    <img
      src="../assets/introduction_to_ai/imgs/confusion_matrix_redblue.png"
      alt="Confusion matrix"
      class="img-small"
    />
  </div>
  <div>
    <h4 style="color: orange; margin-bottom: 0.5rem">Regression</h4>
    <img
      src="../assets/introduction_to_ai/imgs/linear_regression.svg"
      alt="Linear regression fit"
      class="img-small"
    />
  </div>
</div>

Note:
- ShopNow classification: fraud vs legit, “will churn?”, “will return?”
- ShopNow regression: demand forecasting, delivery ETA, lifetime value.
Sources:
- Confusion matrix: https://commons.wikimedia.org/wiki/File:ConfusionMatrixRedBlue.png
- Linear regression: https://commons.wikimedia.org/wiki/File:Linear_regression.svg

---

### Clustering / Dimensionality reduction

<div class="two-col">
  <div>
    <h4 style="color: orange; margin-bottom: 0.5rem">Clustering</h4>
    <img
      src="../assets/introduction_to_ai/imgs/kmeans_convergence.gif"
      alt="K-means convergence animation"
      class="img-small"
      style="width: 85%"
    />
  </div>
  <div>
    <h4 style="color: orange; margin-bottom: 0.5rem">PCA</h4>
    <img
      src="../assets/introduction_to_ai/imgs/gaussian_scatter_pca.svg"
      alt="PCA on Gaussian scatter plot"
      class="img-small"
      style="width: 85%"
    />
  </div>
</div>

Note:
- PCA often used for visualization; also common: t-SNE and UMAP.
- ShopNow: segment customers; visualize products/users.
Sources:
- k-means: https://commons.wikimedia.org/wiki/File:K-means_convergence.gif
- PCA: https://commons.wikimedia.org/wiki/File:GaussianScatterPCA.svg

---

### Anomaly detection

<img
  src="../assets/introduction_to_ai/imgs/isolation_forest_anomaly_scores.png"
  alt="Isolation Forest anomaly score visualization"
  class="img-small"
  style="width: 60%"
/>

Note:
- ShopNow: card testing, bot traffic, unusual return behavior.
Source: https://commons.wikimedia.org/wiki/File:Normalized_Anomaly_Scores_of_Isolation_Forest.png

---

### Ranking & recommender systems

<img
  src="../assets/introduction_to_ai/imgs/collaborative_filtering.gif"
  alt="Collaborative filtering animation"
  class="img-small"
  style="width: 60%"
/>

Note:
- ShopNow: search ranking, homepage feed, “you may also like”.
Source: https://commons.wikimedia.org/wiki/File:Collaborative_filtering.gif

---

### Generative modeling (mention only)

<div class="box" style="text-align: left">
  <div style="color: lightgreen">Generative modeling</div>
  <div class="muted" style="margin-top: 0.6rem">
    generate text/images/audio/code
    <br />
    <span style="color: orange;">We cover this next lecture.</span>
  </div>
</div>

Note:
- Keep short. No transformers/LLMs content here.
- ShopNow (teaser): product description drafts, support agent drafts.

---

<!-- ========================================================= -->
<!-- 5) Why models work (or fail) -->
<!-- ========================================================= -->

<div class="section">
  <div class="kicker">5) Why models work (or fail)</div>
  <div class="title">Generalization + evaluation</div>
  <div class="subtitle">The part that breaks in production</div>
</div>

Note:
- This section is “how to avoid expensive mistakes”.

---

### Train / validation / test

<img
  src="../assets/introduction_to_ai/imgs/train_val_test_split.png"
  alt="Training validation test split diagram"
  class="img-medium"
/>

Note:
- Train: fit parameters. Validation: tune choices. Test: final unbiased check.
- ShopNow tip: use time-based splits for demand/seasonality (don’t shuffle).
Source: https://commons.wikimedia.org/wiki/File:ML_dataset_training_validation_test_sets.png

---

### Cross-validation (k-fold)

<img
  src="../assets/introduction_to_ai/imgs/k_fold_cross_validation.svg"
  alt="K-fold cross validation diagram"
  class="img-medium"
/>

Note:
- Cross-validation stabilizes evaluation when data is limited.
- Time series caveat: use rolling/blocked CV.
Source: https://commons.wikimedia.org/wiki/File:K-fold_cross_validation_EN.svg

---

### Overfitting vs. underfitting

<img
  src="../assets/introduction_to_ai/imgs/overfitted_data.png"
  alt="Overfitted data example"
  class="img-small"
  style="width: 60%"
/>

Note:
- Underfit: too simple → misses structure. Overfit: too complex → learns noise.
Source: https://commons.wikimedia.org/wiki/File:Overfitted_Data.png

---

### Overfitting (training curves)

<img
  src="../assets/introduction_to_ai/imgs/overfitting.svg"
  alt="Overfitting plot: training vs validation error"
  class="img-medium"
/>

Note:
- When validation error rises while training error falls → overfitting.
- Early stopping: stop near best validation point.
Source: https://commons.wikimedia.org/wiki/File:Overfitting_svg.svg

---

### Bias–variance tradeoff (intuition)

<img
  src="../assets/introduction_to_ai/imgs/bias_variance_total_error.svg"
  alt="Bias and variance contributing to total error"
  class="img-medium"
/>

Note:
- High bias: too simple. High variance: too sensitive.
Source: https://commons.wikimedia.org/wiki/File:Bias_and_variance_contributing_to_total_error.svg

---

### Generalization + dataset shift (placeholder)

<div class="two-col">
  <div class="box" style="text-align: left">
    <div style="color: orange">What changes?</div>
    <ul class="muted" style="margin-top: 0.6rem">
      <li>customer behavior</li>
      <li>pricing / promotions</li>
      <li>catalog mix</li>
      <li>fraud strategies</li>
    </ul>
  </div>
  <div class="box" style="text-align: left">
    <div style="color: lightgreen">Visualization (TODO)</div>
    <div class="muted" style="margin-top: 0.6rem">
      Plot <span style="color: yellow">training data</span> distribution vs.
      <span style="color: red">production data</span>
      <br />
      → decision boundary no longer fits
    </div>
    <div class="tiny muted" style="margin-top: 0.7rem">
      (Histogram shift or shifted clusters in a scatter plot)
    </div>
  </div>
</div>

Note:
- Keep as TODO placeholder for a custom plot.
- ShopNow: Black Friday changes everything (distribution shift).

---

### Regularization (L1/L2, dropout, early stopping)

<div class="three-col">
  <div>
    <img
      src="../assets/introduction_to_ai/imgs/l1_l2_balls.svg"
      alt="L1 and L2 balls"
      class="img-small"
      style="width: 95%"
    />
  </div>
  <div>
    <svg width="100%" height="240" viewBox="0 0 520 240" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="520" height="240" fill="transparent" />
      <circle cx="70" cy="70" r="12" fill="rgba(155,220,180,0.9)"/>
      <circle cx="70" cy="120" r="12" fill="rgba(155,220,180,0.9)"/>
      <circle cx="70" cy="170" r="12" fill="rgba(155,220,180,0.9)"/>
      <circle cx="210" cy="55" r="12" fill="rgba(180,180,255,0.9)"/>
      <circle cx="210" cy="105" r="12" fill="rgba(180,180,255,0.25)"/>
      <line x1="200" y1="95" x2="220" y2="115" stroke="rgba(255,80,80,0.9)" stroke-width="4"/>
      <line x1="200" y1="115" x2="220" y2="95" stroke="rgba(255,80,80,0.9)" stroke-width="4"/>
      <circle cx="210" cy="155" r="12" fill="rgba(180,180,255,0.9)"/>
      <circle cx="390" cy="120" r="14" fill="rgba(255,230,150,0.95)"/>
      <g stroke="rgba(255,255,255,0.25)" stroke-width="2">
        <line x1="82" y1="70" x2="198" y2="55"/>
        <line x1="82" y1="120" x2="198" y2="55"/>
        <line x1="82" y1="170" x2="198" y2="55"/>
        <line x1="82" y1="70" x2="198" y2="105"/>
        <line x1="82" y1="120" x2="198" y2="105"/>
        <line x1="82" y1="170" x2="198" y2="105"/>
        <line x1="82" y1="70" x2="198" y2="155"/>
        <line x1="82" y1="120" x2="198" y2="155"/>
        <line x1="82" y1="170" x2="198" y2="155"/>
        <line x1="222" y1="55" x2="375" y2="120"/>
        <line x1="222" y1="105" x2="375" y2="120"/>
        <line x1="222" y1="155" x2="375" y2="120"/>
      </g>
      <text x="60" y="25" fill="rgba(255,255,255,0.75)" font-size="16">dropout</text>
      <text x="250" y="210" fill="rgba(255,255,255,0.6)" font-size="14">randomly drop units during training</text>
    </svg>
  </div>
  <div class="box" style="text-align: left">
    <div style="color: orange">Early stopping</div>
    <div class="muted" style="margin-top: 0.6rem">
      stop training when validation gets worse
    </div>
    <div class="tiny muted" style="margin-top: 0.6rem">
      cheap + effective regularization
    </div>
  </div>
</div>

Note:
- Regularization reduces overfitting.
- L2 (ridge) vs L1 (lasso): lasso encourages sparsity.
Source (L1/L2 balls): https://commons.wikimedia.org/wiki/File:L1_and_L2_balls.svg

---

### Optimization (gradient descent, learning rate)

<img
  src="../assets/introduction_to_ai/imgs/gradient_descent_method.png"
  alt="Gradient descent method diagram"
  class="img-medium"
/>

Note:
- Training = minimize a loss by updating parameters.
- Learning rate: step size (too big diverges; too small is slow).
Source: https://commons.wikimedia.org/wiki/File:Gradient_descent_method.png

---

### Loss functions (MSE vs cross-entropy)

<div class="two-col">
  <div class="box" style="text-align: left">
    <div style="color: orange">Regression: MSE</div>
    <div class="muted" style="margin-top: 0.6rem; font-size: 1.05em">
      \(\mathcal{L} = (y - \hat{y})^2\)
    </div>
    <svg width="100%" height="180" viewBox="0 0 520 180" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="520" height="180" fill="transparent"/>
      <line x1="60" y1="150" x2="470" y2="150" stroke="rgba(255,255,255,0.25)" stroke-width="2"/>
      <line x1="265" y1="20" x2="265" y2="150" stroke="rgba(255,255,255,0.25)" stroke-width="2"/>
      <path d="M 80 150 Q 265 20 450 150" fill="none" stroke="rgba(155,220,180,0.9)" stroke-width="4"/>
      <text x="78" y="170" fill="rgba(255,255,255,0.6)" font-size="14">error</text>
      <text x="275" y="35" fill="rgba(255,255,255,0.6)" font-size="14">min</text>
    </svg>
  </div>
  <div class="box" style="text-align: left">
    <div style="color: orange">Classification: cross-entropy</div>
    <div class="muted" style="margin-top: 0.6rem; font-size: 1.05em">
      \(\mathcal{L} = -\log p(y)\)
    </div>
    <svg width="100%" height="180" viewBox="0 0 520 180" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="520" height="180" fill="transparent"/>
      <line x1="60" y1="150" x2="470" y2="150" stroke="rgba(255,255,255,0.25)" stroke-width="2"/>
      <line x1="60" y1="20" x2="60" y2="150" stroke="rgba(255,255,255,0.25)" stroke-width="2"/>
      <path d="M 70 25 C 120 40, 180 60, 240 90 C 310 125, 380 145, 450 150" fill="none" stroke="rgba(255,220,150,0.95)" stroke-width="4"/>
      <text x="68" y="170" fill="rgba(255,255,255,0.6)" font-size="14">p(correct)</text>
      <text x="82" y="40" fill="rgba(255,255,255,0.6)" font-size="14">high loss</text>
      <text x="360" y="135" fill="rgba(255,255,255,0.6)" font-size="14">low loss</text>
    </svg>
  </div>
</div>

Note:
- Loss defines what “good” means and drives training.
- ShopNow: fraud detection often needs cost-sensitive evaluation (false positives are expensive).

---

### Pitfall: “It works in the notebook” ≠ “It works in the world”

<div class="two-col">
  <div class="box" style="text-align: left">
    <div style="color: orange">Common failure modes</div>
    <ul class="muted" style="margin-top: 0.6rem">
      <li>data leakage</li>
      <li>biased / non-representative data</li>
      <li>dataset shift / drift</li>
      <li>wrong metric / wrong goal</li>
      <li>no monitoring</li>
    </ul>
  </div>
  <div class="box" style="text-align: left">
    <div style="color: lightgreen">E-commerce “gotchas”</div>
    <ul class="muted" style="margin-top: 0.6rem">
      <li>promo periods break assumptions</li>
      <li>bots mimic users</li>
      <li>inventory constraints change outcomes</li>
      <li>feedback loops (recommenders)</li>
    </ul>
  </div>
</div>

Note:
- This is the “production reality check” slide.

---

<!-- ========================================================= -->
<!-- 6) Classical ML toolbox -->
<!-- ========================================================= -->

<div class="section">
  <div class="kicker">6) Classical ML toolbox</div>
  <div class="title">Baselines that still win</div>
  <div class="subtitle">Often faster, cheaper, easier to debug</div>
</div>

Note:
- Pragmatic tip: start with strong baselines before deep nets.

---

### Linear & logistic regression

<div class="two-col">
  <div>
    <img
      src="../assets/introduction_to_ai/imgs/linear_regression.svg"
      alt="Linear regression fit"
      class="img-small"
      style="width: 85%"
    />
  </div>
  <div>
    <img
      src="../assets/introduction_to_ai/imgs/logistic_curve.svg"
      alt="Logistic curve"
      class="img-small"
      style="width: 85%"
    />
  </div>
</div>

Note:
- Linear regression: predict a number. Logistic regression: predict a probability.
- ShopNow: demand forecasting baseline; churn/fraud score baseline.
Sources:
- Linear regression: https://commons.wikimedia.org/wiki/File:Linear_regression.svg
- Logistic curve: https://commons.wikimedia.org/wiki/File:Logistic-curve.svg

---

### Decision trees

<img
  src="../assets/introduction_to_ai/imgs/simple_decision_tree.svg"
  alt="Decision tree diagram"
  class="img-medium"
/>

Note:
- Pros: interpretable. Cons: can overfit.
Source: https://commons.wikimedia.org/wiki/File:Simple_decision_tree.svg

---

### Random forests

<img
  src="../assets/introduction_to_ai/imgs/random_forest_explain.png"
  alt="Random forest explain"
  class="img-medium"
/>

Note:
- Many trees averaged → robust. Strong default for tabular data.
Source: https://commons.wikimedia.org/wiki/File:Random_forest_explain.png

---

### Gradient boosting

<div class="box" style="text-align: left">
  <div style="color: orange">Sequentially fix mistakes</div>
  <div class="muted" style="margin-top: 0.6rem">
    build model₁ → look at errors → add model₂ to correct → add model₃ → …
  </div>
</div>

<svg width="100%" height="200" viewBox="0 0 900 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="rgba(255,255,255,0.65)"/>
    </marker>
  </defs>
  <rect x="40" y="70" width="180" height="70" rx="14" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.25)" stroke-width="2"/>
  <rect x="300" y="70" width="180" height="70" rx="14" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.25)" stroke-width="2"/>
  <rect x="560" y="70" width="180" height="70" rx="14" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.25)" stroke-width="2"/>
  <text x="130" y="110" fill="rgba(255,255,255,0.85)" font-size="18" text-anchor="middle">tree 1</text>
  <text x="390" y="110" fill="rgba(255,255,255,0.85)" font-size="18" text-anchor="middle">tree 2</text>
  <text x="650" y="110" fill="rgba(255,255,255,0.85)" font-size="18" text-anchor="middle">tree 3</text>
  <line x1="220" y1="105" x2="300" y2="105" stroke="rgba(255,255,255,0.35)" stroke-width="3" marker-end="url(#arr)"/>
  <line x1="480" y1="105" x2="560" y2="105" stroke="rgba(255,255,255,0.35)" stroke-width="3" marker-end="url(#arr)"/>
  <text x="260" y="70" fill="rgba(255,165,0,0.9)" font-size="14" text-anchor="middle">fix errors</text>
  <text x="520" y="70" fill="rgba(255,165,0,0.9)" font-size="14" text-anchor="middle">fix errors</text>
  <text x="820" y="110" fill="rgba(155,220,180,0.9)" font-size="18">final model</text>
</svg>

Note:
- Top performer on tabular data.
- Tools: XGBoost, LightGBM, CatBoost.

---

### k-Nearest Neighbors (kNN)

<img
  src="../assets/introduction_to_ai/imgs/knn_explain.png"
  alt="kNN diagram"
  class="img-medium"
/>

Note:
- Simple baseline; can be slow at inference; sensitive to feature scaling.
Source: https://commons.wikimedia.org/wiki/File:K_nearest_neighbour_explain.png

---

### Support Vector Machines (SVM)

<img
  src="../assets/introduction_to_ai/imgs/svm_support_vector_machine.jpg"
  alt="Support vector machine diagram"
  class="img-medium"
/>

Note:
- Maximize margin between classes.
Source: https://commons.wikimedia.org/wiki/File:Support_vector_machine.jpg

---

### Naive Bayes

<img
  src="../assets/introduction_to_ai/imgs/bayes_tree_diagrams.svg"
  alt="Bayes theorem tree diagrams"
  class="img-medium"
/>

Note:
- Surprisingly strong for text classification despite “naive” independence assumption.
Source: https://commons.wikimedia.org/wiki/File:Bayes_theorem_tree_diagrams.svg

---

<!-- ========================================================= -->
<!-- 7) Deep learning essentials (without transformers) -->
<!-- ========================================================= -->

<div class="section">
  <div class="kicker">7) Deep learning essentials</div>
  <div class="title">Neural networks</div>
  <div class="subtitle">Layers, activations, backprop — plus CNN/RNN/embeddings</div>
</div>

Note:
- No transformers/LLMs today. We keep this as “essentials”.

---

### Neural networks: layers

<img
  src="../assets/introduction_to_ai/imgs/artificial_neural_network.svg"
  alt="Artificial neural network diagram"
  class="img-medium"
/>

Note:
- A neural net is a stacked function \(f_\theta(x)\).
Source: https://commons.wikimedia.org/wiki/File:Artificial_neural_network.svg

---

### Activations (nonlinearity)

<div class="two-col">
  <div>
    <img
      src="../neural_networks/assets/sigmoid_activation.svg"
      alt="Sigmoid activation"
      class="img-small"
      style="width: 90%"
    />
  </div>
  <div>
    <img
      src="../neural_networks/assets/relu_activation.svg"
      alt="ReLU activation"
      class="img-small"
      style="width: 90%"
    />
  </div>
</div>

Note:
- Without activations, stacking layers collapses to linear.
- Sigmoid outputs probabilities; ReLU common in hidden layers.
Source (local course assets): `slides/neural_networks/assets/`

---

### Backpropagation (intuition)

<svg width="100%" height="270" viewBox="0 0 900 270" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="rgba(255,255,255,0.65)"/>
    </marker>
    <marker id="arrowBack" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="rgba(255,165,0,0.85)"/>
    </marker>
  </defs>

  <circle cx="120" cy="80" r="18" fill="rgba(155, 220, 180, 0.9)"/>
  <circle cx="120" cy="190" r="18" fill="rgba(155, 220, 180, 0.9)"/>
  <circle cx="360" cy="60" r="18" fill="rgba(180, 180, 255, 0.9)"/>
  <circle cx="360" cy="135" r="18" fill="rgba(180, 180, 255, 0.9)"/>
  <circle cx="360" cy="210" r="18" fill="rgba(180, 180, 255, 0.9)"/>
  <circle cx="600" cy="100" r="18" fill="rgba(180, 180, 255, 0.9)"/>
  <circle cx="600" cy="170" r="18" fill="rgba(180, 180, 255, 0.9)"/>
  <circle cx="800" cy="135" r="22" fill="rgba(255, 230, 150, 0.95)"/>

  <line x1="138" y1="80" x2="342" y2="60" stroke="rgba(255,255,255,0.5)" stroke-width="3" marker-end="url(#arrow)"/>
  <line x1="138" y1="80" x2="342" y2="135" stroke="rgba(255,255,255,0.5)" stroke-width="3" marker-end="url(#arrow)"/>
  <line x1="138" y1="80" x2="342" y2="210" stroke="rgba(255,255,255,0.5)" stroke-width="3" marker-end="url(#arrow)"/>
  <line x1="138" y1="190" x2="342" y2="60" stroke="rgba(255,255,255,0.5)" stroke-width="3" marker-end="url(#arrow)"/>
  <line x1="138" y1="190" x2="342" y2="135" stroke="rgba(255,255,255,0.5)" stroke-width="3" marker-end="url(#arrow)"/>
  <line x1="138" y1="190" x2="342" y2="210" stroke="rgba(255,255,255,0.5)" stroke-width="3" marker-end="url(#arrow)"/>

  <line x1="378" y1="60" x2="582" y2="100" stroke="rgba(255,255,255,0.5)" stroke-width="3" marker-end="url(#arrow)"/>
  <line x1="378" y1="135" x2="582" y2="100" stroke="rgba(255,255,255,0.5)" stroke-width="3" marker-end="url(#arrow)"/>
  <line x1="378" y1="210" x2="582" y2="170" stroke="rgba(255,255,255,0.5)" stroke-width="3" marker-end="url(#arrow)"/>

  <line x1="618" y1="100" x2="776" y2="135" stroke="rgba(255,255,255,0.5)" stroke-width="3" marker-end="url(#arrow)"/>
  <line x1="618" y1="170" x2="776" y2="135" stroke="rgba(255,255,255,0.5)" stroke-width="3" marker-end="url(#arrow)"/>

  <line x1="776" y1="155" x2="630" y2="180" stroke="rgba(255,165,0,0.8)" stroke-width="3" marker-end="url(#arrowBack)"/>
  <line x1="776" y1="115" x2="630" y2="90" stroke="rgba(255,165,0,0.8)" stroke-width="3" marker-end="url(#arrowBack)"/>
  <line x1="582" y1="185" x2="400" y2="225" stroke="rgba(255,165,0,0.8)" stroke-width="3" marker-end="url(#arrowBack)"/>
  <line x1="582" y1="85" x2="400" y2="45" stroke="rgba(255,165,0,0.8)" stroke-width="3" marker-end="url(#arrowBack)"/>

  <text x="100" y="28" fill="rgba(255,255,255,0.8)" font-size="18">forward pass</text>
  <text x="610" y="28" fill="rgba(255,165,0,0.9)" font-size="18">backward pass</text>
  <text x="780" y="205" fill="rgba(255,255,255,0.75)" font-size="16">loss</text>
</svg>

Note:
- Forward pass: compute predictions and loss.
- Backward pass: compute gradients via chain rule.

---

### CNNs (vision)

<img
  src="../assets/introduction_to_ai/imgs/typical_cnn.png"
  alt="Typical CNN diagram"
  class="img-medium"
/>

Note:
- ShopNow: product image classification, defect detection.
Source: https://commons.wikimedia.org/wiki/File:Typical_cnn.png

---

### RNN / LSTM (sequences)

<img
  src="../assets/introduction_to_ai/imgs/the_lstm_cell.svg"
  alt="LSTM cell diagram"
  class="img-medium"
/>

Note:
- Historical sequence model; keeps a state over time.
Source: https://commons.wikimedia.org/wiki/File:The_LSTM_Cell.svg

---

### Embeddings (concept only)

<img
  src="../assets/introduction_to_ai/imgs/cbow_skipgram.png"
  alt="CBOW and Skip-gram diagram"
  class="img-medium"
/>

Note:
- Embeddings map items/text into vectors where similar ≈ close.
- ShopNow: “similar products”, personalization, semantic search.
Source: https://commons.wikimedia.org/wiki/File:CBOW_eta_Skipgram.png

---

### Transfer learning + fine-tuning

<div class="three-col">
  <div class="box" style="text-align: center">
    <div style="color: orange">Pre-train</div>
    <div class="muted tiny" style="margin-top: 0.4rem">large dataset</div>
    <div class="muted" style="margin-top: 0.4rem">general features</div>
  </div>
  <div class="box" style="text-align: center">
    <div style="color: orange">Re-use</div>
    <div class="muted tiny" style="margin-top: 0.4rem">freeze most layers</div>
    <div class="muted" style="margin-top: 0.4rem">keep representations</div>
  </div>
  <div class="box" style="text-align: center">
    <div style="color: orange">Fine-tune</div>
    <div class="muted tiny" style="margin-top: 0.4rem">your small dataset</div>
    <div class="muted" style="margin-top: 0.4rem">adapt to task</div>
  </div>
</div>

Note:
- Practical win: less data + less compute.

---

<!-- ========================================================= -->
<!-- 8) Wrap-up -->
<!-- ========================================================= -->

<div class="section">
  <div class="kicker">8) Wrap-up</div>
  <div class="title">Key takeaways</div>
  <div class="subtitle">A mental model you can reuse</div>
</div>

---

### Key takeaways

<div class="box" style="text-align: left">
  <div style="color: lightgreen; font-size: 0.95em">If you remember 7 things:</div>
  <ul class="muted" style="margin-top: 0.6rem">
    <li>AI evolved from <span style="color: orange;">rules + search</span> to <span style="color: orange;">learning from data</span>.</li>
    <li>Learning types: supervised, unsupervised, semi-/self-supervised, RL.</li>
    <li>Task families: classification, regression, clustering, PCA, anomalies, ranking.</li>
    <li>Generalization is everything: splits, CV, and dataset shift.</li>
    <li>Regularization + good evaluation prevent overfitting.</li>
    <li>Classical ML is still powerful on tabular data.</li>
    <li>Deep learning adds representation learning (CNNs, LSTMs, embeddings).</li>
  </ul>
</div>

Note:
- Invite students to map any AI product to learning type + task family + model family.

---

### Next lecture

<div class="section">
  <div class="kicker">Next</div>
  <div class="title">Generative AI & Agent-Based Systems</div>
  <div class="subtitle">How modern systems generate, reason, and use tools</div>
</div>

Note:
- Next: generative modeling, LLMs, and agents — and what that means for BI.
