---
title: "SetDefaultInitialTreeCondition()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Set initial show/hide setting of tree items.

## Syntax

```psj
SetDefaultInitialTreeCondition(bool AllParts, bool AllItems, bool LoadBCs, bool LocalMeshSettings, bool Connections, bool Coordinates, bool Contacts)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. bool

Display/hide all parts when a document opened.

- 0: Hide
- 1: Show

<!-- @since:5.1.0 -->
### 2. bool

Display/hide all items when a document opened.

- 0: Hide
- 1: Show

<!-- @since:5.1.0 -->
### 3. bool

Display/hide loads and BCs when a document opened.

- 0: Hide
- 1: Show

<!-- @since:5.1.0 -->
### 4. bool

Display/hide local mesh settings when a document opened.

- 0: Hide
- 1: Show

<!-- @since:5.1.0 -->
### 5. bool

Display/hide connections when a document opened.

- 0: Hide
- 1: Show

<!-- @since:5.1.0 -->
### 6. bool

Display/hide coordinates when a document opened.

- 0: Hide
- 1: Show

<!-- @since:5.1.0 -->
### 7. bool

Display/hide contacts when a document opened.

- 0: Hide
- 1: Show

## Return Code

No return code.

## Sample Code

```psj
SetDefaultInitialTreeCondition(0, 1, 0, 0, 0, 1, 1)
```
