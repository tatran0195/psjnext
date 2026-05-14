---
title: "BoundaryConditions.ThermalAttributes()"
description: "Create a thermal attribute."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "BoundaryConditions > ThermalAttributes"
macro _link: "LbcThermalAttributes"
---

## Description

Create a thermal attribute.

## Syntax

```psj
BoundaryConditions.ThermalAttributes(...)
```

## Inputs

<!-- @since:5.1.0 @type:Double @optional @default:5.670000E-8 -->
### `dStefanBoltzmannConstant`

- The Stefan Boltzmann Constant

<!-- @since:5.1.0 @type:Double @optional @default:0 (degC) -->
### `dAbsoluteZero`

- The Absolute Zero.

<!-- @since:5.1.0 @type:Cursor @optional @default:None (create new) -->
### `crEdit`

- The existing thermal attribute.

## Return Code

A _Cursor_ specifying the created thermal attribute.

## Sample Code

```psj {1}
BoundaryConditions.ThermalAttributes(dStefanBoltzmannContact=5.67037e-08)
```
