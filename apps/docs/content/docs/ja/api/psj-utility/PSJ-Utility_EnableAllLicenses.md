---
title: "JPT.EnableAllLicenses()"
description: "Enable/Disable all the licenses feature which is existing in the current Jupiter."
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Enable/Disable all the licenses feature which is existing in the current Jupiter.

## Syntax

```psj
JPT.EnableAllLicenses(...)
```

## Inputs

### `BoolType`

- A _Bool_ describing the enable state of license:
  - _True_: Enable all the licenses.
  - _False_: Disable all the licenses.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {2}
# Disable all the licenses
JPT.EnableAllLicenses(False)
```
