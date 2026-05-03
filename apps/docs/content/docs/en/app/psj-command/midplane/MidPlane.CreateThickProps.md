---
title: "MidPlane.CreateThickProps()"
description: "create thickness properties for mid-plane"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MidPlane > CreateThickProps"
---

## Description

Create thickness properties for mid-plane

## Syntax

```psj
MidPlane.CreateThickProps(crlParts=[], dThickDiff=0.1, dMaxThick=DFLT_DBL, dMinThick=DFLT_DBL, crMatMembrane=None, crMatBend=None, crMatShear=None, crMatCoupl=None, iMatOrientType=0, dMatOrientX=DFLT_DBL, dMatOrientY=DFLT_DBL, dMatOrientZ=DFLT_DBL, crCoord=None, dThickness=DFLT_DBL, dBendStiff=DFLT_DBL, dThickRatio=1, dNSM=DFLT_DBL, dFiberDist1=DFLT_DBL, dFiberDist2=DFLT_DBL, dPlateOff=DFLT_DBL, iNumInterPts=0, bThickSetting=False, iEntityType=0, bDivideProp=False, crlRefPart=[])
```

## Inputs

### `crlParts` @type(List\[Cursor]) @default(\[])

- The part.

### `dThickDiff` @type(Double) @default(0.1)

- The thickness difference.

### `dMaxThick` @type(Double) @default(DFLT\_DBL)

- The maximum thickness.

### `dMinThick` @type(Double) @default(DFLT\_DBL)

- The minimum thickness.

### `crMatMembrane` @type(Cursor) @default(None)

- The material membrane.

### `crMatBend` @type(Cursor) @default(None)

- The material bend.

### `crMatShear` @type(Cursor) @default(None)

- The material shear.

### `crMatCoupl` @type(Cursor) @default(None)

- The material couple.

### `iMatOrientType` @type(Integer) @default(0)

- The material orient type.

### `dMatOrientX` @type(Double) @default(DFLT\_DBL)

- The material orient x.

### `dMatOrientY` @type(Double) @default(DFLT\_DBL)

- The material orient y.

### `dMatOrientZ` @type(Double) @default(DFLT\_DBL)

- The material orient z.

### `crCoord` @type(Cursor) @default(None)

- The coordinate.

### `dThickness` @type(Double) @default(DFLT\_DBL)

- The thickness.

### `dBendStiff` @type(Double) @default(DFLT\_DBL)

- The bend stiff.

### `dThickRatio` @type(Double) @default(1)

- The thickness ratio.

### `dNSM` @type(Double) @default(DFLT\_DBL)

- The n s m.

### `dFiberDist1` @type(Double) @default(DFLT\_DBL)

- The fiber distance 1.

### `dFiberDist2` @type(Double) @default(DFLT\_DBL)

- The fiber distance 2.

### `dPlateOff` @type(Double) @default(DFLT\_DBL)

- The plate off.

### `iNumInterPts` @type(Integer) @default(0)

- The number inter pts.

### `bThickSetting` @type(Boolean) @default(False)

- The thickness setting.

### `iEntityType` @type(Integer) @default(0)

- The entity type.

### `bDivideProp` @type(Boolean) @default(False)

- The divide property.

### `crlRefPart` @type(List\[Cursor]) @default(\[])

- The reference part.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlane.CreateThickProps(crlParts=[], dThickDiff=0.1, dMaxThick=DFLT_DBL, dMinThick=DFLT_DBL, crMatMembrane=None, crMatBend=None, crMatShear=None, crMatCoupl=None, iMatOrientType=0, dMatOrientX=DFLT_DBL, dMatOrientY=DFLT_DBL, dMatOrientZ=DFLT_DBL, crCoord=None, dThickness=DFLT_DBL, dBendStiff=DFLT_DBL, dThickRatio=1, dNSM=DFLT_DBL, dFiberDist1=DFLT_DBL, dFiberDist2=DFLT_DBL, dPlateOff=DFLT_DBL, iNumInterPts=0, bThickSetting=False, iEntityType=0, bDivideProp=False, crlRefPart=[])
```
