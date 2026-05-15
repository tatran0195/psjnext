---
title: "Tools.Measure.Mass.CreateMeasureNote.Material()"
description: "Create a Measure Note for Measure > Mass > By Material"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Tools > Measure > Mass > CreateMeasureNote > Material"
macro _link: "[CreateMeasureNoteMassByMaterial]"
---

## Description

Create a Measure Note for Measure > Mass > By Material

## Syntax

```psj
Tools.Measure.Mass.CreateMeasureNote.Material(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### strNoteName

- Specify the name of the created note.

<!-- @since:5.1.0 @required -->
### crlParts

- Specify parts.

<!-- @since:5.1.0 @required -->
### dDensity

- Specify density of material.

<!-- @since:5.1.0 @optional -->
### crCoordinate

- Specify local coordinate.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### iFontSize

- Specify font size.
- The default value is 16.

<!-- @since:5.1.0 @optional -->
### iFontColor

- Specify font color.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bBold

- Specify bold type or not.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### iBackgroundColor

- Specify background color.
- The default value is 16777215.

<!-- @since:5.1.0 @optional -->
### iOutlineWidth

- Specify outline width.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### iOutlineColor

- Specify outline color.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iArrowWidth

- Specify arrow width.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### iArrowColor

- Specify arrow color.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iArrowType

- Specify arrow type.
  - 0: None.
  - 1: Arrow.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### iTitleType

- Specify title type.
  - 0: None.
  - 1: Measure type.
  - 2: Name of note.
- The default value is 1.

## Return Code

A _CursorStr_ specifying created note.

## Sample Code

```psj {40-43}
#Preapre model
Geometry.Part.Cube(ilAxialNodes=[4, 4, 4], iPartColor=14903267)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

Meshing.SolidMeshing(
  crlParts=[Part(1)], 
  bTet10=True,
  dGradingFactor=1.05,
  dStretchLimit=0.1, 
  iSpeedVsQual=1, 
  iRegion=1, 
  bSafeMode=False, 
  iParallel=8, 
  bInternalMeshOnly=False,
  iPartColor=65280)

Properties.Material.Add(
  strMaterialName="Copper _Alloy", 
  dictMaterialProperty={
    'Density': {
      'density': {'DENSITY': [8300.0]}}, 
    'Elastic': {
      'elastic': {
        'YOUNGS _MODULUS': [110000000000.0], 
        'POISSONS _RATIO': [0.34]}}, 
    }, iMaterialID=1, iMaterialColor=7901428)

Properties.Solid(
  crlTargets=[Part(1)], 
  strName="SolidProperty _1",
  iPropertyColor=16131973, 
  crMaterial=Material(1), 
  iCordM=-2, 
  dDynaRemeshVal1=DFLT _DBL, 
  dDynaRemeshVal2=DFLT _DBL, 
  dDispHG=DFLT _DBL, iFLG=-1)

#Create a Measure Note
Tools.Measure.Mass.CreateMeasureNote.Material(
    strNoteName="Mass1", 
    crlParts=[Part(1)], 
    dDensity=8300)
```
