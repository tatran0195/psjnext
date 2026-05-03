---
title: "BoundaryConditions.ThermalAttributes()"
description: "Create a thermal attribute."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "BoundaryConditions > ThermalAttributes"
macro_link: "LbcThermalAttributes"
---

## Description

Create a thermal attribute.

## Syntax

```psj
BoundaryConditions.ThermalAttributes(...)
```

## Inputs

### `dStefanBoltzmannConstant` @type(Double) @default(5.670000E-8)

- Stefan Boltzmann Constant

### `dAbsoluteZero` @type(Double) @default(0 (degC))

- Absolute Zero.

### `crEdit` @type(Cursor) @default(None (create new))

- Existing thermal attribute.

## Return Code

A _Cursor_ specifying the created thermal attribute.

## Sample Code

```psj {1}
BoundaryConditions.ThermalAttributes(dStefanBoltzmannContact=5.67037e-08)
```
