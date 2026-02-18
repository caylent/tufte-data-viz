---
name: tufte-data-viz
version: "1.0.0"
description: >-
  This skill should be used when the user asks to "create a chart", "build
  a graph", "make a visualization", "plot this data", "create a dashboard",
  "add a sparkline", "review my chart", "style this chart", or when generating
  or modifying code that uses Recharts, ECharts, Chart.js, matplotlib, Plotly,
  seaborn, D3.js, or SVG to render data visually. Applies Edward Tufte's
  principles for clean, honest, high-data-ink-ratio charts and plots.
---

# Tufte Data Visualization

Apply Edward Tufte's principles whenever generating or reviewing code that renders data visually. This skill covers chart generation, not slide/presentation design.

## Workflow

Follow these steps in order when creating any chart:

### Step 1: Identify the message

Before writing code, determine:
1. The key finding or trend the chart must make visible.
2. The comparison context — a baseline, prior period, target, or peer group. A number without context is meaningless.
3. The chart type that best fits the data structure (see Chart type guidance below).

### Step 2: Apply universal rules

Review the 14 rules below. Every rule is a default — deviate only when the user explicitly requests otherwise.

### Step 3: Apply library-specific config

Use the Library quick reference table to find the essential overrides for the target library. For complete code examples and helper functions, read ONE rule file from `rules/` matching the library.

### Step 4: Validate

Run through the validation checklist at the bottom of this file before presenting the chart.

---

## Universal rules

These 14 rules apply to EVERY chart regardless of library.

### 1. Remove top and right borders

No chart should have top or right axis lines, borders, or spines. The bottom and left axes are sufficient. Top and right lines are pure chartjunk.

### 2. Direct labels, not legends

Label each data series directly — at the endpoint of a line, on or beside a bar, next to a cluster. Remove the `<Legend>` component entirely. If there is only one series, the chart title provides that context; no label is needed.

### 3. No gridlines by default

The default is zero gridlines. If the user needs to read precise values, add horizontal-only gridlines at very low opacity (0.08–0.12). Never add vertical gridlines.

### 4. Range-frame axes

Axis lines should span only the range of the data, not from zero to some arbitrary maximum. The axis starts at (or near) the minimum data value and ends at the maximum.

### 5. No 3D effects

No perspective, no depth, no shadows on chart elements. Two-dimensional data gets two-dimensional representation.

### 6. No pie charts unless explicitly requested

Default to a horizontal bar chart sorted by value. If the user explicitly asks for a pie chart: maximum 4 slices, 2D only, start at 12 o'clock, direct percentage labels on each slice.

### 7. Aspect ratio ~1.5:1

Charts should be approximately 50% wider than tall. Standard sizes: 600x400, 750x500, 900x600. Exception: sparklines and small multiples may be more compact.

### 8. Gray first, highlight selectively

The default data series color is medium gray (`#666`). Use a single accent color to highlight the most important series or data point. Never use more than 4 distinct colors.

### 9. Off-white background

Light mode: `#fffff8`. Dark mode: `#151515`. Never use pure white (`#ffffff`) or pure black (`#000000`).

### 10. Serif fonts for data

Use serif fonts for data labels, annotations, and chart titles: `"ET Book", "Palatino Linotype", Palatino, "Book Antiqua", Georgia, serif`. Sans-serif (system-ui, sans-serif) is acceptable only for small axis tick labels (11-12px).

### 11. No dual y-axes

Two y-axes on one chart create false implied correlations. Use small multiples instead — two charts stacked vertically with shared x-axis.

### 12. Annotate the notable

If the data contains a peak, trough, inflection point, or event boundary, add a text annotation pointing to it directly on the chart.

### 13. Show comparison context

Include at least one reference element: a reference line (average, target, prior period), a shaded band, or a second series. A chart showing one line with no context fails the "Compared to what?" test.

### 14. Minimal tooltips

Tooltips should be plain text with the data value and label. No colored background, no border, no arrow pointer, no shadow.

---

## Library quick reference

The universal rules above are sufficient for most charts. For complete code examples and library-specific helpers, read the appropriate rule file from the `rules/` directory in this skill's folder. Only read ONE rule file per task.

| Library | Rule file to read | Essential config (apply even without reading the file) |
|---------|-------------------|--------------------------------------------------------|
| Recharts | `rules/recharts.md` | `<CartesianGrid stroke="none" />`, remove `<Legend />`, `<YAxis axisLine={false} tickLine={false} />`, `<Line dot={false} strokeWidth={1.5} />` |
| ECharts | `rules/echarts.md` | `splitLine: { show: false }`, `legend: { show: false }`, `grid: { show: false }`, use `endLabel` on series |
| Chart.js | `rules/chartjs.md` | `grid: { display: false }`, `border: { display: false }`, `plugins.legend.display: false`, use `chartjs-plugin-datalabels` |
| matplotlib | `rules/matplotlib.md` | `spines['top'].set_visible(False)`, `spines['right'].set_visible(False)`, `spines['bottom'].set_bounds(min, max)`, `font.family: serif` |
| Plotly | `rules/plotly.md` | `showgrid=False`, `showlegend=False`, `plot_bgcolor='#fffff8'`, `zeroline=False` |
| D3/SVG/HTML | `rules/svg-html.md` | `.domain { display: none }`, no `<rect>` backgrounds, `stroke-opacity: 0.1` for any gridlines |

---

## Chart type guidance

### Line chart
- `strokeWidth`: 1.5–2px. No thicker.
- `dot={false}` unless fewer than 7 data points, then small dots (r=2).
- Direct label at the rightmost point of each line (series name + current value).

### Bar chart
- Prefer **horizontal** bars for categorical data — labels read naturally left-to-right.
- Sort bars by value (largest to smallest), not alphabetically.
- Direct value labels on or beside each bar.
- Bar color: `#7a7a7a` default. Highlight one bar with accent color for the key finding.

### Scatter plot
- Gray dots (`#999`, r=3) as default. Highlight key cluster or outlier with accent color.
- Add regression/trend line if meaningful (dashed, thin, accent color).
- Consider rug marks along axes to show marginal distributions.

### Time series
- Label key events directly on the chart ("Recession", "Product launch", "Policy change").
- Use range-frame x-axis spanning the date range of the data.
- For year-over-year comparison, use opacity (current year solid, prior year 30% opacity).

### Small multiples
- Same scale across ALL panels. Never let panels auto-scale independently.
- Shared axis labels — x-axis on bottom row only, y-axis on leftmost column only.
- No panel borders preferred; light gray if needed.

### Sparklines
- Word-sized: ~80x20px. No axes, no labels, no gridlines.
- Mark min and max as small dots (r=1.5). Optionally mark the endpoint.
- Embed inline in text or table cells.

### Data tables
- No zebra striping. Use whitespace and thin horizontal rules every 3-5 rows.
- Right-align numbers. Left-align text. Decimal-align where possible.
- Use old-style figures: `font-feature-settings: 'onum' 1`.

### Slopegraph
- For before/after comparison across categories.
- Label both endpoints with value and category name.
- Lines gray by default; highlight one or two key slopes.

For small multiples, sparklines, and slopegraph implementation patterns, see `rules/small-multiples-sparklines.md`.

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

For full palette details, font loading, and old-style figures, see `rules/typography-and-color.md`.

---

## Anti-pattern detection

When reviewing existing chart code, find and fix these:

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

For per-library detection patterns and one-liner code fixes, see `rules/anti-patterns.md`.

---

## Validation checklist

Before presenting any chart, verify:

- [ ] No top or right borders/spines
- [ ] No Legend component — series labeled directly on the chart
- [ ] Gridlines removed or horizontal-only at opacity <= 0.12
- [ ] Aspect ratio approximately 1.5:1
- [ ] Background is `#fffff8` (light) or `#151515` (dark), not pure white/black
- [ ] Serif font for data labels and titles
- [ ] Default series color is gray (`#666`); color used only for emphasis
- [ ] No 3D effects, no pie chart (unless explicitly requested)
- [ ] Axis lines span only the data range (range-frame)
- [ ] Notable data features annotated directly on chart
- [ ] Comparison context present (reference line, band, or second series)
- [ ] Tooltips are plain text with no decorative styling

---

## Additional resources

### Library-specific rules (read ONE matching the target library)

Complete code examples, helper functions, and theme registrations in `rules/`:

- **`rules/recharts.md`** — Custom Tooltip, direct label component, range-frame tick, full JSX examples
- **`rules/echarts.md`** — Theme registration, base option object, endLabel config, markPoint/markLine
- **`rules/chartjs.md`** — Global defaults, Tufte plugin, datalabels integration, annotation plugin
- **`rules/matplotlib.md`** — Full rcParams dict, `tufte_axes()` helper, sparkline function, seaborn integration
- **`rules/plotly.md`** — Reusable `pio.templates['tufte']`, annotation helpers, Plotly.js equivalent
- **`rules/svg-html.md`** — SVG chart CSS, D3 axis config, inline sparkline generator, HTML table CSS

### Cross-cutting references (read only when specifically needed)

- **`rules/typography-and-color.md`** — Font loading (ET Book CSS), full palette tables, old-style figures
- **`rules/anti-patterns.md`** — Per-library detection heuristics and one-liner fixes
- **`rules/small-multiples-sparklines.md`** — Layout patterns for small multiples, sparkline implementations, slopegraphs

### Working code examples

Complete implementations in `examples/`:

- **`examples/recharts-tufte-line.tsx`** — Recharts line chart with all principles applied
- **`examples/recharts-tufte-bar.tsx`** — Recharts horizontal bar chart
- **`examples/matplotlib-tufte-annotated.py`** — matplotlib annotated time series
- **`examples/plotly-tufte-template.py`** — Plotly template with Tufte styling
- **`examples/echarts-tufte-theme.ts`** — ECharts theme registration
- **`examples/chartjs-tufte-plugin.js`** — Chart.js Tufte plugin and defaults
- **`examples/sparkline-inline.svg`** — Minimal SVG sparkline
