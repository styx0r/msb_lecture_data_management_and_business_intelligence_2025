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

#### Symbolic AI example: rule-based system

<div style="display: flex; gap: 2rem; align-items: center;">
  <div style="flex: 1; text-align: left; font-size: 0.85em;">
    <ul>
      <li><span style="color: orange;">Use case:</span> fraud detection at checkout</li>
      <li><span style="color: orange;">Rules:</span> IF/THEN logic (transparent, brittle)</li>
      <li>
        <span style="color: orange;">Example decision logic:</span><br />
        ≥3 failed payment attempts → block<br />
        else if new customer → if order &gt; €500 AND credit card → manual review; else approve<br />
        else if billing ≠ shipping → if rush shipping OR new address → flag; else approve<br />
        else if high-risk category AND order &gt; €300 → manual review; else approve
      </li>
    </ul>
  </div>
</div>

Note:
- create decision tree on white board
- create the corresponding python code

--

#### <span style="color: lightgreen;"> Create the rule based decision tree!</span>

---

#### Symbolic AI example: search (parcel delivery)

<div style="display: flex; gap: 2rem; align-items: center;">
  <div style="flex: 1; text-align: left; font-size: 0.85em;">
    <ul>
      <li><span style="color: orange;">Use case:</span> parcel delivery shortest route</li>
      <li><span style="color: orange;">State:</span> current city/node in the graph</li>
      <li><span style="color: orange;">Goal:</span> reach destination with minimal cost</li>
      <li><span style="color: orange;">Algorithm:</span> Dijkstra or A* (weighted graph)</li>
    </ul>
  </div>
  <div style="flex: 1;">
<img
  src="../assets/introduction_to_ai/animations/Astar_progress_animation.gif"
  alt="Overview"
  style="
    width: 800px;
    margin: 0 auto 4rem auto;
    background: transparent;
  "
/>
  </div>
</div>

---

#### From Data to Decisions: The ML Family

<img
  src="../assets/introduction_to_ai/imgs/imgs.008.png"
  alt="Overview"
  style="
    width: 800px;
    margin: 0 auto 4rem auto;
    background: transparent;
  "
/>

---

#### <span style="color: lightgreen;">Mini-talk: learning paradigms</span>

- Form 6 groups: 3 <span style="color: orange;">presenters</span> + 3 <span style="color: orange;">challenge teams</span>
- Topics: <span style="color: orange;">supervised</span>, <span style="color: orange;">unsupervised</span>, <span style="color: orange;">reinforcement</span> (each has a presenter + challenger)
- ~25-30 min prep, ~5 min talk + ~3 min Q&A per topic
- Must include: <span style="color: orange;">data</span>, <span style="color: orange;">algorithm</span>, <span style="color: orange;">prediction/output</span>
- Provide one concrete example
- Prep on slides, Miro board, or similar

--

#### <span style="color: lightgreen;">Your example template</span>

<table style="width: 80%; margin: 0 auto; font-size: 0.85em;">
  <tr>
    <th style="text-align: left; width: 25%;">Step</th>
    <th style="text-align: left;">What you answer</th>
  </tr>
  <tr>
    <td>Problem</td>
    <td>What are we trying to predict/optimize?</td>
  </tr>
  <tr>
    <td>Data</td>
    <td>What inputs do we have? Are there labels?</td>
  </tr>
  <tr>
    <td>Algorithm</td>
    <td>Which method would you use (name 1)?</td>
  </tr>
  <tr>
    <td>Prediction</td>
    <td>What is the model output?</td>
  </tr>
</table>

--

#### <span style="color: lightgreen;">Quick reference cards</span>

<div style="display: flex; gap: 1.5rem; text-align: left; font-size: 0.8em;">
  <div style="flex: 1; border: 1px solid #666; border-radius: 10px; padding: 0.7rem;">
    <div style="color: orange; font-weight: bold;">Supervised learning</div>
    <div>Labels available (y)</div>
    <div>Examples: churn, fraud, demand</div>
    <div>Algorithms: linear/logistic reg., trees</div>
  </div>
  <div style="flex: 1; border: 1px solid #666; border-radius: 10px; padding: 0.7rem;">
    <div style="color: orange; font-weight: bold;">Unsupervised learning</div>
    <div>No labels, find structure</div>
    <div>Examples: segmentation, anomalies</div>
    <div>Algorithms: k-means, PCA</div>
  </div>
  <div style="flex: 1; border: 1px solid #666; border-radius: 10px; padding: 0.7rem;">
    <div style="color: orange; font-weight: bold;">Reinforcement learning</div>
    <div>Learn by rewards</div>
    <div>Examples: pricing, routing</div>
    <div>Algorithms: Q-learning, policy gradient</div>
  </div>
</div>

---

#### Supervised vs. Unsupervised: labels or not?

<div style="display: flex; gap: 1.5rem; align-items: center; font-size: 0.9em;">
  <div style="flex: 1; border: 1px solid #666; border-radius: 12px; padding: 0.9rem;">
    <div style="color: orange; font-weight: bold;">Supervised learning</div>
    <div>Inputs <span style="color: orange;">x</span> + labels <span style="color: orange;">y</span></div>
    <div>Goal: predict <span style="color: orange;">y</span> for new x</div>
    <div>Examples: churn, fraud, demand</div>
  </div>
  <div style="flex: 1; border: 1px solid #666; border-radius: 12px; padding: 0.9rem;">
    <div style="color: orange; font-weight: bold;">Unsupervised learning</div>
    <div>Inputs <span style="color: orange;">x</span> only (no labels)</div>
    <div>Goal: discover structure or clusters</div>
    <div>Examples: segmentation, anomalies</div>
  </div>
</div>

---

#### Supervised learning: regression first

<div style="display: flex; gap: 2rem; align-items: center;">
  <div style="flex: 1; text-align: left; font-size: 0.9em;">
    <div><span style="color: orange;">Use case:</span> predict delivery time or demand.</div>
    <ul>
      <li><span style="color: orange;">Inputs (x):</span> distance, traffic, basket size.</li>
      <li><span style="color: orange;">Target (y):</span> delivery time (minutes).</li>
      <li><span style="color: orange;">Output:</span> a number.</li>
    </ul>
  </div>
  <div style="flex: 1;">
    <svg width="380" height="240" viewBox="0 0 380 240" aria-label="Regression line">
      <line x1="40" y1="200" x2="340" y2="200" stroke="#777" stroke-width="2"></line>
      <line x1="40" y1="200" x2="40" y2="30" stroke="#777" stroke-width="2"></line>
      <circle cx="80" cy="160" r="5" fill="#55c2ff"></circle>
      <circle cx="110" cy="150" r="5" fill="#55c2ff"></circle>
      <circle cx="140" cy="145" r="5" fill="#55c2ff"></circle>
      <circle cx="170" cy="130" r="5" fill="#55c2ff"></circle>
      <circle cx="200" cy="120" r="5" fill="#55c2ff"></circle>
      <circle cx="230" cy="110" r="5" fill="#55c2ff"></circle>
      <circle cx="260" cy="95" r="5" fill="#55c2ff"></circle>
      <path d="M70 170 Q170 130 300 80" stroke="#ffa500" stroke-width="3" fill="none"></path>
      <text x="250" y="75" fill="#ffa500" font-size="12">prediction</text>
    </svg>
  </div>
</div>

---

#### Training phase: learn the parameters

<div style="display: flex; gap: 1.5rem; align-items: center;">
  <div style="flex: 1; text-align: left; font-size: 0.9em;">
    <ul>
      <li><span style="color: orange;">Model:</span> y = w1 * x + b</li>
      <li><span style="color: orange;">Loss:</span> how wrong are we?</li>
      <li><span style="color: orange;">Update:</span> adjust w, b to reduce loss</li>
      <li><span style="color: orange;">Result:</span> best-fit line (training)</li>
    </ul>
    <div style="color: #aaa; font-size: 0.75em;">
      If you want: add a 3-step animation of the line moving.
    </div>
  </div>
  <div style="flex: 1;">
    <svg width="380" height="220" viewBox="0 0 380 220" aria-label="Parameter updates">
      <line x1="40" y1="180" x2="340" y2="180" stroke="#777" stroke-width="2"></line>
      <line x1="40" y1="180" x2="40" y2="30" stroke="#777" stroke-width="2"></line>
      <path d="M70 160 Q170 140 300 110" stroke="#888" stroke-width="2" fill="none"></path>
      <path d="M70 170 Q170 130 300 80" stroke="#ffa500" stroke-width="3" fill="none"></path>
      <path d="M70 150 Q170 110 300 60" stroke="#55c2ff" stroke-width="2" fill="none"></path>
      <text x="250" y="105" fill="#888" font-size="11">step 1</text>
      <text x="250" y="75" fill="#ffa500" font-size="11">step 2</text>
      <text x="250" y="55" fill="#55c2ff" font-size="11">step 3</text>
    </svg>
  </div>
</div>

---

#### Regression example: demand forecasting

<div style="display: flex; gap: 2rem; align-items: center;">
  <div style="flex: 1; text-align: left; font-size: 0.9em;">
    <ul>
      <li><span style="color: orange;">Data:</span> past sales, price, promotions, season.</li>
      <li><span style="color: orange;">Model:</span> linear regression.</li>
      <li><span style="color: orange;">Prediction:</span> units sold next week.</li>
      <li><span style="color: orange;">Use:</span> inventory planning.</li>
    </ul>
  </div>
  <div style="flex: 1;">
    <svg width="380" height="220" viewBox="0 0 380 220" aria-label="Forecast line">
      <line x1="40" y1="180" x2="340" y2="180" stroke="#777" stroke-width="2"></line>
      <line x1="40" y1="180" x2="40" y2="30" stroke="#777" stroke-width="2"></line>
      <path d="M50 160 L90 140 L130 150 L170 120 L210 130 L250 110 L290 100" stroke="#55c2ff" stroke-width="2" fill="none"></path>
      <path d="M290 100 L330 90" stroke="#ffa500" stroke-width="3" fill="none"></path>
      <text x="290" y="85" fill="#ffa500" font-size="12">forecast</text>
    </svg>
  </div>
</div>

---

#### Classification example: neural network classifier

<div style="display: flex; gap: 2rem; align-items: center;">
  <div style="flex: 1; text-align: left; font-size: 0.9em;">
    <div><span style="color: orange;">Task:</span> classify orders as fraud or not.</div>
    <ul>
      <li><span style="color: orange;">Inputs:</span> features (device, value, time).</li>
      <li><span style="color: orange;">Output:</span> class probability.</li>
      <li><span style="color: orange;">Model:</span> neural network.</li>
    </ul>
  </div>
  <div style="flex: 1;">
    <div
      style="
        border: 2px dashed #666;
        border-radius: 10px;
        height: 220px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #aaa;
        font-size: 0.75em;
      "
    >
      Insert your neural network classification image here
    </div>
  </div>
</div>

---

#### Unsupervised learning: k-means clustering

<div style="display: flex; gap: 2rem; align-items: center;">
  <div style="flex: 1; text-align: left; font-size: 0.9em;">
    <div><span style="color: orange;">Idea:</span> group similar points without labels.</div>
    <ul>
      <li><span style="color: orange;">Input:</span> customer features only.</li>
      <li><span style="color: orange;">Output:</span> cluster assignment.</li>
      <li><span style="color: orange;">Use:</span> segmentation.</li>
    </ul>
  </div>
  <div style="flex: 1;">
    <svg width="380" height="230" viewBox="0 0 380 230" aria-label="K-means clusters">
      <circle cx="110" cy="150" r="7" fill="#55c2ff"></circle>
      <circle cx="95" cy="130" r="7" fill="#55c2ff"></circle>
      <circle cx="125" cy="135" r="7" fill="#55c2ff"></circle>
      <circle cx="260" cy="110" r="7" fill="#ff6b6b"></circle>
      <circle cx="240" cy="90" r="7" fill="#ff6b6b"></circle>
      <circle cx="280" cy="90" r="7" fill="#ff6b6b"></circle>
      <circle cx="200" cy="190" r="7" fill="#8bdc65"></circle>
      <circle cx="180" cy="170" r="7" fill="#8bdc65"></circle>
      <circle cx="210" cy="165" r="7" fill="#8bdc65"></circle>
      <circle cx="160" cy="70" r="7" fill="#f1c453"></circle>
      <circle cx="180" cy="55" r="7" fill="#f1c453"></circle>
      <circle cx="200" cy="75" r="7" fill="#f1c453"></circle>
    </svg>
  </div>
</div>

---

#### k-means: step-by-step

<div style="display: flex; gap: 1rem; font-size: 0.85em;">
  <div style="flex: 1; border: 1px solid #666; border-radius: 10px; padding: 0.7rem;">
    <div style="color: orange; font-weight: bold;">1) Initialize</div>
    <div>Pick k starting centroids</div>
  </div>
  <div style="flex: 1; border: 1px solid #666; border-radius: 10px; padding: 0.7rem;">
    <div style="color: orange; font-weight: bold;">2) Assign</div>
    <div>Attach points to nearest centroid</div>
  </div>
  <div style="flex: 1; border: 1px solid #666; border-radius: 10px; padding: 0.7rem;">
    <div style="color: orange; font-weight: bold;">3) Update</div>
    <div>Move centroids to the mean</div>
  </div>
  <div style="flex: 1; border: 1px solid #666; border-radius: 10px; padding: 0.7rem;">
    <div style="color: orange; font-weight: bold;">Repeat</div>
    <div>Until centroids stop moving</div>
  </div>
</div>

---

#### k-means example: customer segments

<div style="display: flex; gap: 2rem; align-items: center;">
  <div style="flex: 1; text-align: left; font-size: 0.9em;">
    <ul>
      <li><span style="color: orange;">Features:</span> frequency, basket size, returns.</li>
      <li><span style="color: orange;">Clusters:</span> value seekers, loyalists, premium.</li>
      <li><span style="color: orange;">Action:</span> tailor offers per segment.</li>
    </ul>
  </div>
  <div style="flex: 1;">
    <div
      style="
        border: 2px dashed #666;
        border-radius: 10px;
        height: 200px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #aaa;
        font-size: 0.75em;
      "
    >
      Optional: insert a segmentation chart
    </div>
  </div>
</div>

---

#### <span style="color: lightgreen;"> Try to describe your 3 historical breakthroughs in AI from the beginning of the lecture in more technical terms.</span>

