# Maps

Load this file for any display drawn on geographic space: shaded-area maps (choropleth, "blot" or "patch" maps), dot maps, proportional-symbol maps, flow maps, contour and surface maps, map small multiples, and the base map under any of them.

Maps run through all four of Tufte's books. *The Visual Display of Quantitative Information* (VDQI) opens its history of data graphics with data maps and closes it with Minard's map of Napoleon's campaign. *Envisioning Information* (EI) draws most of its principles from maps: the Tokyo mesh maps, Nolli's Rome, the Swiss topographic sheets, the GEBCO ocean chart. *Visual Explanations* (VE), ch. 2, is a statistical critique of John Snow's cholera map. *Beautiful Evidence* (BE), ch. 5, derives the fundamental principles of analytical design from Minard. Every rule below is Tufte's and names its source. Where Tufte gives no rule, this file says so instead of supplying one.

**What carries over from SKILL.md:** direct labels (rule 2), muted color with strong color only in small areas (rule 8; Tufte took that rule from his writing on maps), comparison context (rule 13), and small multiples (`rules/small-multiples-sparklines.md`). Tufte's graphical integrity principles (VDQI ch. 2), data-ink and chartjunk (VDQI ch. 4–5), the analytical-design principles (BE ch. 5) and the smallest effective difference (VE ch. 4) apply to maps as to any graphic; the rules below cite them where they bear on maps.

**What does not apply:** the rules about axes, baselines, range frames and aspect ratio. A map's frame is set by its projection and extent, not by a data scale.

## Rules

### 1. The map is for an inference; design for that inference

*Source: Tufte, VDQI ch. 1 ("Data Maps"); BE ch. 5 (sixth principle, p. 136); Tufte, edwardtufte.com, "Data Maps" (8 Aug 2001).*

Tufte's data maps carry a great deal of data: each of the redrawn cancer maps in VDQI "portrays some 21,000 numbers" and can be read "at many different levels of analysis," from national pattern to a single county (VDQI p. 16). BE's first question for any analytical display is what content-reasoning task it is supposed to help with. In the 2001 note Tufte says what blot maps are good for: revealing hot spots, suggesting a relationship between a variable and location, and letting readers compare their own area with others. He also says that next to the problems of statistical inference, "the coloring issues are trivial," and warns about ecological correlation: the data are aggregated by county but the inference is usually about individuals, and correlations at the two levels can have opposite signs.

- Decide what the reader is to infer from the map before deciding how it looks.
- Keep the level of the data (areas) and the level of the inference (people) distinct, and say which one the map supports.

### 2. Do not let land area stand for importance

*Source: Tufte, VDQI ch. 1, p. 20; EI ch. 2, pp. 40–41; edwardtufte.com, "Data Maps" (2001).*

Tufte's standing objection to shaded-area maps: they "wrongly equate the visual importance of each county with its geographic area," which he calls "the chronic problem afflicting shaded-in-area designs" (VDQI p. 20). In EI he adds that color is weighted toward empty land and that boundary changes break comparisons over time (p. 41). The remedies he names:

- **Equal-area cells.** The Tokyo mesh maps shade small grid squares of equal size, so each unit has the same visual weight and residents can find their own square (EI pp. 40–41). In 2001 he offers mesh maps as a partial fix for blot maps.
- **Individual marks.** Snow's dot map marks each death, keeping cases visible and avoiding the distortions of aggregation (VE p. 35; see rule 3).

Tufte proposes no other correction (no cartograms, no area-scaled symbols); see "Where Tufte gives no rule."

### 3. Show a rate map and a dot map, not one or the other

*Source: Tufte, VE ch. 2, p. 35.*

Tufte's critique of Snow: the dot map shows deaths but not the population at risk, so an area can look free of cases because few people live there, and "Snow's map does not fully answer the question *Compared with what?*" Conversely, dot maps keep individuals visible, avoid aggregation artefacts, and can be checked case by case. His conclusion is that the cholera data should be displayed on both a dot map and a rate map, with rates computed over small, homogeneous areas.

- For counts of events, show the events (dots) and the rate (events per population or per area at risk).
- Compute rates over units small and uniform enough that the rate means something.

### 4. Test the effect of aggregation, in space and in time

*Source: Tufte, VE ch. 2, pp. 35–36; EI ch. 2, p. 41.*

Tufte reproduces Monmonier's three re-aggregations of Snow's data: in two of them the cluster around the Broad Street pump disappears. For time, weekly totals make the removal of the pump handle look decisive, daily data show no such effect, and shifting the weekly intervals by two days changes the picture again. His rule: "If in doubt, graph the detailed underlying data to assess the effects of aggregation." He also warns that a chartmaker can search many aggregations and show only the ones that favor an argument.

- Before fixing the areal unit or the time bin, draw the data at finer resolution and check that the pattern survives.
- State the unit and the bin on the map; do not change boundaries between maps that are meant to be compared (EI p. 41).

### 5. Show the whole context: where the phenomenon is absent as well

*Source: Tufte, VE ch. 2, pp. 31, 35; VDQI ch. 2 (sixth principle of graphical integrity).*

The credibility of Snow's map comes from contrary cases on the same sheet: the brewery and the workhouse near the pump, with their own water, had few or no deaths (p. 31). Tufte's modern critique is that Snow nonetheless "ignored some areas with cholera and *all* the cholera-free areas and their water pumps" (p. 35). VDQI's sixth principle, that graphics must not quote data out of context, applies to the map's extent and to what is plotted within it.

- Plot the zeros and the exceptions, not only the cases.
- Choose the map's extent to include the comparison, not to crop to the cluster.

### 6. Put the suspected cause on the map with the effect

*Source: Tufte, VE ch. 2, pp. 29–31; BE ch. 5 (second principle).*

Snow placed the data "in an appropriate context for assessing cause and effect": deaths and the pumps on one map. Tufte notes that descriptive narration is not causal explanation and that time alone is a poor explanatory variable when the aim is to intervene (p. 29). Minard draws temperature beneath the retreat so that the fall in temperature can be read against the fall in army size (BE ch. 5).

- When the map is meant to explain, the candidate cause (pumps, roads, plants, elevation) is a data layer, not base-map decoration.

### 7. Carry more variables than two

*Source: Tufte, BE ch. 5, p. 129; EI ch. 5, p. 94; VDQI ch. 1, pp. 23, 40–41.*

Minard's map plots six variables: the size of the army, its position in two dimensions, its direction of movement, temperature, and date (VDQI pp. 40–41; BE p. 129). Every mark on the GEBCO ocean chart encodes four: latitude, longitude, sea or land, and depth or altitude (EI p. 94). Halley's 1686 wind map encodes direction in the shape of each stroke (VDQI p. 23). A map already spends two dimensions on position; Tufte's examples spend the remaining channels (width, value, direction, shape, annotation) on data.

### 8. Color: label, measure, imitate, enliven; above all, do no harm

*Source: Tufte, EI ch. 5, p. 81.*

Tufte's four uses of color on a map: to label (color as noun, water from stone), to measure (color as quantity, altitude), to represent or imitate reality (river blue, shadow), and to enliven or decorate. His first principle for bringing color to information is "Above all, do no harm."

- For each color on the map, name which of the four jobs it does. A color doing none of them is colorjunk.

### 9. Encode quantity by value (light to dark), not by a hue sequence

*Source: Tufte, EI ch. 5, pp. 91–92 and n. 9; VDQI ch. 1, pp. 16–20; edwardtufte.com, "Data Maps" (2001).*

The GEBCO chart's rule is "the deeper or higher, the darker" (EI p. 91). Tufte rejects the spectrum as an order for quantity: a rainbow scale replaces the clear light-to-dark sequence with a disorderly one, and "the mind's eye does not readily give an order to ROYGBIV" (p. 92), so viewers fall back on contours and labels. Controlled hue variation may extend a value scale while keeping a natural sequence (n. 9). Tufte's own redrawing of the cancer maps is in gray scale (VDQI pp. 16–20; 2001 note).

- Sequential data: a single-hue or gray value ramp, dark for more.
- Never a spectral ramp for quantity.

### 10. Do not let color be the only signal: outline the fields and label them

*Source: Tufte, EI ch. 5, pp. 91–94 and nn. 12–13.*

Value scales are easy to learn but open to misreading from edge fluting and simultaneous contrast, and the translation from color to number is nonlinear, noisy and differs between viewers (pp. 92–93). The GEBCO chart's answer: numbered contours outline each color field, which removes edge fluting, makes the fields coherent and allows finer value distinctions (p. 94). Several percent of viewers are color-deficient, so no crucial distinction may rest on red against green (n. 12). Cutpoints and the frequency distribution of the data also shape what the map says (n. 13). Redundant signals are justified by a real ambiguity, not by a wish for more; gratuitous multiplicity is clutter (pp. 93–94).

- Give each class a labeled boundary or a printed value, not only a fill.
- No red/green pairs for a distinction the reader must make.

### 11. Muted fields, strong color in small areas: Imhof's rules

*Source: Tufte, EI ch. 5, pp. 82, 90, 94; EI ch. 3, p. 63.*

Tufte quotes Eduard Imhof's rules for the Swiss topographic maps and builds his own color advice on them (EI pp. 82, 90):

1. Pure, strong colors are unbearable over large adjacent areas; used sparingly on or between dull tones they have extraordinary effect. The extremes of a scale (highest land, deepest trench) enclose small areas, which suits bold color.
2. Light, bright colors mixed with white, placed next to each other over large areas, look unpleasant.
3. Large background areas should be muted or grayish so that small bright areas stand out.
4. Two or more large enclosed areas in different colors make a picture fall apart; unity comes from scattering one area's colors through the other.

Tufte adds that nature's lighter colors (the blues, yellows and grays of sky and shadow) are familiar and authoritative and suppress colorjunk (p. 90), that strong color over broad areas makes a map readable only at poster distance (p. 94), and that small spots of intense, saturated color carry information well, a technique of classical cartography (EI p. 63).

### 12. Layer the base map under the data, and separate the layers

*Source: Tufte, EI ch. 3, "Layering and Separation", pp. 58–62.*

A map in which contours, rivers, roads and names all share one weight, texture and color is unreadable; separating the layers by shape, value, size and color fixes it (p. 58). Heavy ink on the Tiber in Nolli's Rome makes the bridge names vibrate; muting the river brings the names forward (p. 60). In Nolli and in Turgot's Paris the streets carry no ink at all: they are read from the blocks around them (p. 61). Tufte's redesigns thin the block outlines, use gray edges for calm surfaces, and place type so that no awkward white gaps open between names and water (p. 62).

- The base map (coast, water, roads, administrative lines) is the quiet layer: thin, gray, low contrast.
- The data layer reads first. If the base map competes, mute it further rather than brightening the data.
- Let negative space do work: unfilled streets, unoutlined open water.

### 13. Graticule and grid: light gray, and only when the map is a look-up table

*Source: Tufte, EI ch. 3, p. 59; VDQI ch. 5.*

Grid lines on maps and graph paper should be light gray; a dark grid is chartjunk, and a grid is justified only when the graphic serves as a look-up table (EI p. 59).

- No graticule by default. When coordinates must be read off, a light gray one.

### 14. Boundaries say what lies on each side, with the least ink that does so

*Source: Tufte, EI ch. 5, pp. 94–95.*

A map boundary should clearly show what falls on each side of it (p. 95). Between two color fields only the presence of an edge is needed, so an edge line needs only a value close to the scale around it (p. 94). Color cross-hatching lost exactly this boundary detail (p. 94). Of the Parliament map Tufte says the result is "a clear statement about geography, rather than a statement about color" (p. 95).

- Thin, low-contrast boundaries between data regions; no heavy black outlines around every polygon.

### 15. To clarify, add detail

*Source: Tufte, EI ch. 2, "Micro/Macro Readings", pp. 37–41, 51.*

Anderson's map of midtown Manhattan carries individual windows and some 1,686 names and reads at street level and at a glance; the chapter's rule is "to clarify, add detail" (p. 37). The Tokyo mesh maps let a resident find their own square and see it in context, and show population clustered along rail lines (p. 40). "Clutter and confusion are failures of design, not attributes of information" (p. 51); reducing detail is a stylistic choice, not a route to clarity.

- Keep the fine-grained data on the map (every cell, every case) and design so that the overall pattern still reads.
- Do not simplify the data to make the map look clean; fix the layering (rule 12) instead.

### 16. Map small multiples: constant design, constant scale, one eyespan

*Source: Tufte, EI ch. 4, pp. 67, 74–76; EI ch. 1, pp. 28–29; VDQI ch. 1, pp. 16–20; VE ch. 6.*

Small multiples let the eye compare; a constant design keeps attention on changes in the data rather than in the frames (EI p. 67). The twelve Los Angeles smog maps, one per hour, index the same map on time and add up the day's pollution (EI pp. 28–29). The four maps of China's poets by dynasty show birthplaces shifting south-east, a pattern visible only across the series (pp. 74–75). A map of Matsu temples on a separate page cannot be compared with them; comparisons must fall within one eyespan (p. 76). The six cancer maps in VDQI are a small multiple by cancer type and sex.

- Same projection, extent, scale and class breaks on every panel; one legend for all.
- Panels on one page or screen, never one per page.

### 17. Change over space and time: map plus time-series

*Source: Tufte, EI ch. 6, p. 97; VDQI ch. 1, pp. 40–41; BE ch. 5.*

"Painting four-variable narrations of space-time onto flatland combines two familiar designs, the map and the time-series" (EI p. 97). Minard carries time along the route as the width of the flow and ties the dated temperature series to positions on the retreat (VDQI pp. 40–41; BE ch. 5). For a spreading phenomenon Tufte's two designs are the flow line that carries time along its path and the time-indexed small multiple (rule 16).

### 18. Document the map on the map

*Source: Tufte, BE ch. 5, pp. 126, 131, 133–134; BE ch. 1, p. 21; VE ch. 2, p. 34; VDQI ch. 1, pp. 16–20.*

Minard's sheet has a title naming the method and the subject, the author and his credential, a text block explaining the color code and the three scales, and five acknowledged sources (BE pp. 126, 133). Of Minard's Hannibal map Tufte says the north arrow "should appear on every map" (p. 134). Excellent maps, "the heart and soul of good practices in analytical graphics," routinely integrate words, numbers, line art, grids and measurement scales (p. 131). In BE ch. 1 the map is Tufte's model for all evidence images: labels belong on the image, external grids give it scale, and data are more credible in context (p. 21). Snow annotated his map and table with notes on possible errors and gaps in the data, and that annotation is part of the map's credibility (VE p. 34). Tufte's redrawn cancer maps separate "in highest decile, statistically significant" from rates not significantly different from the national figure, and his text flags that death-certificate data follow "diagnostic fashions" (VDQI pp. 16–20).

- On the map: title stating method and subject, author, data sources, measurement scale, north arrow, units, date of the data.
- Mark uncertainty and significance in the classes themselves; note known data problems next to the map.
- Labels on the map, beside the features; no letter codes keyed to a separate list.

### 19. Graphical integrity holds for symbols on maps

*Source: Tufte, VDQI ch. 2 (first and fifth principles); BE ch. 5, p. 127.*

Tufte applies the lie factor even to Minard: the widths of the two flows at the Niemen "were inaccurately constructed in a ratio of 1 to 28" (BE p. 127). A proportional symbol's measured size must be proportional to its value, and a one-dimensional quantity gets no extra dimensions (VDQI ch. 2).

- Flow widths and symbol areas scale linearly with the data.
- No extruded 3D "terrain" of a one-dimensional variable, no perspective tilt on a data map.

## Where Tufte gives no rule

Tufte writes no cartography manual. He gives no rule on map projection, on north-up orientation, on the form of a scale bar, on legend design or placement, on how many classes to use or how to set class breaks (he notes only that cutpoints and the data's distribution matter, EI ch. 5 n. 13), on cartograms, hexagonal binning, kernel density surfaces, basemap imagery, label-placement algorithms, or interactive zoom. This skill adds none. Use what the user asks for or the library's default, and apply the rules above to it. The screen-first rules 15–19 in SKILL.md are not Tufte's and are not repeated here.

## Library notes

Colors and fonts come from `rules/typography-and-color.md`. The specific values below (colormap names, line widths, opacities) are this skill's defaults, not Tufte's.

**geopandas + matplotlib (choropleth of a rate)**

```python
import geopandas as gpd
import matplotlib.pyplot as plt

counties = gpd.read_file("counties.gpkg")
states = gpd.read_file("states.gpkg")
counties["rate"] = counties["deaths"] / counties["population"] * 1e5   # rule 3: a rate, not a count

fig, ax = plt.subplots(figsize=(9, 6))
counties.plot(column="rate", cmap="Greys", scheme="quantiles", k=5,     # rule 9: value ramp, dark = more
              edgecolor="#bbbbbb", linewidth=0.3, ax=ax,                # rule 14: thin low-contrast edges
              legend=True, legend_kwds={"frameon": False, "title": "Deaths per 100,000"})
states.boundary.plot(ax=ax, color="#888888", linewidth=0.6)             # rule 12: muted base layer
ax.set_axis_off()                                                        # rule 13: no graticule by default
ax.set_title("…finding stated as a sentence…")                           # SKILL.md rule 20
ax.annotate("Source: …; units; year of data; author. North is up.",     # rule 18
            xy=(0, 0), xycoords="axes fraction", fontsize=8, color="#666666")
```

- `scheme`/`k` are left to the user; Tufte gives no classification rule.
- geopandas draws no north arrow; add one (rule 18) with an annotation or a small arrow patch.
- For a dot map alongside (rule 3), plot the point layer with `markersize` small and constant, not scaled.

**Plotly (choropleth)**

```python
import plotly.express as px

fig = px.choropleth(df, geojson=geo, locations="fips", color="rate",
                    color_continuous_scale="Greys",                   # rule 9
                    scope="usa", labels={"rate": "Deaths per 100,000"})
fig.update_traces(marker_line_width=0.3, marker_line_color="#bbbbbb")  # rule 14
fig.update_geos(showlakes=False, showcountries=False, showcoastlines=False,
                showframe=False, landcolor="#f4f4f0")                 # rule 12
fig.update_layout(title="…finding stated as a sentence…",
                  coloraxis_colorbar=dict(outlinewidth=0, thickness=10))
```

- Avoid `color_continuous_scale="Rainbow"`, `"Jet"`, `"Turbo"` and any spectral scale for quantity (rule 9).

**Small multiples of maps (either library)**

- One shared color scale and class breaks across all panels; one colorbar or legend for the whole figure (rule 16).
- Same extent and projection on every panel; one title per panel stating what changes.

## Validation checklist

- [ ] The inference the map supports is stated, and the level of data (areas) is not confused with the level of inference (people) (rule 1)
- [ ] Area does not stand for importance; counts have a rate map or equal-area cells beside them (rules 2–3)
- [ ] The pattern survives a change of areal unit and of time bin (rule 4)
- [ ] Zeros, exceptions and the comparison region are on the map (rule 5)
- [ ] Each color does one of: label, measure, imitate, enliven (rule 8)
- [ ] Quantity is encoded light-to-dark, never as a spectrum (rule 9)
- [ ] Classes are bounded or labeled, not carried by color alone; no red/green distinction (rule 10)
- [ ] Large areas muted; strong color only in small areas (rule 11)
- [ ] Base map thinner and grayer than the data layer; no graticule unless needed for look-up (rules 12–13)
- [ ] Boundaries thin and low-contrast (rule 14)
- [ ] Small multiples share projection, extent, scale and breaks, on one page (rule 16)
- [ ] Title, author, sources, scale, north arrow, units, date and data caveats are on the map (rule 18)
- [ ] Symbol sizes and flow widths proportional to the data; no 3D (rule 19)
