---
title: "Connections.BoltConnections.Edge.TypeA()"
description: "Create Lbc TypeA Bolt Edge method"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > BoltConnections > Edge > TypeA"
---

## Description

Create Lbc TypeA Bolt Edge method.

## Syntax

```psj
Connections.BoltConnections.Edge.TypeA(...)
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
### strBarName

- Specify the bar name.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iShaftType

- Specify the shaft type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crCurBarProperty

- Specify the cur bar property.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### dPlaneTol

- Specify the plane tolerance.
- The default value is 20.0.

<!-- @since:5.0.1 @optional -->
### dMaxBoltHeight

- Specify the maximum bolt height.
- The default value is 100.0.

<!-- @since:5.0.1 @optional -->
### bPretensionLoad

- Specify the pretension load.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### iSolverType

- Specify the solver type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dForceValue

- Specify the force value.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iPreTenDof

- Specify the pre ten dof.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crCurCoord

- Specify the cur coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### iBoltFixLength

- Specify the bolt fix length.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iTopSlot

- Specify the top slot.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dRBE1

- Specify the r e1.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iBotSlot

- Specify the bot slot.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dRBE2

- Specify the r e2.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### bIsCreate2ADVCStaticProcessForFixLength

- Specify the is create2 ADVC static process for fix length.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.BoltConnections.Edge.TypeA(crlEdgeCur1, crlEdgeCur2, strRbeName="RBE", strBarName="", iShaftType=0, crCurBarProperty=None, dPlaneTol=20.0, dMaxBoltHeight=100.0, bPretensionLoad=False, iSolverType=0, dForceValue=0.0, iPreTenDof=0, crCurCoord=None, iBoltFixLength=0, iTopSlot=0, dRBE1=0.0, iBotSlot=0, dRBE2=0.0, bIsCreate2ADVCStaticProcessForFixLength=False)
```
