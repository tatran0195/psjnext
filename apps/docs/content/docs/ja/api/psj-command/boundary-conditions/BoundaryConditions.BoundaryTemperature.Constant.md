---
title: "BoundaryConditions.BoundaryTemperature.Constant()"
description: "Create a constant temperature load to part, face, edge or node. User inputs temperature in scalar or in a table format, then it will return temperature load to the specified location"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Boundary Conditions > Boundary Temperature > Constant"
---

## Description

Create a constant temperature load to part, face, edge or node. User inputs temperature in scalar or in a table format, then it will return temperature load to the specified location.

## Syntax

```psj
BoundaryConditions.BoundaryTemperature.Constant(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify name of the temperature load condition.
- The default value is "BoundaryTemperature\_1".

<!-- @since:5.0.1 @required -->
### dFTemp

- Specify the constant temperature value.

<!-- @since:5.0.1 @optional -->
### crTable

- Specify the table entered in the field data.
- The default value is _None_.

<!-- @since:5.0.1 @required -->
### crlTargets

- Specify the list of targets. Target can be face, edge or node.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing temperature load. If this parameter is used, the specified temperature load will be modified. If it is left _None_, a new temperature load will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {3,4,5}
Geometry.Part.Cube()

created _bcs = BoundaryConditions.BoundaryTemperature.Constant(strName="BoundaryTemperature _21",
                                                              dFTemp=373.15, 
                                                              crlTargets=[Face(21)])

JPT.Debugger(created _bcs)
```
