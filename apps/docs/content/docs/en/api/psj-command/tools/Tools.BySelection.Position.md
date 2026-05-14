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

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iType`

- The type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMethod`

- The method.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iStartID`

- The start ID.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iIncrementStep`

- The increment step.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bAscending1`

- The ascending1.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bAscending2`

- The ascending2.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bAscending3`

- The ascending3.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSortFirst`

- The sort first.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iSortSecond`

- The sort second.

<!-- @since:5.0.1 @type:Integer @optional @default:2 -->
### `iSortThird`

- The sort third.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iEnableSortFirst`

- The enable sort first.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnableSortSecond`

- The enable sort second.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnableSortThird`

- The enable sort third.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iOffset1`

- The offset1.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iOffset2`

- The offset2.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iOffset3`

- The offset3.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dTol1`

- The tol1.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dTol2`

- The tol2.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dTol3`

- The tol3.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bSpecialFace`

- The special face.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {14-26}
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
