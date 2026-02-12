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

What makes a good <span style="color: orange;">ETL</span> process?

- <strong>Schema documentation:</strong> clear column names + types (e.g., <em>order_date</em> is a date, not text).
- <strong>Traceability:</strong> know the source of each mart (dependency graph from raw → staging → mart).
- <strong>Monitoring + alerts:</strong> missing data triggers a notification (e.g., Slack/email).
- <strong>Testing + logging:</strong> row counts, null checks, and errors are logged.

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

- higher costs on processing the data (no free lunch)
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

<span style = "color: lightgreen">So what is a potential disadvantage of this structure? (Remember there is no free lunch!)</span>

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
