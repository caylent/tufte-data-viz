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

fig.text(0.125, 0.95, "Revenue Exceeded Target Every Month, Accelerating in H2",
         fontsize=18, fontfamily="serif", color=C["text"])
fig.text(0.125, 0.91, "Monthly revenue vs. target, 2025",
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

fig.text(0.04, 0.95, "Product A Leads With 31% of Total Revenue",
         fontsize=18, fontfamily="serif", color=C["text"])
fig.text(0.04, 0.90, "Revenue by product, sorted by value",
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
fig.text(0.08, 0.98, "North and East Outpaced South and West in 2025",
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
              s=40, alpha=0.7, edgecolors="none")
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


# ==============================================================================
# Chart 8: Slopegraph — Before/After Comparison
# ==============================================================================

plt.rcParams.update(TUFTE_RC)

slope_data = {
    "Engineering": (35, 42),
    "Sales":       (28, 31),
    "Marketing":   (22, 18),
    "Support":     (15, 20),
    "Design":      (12, 15),
}

fig, ax = plt.subplots(figsize=(6, 7))

for name, (before, after) in slope_data.items():
    change = after - before
    color = C["highlight"] if abs(change) == max(abs(b - a) for a, b in slope_data.values()) else C["gray"]
    lw = 2 if color == C["highlight"] else 1.2
    alpha = 1.0 if color == C["highlight"] else 0.5

    ax.plot([0, 1], [before, after], color=color, linewidth=lw, alpha=alpha)

    # Left labels (before)
    ax.text(-0.08, before, f"{name}  {before}%", ha="right", va="center",
            fontsize=11, color=color, fontfamily="serif", alpha=alpha)
    # Right labels (after)
    ax.text(1.08, after, f"{after}%  {name}", ha="left", va="center",
            fontsize=11, color=color, fontfamily="serif", alpha=alpha)

# Column headers
ax.text(0, max(v[0] for v in slope_data.values()) + 3, "2024", ha="center",
        fontsize=13, color=C["text2"], fontfamily="serif", fontweight="bold")
ax.text(1, max(v[1] for v in slope_data.values()) + 3, "2025", ha="center",
        fontsize=13, color=C["text2"], fontfamily="serif", fontweight="bold")

# Clean axes
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(-0.4, 1.4)

fig.text(0.12, 0.96, "Engineering Headcount Grew Most, Marketing Shrank",
         fontsize=16, fontfamily="serif", color=C["text"])
fig.text(0.12, 0.92, "Team size as % of company, 2024 vs. 2025",
         fontsize=12, fontfamily="serif", color=C["text2"])

plt.tight_layout()
plt.subplots_adjust(top=0.89)
plt.savefig("/Users/ranman/dev/caylent/tufte-data-viz/_docs/tufte-slopegraph.png")
plt.close()


# ==============================================================================
# Chart 9: Sparklines in a Table
# ==============================================================================

np.random.seed(42)
metrics = {
    "Revenue":    np.cumsum(np.random.randn(24) * 2 + 1.5),
    "Users":      np.cumsum(np.random.randn(24) * 1 + 2),
    "Conversion": 4 + np.cumsum(np.random.randn(24) * 0.3),
    "Churn":      3 - np.cumsum(np.random.randn(24) * 0.15 + 0.05),
    "NPS":        50 + np.cumsum(np.random.randn(24) * 2),
}

fig, axes = plt.subplots(len(metrics), 1, figsize=(8, 4.5))

for i, (name, data) in enumerate(metrics.items()):
    ax = axes[i]
    ax.plot(data, color=C["gray"], linewidth=1)

    # Min/max dots
    imin, imax = np.argmin(data), np.argmax(data)
    ax.plot(imin, data[imin], "o", color=C["highlight"], markersize=3)
    ax.plot(imax, data[imax], "o", color=C["cat"][0], markersize=3)

    # Endpoint value
    ax.text(len(data) + 0.5, data[-1], f"{data[-1]:.1f}",
            fontsize=10, color=C["text2"], va="center", fontfamily="serif")

    # Metric name
    ax.text(-1, data[len(data)//2], name, ha="right", va="center",
            fontsize=12, color=C["text"], fontfamily="serif")

    # Strip everything
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.margins(y=0.2)

    # Thin separator between rows (except last)
    if i < len(metrics) - 1:
        ax.axhline(y=ax.get_ylim()[0], color="#eeeeee", linewidth=0.5,
                   xmin=-0.15, xmax=1.15, clip_on=False)

fig.text(0.5, 0.98, "Key Metrics, Last 24 Months",
         fontsize=16, fontfamily="serif", color=C["text"], ha="center", va="top")
fig.text(0.5, 0.94, "Red dot = min, blue dot = max",
         fontsize=11, fontfamily="serif", color=C["text2"], ha="center", va="top")

fig.patch.set_facecolor("#fffff8")
plt.tight_layout()
plt.subplots_adjust(top=0.88, left=0.18, right=0.92, hspace=0.4)
plt.savefig("/Users/ranman/dev/caylent/tufte-data-viz/_docs/tufte-sparklines.png")
plt.close()


# ==============================================================================
# Chart 10: Tufte Data Table
# ==============================================================================

fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis("off")

# Table data
headers = ["Region", "Q1", "Q2", "Q3", "Q4", "Total", "vs. Prior"]
rows = [
    ["North",  "12.4",  "14.1",  "16.8",  "18.2",  "$61.5M",  "+18%"],
    ["South",  "8.1",   "9.3",   "11.2",  "12.8",  "$41.4M",  "+12%"],
    ["East",   "6.2",   "7.4",   "8.9",   "9.1",   "$31.6M",  "+22%"],
    ["West",   "5.8",   "6.1",   "6.5",   "7.0",   "$25.4M",  "+5%"],
]

col_x = [0.3, 2.2, 3.4, 4.6, 5.8, 7.2, 8.8]
header_y = 7.0
row_start_y = 6.0
row_spacing = 1.2

# Headers
for j, h in enumerate(headers):
    align = "left" if j == 0 else "right"
    ax.text(col_x[j], header_y, h, fontsize=11, fontfamily="serif",
            color=C["text2"], ha=align, fontweight="bold")

# Top rule
ax.plot([0.1, 9.6], [header_y - 0.35, header_y - 0.35],
        color=C["text"], linewidth=1, clip_on=False)

for i, row in enumerate(rows):
    y = row_start_y - i * row_spacing

    for j, val in enumerate(row):
        align = "left" if j == 0 else "right"
        color = C["text"]
        fontweight = "normal"

        # Highlight the leader in "vs. Prior"
        if j == 6 and val == "+22%":
            color = C["highlight"]
            fontweight = "bold"

        ax.text(col_x[j], y, val, fontsize=11, fontfamily="serif",
                color=color, ha=align, fontweight=fontweight)

    # Thin rule after every row
    if i < len(rows) - 1:
        ax.plot([0.1, 9.6], [y - 0.5, y - 0.5],
                color="#eeeeee", linewidth=0.5, clip_on=False)

# Bottom rule
bottom_y = row_start_y - (len(rows) - 1) * row_spacing - 0.5
ax.plot([0.1, 9.6], [bottom_y, bottom_y],
        color=C["text"], linewidth=1, clip_on=False)

fig.text(0.06, 0.96, "East Region Grew Fastest at 22% Year-Over-Year",
         fontsize=16, fontfamily="serif", color=C["text"])
fig.text(0.06, 0.90, "Quarterly revenue by region, 2025 (millions USD)",
         fontsize=12, fontfamily="serif", color=C["text2"])

fig.patch.set_facecolor("#fffff8")
plt.tight_layout()
plt.subplots_adjust(top=0.82)
plt.savefig("/Users/ranman/dev/caylent/tufte-data-viz/_docs/tufte-data-table.png")
plt.close()


# ==============================================================================
# Chart 11: Animated Before/After GIF
# ==============================================================================

from matplotlib.animation import FuncAnimation, PillowWriter

x_anim = np.arange(1, 13)
y1_anim = np.array([20, 25, 22, 30, 28, 35, 33, 40, 38, 42, 45, 50])
y2_anim = np.array([15, 18, 20, 22, 25, 27, 30, 32, 35, 37, 40, 43])

# Interpolation helper
def lerp(a, b, t):
    return a + (b - a) * t

def make_frame(t):
    """t in [0, 1]: 0 = 'before' (default), 1 = 'after' (Tufte)."""
    fig_a, ax_a = plt.subplots(figsize=(9, 6))

    # Background
    bg = lerp(np.array([1.0, 1.0, 1.0]), np.array([1.0, 1.0, 248/255]), t)
    fig_a.patch.set_facecolor(bg)
    ax_a.set_facecolor(bg)

    # Grid fades out
    if t < 0.8:
        grid_alpha = lerp(0.7, 0.0, t / 0.8)
        ax_a.grid(True, color="#cccccc", linewidth=0.8, alpha=grid_alpha)

    # Spine visibility fades
    for spine_name in ["top", "right"]:
        spine_alpha = lerp(1.0, 0.0, min(t * 2, 1.0))
        ax_a.spines[spine_name].set_alpha(spine_alpha)
        ax_a.spines[spine_name].set_color("black")

    # Bottom/left spines transition color
    frame_color = lerp(np.array([0, 0, 0]), np.array([0.8, 0.8, 0.8]), t)
    for spine_name in ["bottom", "left"]:
        ax_a.spines[spine_name].set_color(frame_color)
        ax_a.spines[spine_name].set_linewidth(lerp(1.0, 0.5, t))

    # Lines: markers shrink, colors shift
    marker_size = lerp(6, 0, t)
    s1_color = lerp(np.array([0.12, 0.47, 0.71]), np.array([0.89, 0.10, 0.11]), t)
    s2_color = lerp(np.array([1.0, 0.5, 0.05]), np.array([0.4, 0.4, 0.4]), t)

    ax_a.plot(x_anim, y1_anim, color=s1_color, linewidth=2,
             marker="o" if marker_size > 0.5 else None, markersize=marker_size)
    ax_a.plot(x_anim, y2_anim, color=s2_color, linewidth=1.5,
             marker="s" if marker_size > 0.5 else None, markersize=marker_size)

    # Legend fades out, direct labels fade in
    legend_alpha = lerp(1.0, 0.0, min(t * 2, 1.0))
    label_alpha = lerp(0.0, 1.0, max((t - 0.5) * 2, 0.0))

    if legend_alpha > 0.05:
        leg = ax_a.legend(["Series A", "Series B"], loc="upper left",
                         frameon=True, facecolor="white", edgecolor="black")
        leg.set_alpha(legend_alpha)
        for text in leg.get_texts():
            text.set_alpha(legend_alpha)
        leg.get_frame().set_alpha(legend_alpha)

    if label_alpha > 0.05:
        ax_a.annotate("Series A", xy=(12, 50), xytext=(8, 0),
                     textcoords="offset points", fontsize=12, color=s1_color,
                     va="center", fontfamily="serif", alpha=label_alpha)
        ax_a.annotate("Series B", xy=(12, 43), xytext=(8, 0),
                     textcoords="offset points", fontsize=12, color=s2_color,
                     va="center", fontfamily="serif", alpha=label_alpha)

    ax_a.set_xticks(x_anim)
    ax_a.set_xticklabels(mlabels, fontsize=9)
    ax_a.set_ylabel("Value", fontsize=12, color="#666666")
    ax_a.tick_params(direction="in" if t > 0.5 else "out",
                    length=lerp(5, 3, t), width=lerp(1, 0.5, t))

    # Title transitions
    title_font = "sans-serif" if t < 0.5 else "serif"
    title_weight = "bold" if t < 0.5 else "normal"
    fig_a.text(0.12, 0.95,
              "Default Chart Style" if t < 0.3 else
              ("" if t < 0.7 else "Series A Outpaced B by 16% in 2025"),
              fontsize=18 if t > 0.7 else 16, fontfamily=title_font,
              fontweight=title_weight, color="#111111")

    plt.tight_layout()
    plt.subplots_adjust(top=0.88)
    return fig_a

# Generate frames: hold before (1s), transition (2s), hold after (2s) at 15fps
frames_before = 15   # 1s hold
frames_trans = 30    # 2s transition
frames_after = 30    # 2s hold
total_frames = frames_before + frames_trans + frames_after

import io
from PIL import Image

pil_frames = []
for i in range(total_frames):
    if i < frames_before:
        t = 0.0
    elif i < frames_before + frames_trans:
        t = (i - frames_before) / frames_trans
    else:
        t = 1.0

    fig_f = make_frame(t)
    buf = io.BytesIO()
    fig_f.savefig(buf, format="png", dpi=100, bbox_inches="tight")
    plt.close(fig_f)
    buf.seek(0)
    pil_frames.append(Image.open(buf).copy())

# Save as GIF
pil_frames[0].save(
    "/Users/ranman/dev/caylent/tufte-data-viz/_docs/before-after-animated.gif",
    save_all=True,
    append_images=pil_frames[1:],
    duration=int(1000 / 15),  # ~67ms per frame = 15fps
    loop=0,
)


print("Generated all showcase images.")
