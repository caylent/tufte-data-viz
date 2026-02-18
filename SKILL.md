---
name: tufte-data-viz
description: >-
  Edward Tufte's data visualization principles for generating clean, honest,
  high-data-ink-ratio charts and plots. Activate when writing or reviewing code
  that creates charts, plots, graphs, data visualizations, sparklines,
  dashboards, histograms, scatter plots, bar charts, line charts, heatmaps,
  small multiples, slopegraphs, or any visual representation of data. Covers
  Recharts, ECharts, Chart.js, matplotlib, Plotly, seaborn, D3.js, SVG, and
  HTML/CSS charts.
---

# Tufte Data Visualization

Apply Edward Tufte's principles whenever generating or reviewing code that renders data visually. This skill covers chart generation, not slide/presentation design.

## When this skill applies

Activate for ANY task that involves:
- Creating a new chart, plot, graph, or data visualization
- Modifying existing visualization code
- Reviewing chart code for quality
- Generating dashboards or data tables
- Creating sparklines or small multiples

## The Tufte test

Before generating any chart, answer these three questions:

1. **"What is the data saying?"** — Identify the key finding or trend. The chart's purpose is to make this finding visible, not to look pretty.
2. **"Compared to what?"** — Every visualization needs comparison context: a baseline, a prior period, a target, or another group. A number without context is meaningless.
3. **"Can I remove this element without losing information?"** — Apply to every gridline, border, legend, background color, and decorative element. If removing it loses nothing, remove it.

---

## Universal rules

These 14 rules apply to EVERY chart regardless of library. They are not suggestions — they are defaults. Only deviate when the user explicitly requests otherwise.

### 1. Remove top and right borders

No chart should have top or right axis lines, borders, or spines. Ever. The bottom and left axes are sufficient for reading values. Top and right lines are pure chartjunk.

### 2. Direct labels, not legends

Label each data series directly — at the endpoint of a line, on or beside a bar, next to a cluster. Remove the `<Legend>` component entirely. If there is only one series, the chart title provides that context; no label is needed.

### 3. No gridlines by default

The default is zero gridlines. If the user needs to read precise values, add horizontal-only gridlines at very low opacity (0.08–0.12). Never add vertical gridlines.

### 4. Range-frame axes

Axis lines should span only the range of the data, not from zero to some arbitrary maximum. The axis starts at (or near) the minimum data value and ends at the maximum. This is the "range frame" — the axis IS a data element showing extent.

### 5. No 3D effects

No perspective, no depth, no shadows on chart elements, no 3D bar charts, no 3D pie charts. Two-dimensional data gets two-dimensional representation.

### 6. No pie charts unless explicitly requested

Default to a horizontal bar chart sorted by value. Pie charts make magnitude comparison difficult. If the user explicitly asks for a pie chart: maximum 4 slices, 2D only, start at 12 o'clock, direct percentage labels on each slice, no "exploded" slices.

### 7. Aspect ratio ~1.5:1

Charts should be approximately 50% wider than tall. Standard sizes: 600x400, 750x500, 900x600. Exception: sparklines and small multiples may be more compact.

### 8. Gray first, highlight selectively

The default data series color is medium gray (`#666` or `#76767680`). Use a single accent color to highlight the most important series or data point. If the user needs categorical colors, use the muted 4-color palette (see Color section below). Never use more than 4 distinct colors.

### 9. Off-white background

Light mode: `#fffff8`. Dark mode: `#151515`. Never use pure white (`#ffffff`) or pure black (`#000000`). The slight warmth/softness reduces eye strain and is the Tufte standard.

### 10. Serif fonts for data

Use serif fonts for data labels, annotations, and chart titles: `"ET Book", "Palatino Linotype", Palatino, "Book Antiqua", Georgia, serif`. Sans-serif fonts (system-ui, sans-serif) are acceptable only for small axis tick labels (11-12px).

### 11. No dual y-axes

Two y-axes on one chart create false implied correlations and confuse readers. Instead, use small multiples — two charts stacked vertically with shared x-axis and independent y-axes.

### 12. Annotate the notable

If the data contains a peak, trough, inflection point, anomaly, or event boundary, add a text annotation pointing to it directly on the chart. Annotations are not optional decoration — they are the analyst's voice guiding the reader.

### 13. Show comparison context

Include at least one reference element: a reference line (average, target, prior period), a shaded band (confidence interval, normal range), or a second series for comparison. A chart showing one line with no context fails the "Compared to what?" test.

### 14. Minimal tooltips

If the chart is interactive, tooltips should be plain text with the data value and label. No colored background, no border, no arrow pointer, no shadow. The tooltip is an information layer, not a design element.

---

## Library quick reference

Load the appropriate rule file for detailed configuration. The table below shows the 3 most critical overrides per library.

| Library | Rule file | Critical overrides |
|---------|-----------|-------------------|
| Recharts | [rules/recharts.md](rules/recharts.md) | `<CartesianGrid stroke="none" />`, remove `<Legend />`, `axisLine={false}` on YAxis |
| ECharts | [rules/echarts.md](rules/echarts.md) | `splitLine: { show: false }`, remove grid borders, `label: { show: true }` on series |
| Chart.js | [rules/chartjs.md](rules/chartjs.md) | `grid: { display: false }`, `border: { display: false }`, use `chartjs-plugin-datalabels` |
| matplotlib | [rules/matplotlib.md](rules/matplotlib.md) | `spines['top'].set_visible(False)`, `spines['right'].set_visible(False)`, `set_bounds()` |
| Plotly | [rules/plotly.md](rules/plotly.md) | `showgrid=False`, `showlegend=False`, `plot_bgcolor='#fffff8'` |
| D3/SVG/HTML | [rules/svg-html.md](rules/svg-html.md) | `.domain { display: none }`, remove rect backgrounds, `stroke-opacity: 0.1` for grids |

---

## Chart type guidance

### Line chart
- `strokeWidth`: 1.5–2px. No thicker.
- `dot={false}` unless fewer than 7 data points, then small dots (r=2).
- Direct label at the rightmost point of each line (series name + current value).
- Thin, light lines. The data speaks through slope and direction, not thickness.

### Bar chart
- Prefer **horizontal** bars for categorical data — labels read naturally left-to-right.
- Sort bars by value (largest to smallest), not alphabetically.
- Direct value labels on or beside each bar via `<LabelList>` or equivalent.
- Bar color: `#7a7a7a` default. Highlight one bar with accent color if there is a key finding.
- Spacing between bars should be at least 30% of bar width.

### Scatter plot
- Gray dots (`#999`, r=3) as default. Highlight key cluster or outlier with accent color.
- Add regression/trend line if meaningful. Style it dashed, thin, and in the accent color.
- Consider rug marks (dot-dash marks) along axes to show marginal distributions.

### Time series
- Always label key events directly on the chart ("Recession", "Product launch", "Policy change").
- Use range-frame x-axis spanning the date range of the data.
- If showing year-over-year comparison, use opacity (current year solid, prior year 30% opacity).

### Small multiples
- Same scale across ALL panels. Never let each panel auto-scale independently.
- Shared axis labels — label the x-axis only on the bottom row, y-axis only on the leftmost column.
- Minimal panel borders (none preferred; light gray if needed).
- See [rules/small-multiples-sparklines.md](rules/small-multiples-sparklines.md) for layout patterns.

### Sparklines
- Word-sized: ~80x20px. No axes, no labels, no gridlines.
- Show min and max as small dots (r=1.5). Optionally mark the endpoint.
- Embed inline in text or table cells.
- See [rules/small-multiples-sparklines.md](rules/small-multiples-sparklines.md) for implementation.

### Data tables
- No zebra striping. Use whitespace and thin horizontal rules (every 3-5 rows).
- Right-align numbers. Left-align text. Decimal-align where possible.
- Use old-style (hanging) figures: `font-feature-settings: 'onum' 1`.
- No heavy borders. No cell backgrounds. The data IS the design.

### Slopegraph
- For before/after comparison across categories.
- Label both endpoints with value and category name.
- Lines colored gray by default; highlight one or two key slopes.

---

## Color and typography quick reference

```
LIGHT MODE
  Background:     #fffff8
  Text primary:   #111111
  Text secondary:  #666666
  Text tertiary:  #999999
  Axis/rule:      #cccccc
  Grid (if used): #eeeeee  (or 8-12% opacity of #000)
  Default series: #666666
  Highlight:      #e41a1c

DARK MODE
  Background:     #151515
  Text primary:   #dddddd
  Text secondary:  #999999
  Text tertiary:  #666666
  Axis/rule:      #444444
  Grid (if used): #333333
  Default series: #999999
  Highlight:      #fc8d62

CATEGORICAL (max 4)
  #4e79a7  Steel blue
  #f28e2b  Tangerine
  #e15759  Coral
  #76b7b2  Sage

FONTS
  Data/titles:  "ET Book", "Palatino Linotype", Palatino, "Book Antiqua", Georgia, serif
  Axis ticks:   system-ui, -apple-system, sans-serif
  Code/mono:    "Consolas", "Monaco", monospace
```

For full palette details, font loading, and old-style figures, see [rules/typography-and-color.md](rules/typography-and-color.md).

---

## Anti-pattern detection

When reviewing existing chart code, look for these patterns and fix them:

| If you see... | Replace with... |
|---------------|-----------------|
| `<Legend />` or legend component | Direct labels on each series |
| `type="pie"` or `Pie` component | Horizontal bar chart sorted by value |
| 3D, perspective, depth, shadow on data | Flat 2D representation |
| Two y-axes / dual axis | Small multiples (two charts, shared x-axis) |
| `gridLines` with opacity > 0.15 | `opacity: 0.1` or remove entirely |
| Rainbow / spectral color palette | Gray default + single highlight color |
| Gauge / speedometer widget | Single number with sparkline and context |
| Zebra-striped table rows | Whitespace + thin rules every 3-5 rows |
| Gradient fills on bars/areas | Solid flat color |
| Rotated axis labels (45/90 degrees) | Horizontal bar chart or abbreviated labels |
| `background: #ffffff` or `#fff` | `#fffff8` (light) or `#151515` (dark) |
| Thick borders / box around chart | Remove entirely |

For comprehensive detection heuristics with per-library code patterns, see [rules/anti-patterns.md](rules/anti-patterns.md).

---

## Reference files

Load these for detailed configuration when working with a specific library:

- [rules/recharts.md](rules/recharts.md) — Recharts component props, custom Tooltip, direct label pattern, complete JSX examples
- [rules/echarts.md](rules/echarts.md) — ECharts option object, theme registration, series labeling
- [rules/chartjs.md](rules/chartjs.md) — Chart.js defaults, Tufte plugin, datalabels integration
- [rules/matplotlib.md](rules/matplotlib.md) — rcParams, spine management, helper functions, seaborn integration
- [rules/plotly.md](rules/plotly.md) — Plotly template, layout defaults, annotation patterns
- [rules/svg-html.md](rules/svg-html.md) — Raw SVG, D3 axis config, HTML table CSS
- [rules/typography-and-color.md](rules/typography-and-color.md) — Font stacks, palettes, loading, old-style figures
- [rules/anti-patterns.md](rules/anti-patterns.md) — Violation detection with per-library code fixes
- [rules/small-multiples-sparklines.md](rules/small-multiples-sparklines.md) — Layout patterns for small multiples, sparkline implementations, slopegraphs
