"""Problem 30 — Exothermic or endothermic?

Domain: Chemistry. Chapter 10 (Control Flow), conditionals.

Problem
-------
If the enthalpy change ΔH is negative, the reaction is exothermic; otherwise endothermic.

Expected output
---------------
Exothermic
"""


delta_h_kj = -92
if delta_h_kj < 0:
    print("Exothermic")
else:
    print("Endothermic")
