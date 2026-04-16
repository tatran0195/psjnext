---
title: BOLT_TYPE_AB
id: BOLT_TYPE_AB
---

## Description

A data type uses to control parameters of bolt type A and B

## Attributes

### `iSeatType`

- An _Int_ specifying Connection.
    - 0 : Create RBE2
    - 1 : Create RBE3
- The default value is 0.

### `iSeatCase`

- An _Int_ specifying seat setting.
    - 0: By diameter.
    - 1: By Layer.
- The default value is 1.

### `dSeatDiameter`

- A _Double_ specifying Seat Diameter.
- The default value is 0.02.

### `iSeatLayer`

- An _Int_ specifying Num of Layer.
- The default value is 1.

### `iShaftType`

- An _Int_ specifying which shaft type is selected.
    - 0 : Bar
    - 1 : RBE2
- The default value is 1.

### `crBarProp`

- A _Cursor_ specifying bar property if shaft type is Bar.
- The default value is _None_.

### `iBotConType`

- An _Int_ specifying which connection is created if iCenterType is Spring.
    - 0 : Create RBE2
    - 1 : Create RBE3
- The default value is 0.

### `iCenterType`

- An _Int_ specifying center connection type.
    - 0 : None
    - 1 : Spring
    - 2 : PreTension
- The default value is 0.

### `iCenterPos`

- An _Int_ specifying center position of Bottom Settings.
    - 0 : Upper
    - 1 : Middle
    - 2 : Bottom
- The default value is 0.

### `dlStiffness`

- A _Double Vector_ specifying stiffness of spring.
- The default value is [0.0, 0.0, 0.0].

### `iUnit`

- An _Int_ specifying Input Unit for dlStiffness.
- The default value is 0.

### `dDampCoef`

- A _Double_ specifying Damping Coef of spring.
- The default value is 0.

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
- The default value is 0.0.

### `pretension`

- A _PRETENSION_LOAD_ specifying Pre Tension Load.
