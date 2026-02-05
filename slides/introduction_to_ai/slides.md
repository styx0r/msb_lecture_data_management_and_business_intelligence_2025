<style>
  .img-full {
    max-width: 100%;
    max-height: 56vh;
    width: 100%;
    height: auto;
    object-fit: contain;
    margin: 0.25rem auto 0 auto;
    background: transparent;
    display: block;
  }

  .img-medium {
    max-width: 100%;
    max-height: 44vh;
    width: 85%;
    height: auto;
    object-fit: contain;
    margin: 0.25rem auto 0 auto;
    background: transparent;
    display: block;
  }

  .img-small {
    max-width: 100%;
    max-height: 38vh;
    width: 70%;
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

  .kbd {
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono",
      "Courier New", monospace;
    font-size: 0.8em;
    padding: 0.15rem 0.35rem;
    border: 1px solid rgba(255, 255, 255, 0.25);
    border-bottom-width: 2px;
    border-radius: 8px;
  }
</style>

### Agenda

- <span style="color: lightgreen;">Motivation & a short history</span>
- <span style="color: lightgreen;">Core concepts (ML, DL, GenAI)</span>
- <span style="color: lightgreen;">How learning works: data → model → training → evaluation</span>
- <span style="color: lightgreen;">Pitfalls + responsible use</span>

Note:
- This lecture is intentionally visual and conceptual (not a math-heavy ML course).
- Deeper dives later: neural nets, LLMs, embeddings, agents.

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
    <ul class="muted" style="margin-top: 0.5rem">
      <li><span style="color: orange;">Prediction</span>: forecast churn & demand</li>
      <li><span style="color: orange;">Detection</span>: anomalies & fraud</li>
      <li><span style="color: orange;">Automation</span>: reports & recurring analysis</li>
      <li><span style="color: orange;">Interfaces</span>: natural-language BI (“chat with data”)</li>
    </ul>
  </div>
</div>

Note:
Source (image): https://commons.wikimedia.org/wiki/File:Artificial-Intelligence.jpg

---

### A very short history (overview)

<img
  src="../assets/introduction_to_ai/imgs/ai_history_timeline.jpg"
  alt="AI history timeline"
  class="img-full"
/>

Note:
Source: https://commons.wikimedia.org/wiki/File:AI-History-Timeline-300dpi.jpg

---

### 1950: <span style="color: orange;">Alan Turing</span> — “Can machines think?”

<img
  src="../assets/introduction_to_ai/imgs/alan_turing_1936.jpg"
  alt="Alan Turing portrait"
  class="img-small"
/>

<span class="muted">Idea: evaluate intelligence via conversation (Turing Test).</span>

Note:
Source: https://commons.wikimedia.org/wiki/File:Alan_Turing_(1912-1954)_in_1936_at_Princeton_University.jpg

---

### 1958: <span style="color: orange;">Perceptron</span> — early neural networks

<img
  src="../assets/introduction_to_ai/imgs/perceptron_rosenblatt.png"
  alt="Rosenblatt perceptron diagram"
  class="img-medium"
/>

Note:
Source: https://commons.wikimedia.org/wiki/File:Rosenblattperceptron.png

---

### 1997: <span style="color: orange;">Deep Blue</span> beats world chess champion

<img
  src="../assets/introduction_to_ai/imgs/deep_blue_vs_kasparov.gif"
  alt="Deep Blue vs Kasparov game 6 animation"
  class="img-medium"
/>

Note:
Source: https://commons.wikimedia.org/wiki/File:Deep_Blue_versus_Kasparov,_1997,_Game_6.gif

---

### 2012: <span style="color: orange;">AlexNet</span> (ImageNet) — deep learning “comes back”

<img
  src="../assets/introduction_to_ai/imgs/alexnet_block_diagram.svg"
  alt="AlexNet block diagram"
  class="img-medium"
/>

Note:
Source: https://commons.wikimedia.org/wiki/File:AlexNet_block_diagram.svg

---

### 2016: <span style="color: orange;">AlphaGo</span> — reinforcement learning at scale

<img
  src="../assets/introduction_to_ai/imgs/alphago_divine_move.jpg"
  alt="AlphaGo vs Lee Sedol divine move visualization"
  class="img-medium"
/>

Note:
Source: https://commons.wikimedia.org/wiki/File:Lee-sedol-alphago-divine-move.jpg

---

### 2017+: <span style="color: orange;">Transformers</span> — foundation for modern LLMs

<img
  src="../assets/introduction_to_ai/imgs/transformer_full_architecture.png"
  alt="Transformer full architecture diagram"
  class="img-medium"
/>

Note:
Source: https://commons.wikimedia.org/wiki/File:Transformer,_full_architecture.png

---

### How do we build AI systems?

<div class="two-col">
  <div class="box" style="text-align: left">
    <div style="color: orange; font-size: 0.95em">Symbolic AI (rules)</div>
    <ul class="muted" style="margin-top: 0.6rem">
      <li>hand-crafted rules & logic</li>
      <li>search, planning, constraints</li>
      <li>works great if rules are explicit</li>
    </ul>
  </div>
  <div class="box" style="text-align: left">
    <div style="color: lightgreen; font-size: 0.95em">Machine learning (learn from data)</div>
    <ul class="muted" style="margin-top: 0.6rem">
      <li>learn patterns from examples</li>
      <li>needs data, evaluation, iteration</li>
      <li>dominates many real-world AI systems</li>
    </ul>
  </div>
</div>

Note:
- Contrast: Deep Blue ≈ search; AlphaGo ≈ learning.

---

### Deep learning = neural networks

<img
  src="../assets/introduction_to_ai/imgs/artificial_neural_network.svg"
  alt="Artificial neural network diagram"
  class="img-small"
/>

Note:
- “Deep” = multiple hidden layers → powerful representations (vision, language, speech).
Source: https://commons.wikimedia.org/wiki/File:Artificial_neural_network.svg

---

### AI ⊃ Machine Learning ⊃ Deep learning

<img
  src="../assets/introduction_to_ai/imgs/ai_ml_dl.svg"
  alt="AI vs ML vs DL diagram"
  class="img-small"
  style="width: 60%"
/>

Note:
- Deep learning is (mostly) neural networks trained on lots of data and compute.
Source: https://commons.wikimedia.org/wiki/File:AI-ML-DL.svg

---

### Where does <span style="color: orange;">Generative AI</span> fit?

<img
  src="../assets/introduction_to_ai/imgs/ai_genai_venn.png"
  alt="AI relation to generative models venn diagram"
  class="img-small"
  style="width: 55%"
/>

Note:
- Generative AI creates new content (text, images, audio, code) — often using transformers.
Source: https://commons.wikimedia.org/wiki/File:Artificial_Intelligence_relation_to_Generative_Models_subset,_Venn_diagram.png

---

### The “learning” problem (one picture)

<div class="two-col">
  <div class="box" style="text-align: left">
    <div style="color: lightgreen; font-size: 0.95em">Inputs</div>
    <div class="muted">data points</div>
    <div style="margin-top: 0.5rem; font-size: 1.2em">
      \(x \rightarrow \hat{y}\)
    </div>
    <div class="tiny muted" style="margin-top: 0.5rem">
      Examples: customer features → churn risk, images → class, text → answer
    </div>
  </div>

  <div class="box" style="text-align: left">
    <div style="color: orange; font-size: 0.95em">Model</div>
    <div style="margin-top: 0.5rem; font-size: 1.2em">
      \(\hat{y} = f_\theta(x)\)
    </div>
    <div class="tiny muted" style="margin-top: 0.5rem">
      \(\theta\) = parameters learned from data
    </div>
  </div>

  <div class="box" style="text-align: left">
    <div style="color: yellow; font-size: 0.95em">Learning / training</div>
    <div style="margin-top: 0.5rem; font-size: 1.2em">
      \(\min_\theta \mathcal{L}(\hat{y}, y)\)
    </div>
    <div class="tiny muted" style="margin-top: 0.5rem">
      minimize a loss → better predictions / behavior
    </div>
  </div>
</div>

Note:
- Key idea: choose a model family and train its parameters to minimize a loss.
- This pattern covers ML, deep learning, and parts of generative AI.

---

### Training vs. inference

<div class="two-col">
  <div class="box" style="text-align: left">
    <div style="color: orange">Training</div>
    <div class="muted" style="margin-top: 0.5rem">
      Many examples \((x, y)\) <br />
      + optimizer <br />
      → update parameters \(\theta\)
    </div>
    <div class="tiny muted" style="margin-top: 0.7rem">
      expensive, done “offline” (hours/days/weeks)
    </div>
  </div>
  <div class="box" style="text-align: left">
    <div style="color: lightgreen">Inference</div>
    <div class="muted" style="margin-top: 0.5rem">
      New input \(x\) <br />
      + fixed \(\theta\) <br />
      → output \(\hat{y}\)
    </div>
    <div class="tiny muted" style="margin-top: 0.7rem">
      cheap(er), done “online” (milliseconds/seconds)
    </div>
  </div>
</div>

Note:
- Practical takeaway: production constraints mostly hit inference (latency, cost, reliability).

---

### Data splitting: training vs. validation vs. test

<img
  src="../assets/introduction_to_ai/imgs/train_val_test_split.png"
  alt="Training validation test split diagram"
  class="img-medium"
/>

Note:
Source: https://commons.wikimedia.org/wiki/File:ML_dataset_training_validation_test_sets.png

---

### Supervised learning

<span style="color: lightgreen;">You have labels.</span>

--

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
Confusion matrix source: https://commons.wikimedia.org/wiki/File:ConfusionMatrixRedBlue.png
Linear regression source: https://commons.wikimedia.org/wiki/File:Linear_regression.svg

---

### Unsupervised learning

<span style="color: lightgreen;">No labels</span> → discover structure (clusters, compression, anomalies).

<img
  src="../assets/introduction_to_ai/imgs/kmeans_convergence.gif"
  alt="K-means convergence animation"
  class="img-medium"
/>

Note:
Source: https://commons.wikimedia.org/wiki/File:K-means_convergence.gif

---

### Reinforcement learning (RL)

<img
  src="../assets/introduction_to_ai/imgs/reinforcement_learning_diagram.svg"
  alt="Reinforcement learning agent-environment diagram"
  class="img-medium"
/>

Note:
Source: https://commons.wikimedia.org/wiki/File:Reinforcement_learning_diagram.svg

---

### Model “zoo” (very rough)

<div class="two-col">
  <div>
    <h4 style="color: orange; margin-bottom: 0.5rem">Decision trees</h4>
    <img
      src="../assets/introduction_to_ai/imgs/simple_decision_tree.svg"
      alt="Simple decision tree diagram"
      class="img-small"
    />
  </div>
  <div>
    <h4 style="color: orange; margin-bottom: 0.5rem">Neural networks</h4>
    <img
      src="../assets/introduction_to_ai/imgs/artificial_neural_network.svg"
      alt="Artificial neural network diagram"
      class="img-small"
    />
  </div>
</div>

Note:
Decision tree source: https://commons.wikimedia.org/wiki/File:Simple_decision_tree.svg
Neural network source: https://commons.wikimedia.org/wiki/File:Artificial_neural_network.svg

---

### Training = optimization (gradient descent)

<img
  src="../assets/introduction_to_ai/imgs/gradient_descent_method.png"
  alt="Gradient descent method diagram"
  class="img-medium"
/>

Note:
Source: https://commons.wikimedia.org/wiki/File:Gradient_descent_method.png

---

### Generalization vs. overfitting

<img
  src="../assets/introduction_to_ai/imgs/overfitting.svg"
  alt="Overfitting plot: training vs validation error"
  class="img-medium"
/>

Note:
Source: https://commons.wikimedia.org/wiki/File:Overfitting_svg.svg

---

### Bias–variance tradeoff (intuition)

<img
  src="../assets/introduction_to_ai/imgs/bias_variance_total_error.svg"
  alt="Bias and variance contributing to total error"
  class="img-medium"
/>

Note:
Source: https://commons.wikimedia.org/wiki/File:Bias_and_variance_contributing_to_total_error.svg

---

### Embeddings: turning “meaning” into vectors

<img
  src="../assets/introduction_to_ai/imgs/cbow_skipgram.png"
  alt="CBOW and Skip-gram (word2vec) diagram"
  class="img-medium"
/>

<span class="muted">Later: embeddings → vector search → RAG.</span>

Note:
Source: https://commons.wikimedia.org/wiki/File:CBOW_eta_Skipgram.png

---

### From “model” to “project”: the lifecycle is iterative

<img
  src="../assets/introduction_to_ai/imgs/crisp_dm_process.png"
  alt="CRISP-DM process diagram"
  class="img-small"
  style="width: 60%"
/>

Note:
Source: https://commons.wikimedia.org/wiki/File:CRISP-DM_Process_Diagram.png

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
    <div style="color: lightgreen">Visualization idea (TODO)</div>
    <div class="muted" style="margin-top: 0.6rem">
      Plot two distributions:
      <br />
      <span style="color: yellow">training data</span> vs.
      <span style="color: red">production data</span>
      <br />
      → decision boundary no longer fits
    </div>
    <div class="tiny muted" style="margin-top: 0.7rem">
      (Add later: simple histogram + shifted histogram, or scatter plot with shifted clusters)
    </div>
  </div>
</div>

Note:
This slide is intentionally a placeholder to insert a custom plot later.

---

### Pitfall: <span style="color: orange;">automation</span> without <span style="color: lightgreen;">judgement</span>

<img
  src="../assets/introduction_to_ai/imgs/ai_moderation_cartoon.jpg"
  alt="AI cartoon: helpful vs overzealous moderation"
  class="img-medium"
/>

Note:
Source: https://commons.wikimedia.org/wiki/File:AI_cartoon_for_assisting_with_content_moderation_on_Wikipedia.jpg

---

### Wrap-up

<div class="box" style="text-align: left">
  <div style="color: lightgreen; font-size: 0.95em">If you remember 5 things:</div>
  <ul class="muted" style="margin-top: 0.6rem">
    <li>AI is bigger than ML; ML is bigger than deep learning.</li>
    <li>Learning = choose a model + minimize a loss on data.</li>
    <li>Generalization matters → splits, metrics, and overfitting checks.</li>
    <li>Embeddings + transformers power modern GenAI/LLMs.</li>
    <li>In production: data shifts, monitoring, and responsible use are key.</li>
  </ul>
</div>

--

<span style="color: lightgreen;">Next:</span> Large Language Models & Agent-based Systems
<br />
<span class="muted">(+ embeddings, vector DBs, and RAG)</span>

