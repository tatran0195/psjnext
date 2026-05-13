---
title: NASTRAN_SUBCASE
id: NASTRAN_SUBCASE
---

## Description

A data type uses to control parameters of Nastran Subcase

## Attributes

### `iId`

- An _Integer_ specifying the subcase ID.
- The default value is 0.

### `strTitle`

- A _String_ specifying the subcase title.
- The default value is "".

### `strArbitraryText`

- A _String_ specifying the arbitrary text input.
- The default value is "".

### `iSubcaseIdForLoad`

- An _Integer_ specifying the subcase ID for load.
- The default value is 0.

### `iSubcaseIdForDload`

- An _Integer_ specifying the subcase ID for dynamic load.
- The default value is 0.

### `iSubcaseIdForSpc`

- An _Integer_ specifying the subcase ID for spc(single point contraint).
- The default value is 0.

### `iSubcaseIdForMpc`

- An _Integer_ specifying the subcase ID for mpc(multi point contraint).
- The default value is 0.

### `iSubcaseIdForBcontact`

- An _Integer_ specifying the contact table ID for 3D contact.
- The default value is 0.

### `iSubcaseIdForTempInit`

- An _Integer_ specifying the subcase ID for temperature initiation.
- The default value is 0.

### `iSubcaseIdForTempLoad`

- An _Integer_ specifying the subcase ID for temperature load.
- The default value is 0.

### `iOutputreqDisplacement`

- An _Integer_ specifying the displacement output request.
    - 0: NONE.
    - DFLT_INT: ALL.
- The default value is 0.

### `iOutputreqStress`

- An _Integer_ specifying the element stress output request.
    - 0: NONE.
    - DFLT_INT: ALL.
- The default value is 0.

### `iOutputreqStrain`

- An _Integer_ specifying the element strain output request.
    - 0: NONE.
    - DFLT_INT: ALL.
- The default value is 0.

### `iOutputreqAcceleration`

- An _Integer_ specifying the acceleration output request.
    - 0: NONE.
    - DFLT_INT: ALL.
- The default value is 0.

### `iOutputreqVelocity`

- An _Integer_ specifying the velocity output request.
    - 0: NONE.
    - DFLT_INT: ALL.
- The default value is 0.

### `iNlparm`

- An _Integer_ specifying the Nonlinear Static Analysis Parameter Selection.
- The default value is 0.
