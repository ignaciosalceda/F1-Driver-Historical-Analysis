# 🏎️ F1 Driver Performance Profiling Project

## 🎯 Objective
To classify Formula 1 drivers into **performance tiers** using a **data-driven, standardized approach** that accounts for historical differences in racing eras, points systems, and equipment (cars).

---

## 📊 Dataset Summary
- Driver race history including:
  - `final_position`
  - `points`
  - `grid_starting_position`
  - `constructor_name`
  - Other relevant metadata

- Calculated for each driver:
  - `ratio_points_per_race`: Total corrected points / total races
  - `win_ratio`: % of times finished above teammate
  - `combined_metric`: product of the above two (used earlier for ranking)

---

## 🧠 Methodology

### 1. **Feature Engineering**
- Computed driver-level metrics:
  - `ratio_points_per_race`
  - `win_ratio`

### 2. **Standardization**
- Scaled both features using **`StandardScaler`** to prepare for clustering.

### 3. **K-Means Clustering**
- Applied **K-Means** clustering on the 2D feature space.
- Used 3 clusters to identify performance tiers:
  - `Elite`
  - `Consistent`
  - `Support`

### 4. **Labeling Tiers**
- Mapped each cluster to a human-readable label based on win rate and scoring performance.

### 5. **Visualization**
- Created a **zoomable, interactive Plotly scatter plot**:
  - Axes: `ratio_points_per_race` vs. `win_ratio`
  - Color: Cluster labels
  - Labels: Driver names shown directly next to each point

---

## 🔬 Technical Validation

- ✔ **Elbow Method**: Identified optimal number of clusters using inertia plot.
- ✔ **Silhouette Score**: Evaluated the quality of separation between clusters.
- ✔ **Centroid Analysis**: Interpreted cluster characteristics.
- ✔ **Cluster Distribution**: Checked for balance in cluster sizes.

---

## ✅ Output
- A labeled, zoomable 2D map of F1 drivers by performance tier.
- A robust, standardized approach to profiling drivers across different F1 eras and contexts.
- An interpretable model that balances scoring performance with teammate-relative dominance.
