"""Problem 37 — Solubility category

Domain: Chemistry. Chapter 10 (Control Flow), conditionals.

Problem
-------
Solubility (g per 100 g water) <0.1 is insoluble, <1 slightly soluble, else soluble.

Expected output
---------------
Solubility 0.35 → Slightly soluble
"""


solubility = 0.35
if solubility < 0.1:
    label = "Insoluble"
elif solubility < 1:
    label = "Slightly soluble"
else:
    label = "Soluble"
print(f"Solubility {solubility} → {label}")
