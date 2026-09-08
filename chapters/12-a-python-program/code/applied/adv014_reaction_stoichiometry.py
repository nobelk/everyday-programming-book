"""Advanced problem 14 — Reaction Stoichiometry (functional)

Subject: Chemistry. Style: functional.

Problem
-------
For the reaction `2 H₂ + O₂ → 2 H₂O`, given moles of H₂ available (`[1, 2, 4, 5, 10]`) and unlimited O₂, compute moles of water produced (it's 1 mole H₂O per 1 mole H₂).

Concepts taught
---------------
`map` over a list, `zip` to combine parallel sequences, identity lambda showing 1:1 mapping.

Expected output
---------------
H2=1 mol → H2O=1 mol, O2 used=0.5 mol
H2=2 mol → H2O=2 mol, O2 used=1.0 mol
H2=4 mol → H2O=4 mol, O2 used=2.0 mol
H2=5 mol → H2O=5 mol, O2 used=2.5 mol
H2=10 mol → H2O=10 mol, O2 used=5.0 mol
"""


hydrogen_moles = [1, 2, 4, 5, 10]
water_produced = list(map(lambda h2: h2, hydrogen_moles))
oxygen_used    = list(map(lambda h2: h2 / 2.0, hydrogen_moles))

for h2, h2o, o2 in zip(hydrogen_moles, water_produced, oxygen_used):
    print(f"H2={h2} mol → H2O={h2o} mol, O2 used={o2} mol")
