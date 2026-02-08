<!-- TODO: 
 - one slide with some examples
 - ai based future is full of ai and human need to find reinvent themself if even possible
 - talking about AGI, superintelligence, ...
 - taking it a little slower and start with the fundamentals.
 - EU AI Act, some regulatories
 - shit in shit out (data)
 - Implications of AI should be a unique little excursion where the students can discuss that
 - what does a world with a superintelligence might look like? -->

Where are we located during the lecture?

<img
  src="../assets/introduction_to_ai/imgs/imgs.001.png"
  alt="Overview"
  style="
    width: 800px;
    margin: 0 auto 4rem auto;
    background: transparent;
  "
/>

---

#### <span style="color: lightgreen;"> Why does AI matter for BI? </span>

<div class="two-col">
  <div>
    <img
      src="../assets/introduction_to_ai/imgs/ai_hero.jpg"
      alt="Artificial Intelligence illustration"
      style="height: 30vh; width: auto; max-width: 100%"
    />
  </div>

--

  <div class="box" style="text-align: left; font-size: 0.85em">
    <div style="color: lightgrey; font-size: 0.95em">From data to dashboards to decisions, e.g.</div>
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

#### Timeline overview (big picture)

<img
  src="../assets/introduction_to_ai/imgs/imgs.002.png"
  alt="Overview"
  style="
    width: 800px;
    margin: 0 auto 4rem auto;
    background: transparent;
  "
/>

Note:
- Use as map, then zoom into characters + turning points.
- In this lecture we stop around AlphaGo; the modern GenAI part is next lecture.
Source: https://commons.wikimedia.org/wiki/File:AI-History-Timeline-300dpi.jpg

--

#### Can machines think?

<img
  src="../assets/introduction_to_ai/imgs/imgs.003.png"
  alt="Overview"
  style="
    width: 800px;
    margin: 0 auto 4rem auto;
    background: transparent;
  "
/>

--

#### A new field was born

<img
  src="../assets/introduction_to_ai/imgs/imgs.004.png"
  alt="Overview"
  style="
    width: 800px;
    margin: 0 auto 4rem auto;
    background: transparent;
  "
/>

---

#### <span style="color: lightgreen;"> How would you define Artificial Intelligence?</span>

--

#### <span style="color: lightgreen;"> Please read the <a href="http://jmc.stanford.edu/articles/dartmouth/dartmouth.pdf">Dartmouth research proposal</a></span>

--

<span style="color: orange;">Artificial Intelligence</span> is the <span style="color: orange;">simulation</span> of <span style="color: orange;">intelligence</span>, especially <span style="color: orange;">learning</span>.

---

#### <span style="color: lightgreen;"> Research 3 historical breakthroughs in the field of AI and describe them.</span>

---

#### Eras of AI

--

#### Era 1: Pre-Deep Learning (1950s-2010)

<div style="display: flex; gap: 2rem; align-items: center;">
  <div style="flex: 1; text-align: left; font-size: 0.85em;">
    <ul>
      <li><span style="color: orange;">Context:</span> Dartmouth 1956, symbolic AI + early ML</li>
      <li><span style="color: orange;">Moore's Law:</span> compute doubles ~every 20 months</li>
      <li><span style="color: orange;">Focus:</span> rules, logic, expert systems, limited data</li>
      <li><span style="color: orange;">AI winters:</span> 1970s and late 1980s funding cuts</li>
    </ul>
  </div>
</div>

--

#### Moore's Law

<img
  src="../assets/introduction_to_ai/imgs/imgs.005.png"
  alt="Overview"
  style="
    width: 800px;
    margin: 0 auto 4rem auto;
    background: transparent;
  "
/>

--

#### Era 2: Deep Learning Era (2010-2015)

<div style="display: flex; gap: 2rem; align-items: center;">
  <div style="flex: 1; text-align: left; font-size: 0.85em;">
    <ul>
      <li><span style="color: orange;">Context:</span> big data + GPUs + new NN techniques</li>
      <li><span style="color: orange;">Acceleration:</span> compute use doubles ~every 6 months</li>
      <li><span style="color: orange;">Focus:</span> image recognition and early NLP</li>
      <li><span style="color: orange;">Milestones:</span> AlexNet (2012) and deep CNNs</li>
    </ul>
  </div>
  <div style="flex: 1;">
    <svg width="360" height="220" viewBox="0 0 360 220" aria-label="Compute acceleration">
      <rect x="0" y="0" width="360" height="220" fill="transparent"></rect>
      <line x1="30" y1="185" x2="330" y2="185" stroke="#888" stroke-width="2"></line>
      <line x1="30" y1="185" x2="30" y2="25" stroke="#888" stroke-width="2"></line>
      <path d="M30 175 L80 150 L130 120 L180 85 L230 55 L280 35 L330 25" stroke="#ff6b6b" stroke-width="3" fill="none"></path>
      <text x="34" y="205" fill="#aaa" font-size="12">2010</text>
      <text x="292" y="205" fill="#aaa" font-size="12">2015</text>
      <text x="40" y="40" fill="#aaa" font-size="12">Compute</text>
      <text x="120" y="70" fill="#ff6b6b" font-size="12">~6 months</text>
      <text x="120" y="85" fill="#ff6b6b" font-size="12">doubling</text>
    </svg>
    <div style="font-size: 0.6em; color: #aaa;">Training compute accelerates</div>
  </div>
</div>

--

#### Era 3: Large-Scale Era (2015-Present)

<div style="display: flex; gap: 2rem; align-items: center;">
  <div style="flex: 1; text-align: left; font-size: 0.85em;">
    <ul>
      <li><span style="color: orange;">Context:</span> models 10-100x larger + massive datasets</li>
      <li><span style="color: orange;">Focus:</span> foundation models, LLMs, advanced vision</li>
      <li><span style="color: orange;">Shift:</span> deployment, alignment, agents (2025-2026)</li>      
    </ul>
  </div>
  <div style="flex: 1;">
    <img
      src="../assets/introduction_to_ai/imgs/imgs.006.png"
      alt="AI timeline"
      style="width: 420px; max-width: 100%; height: auto; background: transparent;"
    />
    <div style="font-size: 0.6em; color: #aaa;">Modern AI timeline (context)</div>
  </div>
</div>

---

#### Classification of AI

<img
  src="../assets/introduction_to_ai/imgs/imgs.007.png"
  alt="Overview"
  style="
    width: 800px;
    margin: 0 auto 4rem auto;
    background: transparent;
  "
/>

---

#### <span style="color: lightgreen;"> Try to describe your 3 historical breakthroughs in AI from the beginning of the lecture in more technical terms.</span>

