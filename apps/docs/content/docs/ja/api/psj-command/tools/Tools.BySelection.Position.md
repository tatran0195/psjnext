---
title: "Tools.BySelection.Position()"
description: "Renumber by position"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > BySelection > Position"
macro _link: "RenumberSpecify _byPosition"
---

## Description

Renumber by position

## Syntax

```psj
Tools.BySelection.Position(crlTargets=[], iType=0, iMethod=0, iStartID=1, iIncrementStep=1, bAscending1=True, bAscending2=False, bAscending3=False, iSortFirst=0, iSortSecond=1, iSortThird=2, iEnableSortFirst=1, iEnableSortSecond=0, iEnableSortThird=0, iOffset1=0, iOffset2=0, iOffset3=0, dTol1=0.0, dTol2=0.0, dTol3=0.0, crCoord=None, bSpecialFace=False)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iType

- Specify the type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iStartID

- Specify the start ID.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iIncrementStep

- Specify the increment step.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### bAscending1

- Specify the ascending1.
- The default value is True.

<!-- @since:5.0.1 @optional -->
### bAscending2

- Specify the ascending2.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### bAscending3

- Specify the ascending3.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### iSortFirst

- Specify the sort first.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iSortSecond

- Specify the sort second.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iSortThird

- Specify the sort third.
- The default value is 2.

<!-- @since:5.0.1 @optional -->
### iEnableSortFirst

- Specify the enable sort first.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iEnableSortSecond

- Specify the enable sort second.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iEnableSortThird

- Specify the enable sort third.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iOffset1

- Specify the offset1.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iOffset2

- Specify the offset2.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iOffset3

- Specify the offset3.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dTol1

- Specify the tol1.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dTol2

- Specify the tol2.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dTol3

- Specify the tol3.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### crCoord

- Specify the coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### bSpecialFace

- Specify the special face.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```pj {14-26}
# model and environment settings
JPT.Exec('ViewShowID(1)')
Geometry.Part.Cube(ilAxialNodes=[4, 4, 4], iPartColor=7434735)
JPT.ViewFitToModel()

# show current node ids
curl _nodes=MainWindow.RightClick.AssociatedPick(crlInput=[Part(1)], strTarget="Node")
ditem _nodes=JPT.MacroListTCursorToListDItem(curl _nodes)

JPT.SelectionByIDs(JPT.DItemType.NODE, [ditem.id for ditem in ditem _nodes], True)
JPT.MessageBoxPSJ("Check current node IDs", JPT.MsgBoxType.MB _INFORMATION _OK)

# renumber nodes
Tools.BySelection.Position(
    crlTargets=[Node(*[ditem _node.id for ditem _node in ditem _nodes])],
    iMethod=2, 
    bAscending2=True, 
    bAscending3=True, 
    iEnableSortSecond=1, 
    iEnableSortThird=1, 
    iOffset1=100, 
    iOffset2=1000, 
    iOffset3=1, 
    dTol1=1e-05, 
    dTol2=1e-05, 
    dTol3=1e-05)
    
# show renumbered node ids
curl _nodes=MainWindow.RightClick.AssociatedPick(crlInput=[Part(1)], strTarget="Node")
ditem _nodes=JPT.MacroListTCursorToListDItem(curl _nodes)
JPT.SelectionByIDs(JPT.DItemType.NODE, [ditem.id for ditem in ditem _nodes], True)
JPT.MessageBoxPSJ("Node IDs have changed and aligned.", JPT.MsgBoxType.MB _INFORMATION _OK)
```
