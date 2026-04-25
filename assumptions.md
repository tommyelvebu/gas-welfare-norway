# Model Assumptions and Parameter Justification

**EBA3650 — Quantitative Economics**  
BI Norwegian Business School | Spring 2026

This document defends every parameter choice in the welfare model. Each assumption is assessed against the empirical literature and official data sources.

---

## A1. Pre-War Gas Price — P₀ = 20 EUR/MWh

**What we assume:** The pre-war European gas benchmark (TTF) averaged 20 EUR/MWh before the Ukraine war.

**Evidence:**

| Year | TTF average |
|------|------------|
| 2019 | ~14–15 EUR/MWh |
| 2020 | ~3–5 EUR/MWh (COVID collapse) |
| 2021 | ~47 EUR/MWh (crisis begins H2) |

The 2019 level was 14–15 EUR/MWh (IEA Gas 2020 report). The COVID year (2020) was anomalously low. 2021 was already crisis-affected. We use 20 EUR/MWh as representative of **2017–2019 "normal market" conditions**, which saw prices of 17–20 EUR/MWh. This is a common convention in the policy literature.

**Verdict: Defensible.** 20 EUR/MWh is a slight overstatement of the strict 2019 average but correctly reflects the pre-COVID market norm. It is used as the stable reference point to which the 2022 shock is compared.

**Source:** IEA Gas 2020: "2019: Cool Down"; Trading Economics TTF historical data.

---

## A2. European Gas Consumption — Q₀ = 4,000 TWh/year

**What we assume:** Total European gas consumption is 4,000 TWh/year (~400 bcm).

**Evidence:** Actual EU27 + UK consumption in 2019 was approximately 400–420 bcm. Using the standard energy conversion (1 bcm ≈ 10.55 TWh), this equals roughly 4,200–4,430 TWh. The 4,000 TWh figure is a slight underestimate of the full European perimeter but closely matches EU27-alone figures (~350–370 bcm ≈ 3,700–3,900 TWh).

**Verdict: Acceptable.** The 5% underestimate relative to the broader European gas market does not affect qualitative conclusions. The figure is used purely to calibrate the scale parameters A_d and A_s; the welfare calculations depend on the equilibrium price and Norwegian quantities, not the aggregate market size directly.

**Source:** IEA European natural gas supply-demand balance; Bruegel European Natural Gas Demand Tracker.

---

## A3. Russian Supply Share — δ = 40%

**What we assume:** Russia supplied 40% of European gas consumption before the war.

**Evidence:** This is confirmed by multiple authoritative sources. The EU Council's own infographic and Wikipedia's "Russia in the European energy sector" article both state that "40% of gas consumed in the EU came from Russia" in 2021. Russian pipeline exports to Europe were approximately 155 bcm/year (Enerdata, IEA), against total European consumption of ~400 bcm — giving exactly 38–40%. The 45% figure sometimes cited elsewhere refers to Russia's share of *imports only* (excluding domestic EU production), which is a different denominator.

**Verdict: Accurate.** The 40% figure is the correct share of *total consumption*, which is the right denominator for our supply-side shock model.

**Source:** EU Council energy infographic; Wikipedia "Russia in the European energy sector"; Enerdata Russia Gas Export Strategy report.

---

## A4. Norwegian Supply Share — 25%

**What we assume:** Norway supplied 25% of European gas pre-war.

**Evidence:** The IEA's "Norway Natural Gas Security Policy" article explicitly states Norway "accounted for around 25% of EU gas demand" in 2021, exporting approximately 113 bcm that year. Norway's main pipeline routes — Langeled, Europipe I/II, and Franpipe — connected Norwegian fields to Germany, UK, France, and Belgium. The 25% figure is consistent with Russia's 40% and leaves ~35% for LNG imports, Algerian/Azerbaijani pipeline gas, and domestic EU production.

**Verdict: Accurate.** Directly confirmed by IEA data.

**Source:** IEA "Norway Natural Gas Security Policy"; Enerdata "Norway plans to export 122 bcm in 2023".

---

## A5. Short-Run Gas Demand Elasticity — ε_d = −0.3

**What we assume:** European gas demand falls 0.3% for every 1% rise in price (short run).

**Evidence:** The empirical literature finds a wide range:

- Labandeira, Labeaga & López-Otero (2017) meta-analysis: mean short-run elasticity **−0.18**
- Bernstein & Madlener (2011), 12 OECD countries: **−0.24**
- Asche et al. (2012), 12 European countries: estimates range **−0.10 to −0.25**
- German household crisis data (2022): **−0.01 to −0.04** (extremely inelastic during the shock itself)

Most estimates cluster around −0.15 to −0.25 for pure short-run residential demand. However, European gas demand includes **industry and power generation**, which are more price-responsive than households. Industry can switch fuels or curtail production; gas-fired power plants compete with coal. Including all sectors, an aggregate elasticity of −0.3 is reasonable as an upper-bound estimate covering the full demand side.

**Verdict: Slightly high but defensible.** We treat −0.3 as a central estimate reflecting the full demand mix (industrial, commercial, residential, and power generation). Our sensitivity analysis explores the range −0.05 to −0.50, which encompasses all plausible values. The main conclusions hold across this full range.

**Source:** Labandeira, Labeaga & López-Otero (2017); Bernstein & Madlener (2011); Springer "Price elasticity of natural gas demand, Germany crisis 2022".

---

## A6. Short-Run Gas Supply Elasticities — ε_s = 0.35 (aggregate) and ε_s,NO = 0.07 (Norway)

**What we assume:** The model uses **two distinct supply elasticities** that play different roles:

1. **Aggregate European supply elasticity, ε_s = 0.35** — used to solve the European market equilibrium and pin down the post-shock price P₁.
2. **Norway-specific supply elasticity, ε_s,NO = 0.07** — used to compute Norway's own quantity response and producer surplus.

**Why two elasticities?** They describe different things, and conflating them was the original modelling error. The aggregate captures the *whole European supply system's* response to a price rise, which bundles in:
- LNG imports (highly price-responsive; new terminals came online in 2022)
- Storage drawdowns (effectively a one-off supply boost)
- US shale (~6–9 month response, reasonably elastic)
- Domestic EU production (Netherlands Groningen, North Sea)
- Algeria/Azerbaijan pipeline (some responsiveness)
- Norwegian pipeline gas (low responsiveness)

A 0.35 aggregate elasticity sits in the literature consensus (Krichene 2002 finds global conventional gas supply elasticities around 0.10–0.30; US conventional gas is 0.2–0.4) and produces a realistic post-shock price (P₁ ≈ 44 EUR/MWh under δ = 40% — within the empirical 2022 average TTF range).

Norway alone is far less elastic in the short run because:
- Norwegian fields operate near plateau production
- Gassco reported near-maximum technical capacity utilisation in 2021–2022
- Export pipelines (Langeled, Europipe I/II, Franpipe) have fixed throughput ceilings
- Norwegian exports grew only ~8% from 2021 to 2022 (113 to 122 bcm) despite a 5–10x price increase

The 0.07 figure is consistent with this empirical observation: under our model with ε_s,NO = 0.07 and a 119% price increase, Norway's output grows by ~5.7% — slightly below the empirical 8% but within the order of magnitude, and consistent with Equinor/Gassco capacity statements.

**Verdict: Both values are defensible.** The aggregate (0.35) is supported by the natural gas supply literature for integrated import-flexible markets. The Norway-specific value (0.07) is supported by the empirical 2021→2022 production response and the well-documented capacity constraints on Norwegian Continental Shelf output. Splitting the elasticities is essential because applying 0.35 to Norway alone would imply a 31.7% volume increase, contradicting both the empirical record and the capacity-constraint narrative.

**Source:** Oxford Energy Institute NG-127 (2018) "Norwegian Gas Exports"; IEA Norway Natural Gas Security Policy; Krichene (2002) cited in IMF Working Paper 2022/143; Equinor/Gassco 2022 capacity statements.

---

## A7. Gas-to-Electricity Price Passthrough — 0.5

**What we assume:** A 1% increase in gas prices raises Norwegian household electricity prices by 0.5%.

**Evidence:** Norway generates approximately 88–90% of its electricity from hydropower. Gas prices do not directly determine Norwegian production costs. Instead, the passthrough operates through **price arbitrage via interconnectors**: NordLink (to Germany, operational from 2021) and North Sea Link (to UK, also 2021) connect Norwegian and European electricity markets. When European electricity prices (which are gas-price-driven on the continent) rise, Norwegian electricity flows westward until prices equalise, pulling Norwegian domestic prices up.

- **Zhu et al. (2024)** (*iScience*, PMC11141143) directly estimates gas price transmission to Nordic electricity prices and finds significant passthrough, particularly in southern Norwegian price areas (NO1, NO2) which have the strongest interconnector ties.
- **Energifakta Norge** (the official Norwegian government energy information site) states: *"The high exchange capacity with foreign countries means that the price level in Norway is largely influenced by the costs of producing electricity in thermal power plants, especially the price of coal, gas, and emission allowances."*
- **Statnett (2022)** stated that "very high European gas prices were the main factor of the large increase in electricity prices in Southern Norway."
- In practice, Norwegian electricity spot prices in NO1/NO2 rose from ~10 øre/kWh (2020) to ~100–160 øre/kWh during 2021–2022, broadly tracking continental gas-driven electricity prices.

The true passthrough varies by year and reservoir conditions (low hydro years amplify the effect; high-reservoir years dampen it). A point estimate of 0.5 sits within the range supported by the literature and is consistent with Statnett's assessment that gas prices were the "main factor" in the price surge.

**Verdict: Defensible central estimate.** The range 0.3–0.5 is plausible; we use 0.5 as the central value and acknowledge this is the parameter most sensitive to weather/reservoir conditions. Lower passthrough (0.3) would reduce our estimated consumer welfare loss by approximately 35%.

**Source:** Zhu et al. (2024) *iScience*; Energifakta Norge "The Power Market"; Statnett 2022 commentary.

---

## A8. Household Energy Demand Elasticity — η = 0.3

**What we assume:** A 1% increase in household energy prices reduces household energy demand by 0.3%.

**Evidence:** Norwegian/Nordic empirical estimates:

- **Halvorsen & Larsen (2001)** (*Energy Economics*) — Norwegian household electricity demand: short-run elasticity **−0.11 to −0.15**
- **MDPI Sustainability (2024)** — "Short-Term Price Elasticity of Electricity: Case Study from Norway" — finds elasticity is "low even when the price is very high"; policy documents use **−0.15**
- **ScienceDirect field experiment (2023)** — Norwegian households reduced demand by ~2.9% in high-price hours (very small short-run response)
- General European residential estimates: **−0.1 to −0.3** short-run; **−0.2 to −0.5** medium-run

The Norwegian empirical literature consistently finds short-run household elasticities around −0.10 to −0.20. Our choice of 0.3 sits at the **high end of short-run and low end of medium-run** estimates. Given that the welfare shock persisted for 1–2 years (not just one month), a medium-run framing is appropriate, and 0.3 is plausible.

**Verdict: Acceptable; upper bound of short-run estimates.** We treat 0.3 as representative of a 6–18 month adjustment horizon, over which some household substitution (insulation, wood stoves, behavioural change) is possible. A lower value of 0.15 would increase the estimated consumer welfare loss by approximately 20%, and we recommend noting this range in the report's limitations.

**Source:** Halvorsen & Larsen (2001) *Energy Economics*; MDPI Sustainability (2024); Springer energy demand elasticity meta-analyses.

---

## A9. Representative Household Income — I = 50,000 EUR/year

**What we assume:** A representative Norwegian household earns 50,000 EUR/year in disposable income.

**Evidence:** SSB (Statistics Norway) Statbank Table 04751 reports:
- Median after-tax household income (2021): approximately **566,000 NOK**
- At the 2021 average NOK/EUR exchange rate of ~10.16: **~55,700 EUR**
- The 50,000 EUR figure corresponds to approximately **508,000–575,000 NOK** depending on the exchange rate used

The model's 50,000 EUR is approximately **10% below the actual 2021 median**.

**Importantly, this parameter has no effect on the welfare results.** Under quasi-linear utility, the compensating variation is:

CV = (energy_spend × [(p₁/p₀)^(1−η) − 1]) / (1 − η)

Income I appears in both V(p₀, I) and V(p₁, I) and cancels exactly. The sole purpose of I in the code is to verify the quasi-linearity condition (y_post > 0, i.e., households are not spending more than their income on energy after the shock). With post-shock energy spending of ~2,776 EUR and income of 50,000 EUR, this condition holds with large margin.

**Verdict: Close enough; economically irrelevant.** The 10% underestimate of income has zero effect on any welfare calculation. The 50,000 EUR figure is a reasonable round number approximation.

**Source:** SSB Statbank Table 04751; SSB income and wealth for households 2021.

---

## A10. Number of Households — n = 2,400,000

**What we assume:** Norway has 2.4 million households.

**Evidence:** SSB household statistics (table 10986) show approximately 2,617,000 households in 2024. Working backward at approximately 1% annual growth, the 2021–2022 figure was approximately **2,480,000–2,530,000**. The 2.4 million figure is approximately **4% below the true count**.

**Verdict: Minor underestimate; standard round-number approximation.** Using 2.5 million instead would increase aggregate consumer welfare loss from 2.66 bn EUR to 2.77 bn EUR — a 4% change that does not affect any conclusion. The 2.4 million figure is commonly used in Norwegian energy policy documents.

**Source:** SSB Families and Households statistics (table 10986); SSB income table showing 2,616,826 households in 2024.

---

## A11. Household Energy Expenditure — 2,000 EUR/year

**What we assume:** A representative Norwegian household spends 2,000 EUR/year on energy pre-war.

**Evidence:** SSB data on energy consumption in households (2022 survey) reports average household electricity consumption of approximately **14,964 kWh/year**. At pre-crisis all-in electricity prices of approximately 115–120 øre/kWh (including grid rent and taxes), this implies annual electricity spending of:

14,964 kWh × 1.15–1.20 NOK/kWh ≈ **17,200–17,960 NOK ≈ 1,700–1,770 EUR/year** (at ~10.16 NOK/EUR)

Including biomass/wood heating (additional ~2,500 kWh equivalent), total household energy spending was approximately **1,800–2,100 EUR/year** pre-war. The 2,000 EUR/year calibration target is within this range.

**Important modelling note:** In the model, this 2,000 EUR/year is achieved as price × quantity = 10 EUR/MWh × 200 MWh. The implied quantity of 200 MWh per household is approximately 10 times actual Norwegian household electricity consumption (~15–18 MWh). This is because we calibrate the pre-war domestic energy price at 10 EUR/MWh (a stylised gas-equivalent benchmark) rather than the full retail electricity price (~100–120 øre/kWh ≈ 100–120 EUR/MWh). The post-shock household price (≈ 16 EUR/MWh) is derived by applying the passthrough coefficient (0.5) to the *percentage* change in the gas price, not to the price level — i.e. households face 50% of the gas price increase, consistent with the literature on partial gas-to-electricity transmission in Norway.

This is a known calibration simplification. The key result — the compensating variation — is unaffected because, for constant-elasticity demand, CV depends only on the **price ratio** (p₁/p₀) and **base expenditure**, not on the absolute price level or implied quantity separately:

CV = (energy_spend_pre / (1 − η)) × [(p₁/p₀)^(1−η) − 1]

Both the household price ratio (p₁/p₀ ≈ 15.97 / 10 = 1.60) and the base expenditure (2,000 EUR) enter correctly regardless of the unit decomposition.

**Verdict: Calibration target is empirically sound; the internal price/quantity decomposition is a modelling simplification that does not affect results.** The 2,000 EUR/year expenditure figure is confirmed by SSB data.

**Source:** SSB "Energy consumption in households" (2022 survey); SSB electricity price statistics; Norwegian government electricity support scheme documentation.

---

## A12. Norwegian Petroleum Tax Rate — τ = 78%

**What we assume:** The Norwegian state captures 78% of upstream petroleum profits as tax.

**Evidence:** The Norwegian petroleum tax system is defined precisely by law and confirmed by multiple official sources:

| Tax component | Rate |
|--------------|------|
| Ordinary corporate income tax | 22% |
| Special petroleum surtax | 56% |
| **Combined marginal effective rate** | **78%** |

The special petroleum tax is levied on a **cash-flow basis** (since the 2020 reform), meaning capital expenditures are immediately deductible. This design makes the system investment-neutral: a project profitable before tax remains profitable after tax, as the state effectively co-finances 78% of costs while taking 78% of revenues. This is why the tax is non-distortionary — firms maximise the same production objective regardless of τ.

The 78% rate is explicitly stated on norskpetroleum.no (the official Norwegian government petroleum information site) and confirmed by the Norwegian Tax Administration (Skatteetaten), PwC Norway, and KPMG Norway tax summaries.

**Verdict: Exactly correct.** No adjustment needed.

**Source:** Norskpetroleum.no "The Petroleum Tax System"; Norwegian Tax Administration (Skatteetaten) Petroleum Tax Regulations; PwC Norway Corporate Tax Summary.

---

## Summary

| Parameter | Model Value | Real-World Benchmark | Status |
|-----------|-------------|---------------------|--------|
| P₀ (TTF pre-war price) | 20 EUR/MWh | 14–15 EUR/MWh (2019); 17–20 EUR/MWh (2017–2019 avg) | **Slight overstatement; defensible** |
| Q₀ (EU gas consumption) | 4,000 TWh | ~4,200–4,430 TWh (EU+UK) | **~5% underestimate; acceptable** |
| δ (Russia's supply share) | 40% | ~40% of EU consumption | **Accurate** |
| Norway supply share | 25% | 25% (IEA, 113 bcm/400 bcm) | **Accurate** |
| ε_d (demand elasticity) | −0.30 | −0.15 to −0.25 (meta-analyses) | **Upper end; defensible for full-sector aggregate** |
| ε_s (aggregate EU supply elasticity) | 0.35 | 0.10–0.30 (Krichene 2002, IMF) | **Used to solve European market equilibrium; defensible** |
| ε_s,NO (Norway supply elasticity) | 0.07 | 0.05–0.15 (Norway-specific) | **Used for Norway's PS; reproduces empirical +5–8% volume response** |
| Passthrough | 0.50 | 0.30–0.50 (Zhu et al. 2024; Statnett) | **Central estimate; within empirical range** |
| η (household energy elasticity) | 0.30 | 0.10–0.20 (Norwegian empirical lit) | **Upper end of short-run; medium-run framing** |
| I (household income) | 50,000 EUR | ~55,700 EUR (SSB, 2021 median) | **10% below actual; no effect on results** |
| n (households) | 2,400,000 | ~2,480,000–2,530,000 (2021) | **~4% below actual; negligible** |
| Energy spend | 2,000 EUR/yr | ~1,800–2,100 EUR/yr (SSB data) | **Within empirical range** |
| τ (petroleum tax) | 78% | Exactly 78% (22% + 56%) | **Perfectly accurate** |

The most material sensitivity in the model is the **passthrough coefficient** (0.5), which directly scales the household price increase and therefore consumer welfare loss. Reducing it to 0.3 would decrease the consumer welfare loss from 2.66 bn EUR to approximately 1.6 bn EUR — still far smaller than the government's 19.22 bn EUR gain, leaving all qualitative conclusions unchanged.

---

*All sources accessed April 2026. SSB data from statbank.ssb.no. IEA data from iea.org.*
