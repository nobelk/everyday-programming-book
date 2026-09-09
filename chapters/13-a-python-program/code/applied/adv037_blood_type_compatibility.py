"""Advanced problem 37 — Blood-Type Compatibility (imperative)

Subject: Biology. Style: imperative.

Problem
-------
Print whether each pair of (donor, recipient) blood types is compatible.

Concepts taught
---------------
Dict-of-lists, membership check, conditional output.

Expected output
---------------
O- → A+: compatible
AB+ → O-: NOT compatible
B+ → AB+: compatible
A- → B-: NOT compatible
"""


compatibility = {
    "O-":  ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"],
    "O+":  ["O+", "A+", "B+", "AB+"],
    "A-":  ["A-", "A+", "AB-", "AB+"],
    "A+":  ["A+", "AB+"],
    "B-":  ["B-", "B+", "AB-", "AB+"],
    "B+":  ["B+", "AB+"],
    "AB-": ["AB-", "AB+"],
    "AB+": ["AB+"],
}

pairs = [("O-", "A+"), ("AB+", "O-"), ("B+", "AB+"), ("A-", "B-")]

for donor, recipient in pairs:
    if recipient in compatibility[donor]:
        print(f"{donor} → {recipient}: compatible")
    else:
        print(f"{donor} → {recipient}: NOT compatible")
