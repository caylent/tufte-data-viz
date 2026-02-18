# tufte-data-viz

An agent skill that applies [Edward Tufte's](https://www.edwardtufte.com/) data visualization principles when generating charts, plots, and graphs. Produces clean, honest, high-data-ink-ratio visualizations across multiple charting libraries.

## Install

```bash
npx skills add caylent/tufte-data-viz
```

## What it does

When active, this skill ensures every chart Claude generates follows Tufte's core principles:

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
