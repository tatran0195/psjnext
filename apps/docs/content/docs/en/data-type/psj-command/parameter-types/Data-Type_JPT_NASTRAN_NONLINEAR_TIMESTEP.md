---
title: NASTRAN_NONLINEAR_TIMESTEP
id: NASTRAN_NONLINEAR_TIMESTEP
---

## Description

A data type uses to defines parametric controls and data for nonlinear transient structural analysis(SOL 129).

## Attributes

### `iNDT`

- An _Integer_ specifying the Number of time steps of value DT.
- The default value is DFLT_INT.

### `dDT`

- A _Double_ specifying the Time increment.
- The default value is DFLT_DBL.

### `iMAXITER`

- An _Integer_ specifying the limit on number of iterations for each time step.
- The default value is DFLT_DBL.
