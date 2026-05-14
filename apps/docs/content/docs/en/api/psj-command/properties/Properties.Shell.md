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

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlTargets`

- The target to assign the Shell property. The target can be Part, Face, or 2D Element.

<!-- @since:5.0.1 @type:String @optional @default:"Shell Property" -->
<!-- @since:5.1.0 @default:"ShellProperty" -->
### `strName`

- The property name.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iPropertyId`

- The property identification number (ID number).

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iPropertyColor`

- The property color.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMatMembrane`

- The material for membrane behavior.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMatBend`

- The material for bending behavior.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMatShear`

- The material for lateral shear behavior.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMatCoupl`

- The material for coupled film-bending behavior.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
<!-- @since:5.1.0 @default:DFLT _DBL -->
### `dMatOrient1`

- The theta angle 1 when material orientation is defined by angle.

<!-- @since:5.0.1 @type:Double @required -->
<!-- @since:5.1.0 @optional @default:DFLT _DBL -->
### `dThickness`

- The thickness of element in millimeters.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
<!-- @since:5.1.0 @default:DFLT _DBL -->
### `dBendStiff`

- The bending stiffness parameter.

<!-- @since:5.0.1 @type:Double @optional @default:0.5 -->
<!-- @since:5.1.0 @default:DFLT _DBL -->
### `dThickRatio`

- The thickness ratio of the lateral shear stiffness.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
<!-- @since:5.1.0 @default:DFLT _DBL -->
### `dNSM`

- The Non-Structural Mass which is a contribution to the model mass from features that have negligible structural stiffness.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
<!-- @since:5.1.0 @default:DFLT _DBL -->
### `dFiberDist1`

- The Fiber distances 1 for stress computation from the reference plane.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
<!-- @since:5.1.0 @default:DFLT _DBL -->
### `dFiberDist2`

- The Fiber distances 2 for stress computation from the reference plane.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
<!-- @since:5.1.0 @default:DFLT _DBL -->
### `dPlateOff`

- The offset value from the reference plane.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
<!-- @since:5.1.0 @default:DFLT _DBL -->
### `iItgPts`

- The integral number of shell elements.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMatOrientType`

- The material orientation type (Angle - 0 or Coordinate system - 1).

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crLocalCS`

- The Local coordinate system when material orientation is defined by Coordinate system.
  The X axis of the coordinate system is projected to the element plane.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing Shell property setting item.
  - If this parameter is used, the specified Shell property setting item will be modified.
  - If it is left _None_, a new Shell property setting item will be created.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDuplicateOpt`

- The duplicate option. When the property is already assigned to some of the selected bodies
  - If this value = 6 means the existing property will be changed.
  - If this value = 2 or 7 means the property will be assigned only to bodies that do not have the property assigned yet.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iPanelLabelId`

- The panel label ID.

<!-- @since:5.1.0 @type:String @optional @default:'' -->
### `strPanelLabelName`

- The panel label name.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iPanelLabelERP`

- Whether to enable the ERP function.

<!-- @since:5.1.0 @type:Integer @optional @default:DFLT _INT -->
### `iTempVariation`

- The temperature variation value (Natural numbers only).

<!-- @since:5.0.1 @type:Integer @removed:5.1.0 @optional @deprecated @default:1 -->
### `iPID`

- The property identification number (ID number).

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
