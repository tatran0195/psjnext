---
title: "Connections.BoltConnections.Edge.TypeC()"
description: "Create Lbc TypeC Bolt Edge method"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > BoltConnections > Edge > TypeC"
---

## Description

Create Lbc TypeC Bolt Edge method.

## Syntax

```psj
Connections.BoltConnections.Edge.TypeC(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlEdgeCur1

- Specify the edge cur1.

<!-- @since:5.0.1 @required -->
### crlEdgeCur2

- Specify the edge cur2.

<!-- @since:5.0.1 @optional -->
### strRbeName

- Specify the rbe name.
- The default value is "RBE".

<!-- @since:5.0.1 @optional -->
### dPlaneTol

- Specify the plane tolerance.
- The default value is 20.0.

<!-- @since:5.0.1 @optional -->
### dMaxBoltHeight

- Specify the maximum bolt height.
- The default value is 100.0.

<!-- @since:5.0.1 @optional -->
### iConnectionType

- Specify the connection type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iCoincidentNodes

- Specify the coincident nodes.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### dTolerance

- Specify the tolerance.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iGround

- Specify the ground.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dStiffnessX

- Specify the stiffness x.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dStiffnessY

- Specify the stiffness y.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dStiffnessZ

- Specify the stiffness z.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iLocalStiffUnit

- Specify the local stiff unit.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dRotateStiffX

- Specify the rotate stiff x.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dRotateStiffY

- Specify the rotate stiff y.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dRotateStiffZ

- Specify the rotate stiff z.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iLocalRotateStiffUnit

- Specify the local rotate stiff unit.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dDampCoef

- Specify the damp coefficient .
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dStressCoef

- Specify the stress coefficient .
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### crCurCoord

- Specify the cur coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### iTopRbeType

- Specify the top rbe type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dTopPitch

- Specify the top pitch.
- The default value is 10.

<!-- @since:5.0.1 @optional -->
### dTopRemoveDepth

- Specify the top remove depth.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iBotRbeType

- Specify the bot rbe type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dBotPitch

- Specify the bot pitch.
- The default value is 10.

<!-- @since:5.0.1 @optional -->
### dBotRemoveDepth

- Specify the bot remove depth.
- The default value is 0.0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.BoltConnections.Edge.TypeC(crlEdgeCur1, crlEdgeCur2, strRbeName="RBE", dPlaneTol=20.0, dMaxBoltHeight=100.0, iConnectionType=0, iCoincidentNodes=1, dTolerance=0.0, iGround=0, dStiffnessX=0.0, dStiffnessY=0.0, dStiffnessZ=0.0, iLocalStiffUnit=0, dRotateStiffX=0.0, dRotateStiffY=0.0, dRotateStiffZ=0.0, iLocalRotateStiffUnit=0, dDampCoef=0.0, dStressCoef=0.0, crCurCoord=None, iTopRbeType=0, dTopPitch=10, dTopRemoveDepth=0.0, iBotRbeType=0, dBotPitch=10, dBotRemoveDepth=0.0)
```
