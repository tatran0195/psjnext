---
title: NASTRAN_NONLINEAR
id: NASTRAN_NONLINEAR
---

## Description

A data type uses to defines a set of parameters for nonlinear static analysis iteration strategy.

## Attributes

### `iNINC`

- An _Integer_ specifying the Number of increments.
- The default value is 1.

### `iKMETHOD`

- An _Integer_ specifying the method for controlling stiffness updates.
    - 0: AUTO.
    - 1: ITER.
    - 2: SEMI.
    - 3: FNT.
    - 4: PFNT.
- The default value is 3.

### `iMAXITER`

- An _Integer_ specifying the Limit on number of iterations for each load increment.
- The default value is 1.

### `bUseEPSU`

- A _Boolean_ enable/disable the error tolerance for displacement (U) criterion.
- The default value is _False_.

### `bUseEPSP`

- A _Boolean_ enable/disable the Error tolerance for load (P) criterion.
- The default value is _False_.

### `bUseEPSW`

- A _Boolean_ enable/disable the Error tolerance for work (W) criterion.
- The default value is _False_.

### `dEPSU`

- A _Double_ specifying the error tolerance for displacement (U) criterion value.
- The default value is 1.0E-2.

### `dEPSP`

- A _Double_ specifying the Error tolerance for load (P) criterion value.
- The default value is 1.0E-2.

### `dEPSW`

- A _Double_ specifying the Error tolerance for work (W) criterion value.
- The default value is 1.0E-2.
