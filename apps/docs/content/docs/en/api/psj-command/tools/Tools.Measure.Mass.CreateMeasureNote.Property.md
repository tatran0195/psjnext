---
title: "Tools.Measure.Mass.CreateMeasureNote.Property()"
description: "Create a Measure Note for Measure > Mass > By Property"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Tools > Measure > Mass > CreateMeasureNote > Property"
macro _link: "[CreateMeasureNoteMassByProperty]"
---

## Description

Create a Measure Note for Measure > Mass > By Property

## Syntax

```psj
Tools.Measure.Mass.CreateMeasureNote.Property(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `strNoteName`

- The name of the created note.

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlParts`

- The parts.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crCoordinate`

- The local coordinate.

<!-- @since:5.1.0 @type:Integer @optional @default:16 -->
### `iFontSize`

- The font size.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iFontColor`

- The font color.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bBold`

- The bold type or not.

<!-- @since:5.1.0 @type:Integer @optional @default:16777215 -->
### `iBackgroundColor`

- The background color.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iOutlineWidth`

- The outline width.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iOutlineColor`

- The outline color.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iArrowWidth`

- The arrow width.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iArrowColor`

- The arrow color.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iArrowType`

- The arrow type.
  - 0: None.
  - 1: Arrow.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iTitleType`

- The title type.
  - 0: None.
  - 1: Measure type.
  - 2: Name of note.

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
Tools.Measure.Mass.CreateMeasureNote.Property(
  strNoteName="Mass1", 
  crlParts=[Part(1)])
```
