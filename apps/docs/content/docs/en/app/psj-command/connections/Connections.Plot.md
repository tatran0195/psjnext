---
title: "Connections.Plot()"
description: "Create 1D plot connection"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Plot"
macro_link: "[Property1DPlot](../../macro/connections/Property1DPlot)"
---

## Description

Create 1D plot connection.

## Syntax

```psj
Connections.Plot(...)
```

## Inputs

### `strName` @type(String) @default("PLOT\_1")

- The name of the 1D plot connection to be created.

### `iPID` @type(Integer) @default(1)

- The ID of the 1D plot connection to be created.

### `crlTargets` @type(List\[Cursor])

- The list of the selected targets to set Nastran data plot. This targets can be bar part, 1D edge, element edge, or node.
- This is the require input.

### `crEdit` @type(Cursor) @default(None)

- An existing connection plot.
  - If this parameter is used, the specified connection plot will be modified.
  - If it is lef&#x74;_&#x4E;one_, a new connection plot will be created.

## Return Code

A _Cursor_ specifying the created or the modified connection.

## Sample Code

```psj {2}
Geometry.Part.Cube()
created_connection = Connections.Plot(crlTargets=[Edge(18)])
JPT.Debugger(created_connection)
```
