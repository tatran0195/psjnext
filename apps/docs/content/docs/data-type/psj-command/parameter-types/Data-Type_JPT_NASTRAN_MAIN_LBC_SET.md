---
title: NASTRAN_MAIN_LBC_SET
id: NASTRAN_MAIN_LBC_SET
---

## Description

A data type uses to Define the boundary conditions that act on the entire analysis to be defined on the specific SUBCASE.

## Attributes

### `iSubcaseIdForLoad`

- An _Integer_ specifying the load set.
- The default value is DFLT_INT.

### `iSubcaseIdForDload`

- An _Integer_ specifying the dynamic load case.
- The default value is DFLT_INT.

### `iSubcaseIdForSpc`

- An _Integer_ specifying the Spc (single point constraints) set.
- The default value is DFLT_INT.

### `iSubcaseIdForMpc`

- An _Integer_ specifying the Mpc (Multi point constraints) set.
- The default value is DFLT_INT.

### `iSubcaseIdForTempInit`

- An _Integer_ specifying the initial temperature set.
- The default value is DFLT_INT.

### `iSubcaseIdForTempLoad`

- An _Integer_ specifying the temperature load set.
- The default value is DFLT_INT.
