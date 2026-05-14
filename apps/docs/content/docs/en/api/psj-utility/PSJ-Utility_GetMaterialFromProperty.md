---
title: "JPT.GetMaterialFromProperty()"
description: "Get the used material information (Name, ID, etc.) from the inputted property ID"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get the used material information (Name, ID, etc.) from the inputted property ID if it's exist.

## Syntax

```psj
JPT.GetMaterialFromProperty(propertyID)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @required -->
### `propertyID`

- The material property ID.

## Return Code

A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object containing information of the material using for the inputted property.

## Sample Code

```psj {20,27}
# Prepare model
Geometry.Part.Cube(iPartColor=7731061)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube _2", iPartColor=11908427)
JPT.ViewFitToModel()
Meshing.SolidMeshing(crlParts=[Part(2)], bTet10=True, dGradingFactor=1.05, dStretchLimit=0.1, iSpeedVsQual=1,
    iRegion=1, bSafeMode=False, iParallel=4, bInternalMeshOnly=False, iPartColor=65280)
Properties.Material.Add("Concrete", [Density([(DENSITY, 2.3e-09)]), Elastic([(YOUNGS _MODULUS, 30000.0),
    (POISSONS _RATIO, 0.18)])])
Properties.Material.Add("Magnesium _Alloy", [Density([(DENSITY, 1.8e-09)]), Elastic([(YOUNGS _MODULUS, 45000.0),
    (POISSONS _RATIO, 0.35)])])
Properties.Shell(crlTargets=[Face(26, 25)], strName="Shell Property 1", iPropertyColor=16131973,
    crMatMembrane=Material(1), crMatBend=Material(1), crMatShear=Material(1), dMatOrient1=DFLT _DBL,
    dThickness=0.001, dBendStiff=DFLT _DBL, dThickRatio=DFLT _DBL, dNSM=DFLT _DBL, dFiberDist1=DFLT _DBL,
    dFiberDist2=DFLT _DBL, dPlateOff=DFLT _DBL, iItgPts=DFLT _INT)
Properties.Solid(crlTargets=[Part(2)], strName="Solid Property 2", iPropertyId=2, iPropertyColor=4955455,
    crMaterial=Material(2), iCordM=-2, dDynaRemeshVal1=DFLT _DBL, dDynaRemeshVal2=DFLT _DBL, dDispHG=DFLT _DBL,
    iFLG=-1)

# Get material information of the property with ID = 1 (Shell)
dItemShellMat = JPT.GetMaterialFromProperty(1)
JPT.Debugger(dItemShellMat)
print("Applied material on shells: ")
print("--- Name: %s" %str(dItemShellMat.name))
print("--- ID: %s" %str(dItemShellMat.id))

# Get material information of the property with ID = 2 (Solid)
dItemSolidlMat = JPT.GetMaterialFromProperty(2)
JPT.Debugger(dItemSolidlMat)
print("Applied material on solid: ")
print("--- Name: %s" %str(dItemSolidlMat.name))
print("--- ID: %s" %str(dItemSolidlMat.id))
```
