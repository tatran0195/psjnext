---
title: "Connections.BoltConnections.Edge.TypeB()"
description: "Create Lbc TypeB Bolt Edge method"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > BoltConnections > Edge > TypeB"
---

## Description

Create Lbc TypeB Bolt Edge method.

## Syntax

```psj
Connections.BoltConnections.Edge.TypeB(...)
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

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strBarName`

- The bar name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iShaftType`

- The shaft type.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCurBarProperty`

- The cur bar property.

<!-- @since:5.0.1 @type:Double @optional @default:20.0 -->
### `dPlaneTol`

- The plane tolerance.

<!-- @since:5.0.1 @type:Double @optional @default:100.0 -->
### `dMaxBoltHeight`

- The maximum bolt height.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bPretensionLoad`

- The pretension load.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSolverType`

- The solver type.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dForceValue`

- The force value.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPreTenDof`

- The pre ten dof.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCurCoord`

- The cur coordinate.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iBoltFixLength`

- The bolt fix length.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iTopSlot`

- The top slot.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dRBE1`

- The r e1.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dRBE2`

- The r e2.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dBotDtDia`

- The bot data dia.

<!-- @since:5.0.1 @type:Double @optional @default:10.0 -->
### `dPitch`

- The pitch.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iBotRbeConnType`

- The bot rbe conn type.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bIfCreate2ADVCStaticProcessForBoltFixLength`

- If create2 ADVC static process for bolt fix length.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.BoltConnections.Edge.TypeB(crlEdgeCur1, crlEdgeCur2, strRbeName="RBE", strBarName="", iShaftType=0, crCurBarProperty=None, dPlaneTol=20.0, dMaxBoltHeight=100.0, bPretensionLoad=False, iSolverType=0, dForceValue=0.0, iPreTenDof=0, crCurCoord=None, iBoltFixLength=0, iTopSlot=0, dRBE1=0.0, dRBE2=0.0, dBotDtDia=0.0, dPitch=10.0, iBotRbeConnType=0, bIfCreate2ADVCStaticProcessForBoltFixLength=False)
```
