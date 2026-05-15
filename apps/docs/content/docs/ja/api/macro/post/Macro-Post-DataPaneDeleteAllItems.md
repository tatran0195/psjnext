---
title: "DataPaneDeleteAllItems()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Delete all items in specific pane of Watch Data Window.

## Syntax

```psj
DataPaneDeleteAllItems(int pane)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. int

Pane number. 1: Node, 2: Element, 3: Position, 3: Node Plot Scan, 4: Element Plot Scan, 5: Position Plot Scan, 6: Strain Gauge, 7: Peak Search, 8: Max/Min, 9: Area Max/Min, 10: Fatigue Strentgh, 11: Compare.

## Return Code

Nothing.

## Sample Code

```psj
DataPaneDeleteAllItems(1)
```
