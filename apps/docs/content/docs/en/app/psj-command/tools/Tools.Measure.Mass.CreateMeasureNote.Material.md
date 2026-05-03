---
title: "Tools.Measure.Mass.CreateMeasureNote.Material()"
description: "Create a Measure Note for Measure > Mass > By Material"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Tools > Measure > Mass > CreateMeasureNote > Material"
macro_link: "[CreateMeasureNoteMassByMaterial]"
---

## Description

Create a Measure Note for Measure > Mass > By Material

## Syntax

```psj
Tools.Measure.Mass.CreateMeasureNote.Material(...)
```

## Inputs

### `strNoteName` @type(String) @required

- The name of the created note.

### `crlParts` @type(List\[Cursor]) @required

- Parts.

### `dDensity` @type(Double) @required

- Density of material.

### `crCoordinate` @type(Cursor) @default(None)

- Local coordinate.

### `iFontSize` @type(Integer) @default(16)

- Font size.

### `iFontColor` @type(Integer) @default(0)

- Font color.

### `bBold` @type(Boolean) @default(False)

- Bold type or not.

### `iBackgroundColor` @type(Integer) @default(16777215)

- Background color.

### `iOutlineWidth` @type(Integer) @default(1)

- Outline width.

### `iOutlineColor` @type(Integer) @default(0)

- Outline color.

### `iArrowWidth` @type(Integer) @default(1)

- Arrow width.

### `iArrowColor` @type(Integer) @default(0)

- Arrow color.

### `iArrowType` @type(Integer) @default(1)

- Arrow type.
  - 0: None.
  - 1: Arrow.

### `iTitleType` @type(Integer) @default(1)

- Title type.
  - 0: None.
  - 1: Measure type.
  - 2: Name of note.

## Return Code

A _CursorStr_ specifying created note.

## Sample Code

```psj{40-43}
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
  strMaterialName="Copper_Alloy", 
  dictMaterialProperty={
    'Density': {
      'density': {'DENSITY': [8300.0]}}, 
    'Elastic': {
      'elastic': {
        'YOUNGS_MODULUS': [110000000000.0], 
        'POISSONS_RATIO': [0.34]}}, 
    }, iMaterialID=1, iMaterialColor=7901428)

Properties.Solid(
  crlTargets=[Part(1)], 
  strName="SolidProperty_1",
  iPropertyColor=16131973, 
  crMaterial=Material(1), 
  iCordM=-2, 
  dDynaRemeshVal1=DFLT_DBL, 
  dDynaRemeshVal2=DFLT_DBL, 
  dDispHG=DFLT_DBL, iFLG=-1)

#Create a Measure Note
Tools.Measure.Mass.CreateMeasureNote.Material(
    strNoteName="Mass1", 
    crlParts=[Part(1)], 
    dDensity=8300)
```
