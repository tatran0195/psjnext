---
title: "Properties.Shell()"
description: "Assign Shell property to the selected entities"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > Shell"
---

## Description

Assign Shell property to the selected entities.

## Syntax

```psj
Properties.Shell(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlTargets

- Specify the target to assign the Shell property. The target can be Part, Face, or 2D Element.

<!-- @since:5.0.1 @optional -->
<!-- @since:5.1.0 -->
### strName

- Specify the property name.
- The default value is "ShellProperty".

<!-- @since:5.1.0 @optional -->
### iPropertyId

- Specify the property identification number (ID number).
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### iPropertyColor

- Specify the property color.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crMatMembrane

- Specify the material for membrane behavior.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crMatBend

- Specify the material for bending behavior.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crMatShear

- Specify the material for lateral shear behavior.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crMatCoupl

- Specify the material for coupled film-bending behavior.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
<!-- @since:5.1.0 -->
### dMatOrient1

- Specify the theta angle 1 when material orientation is defined by angle.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @required -->
<!-- @since:5.1.0 @optional -->
### dThickness

- Specify the thickness of element in millimeters.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
<!-- @since:5.1.0 -->
### dBendStiff

- Specify the bending stiffness parameter.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
<!-- @since:5.1.0 -->
### dThickRatio

- Specify the thickness ratio of the lateral shear stiffness.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
<!-- @since:5.1.0 -->
### dNSM

- Specify the Non-Structural Mass which is a contribution to the model mass from features that have negligible structural stiffness.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
<!-- @since:5.1.0 -->
### dFiberDist1

- Specify the Fiber distances 1 for stress computation from the reference plane.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
<!-- @since:5.1.0 -->
### dFiberDist2

- Specify the Fiber distances 2 for stress computation from the reference plane.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
<!-- @since:5.1.0 -->
### dPlateOff

- Specify the offset value from the reference plane.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
<!-- @since:5.1.0 -->
### iItgPts

- Specify the integral number of shell elements.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iMatOrientType

- Specify the material orientation type (Angle - 0 or Coordinate system - 1).
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crLocalCS

- Specify the Local coordinate system when material orientation is defined by Coordinate system.
  The X axis of the coordinate system is projected to the element plane.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing Shell property setting item.
  - If this parameter is used, the specified Shell property setting item will be modified.
  - If it is left _None_, a new Shell property setting item will be created.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### iDuplicateOpt

- Specify the duplicate option. When the property is already assigned to some of the selected bodies
  - If this value = 6 means the existing property will be changed.
  - If this value = 2 or 7 means the property will be assigned only to bodies that do not have the property assigned yet.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iPanelLabelId

- Specify the panel label ID.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### strPanelLabelName

- Specify the panel label name.
- The default value is ''.

<!-- @since:5.1.0 @optional -->
### iPanelLabelERP

- Specify whether to enable the ERP function.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iTempVariation

- Specify the temperature variation value (Natural numbers only).
- The default value is DFLT\_INT.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### iPID

- Specify the property identification number (ID number).
- The default value is 1.

## Return Code

A _Cursor_ specifying the created shell property.

## Sample Code

```psj {12-18}
Geometry.Part.Cube()
Properties.Material.Add(strMaterialName="Structural _Steel", 
                        dictMaterialProperty={
                          'Density': {'density': {'DENSITY': [7850.000000000001]}}, 
                          'Elastic': {'elastic': {'YOUNGS _MODULUS': [200000000000.0], 
                          'POISSONS _RATIO': [0.3]}}, 
                          'Expansion': {'expansion': {'ALPHA': [1.2e-05]}}, 
                          'Conductivity': {'conductivity': {'CONDUCTIVITY': [59.0]}}, 
                          'SpecificHeat': {'specificHeat': {'SPECIFIC _HEAT': [461.0]}}}, 
                        iMaterialID=5, 
                        iMaterialColor=10264731)
created _prop = Properties.Shell(crlTargets=[Face(26, 24)], 
                              strName="ShellProperty _1", 
                              iPropertyColor=15329791, 
                              crMatMembrane=Material(5), 
                              crMatBend=Material(5), 
                              crMatShear=Material(5), 
                              dThickness=0.01)
JPT.Debugger(created _prop)
```
