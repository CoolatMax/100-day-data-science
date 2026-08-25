# 🚀 100-Day Data Science Roadmap: Engineering → Predictive Modeling

> **Goal:** Transition from Civil Engineering + Infrastructure into a specialist **Data Science / Predictive Modeling** role in **Renewable Energy, CleanTech, or Aerospace**.

This repository documents my **100-day, hands-on transition into Data Science**, with every day producing a concrete artifact that can be committed to GitHub and shared publicly.

My approach is deliberately **domain-driven**: instead of learning Data Science through generic datasets, I apply every concept to real physical systems such as **solar generation, wind/grid data, equipment health, aerospace telemetry, predictive maintenance, geospatial systems, and time-series forecasting**.

---

## 🎯 Target Roles

I'm building toward roles such as:

* **Data Scientist — Renewable Energy**
* **Predictive Modeling Specialist**
* **Energy Data Scientist**
* **Machine Learning Engineer — CleanTech**
* **Predictive Maintenance Data Scientist**
* **Aerospace Data Scientist**
* **Telemetry / Prognostics Analyst**
* **Structural Health / Asset Analytics Specialist**

### Why this path?

My background combines:

**Civil Engineering → Infrastructure Planning → Water/Wastewater → Technical Documentation → Data Science**

That gives me a useful foundation for working with **physical systems, infrastructure data, engineering constraints, operational measurements, and domain-specific modeling**.

The goal is not to become a generic data analyst.

The goal is to become a **domain-focused predictive modeling specialist for physical industries**.

---

# 🧭 Roadmap Architecture

```text
                         100 DAYS
                            │
          ┌─────────────────┴─────────────────┐
          │                                   │
   RENEWABLE ENERGY                      AEROSPACE
          │                                   │
 Solar • Wind • Grid                    Telemetry
 Storage • Climate                      Predictive Maintenance
 GIS • Forecasting                      Prognostics
          │                                   │
          └───────────────┬───────────────────┘
                          │
                    CORE DATA SCIENCE
                          │
        ┌─────────────────┼──────────────────┐
        │                 │                  │
      Python             SQL              Statistics
        │                 │                  │
      Pandas           Data Modeling       Math
        │                 │                  │
        └─────────────────┼──────────────────┘
                          │
                    MACHINE LEARNING
                          │
             ┌────────────┼────────────┐
             │            │            │
          Regression  Classification  Clustering
             │            │            │
             └────────────┼────────────┘
                          │
              ADVANCED INDUSTRIAL ML
                          │
       Time Series • Anomaly Detection
       Geospatial • Forecasting • Monitoring
                          │
                          ▼
                 DEPLOYED CAPSTONE
                    STREAMLIT APP
```

---

# 📅 100-Day Progress Tracker

| Phase      |   Days | Focus                                           | Outcome                     |
| ---------- | -----: | ----------------------------------------------- | --------------------------- |
| 🟢 Phase 1 |   1–20 | Python, SQL, Git/GitHub                         | Reproducible data pipeline  |
| 🔵 Phase 2 |  21–40 | Pandas, NumPy, Visualization, GIS               | Feature datasets + EDA      |
| 🟣 Phase 3 |  41–60 | Math, Statistics, EDA                           | Statistical baseline        |
| 🟠 Phase 4 |  61–80 | Machine Learning                                | Production-style ML package |
| 🔴 Phase 5 | 81–100 | Time Series, Anomaly Detection, GIS, Deployment | End-to-end capstone         |

### Progress

```text
Phase 1  ████████████████████  20 / 20
Phase 2  ████████████████████  20 / 20
Phase 3  ████████████████████  20 / 20
Phase 4  ████████████████████  20 / 20
Phase 5  ████████████████████  20 / 20

Total: 100 Days
```

> Update this section every day as the roadmap progresses.

---

# 🧱 Phase 1 — Python, SQL & Docs-as-Code

### Days 1–20

**Objective:** Build the programming and data-engineering foundation required for serious ML work.

### Topics

* Python fundamentals
* Functions and modules
* File handling
* JSON / CSV
* Exception handling
* Logging
* `pytest`
* Git
* GitHub
* README engineering
* SQL fundamentals
* SQL aggregation
* JOINs
* Window functions
* CTEs
* SQLite
* NumPy
* Pandas
* Datetime handling
* Reproducible pipelines

### Industry Applications

**Renewable Energy**

* NREL solar datasets
* Open Power System Data
* Solar production analysis
* Site-level KPIs
* Resource-performance relationships
* Renewable data pipelines

**Aerospace**

* NASA C-MAPSS
* Engine telemetry
* Sensor validation
* Engine-level KPI extraction
* Cycle-based analysis
* Telemetry pipelines

### Phase Deliverable

```text
Raw Data
   ↓
Quality Checks
   ↓
Python Processing
   ↓
SQLite
   ↓
Feature Extraction
   ↓
KPI Dataset
   ↓
Markdown Report
```

---

# 📊 Phase 2 — Data Wrangling & Analysis

### Days 21–40

**Objective:** Turn messy physical-world datasets into reliable analytical datasets.

### Tools

```text
NumPy
Pandas
Matplotlib
Seaborn
GeoPandas
```

### Topics

* Missing-data analysis
* Data reshaping
* GroupBy
* Rolling windows
* Lag features
* Categorical variables
* Outlier detection
* Feature engineering
* Data-quality reporting
* Correlation analysis
* Hypothesis-driven EDA
* GIS fundamentals
* CRS transformation
* Spatial joins
* Raster/vector concepts
* Spatial enrichment

### Industry Applications

#### Renewable Energy

* Site performance analysis
* Weather/resource relationships
* Solar resource mapping
* Geographic site comparison
* Environmental features
* Production anomaly candidates

#### Aerospace

* Sensor distributions
* Engine health exploration
* Telemetry trends
* Operating-regime analysis
* Sensor correlations
* Geographic asset analysis

### Phase Deliverable

A **versioned feature dataset** with:

* Data dictionary
* Provenance
* Quality report
* EDA notebook
* Feature engineering pipeline

---

# 📐 Phase 3 — Mathematics, Statistics & EDA

### Days 41–60

**Objective:** Develop the mathematical intuition required to understand and debug machine-learning models.

### Mathematics

* Vectors
* Matrices
* Dot products
* Matrix transformations
* Eigenvectors
* PCA
* Derivatives
* Gradients
* Optimization
* Gradient descent

### Statistics

* Descriptive statistics
* Probability
* Distributions
* Bayesian reasoning
* Conditional probability
* Confidence intervals
* Hypothesis testing
* t-tests
* Mann–Whitney tests
* ANOVA
* Regression assumptions
* Residual analysis
* Data leakage
* Confounding
* Class imbalance

### Industry Questions

Instead of asking only:

> "Can I calculate the mean?"

I want to answer:

> "What does normal operation look like?"

> "How uncertain is this estimate?"

> "Is this difference statistically meaningful?"

> "Is this sensor actually predictive?"

> "Am I leaking future information?"

### Phase Deliverable

A complete **statistical baseline report** containing:

```text
Distributions
      ↓
Uncertainty
      ↓
Hypothesis Tests
      ↓
Residual Diagnostics
      ↓
Feature Screening
      ↓
Modeling Candidates
```

---

# 🤖 Phase 4 — Machine Learning Core

### Days 61–80

**Objective:** Move from statistical analysis into predictive modeling.

### Core Stack

```python
Python
NumPy
Pandas
Scikit-Learn
Matplotlib
Seaborn
GeoPandas
```

### Algorithms

* Linear Regression
* Ridge
* Lasso
* Logistic Regression
* Decision Trees
* Random Forest
* Gradient Boosting
* Clustering
* PCA
* Ensemble Methods

### Modeling Concepts

* Train / validation / test
* Cross-validation
* Time-aware validation
* Group-aware validation
* Feature engineering
* Feature importance
* Permutation importance
* Partial dependence
* Hyperparameter tuning
* Class imbalance
* Threshold optimization
* Model comparison
* Model cards

### Renewable Energy Models

Potential problems:

```text
Solar Production Forecasting
PV Underperformance Detection
Renewable Asset Classification
Site Segmentation
Energy Performance Prediction
```

### Aerospace Models

Potential problems:

```text
Engine Health Prediction
Degradation Classification
Predictive Maintenance
Remaining Useful Life
Sensor Anomaly Detection
Fleet Segmentation
```

### Phase Deliverable

A complete ML release containing:

```text
Dataset
   ↓
Preprocessing Pipeline
   ↓
Feature Engineering
   ↓
Model
   ↓
Validation
   ↓
Benchmark
   ↓
Model Interpretation
   ↓
Model Card
   ↓
Serialized Model
```

---

# ⏱️ Phase 5 — Advanced Industrial Modeling

### Days 81–100

**Objective:** Apply Data Science to the types of sequential, spatial and operational problems encountered in real engineering systems.

---

## Time-Series Modeling

* Trend
* Seasonality
* Stationarity
* Autocorrelation
* Lag features
* Rolling features
* Forecast horizons
* Forecast validation
* Exponential smoothing
* ML forecasting

### Renewable applications

```text
Next-hour generation
Next-day production
Weather-aware forecasting
Site-level forecasting
Forecast error analysis
```

### Aerospace applications

```text
Next-cycle sensor prediction
Telemetry trend forecasting
Degradation forecasting
Engine health trajectories
```

---

# 🚨 Anomaly Detection

Learn:

* Z-score methods
* Robust thresholds
* Isolation Forest
* Distribution shifts
* Change-point concepts

### Renewable

Detect:

* Unexpected production drops
* Resource/output mismatch
* Sensor failures
* Persistent underperformance

### Aerospace

Detect:

* Sensor anomalies
* Degradation patterns
* Abnormal telemetry
* Operational regime changes

---

# 🌍 Geospatial Modeling

Use:

* GeoPandas
* CRS transformations
* Spatial joins
* Spatial features
* Spatial validation

### Renewable

```text
Site coordinates
      ↓
Climate / Resource Context
      ↓
Spatial Features
      ↓
Performance Modeling
```

### Aerospace

```text
Airport / Asset Geography
      ↓
Regional Context
      ↓
Spatial Features
      ↓
Asset / Operational Analysis
```

---

# 🖥️ Deployment

### Streamlit

Build interactive applications showing:

### Renewable Dashboard

* Asset map
* Production KPIs
* Forecast
* Anomaly alerts
* Weather context
* Site filtering

### Aerospace Dashboard

* Fleet overview
* Engine health
* Sensor trends
* Degradation probability
* Anomaly alerts
* Asset filtering

---

# 🏆 Final Capstone

## Option A — Renewable Energy

### Renewable Asset Performance & Forecasting Platform

```text
Open Renewable Dataset
        ↓
Data Quality Pipeline
        ↓
Feature Engineering
        ↓
Time-Series Forecasting
        ↓
Anomaly Detection
        ↓
Geospatial Analysis
        ↓
Model Evaluation
        ↓
Streamlit Dashboard
```

### Example Questions

* How much energy should this asset produce?
* When is an asset underperforming relative to its resource?
* Which sites behave differently?
* What signals predict performance deterioration?
* Can anomalies be detected before a major production loss?

---

# ✈️ Option B — Aerospace

## Aircraft Engine Health & Predictive Maintenance Platform

```text
NASA Telemetry
       ↓
Data Quality Pipeline
       ↓
Sensor Feature Engineering
       ↓
Health / Degradation Model
       ↓
Anomaly Detection
       ↓
Time-Series Analysis
       ↓
Model Evaluation
       ↓
Streamlit Dashboard
```

### Example Questions

* Is the engine behaving normally?
* Which sensors are most predictive of degradation?
* Can degradation be detected before failure?
* Which engines require attention first?
* Can future health be predicted from recent telemetry?

---

# 🌐 Open Dataset Sources

## Renewable Energy / CleanTech

| Source                                                                | Useful For                                          |
| --------------------------------------------------------------------- | --------------------------------------------------- |
| [NREL Solar Data & Tools](https://www.nrel.gov/solar/data-tools.html) | Solar irradiance, PV and renewable-energy datasets  |
| [NREL Developer Network](https://developer.nrel.gov/)                 | APIs and programmatic renewable-energy data         |
| [Open Power System Data](https://data.open-power-system-data.org/)    | Electricity load, wind, solar and power-system data |
| [NOAA Climate Data](https://www.ncei.noaa.gov/cdo-web/)               | Weather and climate features                        |
| [USGS Data](https://www.usgs.gov/products/data)                       | Environmental and geospatial datasets               |

## Aerospace / Telemetry

| Source                                                                                                                                                 | Useful For                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------- |
| [NASA Prognostics Center of Excellence](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/) | Prognostics and predictive-maintenance datasets |
| [NASA C-MAPSS](https://data.nasa.gov/)                                                                                                                 | Turbofan engine telemetry                       |
| [NASA Open Data](https://data.nasa.gov/)                                                                                                               | Aerospace and scientific datasets               |
| [NOAA NCEI](https://www.ncei.noaa.gov/access)                                                                                                          | Weather/environmental context                   |
| [USGS APIs](https://earthquake.usgs.gov/fdsnws/event/1/)                                                                                               | Open geospatial/event data                      |

---

# 🛠️ Technology Stack

## Programming

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-336791?style=for-the-badge\&logo=postgresql\&logoColor=white)

## Data Science

![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge\&logo=numpy\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge\&logo=pandas\&logoColor=white)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge\&logo=scikit-learn\&logoColor=white)

## Visualization & GIS

![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge)
![GeoPandas](https://img.shields.io/badge/GeoPandas-139C5A?style=for-the-badge)

## Engineering Workflow

![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge\&logo=git\&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge\&logo=github\&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge\&logo=jupyter\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)

---

# 📚 Daily Execution System

Every day follows the same workflow:

```text
1. Learn one concept
        ↓
2. Apply it to physical-industry data
        ↓
3. Build a micro-project
        ↓
4. Document the result
        ↓
5. Commit to GitHub
        ↓
6. Share the learning on LinkedIn
```

### Daily GitHub Standard

Every day should ideally produce:

```text
/Day-XX/
├── README.md
├── notebook.ipynb
├── src/
├── data/
└── outputs/
```

Where appropriate:

```text
README.md
    ↓
Problem
Dataset
Approach
Results
Limitations
Next Step
```

---

# 🔥 100-Day Micro-Project Philosophy

The goal is **not**:

> Learn Python → Learn Pandas → Learn ML → Make one project.

The goal is:

> **Learn → Build → Document → Commit → Communicate**

100 days × 1 deliverable = **100 public evidence points of progress**

And because every project has two tracks:

```text
100 Days
   ×
2 Industry Options
   =
200 Micro-Project Opportunities
```

---

# 📈 Portfolio Strategy

By the end of the roadmap, the portfolio should contain evidence of:

| Capability        | Evidence                           |
| ----------------- | ---------------------------------- |
| Python            | Reusable analysis modules          |
| SQL               | Industrial feature queries         |
| Data Wrangling    | Clean feature datasets             |
| Statistics        | Statistical baseline reports       |
| Machine Learning  | Benchmark + trained models         |
| Time Series       | Forecasting project                |
| Anomaly Detection | Industrial monitoring prototype    |
| GIS               | Spatial feature/model analysis     |
| MLOps Thinking    | Pipelines + model cards            |
| Deployment        | Streamlit application              |
| Domain Knowledge  | Renewable + Aerospace projects     |
| Communication     | Technical READMEs + LinkedIn posts |

---

# 🧠 What I Want to Be Able to Say After Day 100

> **"I don't just know Machine Learning algorithms. I can take physical-world engineering data, clean and analyze it, engineer domain-specific features, build statistically valid predictive models, validate them appropriately, detect anomalies, incorporate spatial and temporal context, and deploy the result as a usable application."**

That is the capability this roadmap is designed to demonstrate.

---

# 🗂️ Suggested Repository Structure

```text
100-day-data-science/
│
├── README.md
│
├── phase-01-python-sql/
│   ├── day-01/
│   ├── day-02/
│   └── ...
│
├── phase-02-data-analysis/
│   ├── day-21/
│   ├── day-22/
│   └── ...
│
├── phase-03-math-statistics/
│   ├── day-41/
│   ├── day-42/
│   └── ...
│
├── phase-04-machine-learning/
│   ├── day-61/
│   ├── day-62/
│   └── ...
│
├── phase-05-advanced-modeling/
│   ├── day-81/
│   ├── day-82/
│   └── ...
│
├── capstone-renewable/
│
├── capstone-aerospace/
│
└── resources/
```

---

# ✅ Progress Log

Update this table throughout the journey.

| Day | Topic              | Renewable Track           | Aerospace Track                 | Status |
| --: | ------------------ | ------------------------- | ------------------------------- | ------ |
|  01 | Python Environment | NREL data loader          | NASA telemetry loader           | ⬜      |
|  02 | Functions          | Solar analytics functions | Engine summary functions        | ⬜      |
|  03 | Validation         | Irradiance QC             | Telemetry QC                    | ⬜      |
|  04 | Data Structures    | Site metadata             | Engine metadata                 | ⬜      |
|  05 | File I/O           | Dataset manifest          | Telemetry report                | ⬜      |
| ... | ...                | ...                       | ...                             | ⬜      |
|  20 | Pipeline           | Renewable pipeline        | Telemetry pipeline              | ⬜      |
|  40 | Feature Dataset    | Renewable features        | Aerospace features              | ⬜      |
|  60 | Statistics         | Statistical baseline      | Statistical baseline            | ⬜      |
|  80 | ML Release         | Renewable model           | Aerospace model                 | ⬜      |
| 100 | Capstone           | Energy platform           | Predictive maintenance platform | ⬜      |

> The full 100-day interactive roadmap contains the detailed daily blueprint for all remaining days.

---

# 📌 Repository Principles

### 1. Reproducibility

Every analysis should be reproducible from a clean environment.

### 2. Domain-first feature engineering

Features should have a physical or operational rationale whenever possible.

### 3. Leakage prevention

The model must never use information that would not be available at prediction time.

### 4. Appropriate validation

Use:

* Time-based splits for forecasting
* Group-based splits for fleet/engine data
* Spatial splits for location-dependent models

### 5. Model before complexity

Start with a strong baseline.

Then add complexity only when the data proves it is useful.

### 6. Communicate every result

Every project should explain:

```text
What was the problem?
What data was used?
What was built?
What happened?
What does it mean?
What are the limitations?
What should happen next?
```

---

# 🚀 Final Outcome

By Day 100, this repository should demonstrate a complete transition from:

```text
Engineering Background
        ↓
Programming
        ↓
Data Analysis
        ↓
Statistics
        ↓
Machine Learning
        ↓
Time-Series
        ↓
Geospatial Modeling
        ↓
Anomaly Detection
        ↓
Deployment
        ↓
Predictive Modeling Specialist
```

---

## Current Status

**🎯 Target:** Predictive Modeling / Data Science Specialist
**🏭 Industries:** Renewable Energy + Aerospace
**📅 Roadmap:** 100 Days
**🔬 Approach:** Domain-driven + project-based
**📦 Deliverables:** 100 daily artifacts + 2 capstone tracks
**🧰 Core Stack:** Python · SQL · Pandas · NumPy · Scikit-Learn · GeoPandas · Git · Streamlit

---

## ⭐ Follow the Journey

Every day I am documenting what I learn, what I build, what failed, and what I would change.

The objective is simple:

> **100 days of consistent execution → a portfolio that proves predictive modeling ability in real physical industries.**

---

### Related Projects

* ☀️ Renewable Energy Analytics
* 🌬️ Wind / Grid Forecasting
* 🔋 Energy Storage Modeling
* ✈️ Aerospace Telemetry
* 🔧 Predictive Maintenance
* 🌍 Geospatial Engineering Analytics
* 📈 Time-Series Forecasting
* 🚨 Industrial Anomaly Detection

---

**Built with engineering discipline, one dataset and one commit at a time.**
