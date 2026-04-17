---
title: NASTRAN_PSD_DATA
id: NASTRAN_PSD_DATA
---

## Description

A data type uses to Defines load set power spectral density factors for use in random analysis having the frequency dependent form.
$$S_{jk} = (X + iY)G(F)$$

## Attributes

### `iMasterID`

- An _Integer_ specifying the Subcase identification number of the excited load set.
- The default value is 0.

### `iSlaveID`

- An _Integer_ specifying the Subcase identification number of the applied load set.
- The default value is 0.

### `dRealX`

- A _Double_ specifying the real part of the complex number.
- The default value is 1.0.

### `dImagY`

- A _Double_ specifying the imaginary part of the complex number.
- The default value is 0.0.

### `iTableID`

- An _Integer_ specifying the Identification number of a TABRNDi entry that defines G(F).
- The default value is 0.0.
