---
title: "Tools.Measure.Mass.Material()"
description: "Measure mass by using the specified material's density"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Measure > Mass > Material"
---

## Description

Measure mass by using the specified material's density.

## Syntax

```psj
Tools.Measure.Mass.Material(...)
```

## Inputs

### `crlParts` @type(List\[Cursor])

- The list of parts to measure the mass. This argurment could be in Part type and/or Bar type. If this parameter is \[],`crlMassConditions`must be specified.
  - If the measurement is applied to`crlParts`only, then`crlParts`is a required input.
  - If the measurement is applied to`crlMassConditions`only, then`crlParts`would have the default value is \[].

### `crlMassConditions` @type(List\[Cursor])

- The list of mass conditions created b&#x79;_[Connections.MassElements](../connections/Connections.MassElements)_. If this is \[],`crlParts`must be specified.
  - If the measurement is applied to`crlMassConditions`only, then`crlMassConditions`is a required input.
  - If the measurement is applied to`crlParts`only, then`crlMassConditions`would have the default value is \[].

### `dMaterialDensity` @type(String) @required

- The material density (default unit: kg/m3).

### `strTarget` @type(String) @default("Mass")

- The target value of mass information to be outputted. Depending on the target information, this parameter can be one of the following:
  - I&#x66;_&#x73;trTarget="Mass"_: Return the mass value.
  - I&#x66;_&#x73;trTarget="Gravity Center X"_: Return the X position of Gravity Center.
  - I&#x66;_&#x73;trTarget="Gravity Center Y"_: Return the Y position of Gravity Center.
  - I&#x66;_&#x73;trTarget="Gravity Center Z"_: Return the Z position of Gravity Center.
  - I&#x66;_&#x73;trTarget="Moment Inertial XX"_: Return the Moment of Inertia about X axis.
  - I&#x66;_&#x73;trTarget="Moment Inertial YY"_: Return the Moment of Inertia about Y axis.
  - I&#x66;_&#x73;trTarget="Moment Inertial ZZ"_: Return the Moment of Inertia about Z axis.
  - I&#x66;_&#x73;trTarget="Moment Inertial XY"_: Return the product of Moment of Inertia on XY.
  - I&#x66;_&#x73;trTarget="Moment Inertial YZ"_: Return the product of Moment of Inertia on YZ.
  - I&#x66;_&#x73;trTarget="Moment Inertial XZ"_: Return the product of Moment of Inertia on XZ.
  - I&#x66;_&#x73;trTarget="Principal Moment X"_: Return the Moment of Inertia about Principal axis 11.
  - I&#x66;_&#x73;trTarget="Principal Moment Y"_: Return the Moment of Inertia about Principal axis 22.
  - I&#x66;_&#x73;trTarget="Principal Moment Z"_: Return the Moment of Inertia about Principal axis 33.
  - I&#x66;_&#x73;trTarget="Traits Vector XX"_: Return the X direction of Principal axis 11.
  - I&#x66;_&#x73;trTarget="Traits Vector XY"_: Return the Y direction of Principal axis 11.
  - I&#x66;_&#x73;trTarget="Traits Vector XZ"_: Return the Z direction of Principal axis 11.
  - I&#x66;_&#x73;trTarget="Traits Vector YX"_: Return the X direction of Principal axis 22.
  - I&#x66;_&#x73;trTarget="Traits Vector YY"_: Return the Y direction of Principal axis 22.
  - I&#x66;_&#x73;trTarget="Traits Vector YZ"_: Return the Z direction of Principal axis 22.
  - I&#x66;_&#x73;trTarget="Traits Vector ZX"_: Return the X direction of Principal axis 33.
  - I&#x66;_&#x73;trTarget="Traits Vector ZY"_: Return the Y direction of Principal axis 33.
  - I&#x66;_&#x73;trTarget="Traits Vector ZZ"_: Return the Z direction of Principal axis 33.
  - I&#x66;_&#x73;trTarget="Euler Angle X"_: Return the rotation angle of main axis with X axis.
  - I&#x66;_&#x73;trTarget="Euler Angle Y"_: Return the rotation angle of main axis with Y axis.
  - I&#x66;_&#x73;trTarget="Euler Angle Z"_: Return the rotation angle of main axis with Z axis.

### `bGravityCenter` @type(Boolean) @default(False)

- The use of gravity center Coordinate System to measure the mass.
  - I&#x66;_&#x54;rue_,`crCoord`will not be disable. All information will be outputted based on referring to Gravity Center Coordinate System.
  - I&#x66;_&#x46;alse_,`crCoord`will be defined. All information will be outputted based on referring to Coordinate System that the`crCoord`specified.

### `crCoord` @type(Cursor) @default(None (Global Coordinate))

- The Coordinate System to measure the mass. This parameter cannot be used when`bGravityCenter`i&#x73;_&#x54;rue_.

### `iPrecision` @type(Integer) @default(6)

- The number of digit after floating point. The greater`iPrecision`could be, the more accuracy of mass value can be measured.

## Return Code

A _Double_ specifying the value of Mass information.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

mass = Tools.Measure.Mass.Material(crlParts=[Part(1)], 
                                   dMaterialDensity=2300.0)

JPT.Debugger(mass)
```
