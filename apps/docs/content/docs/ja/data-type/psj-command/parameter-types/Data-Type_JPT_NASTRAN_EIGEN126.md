---
title: NASTRAN_EIGEN126
id: NASTRAN_EIGEN126
---

## Description

A data type uses to control parameters of Nastran Eigen126

## Attributes

### `iModalExtractionMethod`

- An _Integer_ specifying modal extraction method.
- The default value is 0 which represent for Lanczos eigenvalue extraction method.

### `dModalStartFreq`

- A _Double_ specifying the starting frequency value.
- The default value is DFLT_DBL.

### `dModalEndFreq`

- A _Double_ specifying the ending frequency value.
- The default value is DFLT_DBL.

### `iModalNoOfModes`

- An _Integer_ specifying the number of modes.
- The default value is DFLT_INT.

### `iBRsvec`

- An _Integer_ specifying the Residual Vector Selection.
- The default value is 0.

### `iMLDSExtractionMethod`

- An _Integer_ specifying the eigenvalue extraction method used by the MLDS reduction.
- The default value is 0 which represent for Lanczos eigenvalue extraction method..

### `dMLDSStartFreq`

- A _Double_ specifying the starting frequency value used by the MLDS reduction.
- The default value is DFLT_DBL.

### `dMLDSEndFreq`

- A _Double_ specifying the ending frequency value used by the MLDS reduction.
- The default value is DFLT_DBL.

### `iMLDSNoOfModes`

- A _Double_ specifying the number of modes used by the MLDS reduction.
- The default value is DFLT_DBL.
