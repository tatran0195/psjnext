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

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlEdgeCur1`

- The edge cur1.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlEdgeCur2`

- The edge cur2.

<!-- @since:5.0.1 @type:String @optional @default:"RBE" -->
### `strRbeName`

- The rbe name.

<!-- @since:5.0.1 @type:Double @optional @default:20.0 -->
### `dPlaneTol`

- The plane tolerance.

<!-- @since:5.0.1 @type:Double @optional @default:100.0 -->
### `dMaxBoltHeight`

- The maximum bolt height.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iConnectionType`

- The connection type.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iCoincidentNodes`

- The coincident nodes.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dTolerance`

- The tolerance.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iGround`

- The ground.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dStiffnessX`

- The stiffness x.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dStiffnessY`

- The stiffness y.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dStiffnessZ`

- The stiffness z.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iLocalStiffUnit`

- The local stiff unit.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dRotateStiffX`

- The rotate stiff x.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dRotateStiffY`

- The rotate stiff y.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dRotateStiffZ`

- The rotate stiff z.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iLocalRotateStiffUnit`

- The local rotate stiff unit.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dDampCoef`

- The damp coefficient .

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dStressCoef`

- The stress coefficient .

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCurCoord`

- The cur coordinate.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iTopRbeType`

- The top rbe type.

<!-- @since:5.0.1 @type:Double @optional @default:10 -->
### `dTopPitch`

- The top pitch.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dTopRemoveDepth`

- The top remove depth.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iBotRbeType`

- The bot rbe type.

<!-- @since:5.0.1 @type:Double @optional @default:10 -->
### `dBotPitch`

- The bot pitch.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dBotRemoveDepth`

- The bot remove depth.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.BoltConnections.Edge.TypeC(crlEdgeCur1, crlEdgeCur2, strRbeName="RBE", dPlaneTol=20.0, dMaxBoltHeight=100.0, iConnectionType=0, iCoincidentNodes=1, dTolerance=0.0, iGround=0, dStiffnessX=0.0, dStiffnessY=0.0, dStiffnessZ=0.0, iLocalStiffUnit=0, dRotateStiffX=0.0, dRotateStiffY=0.0, dRotateStiffZ=0.0, iLocalRotateStiffUnit=0, dDampCoef=0.0, dStressCoef=0.0, crCurCoord=None, iTopRbeType=0, dTopPitch=10, dTopRemoveDepth=0.0, iBotRbeType=0, dBotPitch=10, dBotRemoveDepth=0.0)
```
