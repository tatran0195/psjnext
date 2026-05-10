---
title: BOLT_TYPE_C
id: BOLT_TYPE_C
---

## Description

A data type uses to control parameters of bolt type C

## Attributes

### `iTopConType`

- An _Int_ specifying Connection.
    - 0 : Create RBE2
    - 1 : Create RBE3
- The default value is 0.

### `iBotConType`

- An _Int_ specifying which connection is created if iCenterType is Spring.
    - 0 : Create RBE2
    - 1 : Create RBE3
- The default value is 0.

### `iCenterType`

- An _Int_ specifying center connection type.
    - 0 : None
    - 1 : Spring
- The default value is 0.

### `dlStiffness`

- A _Double Vector_ specifying stiffness of spring.
- The default value is [0.0, 0.0, 0.0].

### `iUnit`

- An _Int_ specifying Input Unit for dlStiffness.
- The default value is 0.

### `dDampCoef`

- A _Double_ specifying Damping Coef of spring.
- The default value is 0.0.

### `crCoord`

- A _Cursor_ specifying Local Coordinate.
- The default value is _None_.

### `dlRStiffness`

- A _Double Vector_ specifying rotational stiffness of spring.
- The default value is [0.0, 0.0, 0.0].

### `iRUnit`

- An _Int_ specifying Input Unit for dlRStiffness.
- The default value is 0.

### `dStressCoef`

- A _Double_ specifying Stress Coef of spring.
- The default value is 0.

### `pretension`

- A _PRETENSION_LOAD_ specifying Pre Tension Load.
