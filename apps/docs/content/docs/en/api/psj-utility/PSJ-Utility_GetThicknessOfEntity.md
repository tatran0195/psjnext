---
title: "JPT.GetThicknessOfEntity()"
description: "Get thickness of the inputted entity ID (Available for Part/Face/Element only)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get thickness of the inputted entity ID (Available for Part/Face/Element only).

## Syntax

```psj
JPT.GetThicknessOfEntity(DItemType, entityID)
```

## Inputs

<!-- @since:5.0.1 @type:DItemType @required -->
### `DItemType`

- The _[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.

<!-- @since:5.0.1 @type:Integer @required -->
### `entityID`

- The ID of Part/Face/Element.

## Return Code

A _Double_ specifying the thickness of the target entity.

## Sample Code

```psj {25-28}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.012, 0.0, 0.0], strName="Cube _2", iPartColor=6149981)
Properties.Material.Add(strMaterialName="Structural _Steel", listMaterialProperty=[Density([(DENSITY, 7.85e-09)]),
    Elastic([(YOUNGS _MODULUS, 200000.0), (POISSONS _RATIO, 0.3)])])
Properties.Shell(crlTargets=[Face(26)], strName="Shell Property 1", iPropertyColor=16131973,
    crMatMembrane=Material(1), crMatBend=Material(1), crMatShear=Material(1), dMatOrient1=DFLT _DBL,
    dThickness=0.005, dBendStiff=DFLT _DBL, dThickRatio=DFLT _DBL, dNSM=DFLT _DBL, dFiberDist1=DFLT _DBL,
    dFiberDist2=DFLT _DBL, dPlateOff=DFLT _DBL, iItgPts=DFLT _INT)
Properties.Shell(crlTargets=[Face(52)], strName="Shell Property 2", iPropertyId=2, iPropertyColor=7010958,
    crMatMembrane=Material(1), crMatBend=Material(1), crMatShear=Material(1), dMatOrient1=DFLT _DBL,
    dThickness=0.01, dBendStiff=DFLT _DBL, dThickRatio=DFLT _DBL, dNSM=DFLT _DBL, dFiberDist1=DFLT _DBL,
    dFiberDist2=DFLT _DBL, dPlateOff=DFLT _DBL, iItgPts=DFLT _INT)
Properties.Shell(crlTargets=[Face(22)], strName="Shell Property 3", iPropertyId=3, iPropertyColor=3962802,
    crMatMembrane=Material(1), crMatBend=Material(1), crMatShear=Material(1), dMatOrient1=DFLT _DBL,
    dThickness=0.015, dBendStiff=DFLT _DBL, dThickRatio=DFLT _DBL, dNSM=DFLT _DBL, dFiberDist1=DFLT _DBL,
    dFiberDist2=DFLT _DBL, dPlateOff=DFLT _DBL, iItgPts=DFLT _INT)
Properties.Shell(crlTargets=[Face(48)], strName="Shell Property 4", iPropertyId=4, iPropertyColor=6396734,
    crMatMembrane=Material(1), crMatBend=Material(1), crMatShear=Material(1), dMatOrient1=DFLT _DBL,
    dThickness=0.02, dBendStiff=DFLT _DBL, dThickRatio=DFLT _DBL, dNSM=DFLT _DBL, dFiberDist1=DFLT _DBL,
    dFiberDist2=DFLT _DBL, dPlateOff=DFLT _DBL, iItgPts=DFLT _INT)
JPT.ViewFitToModel()

#Get all the existing connections
dThickness _1 = JPT.GetThicknessOfEntity(JPT.DItemType.FACE,26)
dThickness _2 = JPT.GetThicknessOfEntity(JPT.DItemType.FACE,52)
dThickness _3 = JPT.GetThicknessOfEntity(JPT.DItemType.FACE,22)
dThickness _4 = JPT.GetThicknessOfEntity(JPT.DItemType.FACE,48)
JPT.Debugger(dThickness _1)
JPT.Debugger(dThickness _2)
JPT.Debugger(dThickness _3)
JPT.Debugger(dThickness _4)
```
