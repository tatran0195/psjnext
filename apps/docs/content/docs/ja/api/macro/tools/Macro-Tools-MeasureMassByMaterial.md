---
title: "MeasureMassByMaterial()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Measure Mass By Material.

## Syntax

```psj
MeasureMassByMaterial. (Cursor[] parts, Cursor[] massConditions, double dMaterialDensity, String strTarget, Bool bGravityCenter, Cursor crRefCoord, int iPrecision)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

A List of Cursor specifying the list of parts to measure the mass. This argurment could be in Part type and/or Bar type. If this parameter is \[], massConditions must be specified.

<!-- @since:5.0.1 -->
### 2. Cursor\[]

A List of Cursor specifying the list of mass conditions. If this is \[], parts must be specified.

<!-- @since:5.0.1 -->
### 3. double\[]

A String specifying the material density (default unit: kg/m3).

<!-- @since:5.0.1 -->
### 4. String

- A _String_ specifying the target value of mass information to be outputted. Depending on the target information, this parameter can be one of the following:
  - If _strTarget="Mass"_: Return the mass value.
  - If _strTarget="Gravity Center X"_: Return the X position of Gravity Center.
  - If _strTarget="Gravity Center Y"_: Return the Y position of Gravity Center.
  - If _strTarget="Gravity Center Z"_: Return the Z position of Gravity Center.
  - If _strTarget="Moment Inertial XX"_: Return the Moment of Inertia about X axis.
  - If _strTarget="Moment Inertial YY"_: Return the Moment of Inertia about Y axis.
  - If _strTarget="Moment Inertial ZZ"_: Return the Moment of Inertia about Z axis.
  - If _strTarget="Moment Inertial XY"_: Return the product of Moment of Inertia on XY.
  - If _strTarget="Moment Inertial YZ"_: Return the product of Moment of Inertia on YZ.
  - If _strTarget="Moment Inertial XZ"_: Return the product of Moment of Inertia on XZ.
  - If _strTarget="Principal Moment X"_: Return the Moment of Inertia about Principal axis 11.
  - If _strTarget="Principal Moment Y"_: Return the Moment of Inertia about Principal axis 22.
  - If _strTarget="Principal Moment Z"_: Return the Moment of Inertia about Principal axis 33.
  - If _strTarget="Traits Vector XX"_: Return the X direction of Principal axis 11.
  - If _strTarget="Traits Vector XY"_: Return the Y direction of Principal axis 11.
  - If _strTarget="Traits Vector XZ"_: Return the Z direction of Principal axis 11.
  - If _strTarget="Traits Vector YX"_: Return the X direction of Principal axis 22.
  - If _strTarget="Traits Vector YY"_: Return the Y direction of Principal axis 22.
  - If _strTarget="Traits Vector YZ"_: Return the Z direction of Principal axis 22.
  - If _strTarget="Traits Vector ZX"_: Return the X direction of Principal axis 33.
  - If _strTarget="Traits Vector ZY"_: Return the Y direction of Principal axis 33.
  - If _strTarget="Traits Vector ZZ"_: Return the Z direction of Principal axis 33.
  - If _strTarget="Euler Angle X"_: Return the rotation angle of main axis with X axis.
  - If _strTarget="Euler Angle Y"_: Return the rotation angle of main axis with Y axis.
  - If _strTarget="Euler Angle Z"_: Return the rotation angle of main axis with Z axis.
- The default value is "Mass".

<!-- @since:5.0.1 -->
### 5. Bool

- A _Boolean_ specifying the use of gravity center Coordinate System to measure the mass.

<!-- @since:5.0.1 -->
### 6. Cursor

- A _Cursor_ specifying the Coordinate System to measure the mass. This parameter cannot be used when `bGravityCenter` is _True_.
- The default value is _None_ (Global Coordinate).

<!-- @since:5.0.1 -->
### 7. int

- An _Integer_ specifying the number of digit after floating point. The greater `iPrecision` could be, the more accuracy of mass value can be measured.
- The default value is 6.

## Return Code

A _Double_ specifying the value of Mass information.

## Sample Code

```psj
MeasureMassByMaterial([3:1], [], 2300, "Mass", 0, 0:0, 6)
```
