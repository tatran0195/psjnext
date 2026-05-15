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

<!-- @since:5.1.0 @optional -->
### dStefanBoltzmannConstant

- Specify Stefan Boltzmann Constant
- The default value is 5.670000E-8.

<!-- @since:5.1.0 @optional -->
### dAbsoluteZero

- Specify Absolute Zero.
- The default value is 0 (degC).

<!-- @since:5.1.0 @optional -->
### crEdit

- Specify existing thermal attribute.
- The default value is _None_ (create new).

## Return Code

A _Cursor_ specifying the created thermal attribute.

## Sample Code

```psj {1}
BoundaryConditions.ThermalAttributes(dStefanBoltzmannContact=5.67037e-08)
```
