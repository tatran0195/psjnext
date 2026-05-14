---
title: "Tools.Measure.Mass.Property()"
description: "Measure mass by using the applied property"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Measure > Mass > Property"
---

## Description

Measure mass by using the applied property.

## Syntax

```psj
Tools.Measure.Mass.Property(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional -->
### `crlParts`

- The list of parts to measure the mass. This argurment could be in Part type and/or Bar type. If this parameter is \[],`crlMassConditions` must be specified.
  - If the measurement is applied to `crlParts` only, then `crlParts` is a required input.
  - If the measurement is applied to `crlMassConditions` only, then `crlParts` would have the default value is \[].

<!-- @since:5.0.1 @type:List[Cursor] @optional -->
### `crlMassConditions`

- The list of mass conditions created by_[Connections.MassElements](../connections/Connections.MassElements)_. If this is \[], `crlParts` must be specified.
  - If the measurement is applied to `crlMassConditions` only, then `crlMassConditions` is a required input.
  - If the measurement is applied to `crlParts` only, then `crlMassConditions` would have the default value is \[].

<!-- @since:5.0.1 @type:String @optional @default:"Mass" -->
### `strTarget`

- The target value of mass information to be outputted. Depending on the target information, this parameter can be one of the following:
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

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bGravityCenter`

- The use of gravity center Coordinate System to measure the mass.
  - If _True_, `crCoord` will not be disable. All information will be outputted based on referring to Gravity Center Coordinate System.
  - If _False_, `crCoord` will be defined. All information will be outputted based on referring to Coordinate System that the `crCoord` specified.

<!-- @since:5.0.1 @type:Cursor @optional @default:None (Global Coordinate) -->
### `crCoord`

- The Coordinate System to measure the mass. This parameter cannot be used when`bGravityCenter` is _True_.

<!-- @since:5.0.1 @type:Integer @optional @default:6 -->
### `iPrecision`

- The number of digit after floating point. The greater`iPrecision` could be, the more accuracy of mass value can be measured.

## Return Code

A _Double_ specifying the value of Mass information.

## Sample Code

```psj {24}
Geometry.Part.Cube()
Properties.Material.Add("Copper _Alloy", 
                        [Density([(DENSITY, 
                                   8.3e-09)]), 
                        Elastic([(YOUNGS _MODULUS, 
                                  110000.0), 
                                 (POISSONS _RATIO, 
                                  0.34)])])
Properties.Shell(strName="Shell Property 1", 
                 crMatMembrane=Material(1), 
                 crMatBend=Material(1), 
                 crMatShear=Material(1), 
                 dMatOrient1=DFLT _DBL, 
                 dThickness=0.001, 
                 dBendStiff=DFLT _DBL, 
                 dThickRatio=DFLT _DBL, 
                 dNSM=DFLT _DBL, 
                 dFiberDist1=DFLT _DBL, 
                 dFiberDist2=DFLT _DBL,
                 dPlateOff=DFLT _DBL, 
                 iItgPts=DFLT _INT, 
                 crlTargets=[Part(1)])

mass = Tools.Measure.Mass.Property(crlParts=[Part(1)])

JPT.Debugger(mass)
```
