# Who Gains When Gas Prices Surge?

**A Welfare Analysis of Norway's Gas Economy Under the Ukraine War Supply Shock**

EBA3650 Quantitative Economics | BI Norwegian Business School | Spring 2026

---

## Project Structure

```
gas_welfare_project/
├── gas_welfare_analysis.ipynb              ← Full notebook (the deliverable)
├── exam_proposal.pdf                       ← Submitted project proposal
├── README.md
├── member_1/
│   └── section3_gas_market.ipynb           ← Partial equilibrium, equilibrium solving, PS
├── member_2/
│   └── section4_consumer_welfare.ipynb     ← Quasi-linear utility, CV, household welfare
├── member_3/
│   └── section5_petroleum_tax.ipynb        ← Tax decomposition, Ramsey, "who gains?"
└── member_4/
    └── sections_integration.ipynb          ← Intro, background, sensitivity, conclusion
```

## How to Run

```bash
jupyter notebook gas_welfare_analysis.ipynb
```

### Requirements

- Python 3.8+
- numpy
- scipy
- matplotlib

```bash
pip install numpy scipy matplotlib
```

## Division of Work

Each member has their own sub-notebook in `member_X/` that runs independently. Edit your section there, then integrate changes back into the full notebook.

| Member | Folder | Section | What to Own |
|--------|--------|---------|-------------|
| 1 | `member_1/` | Section 3 (Partial Equilibrium Model) | Supply/demand, equilibrium solving, producer surplus |
| 2 | `member_2/` | Section 4 (Consumer Welfare) | Quasi-linear utility, compensating variation, welfare loss |
| 3 | `member_3/` | Section 5 (Petroleum Tax) | Resource rent tax / Ramsey framing, tax decomposition, distributional analysis |
| 4 | `member_4/` | Sections 1-2, 6-7 (Integration) | Intro, background, sensitivity analysis, conclusion, presentation |

## Key Results (Baseline)

- **Pre-war gas price:** 20 EUR/MWh --> **Post-shock:** 43.89 EUR/MWh (+119%)
- **Norwegian PS gain (gross):** +24.6 bn EUR
- **Government revenue gain (78% tax):** +19.2 bn EUR
- **Firm profit gain (22%):** +5.4 bn EUR
- **Consumer welfare loss:** -2.7 bn EUR
- **Net welfare:** +22.0 bn EUR -- **Norway is a net winner**
- Government could compensate every household **7.2x over** and still be ahead
