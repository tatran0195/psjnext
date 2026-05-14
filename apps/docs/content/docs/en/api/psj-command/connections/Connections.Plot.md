---
title: "Connections.Plot()"
description: "Create 1D plot connection"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Plot"
macro _link: "[Property1DPlot](../../macro/connections/Property1DPlot)"
---

## Description

Create 1D plot connection.

## Syntax

```psj
Connections.Plot(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"PLOT _1" -->
### `strName`

- The name of the 1D plot connection to be created.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iPID`

- The ID of the 1D plot connection to be created.

<!-- @since:5.0.1 @type:List[Cursor] @optional -->
### `crlTargets`

- The list of the selected targets to set Nastran data plot. This targets can be bar part, 1D edge, element edge, or node.
- This is the require input.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing connection plot.
  - If this parameter is used, the specified connection plot will be modified.
  - If it is left _None_, a new connection plot will be created.

## Return Code

A _Cursor_ specifying the created or the modified connection.

## Sample Code

```psj {2}
Geometry.Part.Cube()
created _connection = Connections.Plot(crlTargets=[Edge(18)])
JPT.Debugger(created _connection)
```
