# tufte-data-viz

An agent skill that applies [Edward Tufte's](https://www.edwardtufte.com/) data visualization principles when generating charts, plots, and graphs. Produces clean, honest, high-data-ink-ratio visualizations across multiple charting libraries.

## Install

```bash
npx skills add caylent/tufte-data-viz
```

## Before & After

The same data, default styling vs. Tufte principles applied:

![Before and after comparison — default chart style vs. Tufte style](https://raw.githubusercontent.com/caylent/tufte-data-viz/main/_docs/before-after.png)

## Examples

### Line chart — direct labels, range-frame axes, annotation

![Tufte-styled line chart showing revenue vs. target with direct labels and peak annotation](https://raw.githubusercontent.com/caylent/tufte-data-viz/main/_docs/tufte-line-chart.png)

### Horizontal bar chart — sorted by value, highlighted leader

![Tufte-styled horizontal bar chart with direct value labels and highlighted top product](https://raw.githubusercontent.com/caylent/tufte-data-viz/main/_docs/tufte-bar-chart.png)

### Small multiples — shared scale, minimal chrome

![Small multiples showing revenue trend by region with shared y-axis](https://raw.githubusercontent.com/caylent/tufte-data-viz/main/_docs/small-multiples.png)

## What it does

When active, this skill ensures every chart follows Tufte's core principles:

- **Maximize data-ink ratio** — remove gridlines, borders, legends, and decoration that don't convey data
- **Direct labeling** — label series on the chart itself, not in a separate legend
- **Range-frame axes** — axis lines span only the data range, not arbitrary bounds
- **Honest representation** — no 3D effects, no pie charts (unless forced), no dual y-axes
- **Typography** — serif fonts for data, off-white backgrounds, gray as primary color
- **Annotation** — notable features are called out directly on the chart

## Supported libraries

| Library | Rule file | Language |
|---------|-----------|----------|
| [Recharts](https://recharts.org/) | `rules/recharts.md` | React/JSX |
| [ECharts](https://echarts.apache.org/) | `rules/echarts.md` | JavaScript |
| [Chart.js](https://www.chartjs.org/) | `rules/chartjs.md` | JavaScript |
| [matplotlib](https://matplotlib.org/) | `rules/matplotlib.md` | Python |
| [Plotly](https://plotly.com/) | `rules/plotly.md` | Python/JS |
| D3.js / SVG / HTML | `rules/svg-html.md` | Web |

## Additional references

- `rules/typography-and-color.md` — font stacks, palettes, hex values
- `rules/anti-patterns.md` — common violations and one-liner fixes
- `rules/small-multiples-sparklines.md` — advanced Tufte techniques

## Based on

- *The Visual Display of Quantitative Information* (1983)
- *Envisioning Information* (1990)
- *Visual Explanations* (1997)
- *Beautiful Evidence* (2006)

## License

MIT
