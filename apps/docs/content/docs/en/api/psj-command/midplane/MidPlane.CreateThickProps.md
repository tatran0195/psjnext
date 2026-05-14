---
title: "MidPlane.CreateThickProps()"
description: "create thickness properties for mid-plane"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MidPlane > CreateThickProps"
---

## Description

Create thickness properties for mid-plane

## Syntax

```psj
MidPlane.CreateThickProps(crlParts=[], dThickDiff=0.1, dMaxThick=DFLT _DBL, dMinThick=DFLT _DBL, crMatMembrane=None, crMatBend=None, crMatShear=None, crMatCoupl=None, iMatOrientType=0, dMatOrientX=DFLT _DBL, dMatOrientY=DFLT _DBL, dMatOrientZ=DFLT _DBL, crCoord=None, dThickness=DFLT _DBL, dBendStiff=DFLT _DBL, dThickRatio=1, dNSM=DFLT _DBL, dFiberDist1=DFLT _DBL, dFiberDist2=DFLT _DBL, dPlateOff=DFLT _DBL, iNumInterPts=0, bThickSetting=False, iEntityType=0, bDivideProp=False, crlRefPart=[])
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:Double @optional @default:0.1 -->
### `dThickDiff`

- The thickness difference.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMaxThick`

- The maximum thickness.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMinThick`

- The minimum thickness.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMatMembrane`

- The material membrane.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMatBend`

- The material bend.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMatShear`

- The material shear.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMatCoupl`

- The material couple.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMatOrientType`

- The material orient type.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMatOrientX`

- The material orient x.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMatOrientY`

- The material orient y.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMatOrientZ`

- The material orient z.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dThickness`

- The thickness.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dBendStiff`

- The bend stiff.

<!-- @since:5.0.1 @type:Double @optional @default:1 -->
### `dThickRatio`

- The thickness ratio.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dNSM`

- The n s m.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dFiberDist1`

- The fiber distance 1.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dFiberDist2`

- The fiber distance 2.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dPlateOff`

- The plate off.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iNumInterPts`

- The number inter pts.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bThickSetting`

- The thickness setting.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEntityType`

- The entity type.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDivideProp`

- The divide property.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlRefPart`

- The reference part.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlane.CreateThickProps(crlParts=[], dThickDiff=0.1, dMaxThick=DFLT _DBL, dMinThick=DFLT _DBL, crMatMembrane=None, crMatBend=None, crMatShear=None, crMatCoupl=None, iMatOrientType=0, dMatOrientX=DFLT _DBL, dMatOrientY=DFLT _DBL, dMatOrientZ=DFLT _DBL, crCoord=None, dThickness=DFLT _DBL, dBendStiff=DFLT _DBL, dThickRatio=1, dNSM=DFLT _DBL, dFiberDist1=DFLT _DBL, dFiberDist2=DFLT _DBL, dPlateOff=DFLT _DBL, iNumInterPts=0, bThickSetting=False, iEntityType=0, bDivideProp=False, crlRefPart=[])
```
