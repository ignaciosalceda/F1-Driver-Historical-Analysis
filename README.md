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
  - `win_ratio`: % of races where the driver beat their teammate
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
- Used 6 clusters to identify performance tiers:
  - `Elite`
  - `Winners`
  - `Overperformers`
  - `Decent`
  - `Underperformers`
  - `Poor`

### 4. **Labeling Tiers**
- Mapped each cluster to a human-readable label based on relative performance to teammates and scoring consistency.

---

## 💻 Streamlit App

A full **interactive web app** was built using **Streamlit**:

- 🧍 **Driver Explorer**: Select any driver to see:
  - Their cluster label and visual definition
  - Highlighted position in a 2D plot of all drivers
  - A ranking table showing nearby drivers in performance

- 📖 **Project Overview Page**:
  - Explains the methodology, clusters, and why this analysis matters
  - Helps casual and expert F1 fans alike understand the value of this data-centric approach

- 🖼️ (Optional) Integration with Wikipedia API for fetching driver images was tested and removed to optimize performance.

> The app allows fans to **explore, compare, and understand** driver greatness beyond surface-level stats.

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
- A full-featured, user-friendly Streamlit app.
