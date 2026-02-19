"""Generate showcase images for the README."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# --- Tufte defaults -----------------------------------------------------------

TUFTE_RC = {
    "font.family": "serif",
    "font.serif": ["Palatino", "Palatino Linotype", "Georgia", "DejaVu Serif"],
    "font.size": 12,
    "figure.facecolor": "#fffff8",
    "figure.dpi": 200,
    "axes.facecolor": "#fffff8",
    "axes.edgecolor": "#cccccc",
    "axes.linewidth": 0.5,
    "axes.labelcolor": "#666666",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": False,
    "xtick.color": "#999999",
    "ytick.color": "#999999",
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.major.size": 3,
    "ytick.major.size": 3,
    "xtick.major.width": 0.5,
    "ytick.major.width": 0.5,
    "lines.linewidth": 1.5,
    "savefig.facecolor": "#fffff8",
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.3,
}

C = {
    "text": "#111111",
    "text2": "#666666",
    "text3": "#999999",
    "gray": "#666666",
    "highlight": "#e41a1c",
    "axis": "#cccccc",
    "cat": ["#4e79a7", "#f28e2b", "#e15759", "#76b7b2"],
}


def tufte_axes(ax, x_data, y_data):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_bounds(min(x_data), max(x_data))
    ax.spines["left"].set_bounds(min(y_data), max(y_data))
    ax.tick_params(direction="in", length=3, width=0.5)


# ==============================================================================
# Chart 1: Tufte Line Chart
# ==============================================================================

plt.rcParams.update(TUFTE_RC)

months = np.arange(1, 13)
mlabels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
           "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [42, 48, 51, 49, 56, 62, 58, 65, 71, 68, 75, 82]
target  = [40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62]

fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(months, target, color=C["gray"], linewidth=1, linestyle="--")
ax.plot(months, revenue, color=C["highlight"], linewidth=2)
tufte_axes(ax, months, revenue + target)

# Direct labels
ax.annotate("Revenue", xy=(12, 82), xytext=(8, 0), textcoords="offset points",
            fontsize=12, color=C["highlight"], va="center", fontfamily="serif")
ax.annotate("Target", xy=(12, 62), xytext=(8, 0), textcoords="offset points",
            fontsize=12, color=C["gray"], va="center", fontfamily="serif")

# Annotate peak
ax.annotate("Peak: $82k", xy=(12, 82), xytext=(0, 18), textcoords="offset points",
            fontsize=11, fontstyle="italic", color="#333", fontfamily="serif",
            ha="center", arrowprops=dict(arrowstyle="-", color="#ccc", lw=0.5))

ax.set_xticks(months)
ax.set_xticklabels(mlabels)
ax.set_ylabel("Revenue ($k)", fontsize=12, color=C["text2"])

fig.text(0.125, 0.95, "Monthly Revenue vs. Target, 2025",
         fontsize=18, fontfamily="serif", color=C["text"])
fig.text(0.125, 0.91, "Revenue exceeded target every month, accelerating in H2",
         fontsize=13, fontfamily="serif", color=C["text2"])

plt.tight_layout()
plt.subplots_adjust(top=0.88)
plt.savefig("/Users/ranman/dev/caylent/tufte-data-viz/_docs/tufte-line-chart.png")
plt.close()


# ==============================================================================
# Chart 2: Tufte Horizontal Bar Chart
# ==============================================================================

categories = ["Product A", "Product B", "Product C", "Product D", "Product E"]
values = [42, 38, 27, 19, 12]

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.barh(categories, values, color=C["gray"], height=0.55)

# Highlight the leader
bars[0].set_color(C["highlight"])

for bar, val in zip(bars, values):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
            f"${val}k", va="center", fontsize=12, color=C["text2"], fontfamily="serif")

for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_xticks([])
ax.tick_params(left=False)
ax.invert_yaxis()

fig.text(0.04, 0.95, "Revenue by Product",
         fontsize=18, fontfamily="serif", color=C["text"])
fig.text(0.04, 0.90, "Product A leads with 31% of total revenue",
         fontsize=13, fontfamily="serif", color=C["text2"])

plt.tight_layout()
plt.subplots_adjust(top=0.85)
plt.savefig("/Users/ranman/dev/caylent/tufte-data-viz/_docs/tufte-bar-chart.png")
plt.close()


# ==============================================================================
# Chart 3: Before/After Comparison
# ==============================================================================

np.random.seed(42)
x = np.arange(1, 13)
y1 = np.array([20, 25, 22, 30, 28, 35, 33, 40, 38, 42, 45, 50])
y2 = np.array([15, 18, 20, 22, 25, 27, 30, 32, 35, 37, 40, 43])

fig, axes = plt.subplots(1, 2, figsize=(16, 5.5))

# --- BEFORE: Default matplotlib (chartjunk) ---
ax = axes[0]
for param in ["axes.spines.top", "axes.spines.right", "axes.grid"]:
    ax.spines["top"].set_visible(True)
    ax.spines["right"].set_visible(True)
ax.set_facecolor("#ffffff")
ax.grid(True, color="#cccccc", linewidth=0.8, alpha=0.7)
ax.plot(x, y1, "o-", color="#1f77b4", linewidth=2, markersize=6, label="Series A")
ax.plot(x, y2, "s-", color="#ff7f0e", linewidth=2, markersize=6, label="Series B")
ax.legend(loc="upper left", frameon=True, facecolor="white", edgecolor="black")
ax.set_title("Default Chart Style", fontsize=16, fontweight="bold", fontfamily="sans-serif")
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Value", fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(mlabels, fontsize=9)
ax.spines["top"].set_visible(True)
ax.spines["right"].set_visible(True)
ax.spines["top"].set_color("black")
ax.spines["right"].set_color("black")
ax.spines["bottom"].set_color("black")
ax.spines["left"].set_color("black")
for s in ax.spines.values():
    s.set_linewidth(1)
ax.tick_params(direction="out", length=5, width=1)
fig.text(0.26, 0.02, "BEFORE", fontsize=14, fontfamily="sans-serif",
         color="#cc0000", ha="center", fontweight="bold")

# --- AFTER: Tufte style ---
ax = axes[1]
ax.set_facecolor("#fffff8")
ax.plot(x, y1, color=C["highlight"], linewidth=2)
ax.plot(x, y2, color=C["gray"], linewidth=1.5)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_bounds(min(x), max(x))
ax.spines["left"].set_bounds(min(y2), max(y1))
ax.spines["bottom"].set_color(C["axis"])
ax.spines["left"].set_color(C["axis"])
ax.spines["bottom"].set_linewidth(0.5)
ax.spines["left"].set_linewidth(0.5)
ax.tick_params(direction="in", length=3, width=0.5, colors=C["text3"])
ax.set_xticks(x)
ax.set_xticklabels(mlabels, fontsize=9, color=C["text3"])
ax.set_ylabel("Value", fontsize=12, color=C["text2"], fontfamily="serif")

# Direct labels
ax.annotate("Series A", xy=(12, 50), xytext=(8, 0), textcoords="offset points",
            fontsize=12, color=C["highlight"], va="center", fontfamily="serif")
ax.annotate("Series B", xy=(12, 43), xytext=(8, 0), textcoords="offset points",
            fontsize=12, color=C["gray"], va="center", fontfamily="serif")

ax.set_title("Tufte Style", fontsize=16, fontweight="normal", fontfamily="serif",
             color=C["text"])
fig.text(0.74, 0.02, "AFTER", fontsize=14, fontfamily="serif",
         color=C["highlight"], ha="center", fontweight="bold")

fig.patch.set_facecolor("#fffff8")
plt.tight_layout()
plt.subplots_adjust(bottom=0.1, wspace=0.25)
plt.savefig("/Users/ranman/dev/caylent/tufte-data-viz/_docs/before-after.png")
plt.close()


# ==============================================================================
# Chart 4: Small Multiples
# ==============================================================================

np.random.seed(7)
regions = ["North", "South", "East", "West"]
data = {r: np.cumsum(np.random.randn(12) * 3 + 2) for r in regions}
global_min = min(min(v) for v in data.values()) - 2
global_max = max(max(v) for v in data.values()) + 2

fig, axes = plt.subplots(1, 4, figsize=(16, 3.5), sharey=True)

for ax, region in zip(axes, regions):
    ax.plot(x, data[region], color=C["gray"], linewidth=1.5)
    ax.set_title(region, fontsize=14, fontfamily="serif", fontweight="normal",
                 color=C["text"], loc="left")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_color(C["axis"])
    ax.spines["bottom"].set_linewidth(0.5)
    ax.spines["left"].set_color(C["axis"])
    ax.spines["left"].set_linewidth(0.5)
    ax.set_ylim(global_min, global_max)
    ax.tick_params(direction="in", length=3, width=0.5, colors=C["text3"], labelsize=9)
    ax.set_xticks([1, 4, 7, 10])
    ax.set_xticklabels(["Jan", "Apr", "Jul", "Oct"], fontsize=9)

# Only show y-axis label on leftmost
for ax in axes[1:]:
    ax.tick_params(labelleft=False)
    ax.spines["left"].set_visible(False)

fig.patch.set_facecolor("#fffff8")
fig.text(0.08, 0.98, "Revenue Trend by Region",
         fontsize=16, fontfamily="serif", color=C["text"], va="top")
plt.tight_layout()
plt.subplots_adjust(top=0.82, wspace=0.1)
plt.savefig("/Users/ranman/dev/caylent/tufte-data-viz/_docs/small-multiples.png")
plt.close()

# ==============================================================================
# Chart 5: Dark Mode Line Chart (Rule 19)
# ==============================================================================

TUFTE_DARK_RC = {
    **TUFTE_RC,
    "figure.facecolor": "#151515",
    "axes.facecolor": "#151515",
    "axes.edgecolor": "#444444",
    "axes.labelcolor": "#999999",
    "xtick.color": "#666666",
    "ytick.color": "#666666",
    "savefig.facecolor": "#151515",
}

CD = {
    "text": "#dddddd",
    "text2": "#999999",
    "text3": "#666666",
    "gray": "#999999",
    "highlight": "#fc8d62",
    "axis": "#444444",
    "cat": ["#6a9fd8", "#f2a860", "#e87a7c", "#8accc7"],
}

plt.rcParams.update(TUFTE_DARK_RC)

fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(months, target, color=CD["gray"], linewidth=1, linestyle="--")
ax.plot(months, revenue, color=CD["highlight"], linewidth=2)
tufte_axes(ax, months, revenue + target)
ax.spines["bottom"].set_color(CD["axis"])
ax.spines["left"].set_color(CD["axis"])

ax.annotate("Revenue", xy=(12, 82), xytext=(8, 0), textcoords="offset points",
            fontsize=12, color=CD["highlight"], va="center", fontfamily="serif")
ax.annotate("Target", xy=(12, 62), xytext=(8, 0), textcoords="offset points",
            fontsize=12, color=CD["gray"], va="center", fontfamily="serif")

ax.annotate("Peak: $82k", xy=(12, 82), xytext=(0, 18), textcoords="offset points",
            fontsize=11, fontstyle="italic", color=CD["text2"], fontfamily="serif",
            ha="center", arrowprops=dict(arrowstyle="-", color=CD["axis"], lw=0.5))

ax.set_xticks(months)
ax.set_xticklabels(mlabels)
ax.set_ylabel("Revenue ($k)", fontsize=12, color=CD["text2"])

fig.text(0.125, 0.95, "Revenue Beat Target Every Month in 2025",
         fontsize=18, fontfamily="serif", color=CD["text"])
fig.text(0.125, 0.91, "Gap widened from 2k in Jan to 20k in Dec, accelerating in H2",
         fontsize=13, fontfamily="serif", color=CD["text2"])

plt.tight_layout()
plt.subplots_adjust(top=0.88)
plt.savefig("/Users/ranman/dev/caylent/tufte-data-viz/_docs/tufte-dark-mode.png")
plt.close()


# ==============================================================================
# Chart 6: Accessible Scatter — Dual Encoding (Rule 16)
# ==============================================================================

plt.rcParams.update(TUFTE_RC)

np.random.seed(99)
groups = {
    "Enterprise":  {"x": np.random.normal(70, 12, 15), "y": np.random.normal(85, 8, 15),
                    "marker": "o", "color": "#4e79a7"},
    "Mid-Market":  {"x": np.random.normal(45, 10, 20), "y": np.random.normal(60, 10, 20),
                    "marker": "s", "color": "#f28e2b"},
    "SMB":         {"x": np.random.normal(25, 8, 25),  "y": np.random.normal(35, 12, 25),
                    "marker": "D", "color": "#76b7b2"},
}

fig, ax = plt.subplots(figsize=(9, 6))

for name, g in groups.items():
    ax.scatter(g["x"], g["y"], marker=g["marker"], c=g["color"],
              s=40, alpha=0.7, edgecolors="none", label=name)
    # Direct label at cluster centroid
    cx, cy = np.mean(g["x"]), np.mean(g["y"])
    ax.annotate(name, xy=(cx, cy), xytext=(12, 0), textcoords="offset points",
                fontsize=12, color=g["color"], va="center", fontfamily="serif",
                fontweight="bold")

all_x = np.concatenate([g["x"] for g in groups.values()])
all_y = np.concatenate([g["y"] for g in groups.values()])
tufte_axes(ax, all_x, all_y)

ax.set_xlabel("Deal Cycle (days)", fontsize=12, color=C["text2"])
ax.set_ylabel("Win Rate (%)", fontsize=12, color=C["text2"])

fig.text(0.125, 0.95, "Enterprise Wins Faster and More Often",
         fontsize=18, fontfamily="serif", color=C["text"])
fig.text(0.125, 0.91, "Each shape = segment (accessible without color)",
         fontsize=13, fontfamily="serif", color=C["text2"])

plt.tight_layout()
plt.subplots_adjust(top=0.88)
plt.savefig("/Users/ranman/dev/caylent/tufte-data-viz/_docs/tufte-accessible-scatter.png")
plt.close()


# ==============================================================================
# Chart 7: Light vs Dark Side-by-Side (Rule 19)
# ==============================================================================

fig, axes = plt.subplots(1, 2, figsize=(16, 5.5))

themes = [
    {"bg": "#fffff8", "text": "#111111", "text2": "#666666", "text3": "#999999",
     "gray": "#666666", "highlight": "#e41a1c", "axis": "#cccccc", "label": "Light Mode"},
    {"bg": "#151515", "text": "#dddddd", "text2": "#999999", "text3": "#666666",
     "gray": "#999999", "highlight": "#fc8d62", "axis": "#444444", "label": "Dark Mode"},
]

products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
vals = [42, 38, 27, 19, 12]

for ax, t in zip(axes, themes):
    ax.set_facecolor(t["bg"])
    bars = ax.barh(products, vals, color=t["gray"], height=0.55)
    bars[0].set_color(t["highlight"])

    for bar, val in zip(bars, vals):
        ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
                f"${val}k", va="center", fontsize=12, color=t["text2"], fontfamily="serif")

    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_xticks([])
    ax.tick_params(left=False, colors=t["text3"])
    ax.set_yticks(range(len(products)))
    ax.set_yticklabels(products, color=t["text2"], fontfamily="serif")
    ax.invert_yaxis()

    ax.set_title(t["label"], fontsize=14, fontfamily="serif", color=t["text2"],
                 fontweight="normal", loc="left", pad=8)

fig.patch.set_facecolor("#fffff8")
# Split background: left half light, right half dark
from matplotlib.patches import Rectangle
fig.patches.append(Rectangle((0.5, 0), 0.5, 1, transform=fig.transFigure,
                              facecolor="#151515", zorder=-1))

fig.text(0.25, 1.0, r"Product A Leads Revenue at $42k",
         fontsize=16, fontfamily="serif", color="#111111", ha="center", va="top")
fig.text(0.75, 1.0, r"Product A Leads Revenue at $42k",
         fontsize=16, fontfamily="serif", color="#dddddd", ha="center", va="top")

plt.tight_layout()
plt.subplots_adjust(top=0.85, wspace=0.3)
plt.savefig("/Users/ranman/dev/caylent/tufte-data-viz/_docs/tufte-light-dark.png")
plt.close()


print("Generated all showcase images.")
