---
title: "Tools.BySelection.Position()"
description: "Renumber by position"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > BySelection > Position"
macro_link: "RenumberSpecify_byPosition"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Renumber by position

## Syntax

```psj
Tools.BySelection.Position(crlTargets=[], iType=0, iMethod=0, iStartID=1, iIncrementStep=1, bAscending1=True, bAscending2=False, bAscending3=False, iSortFirst=0, iSortSecond=1, iSortThird=2, iEnableSortFirst=1, iEnableSortSecond=0, iEnableSortThird=0, iOffset1=0, iOffset2=0, iOffset3=0, dTol1=0.0, dTol2=0.0, dTol3=0.0, crCoord=None, bSpecialFace=False)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `iType` @type(Integer) @default(0)

- The type.

### `iMethod` @type(Integer) @default(0)

- The method.

### `iStartID` @type(Integer) @default(1)

- The start ID.

### `iIncrementStep` @type(Integer) @default(1)

- The increment step.

### `bAscending1` @type(Boolean) @default(True)

- The ascending1.

### `bAscending2` @type(Boolean) @default(False)

- The ascending2.

### `bAscending3` @type(Boolean) @default(False)

- The ascending3.

### `iSortFirst` @type(Integer) @default(0)

- The sort first.

### `iSortSecond` @type(Integer) @default(1)

- The sort second.

### `iSortThird` @type(Integer) @default(2)

- The sort third.

### `iEnableSortFirst` @type(Integer) @default(1)

- The enable sort first.

### `iEnableSortSecond` @type(Integer) @default(0)

- The enable sort second.

### `iEnableSortThird` @type(Integer) @default(0)

- The enable sort third.

### `iOffset1` @type(Integer) @default(0)

- The offset1.

### `iOffset2` @type(Integer) @default(0)

- The offset2.

### `iOffset3` @type(Integer) @default(0)

- The offset3.

### `dTol1` @type(Double) @default(0.0)

- The tol1.

### `dTol2` @type(Double) @default(0.0)

- The tol2.

### `dTol3` @type(Double) @default(0.0)

- The tol3.

### `crCoord` @type(Cursor) @default(None)

- The coordinate.

### `bSpecialFace` @type(Boolean) @default(False)

- The special face.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj{14-26}
# model and environment settings
JPT.Exec('ViewShowID(1)')
Geometry.Part.Cube(ilAxialNodes=[4, 4, 4], iPartColor=7434735)
JPT.ViewFitToModel()

# show current node ids
curl_nodes=MainWindow.RightClick.AssociatedPick(crlInput=[Part(1)], strTarget="Node")
ditem_nodes=JPT.MacroListTCursorToListDItem(curl_nodes)

JPT.SelectionByIDs(JPT.DItemType.NODE, [ditem.id for ditem in ditem_nodes], True)
JPT.MessageBoxPSJ("Check current node IDs", JPT.MsgBoxType.MB_INFORMATION_OK)

# renumber nodes
Tools.BySelection.Position(
    crlTargets=[Node(*[ditem_node.id for ditem_node in ditem_nodes])],
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
curl_nodes=MainWindow.RightClick.AssociatedPick(crlInput=[Part(1)], strTarget="Node")
ditem_nodes=JPT.MacroListTCursorToListDItem(curl_nodes)
JPT.SelectionByIDs(JPT.DItemType.NODE, [ditem.id for ditem in ditem_nodes], True)
JPT.MessageBoxPSJ("Node IDs have changed and aligned.", JPT.MsgBoxType.MB_INFORMATION_OK)
```
