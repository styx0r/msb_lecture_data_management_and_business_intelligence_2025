<style>
.small-list {
    font-size: 0.7em;
    list-style: none; /* Remove default list styling */
    counter-reset: section; /* Initialize counter */
}

.small-list li {
    counter-increment: section; /* Increment counter */
    margin-bottom: 0.5em; /* Add spacing between items */
}

.smaller-list {
    font-size: 0.6em;
    list-style: none; /* Remove default list styling */
    counter-reset: section; /* Initialize counter */
}

.smaller-list li {
    counter-increment: section; /* Increment counter */
    margin-bottom: 0.5em; /* Add spacing between items */
}

.small-text {
    font-size: 0.7em;
}

.smaller-text {
    font-size: 0.6em;
}
</style>

Where are we located during the lecture?

<img
  src="../assets/data_management/imgs/imgs.001.png"
  alt="Overview"
  style="
    width: 800px;
    margin: 0 auto 4rem auto;
    background: transparent;
  "
/>

---

<span style="color: orange;">Outlook</span>

- data management architectures
- lyvy's architecture
- realtime architecture
- Cloud vs. On-Premise

---

<span style="color: orange;">Data management architectures</span>

---

<span style="color: orange;">Data Warehouse</span>

--

<img
  src="../assets/data_management/imgs/imgs.002.png"
  alt="Data Warehouse"
  style="
    width: 1600px;
    margin: 0 auto 4rem auto;
    background: transparent;
  "
/>

--

<span style="color: orange;">Description</span>

<ol class="small-list">
<li>Central hub for cleaned, structured data (e.g., <em>sales_orders</em>, <em>customers</em>, <em>products</em>).</li>
<li>Data from many sources is collected, cleaned, and loaded (ETL) into consistent tables.</li>
<li>Library analogy: to answer “Q4 revenue in Germany”, you go to the right shelf (sales) and index (country, date).</li>
<li>Result: fast, consistent reporting and BI dashboards.</li>
</ol>

--

<span style='color: lightgreen'>What can be high cost drivers in a pure data warehouse architecture?</span>

--

<span style="color: orange;">Answer (examples)</span>

<ol class="small-list">
<li><strong>Schema changes:</strong> changing a mart often means reprocessing months/years of data.</li>
<li><strong>Complex ETL:</strong> many joins and transformations increase compute time.</li>
<li><strong>Large history reloads:</strong> backfills are expensive.</li>
<li><strong>Many marts:</strong> maintaining many curated tables adds cost and effort.</li>
</ol>

--

<span style="color: orange;">Pros</span>

<ol class="small-list">
<li><strong>Clear lineage:</strong> you can see how a table was built (e.g., dbt model “monthly_revenue”).</li>
<li><strong>Fast queries:</strong> dashboards load quickly on curated data marts (e.g., sales by month).</li>
<li><strong>Stronger governance:</strong> access control by domain (e.g., HR mart separate from sales).</li>
</ol>

--

<span style="color: orange;">Cons</span>

<ol class="small-list">
<li><strong>Less flexible for raw exploration:</strong> not ideal for logs/text/audio without extra storage.</li>
<li><strong>Schema changes are costly:</strong> changing a mart can require reloading pipelines.</li>
<li><strong>Raw data may be lost:</strong> if the source keeps data only briefly (e.g., 7‑day logs).</li>
</ol>

--

#### Example: e-commerce dashboard

<ul class="small-list">
  <li>Daily funnel: sessions → add_to_cart → orders</li>
  <li>Bounce rate and conversion rate</li>
  <li>Slice by <em>utm_source</em> (organic / paid / email)</li>
</ul>

--

#### Raw tables (messy)

<div class="two-col">
  <div>
    <div style="color: orange;">raw_web_events</div>
    <table class="small-list">
      <tr><th>event_time</th><th>session_id</th><th>user_id</th><th>event</th><th>utm_source</th></tr>
      <tr><td>2024/10/01 12:01</td><td>s-11</td><td>u-7</td><td>page_view</td><td>paid</td></tr>
      <tr><td>2024/10/01 12:02</td><td>s-11</td><td>u-7</td><td>add_to_cart</td><td>paid</td></tr>
      <tr><td>2024/10/01 12:03</td><td>s-12</td><td>u-9</td><td>page_view</td><td>organic</td></tr>
    </table>
  </div>
  <div>
    <div style="color: orange;">raw_orders</div>
    <table class="small-list">
      <tr><th>order_time</th><th>order_id</th><th>user_id</th><th>total_cents</th><th>currency</th></tr>
      <tr><td>2024-10-01T12:05Z</td><td>O-1001</td><td>u-7</td><td>129900</td><td>USD</td></tr>
      <tr><td>2024-10-01T12:10Z</td><td>O-1002</td><td>u-9</td><td>4990</td><td>EUR</td></tr>
    </table>
  </div>
</div>

<div style="margin-top: 0.6rem; font-size: 0.85em;">
  Messy: different time formats, multiple events per session, currencies not aligned.
</div>

--

#### Staging tables (cleaned, reusable)

<div class="two-col">
  <div>
    <div style="color: orange;">stg_sessions</div>
    <table class="small-list">
      <tr><th>session_id</th><th>date</th><th>utm_source</th><th>events</th><th>bounce</th></tr>
      <tr><td>s-11</td><td>2024-10-01</td><td>paid</td><td>5</td><td>0</td></tr>
      <tr><td>s-12</td><td>2024-10-01</td><td>organic</td><td>1</td><td>1</td></tr>
    </table>
  </div>
  <div>
    <div style="color: orange;">stg_orders</div>
    <table class="small-list">
      <tr><th>order_id</th><th>date</th><th>session_id</th><th>revenue_eur</th></tr>
      <tr><td>O-1001</td><td>2024-10-01</td><td>s-11</td><td>118.00</td></tr>
      <tr><td>O-1002</td><td>2024-10-01</td><td>s-12</td><td>49.90</td></tr>
    </table>
  </div>
</div>

<div style="margin-top: 0.6rem; font-size: 0.85em;">
  Staging is clean + reusable for multiple marts (marketing, finance, product).
</div>

--

#### Mart table (dashboard-specific)

<div style="color: orange;">mart_daily_funnel</div>
<table class="small-list">
  <tr><th>date</th><th>utm_source</th><th>sessions</th><th>bounces</th><th>add_to_cart</th><th>orders</th><th>conversion</th></tr>
  <tr><td>2024-10-01</td><td>paid</td><td>120</td><td>18</td><td>45</td><td>20</td><td>16.7%</td></tr>
  <tr><td>2024-10-01</td><td>organic</td><td>180</td><td>40</td><td>30</td><td>15</td><td>8.3%</td></tr>
</table>

<div style="margin-top: 0.6rem; font-size: 0.85em;">
  This is built exactly for the dashboard charts (fast and simple).
</div>

--

#### What makes a good <span style="color: orange;">ETL</span> process?

- <strong>Schema documentation:</strong> clear column names + types (e.g., <em>order_date</em> is a date, not text).
- <strong>Traceability:</strong> know the source of each mart (dependency graph from raw → staging → mart).
- <strong>Monitoring + alerts:</strong> missing data triggers a notification (e.g., Slack/email).
- <strong>Testing + logging:</strong> row counts, null checks, and errors are logged.

--

#### Use <span style="color: orange;">tooling</span> meant for this purpose

- Often done with plain Python: connect to sources, transform data, and load into the warehouse.
- <span style="color: orange;">by far better:</span> use <span style="color: orange;">dbt</span> to get documentation, tests, and lineage (what makes a good ETL process).

--

#### by convention with structure

<img
  src="../assets/data_management/imgs/imgs.009.png"
  alt="Data Lake"
  style="
    width: 1600px;
    margin: 0 auto 4rem auto;
    background: transparent;
  "
/>

--

#### additionally webui for documentation & tracing

<img
  src="../assets/data_management/imgs/imgs.010.png"
  alt="Data Lake"
  style="
    width: 1600px;
    margin: 0 auto 4rem auto;
    background: transparent;
  "
/>

---

<span style="color: orange;">Data Lake</span>

--

<img
  src="../assets/data_management/imgs/imgs.003.png"
  alt="Data Lake"
  style="
    width: 1600px;
    margin: 0 auto 4rem auto;
    background: transparent;
  "
/>

--

<span style="color: orange;">Description</span>

<ol class="small-list">
<li>A Data Lake serves as a central hub for storing all kinds of data</li>
<li>Information is extracted and directly loaded into the storage, <b>without transformations.</b></li>
<li>The design of a Data Lake resembles a copy of the original data sources, enabling data exploration, data science and machine learning tasks.</li>
<li>This organization allows businesses to persist data sources and making them long-term available.</li>
</ol>

--

<span style = "color: lightgreen">Please provide a short list of pros and cons for the Data Lake.</span>

--

<span style="color: orange;">Pros</span>

- high flexibility, agility and no limits regarding
  - data format structure
  - type of data
  - amount of data
- typically low costs on storage size (roughly ranges from $0.01 to $0.025 / GB / month)

--

<span style="color: orange;">Cons</span>

- higher costs on processing the data
- lack of structure, therefore lack of transparency: risk of becoming a data swamp
- security challenges: might be challenging to identify security threats because of vast amount of data in vast amount of formats
- no default query execution: another tooling is necessary

---

<span style="color: orange;">Hybrid Data Lake</span>

--

<img
  src="../assets/data_management/imgs/imgs.004.png"
  alt="Hybrid Data Lake"
  style="
    width: 1600px;
    margin: 0 auto 4rem auto;
    background: transparent;
  "
/>

--

<span style="color: orange;">Description</span>

<ol class="small-list">
<li>A Hybrid Data Lake combines the advantages of Data Warehouses and Data Lakes</li>
<li>to the expense of complexity.</li>
</ol>

--

Regarding costs, in a Hybrid Data Lake setting, the amount of storage is increased.

<span style = "color: lightgreen">When is it still advisable?</span>

---

<span style="color: orange;">Data Lakehouse</span>

--

<img
  src="../assets/data_management/imgs/imgs.005.png"
  alt="Lakehouse"
  style="
    width: 1600px;
    margin: 0 auto 4rem auto;
    background: transparent;
  "
/>

--

<span style="color: orange;">Description</span>

<ol class="small-list">
<li>A Lakehouse combines the advantages of Data Warehouses and Data Lakes</li>
<li>and still keeps complexity low.</li>
<li>Often standalone query engine is necessary.</li>
</ol>

<span style = "color: lightgreen">So what is a potential disadvantage of this structure?</span>

--

<span style="color: orange;">Hybrid Data Lake or Lakehouse?</span>

- Hybrid Data Lake can provide high performance (low latency for e.g. operational BI) data with cheap data query costs
- Lakehouse lower complexity, less expenses regarding maintenance and still good performance, sufficient for most cases

---

<span style='color:red'>Don't think of these architectures as being set in stone. They all have advantages and disadvantages and are applied in modified and combined forms.</span>

---

<span style="color: orange;">On-Premises vs. Cloud</span>

<span style="color: lightgreen;">
Please study the following link and explain with your words the difference between On-Premises and Cloud.
What different levels are there in the cloud sector and how do they differ?
</span>

[On-Premises vs. Cloud](https://www.bmc.com/blogs/saas-vs-paas-vs-iaas-whats-the-difference-and-how-to-choose/)

---

<span style="color: orange;">Deep-dive into lyvy's architecture</span>

--

<img
  src="../assets/data_management/imgs/imgs.007.png"
  alt="Lakehouse"
  style="
    width: 1600px;
    margin: 0 auto 4rem auto;
    background: transparent;
  "
/>

---

<span style="color: orange;">A realtime architecture</span>

--

<img
  src="../assets/data_management/imgs/imgs.008.png"
  alt="Lakehouse"
  style="
    width: 1600px;
    margin: 0 auto 4rem auto;
    background: transparent;
  "
/>
