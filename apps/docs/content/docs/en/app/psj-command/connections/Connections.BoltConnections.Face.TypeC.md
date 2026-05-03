---
title: "Connections.BoltConnections.Face.TypeC()"
description: "Create Lbc TypeC Bolt Face method"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > BoltConnections > Face > TypeC"
---

## Description

Create Lbc TypeC Bolt Face method.

## Syntax

```psj
Connections.BoltConnections.Face.TypeC(...)
```

## Inputs

### `crlFaceCur1` @type(List\[Cursor]) @required

- The face cur1.

### `crlFaceCur2` @type(List\[Cursor]) @required

- The face cur2.

### `strRbeName` @type(String) @default("RBE")

- The rbe name.

### `dPlaneTol` @type(Double) @default(20)

- The plane tolerance.

### `dMaxBoltHeight` @type(Double) @default(100)

- The maximum bolt height.

### `dMaxDiameter` @type(Double) @default(0)

- The maximum diameter.

### `dMinDiameter` @type(Double) @default(0)

- The minimum diameter.

### `iConnectionType` @type(Integer) @default(0)

- The connection type.

### `iCoincidentNodes` @type(Integer) @default(1)

- The coincident nodes.

### `dTolerance` @type(Double) @default(0.0)

- The tolerance.

### `iGround` @type(Integer) @default(0)

- The ground.

### `dStiffnessX` @type(Double) @default(0.0)

- The stiffness x.

### `dStiffnessY` @type(Double) @default(0.0)

- The stiffness y.

### `dStiffnessZ` @type(Double) @default(0.0)

- The stiffness z.

### `iLocalStiffUnit` @type(Integer) @default(0)

- The local stiff unit.

### `dRotateStiffX` @type(Double) @default(0.0)

- The rotate stiff x.

### `dRotateStiffY` @type(Double) @default(0.0)

- The rotate stiff y.

### `dRotateStiffZ` @type(Double) @default(0.0)

- The rotate stiff z.

### `iLocalRotateStiffUnit` @type(Integer) @default(0)

- The local rotate stiff unit.

### `dDampCoef` @type(Double) @default(0.0)

- The damp coefficient .

### `dStressCoef` @type(Double) @default(0.0)

- The stress coefficient .

### `crCurCoord` @type(Cursor) @default(None)

- The cur coordinate.

### `iTopRbeType` @type(Integer) @default(0)

- The top rbe type.

### `dTopPitch` @type(Double) @default(10)

- The top pitch.

### `dTopRemoveDepth` @type(Double) @default(0.0)

- The top remove depth.

### `iBotRbeType` @type(Integer) @default(0)

- The bot rbe type.

### `dBotPitch` @type(Double) @default(10)

- The bot pitch.

### `dBotRemoveDepth` @type(Double) @default(0.0)

- The bot remove depth.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.BoltConnections.Face.TypeC(crlFaceCur1, crlFaceCur2, strRbeName="RBE", dPlaneTol=20, dMaxBoltHeight=100, dMaxDiameter=0, dMinDiameter=0, iConnectionType=0, iCoincidentNodes=1, dTolerance=0.0, iGround=0, dStiffnessX=0.0, dStiffnessY=0.0, dStiffnessZ=0.0, iLocalStiffUnit=0, dRotateStiffX=0.0, dRotateStiffY=0.0, dRotateStiffZ=0.0, iLocalRotateStiffUnit=0, dDampCoef=0.0, dStressCoef=0.0, crCurCoord=None, iTopRbeType=0, dTopPitch=10, dTopRemoveDepth=0.0, iBotRbeType=0, dBotPitch=10, dBotRemoveDepth=0.0)
```
