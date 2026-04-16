---
title: NASTRAN_CASE_CONTROL
id: NASTRAN_CASE_CONTROL
---

## Description

A data type uses to control parameters of Nastran Case Control

## Attributes

### `iECHO`

- An _Integer_ specifying the Echo Request of the Bulk Data.
    - 0: No echo will be output.
    - 1: Sorted echo will be output.
    - 2: Unsorted echo will be output.
    - 3: Sorted and Unsorted echo will be output.
- The default value is 0.

### `strTitle`

- An _string_ specifying the title at the time of print output.
- The default value is "".
