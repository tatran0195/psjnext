---
title: "Connections.BoltConnections.Edge.TypeA()"
description: "Create Lbc TypeA Bolt Edge method"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > BoltConnections > Edge > TypeA"
---

## Description

Create Lbc TypeA Bolt Edge method.

## Syntax

```psj
Connections.BoltConnections.Edge.TypeA(...)
```

## Inputs

### `crlEdgeCur1` @type(List\[Cursor]) @required

- The edge cur1.

### `crlEdgeCur2` @type(List\[Cursor]) @required

- The edge cur2.

### `strRbeName` @type(String) @default("RBE")

- The rbe name.

### `strBarName` @type(String) @default("")

- The bar name.

### `iShaftType` @type(Integer) @default(0)

- The shaft type.

### `crCurBarProperty` @type(Cursor) @default(None)

- The cur bar property.

### `dPlaneTol` @type(Double) @default(20.0)

- The plane tolerance.

### `dMaxBoltHeight` @type(Double) @default(100.0)

- The maximum bolt height.

### `bPretensionLoad` @type(Boolean) @default(False)

- The pretension load.

### `iSolverType` @type(Integer) @default(0)

- The solver type.

### `dForceValue` @type(Double) @default(0.0)

- The force value.

### `iPreTenDof` @type(Integer) @default(0)

- The pre ten dof.

### `crCurCoord` @type(Cursor) @default(None)

- The cur coordinate.

### `iBoltFixLength` @type(Integer) @default(0)

- The bolt fix length.

### `iTopSlot` @type(Integer) @default(0)

- The top slot.

### `dRBE1` @type(Double) @default(0.0)

- The r e1.

### `iBotSlot` @type(Integer) @default(0)

- The bot slot.

### `dRBE2` @type(Double) @default(0.0)

- The r e2.

### `bIsCreate2ADVCStaticProcessForFixLength` @type(Boolean) @default(False)

- The is create2 ADVC static process for fix length.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.BoltConnections.Edge.TypeA(crlEdgeCur1, crlEdgeCur2, strRbeName="RBE", strBarName="", iShaftType=0, crCurBarProperty=None, dPlaneTol=20.0, dMaxBoltHeight=100.0, bPretensionLoad=False, iSolverType=0, dForceValue=0.0, iPreTenDof=0, crCurCoord=None, iBoltFixLength=0, iTopSlot=0, dRBE1=0.0, iBotSlot=0, dRBE2=0.0, bIsCreate2ADVCStaticProcessForFixLength=False)
```
