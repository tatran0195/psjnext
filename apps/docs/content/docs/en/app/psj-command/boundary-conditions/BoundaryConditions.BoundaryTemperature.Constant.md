---
title: "BoundaryConditions.BoundaryTemperature.Constant()"
description: "Create a constant temperature load to part, face, edge or node. User inputs temperature in scalar or in a table format, then it will return temperature load to the specified location"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Boundary Conditions > Boundary Temperature > Constant"
---

## Description

Create a constant temperature load to part, face, edge or node. User inputs temperature in scalar or in a table format, then it will return temperature load to the specified location.

## Syntax

```psj
BoundaryConditions.BoundaryTemperature.Constant(...)
```

## Inputs

### `strName` @type(String) @default("BoundaryTemperature\_1")

- Name of the temperature load condition.

### `dFTemp` @type(Double) @required

- The constant temperature value.

### `crTable` @type(Cursor) @default(None)

- The table entered in the field data.

### `crlTargets` @type(List\[Cursor]) @required

- The list of targets. Target can be face, edge or node.

### `crEdit` @type(Cursor) @default(None)

- An existing temperature load. If this parameter is used, the specified temperature load will be modified. If it is lef&#x74;_&#x4E;one_, a new temperature load will be created.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {3,4,5}
Geometry.Part.Cube()

created_bcs = BoundaryConditions.BoundaryTemperature.Constant(strName="BoundaryTemperature_21",
                                                              dFTemp=373.15, 
                                                              crlTargets=[Face(21)])

JPT.Debugger(created_bcs)
```
