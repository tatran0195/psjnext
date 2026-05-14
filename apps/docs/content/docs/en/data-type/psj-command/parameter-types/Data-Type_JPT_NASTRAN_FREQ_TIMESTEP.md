---
title: NASTRAN_FREQ_TIMESTEP
id: NASTRAN_FREQ_TIMESTEP
---

## Description

A data type uses to control parameters of Nastran Freq Timestep

## Attributes

### `iNumberOfSteps`

- An _Integer_ specifying the Number time steps of value DTi.
- The default value is DFLT_INT.

### `dTimeIncrement`

- A _Double_ specifying the time increment.
- The default value is DFLT_DBL.

### `iOutputInterval`

- An _Integer_ specifying the Skip factor for output. Every NOi-th step will be saved for output.
- The default value is DFLT_INT.

### `iDampingType`

- An _Integer_ specifying the Modal Damping Table type.
  - 0: None type.
  - 1: CRIT type (Critical damping ratio) .
  - 2: G type (Structural damping coefficient).
  - 3: Q type (Q factor).
- The default value is 2.

### `iModalDampingTableId`

- An _Integer_ specifying the modal damping table ID..
- The default value is 0.
