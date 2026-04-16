---
title: NASTRAN_FREQUENCY
id: NASTRAN_FREQUENCY
---

## Description

A data type uses to Defines a set of frequencies to be used in the solution of frequency response problems by specification of a starting frequency, frequency increment, and the number of increments desired

## Attributes

### `dStartFrequency`

- A _Double_ specifying the first Frequency in set.
- The default value is DFLT_DBL.

### `dIncrement`

- A _Double_ specifying the Frequency increment.
- The default value is DFLT_DBL.

### `iNumberOfInc`

- An _Integer_ specifying the number of frequency increments.
- The default value is DFLT_INT.

### `iTableId`

- An _Integer_ specifying the ID of frequency response table.
- The default value is 0.
