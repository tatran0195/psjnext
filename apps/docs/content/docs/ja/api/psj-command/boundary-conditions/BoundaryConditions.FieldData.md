---
title: "BoundaryConditions.FieldData()"
description: "Create a field data table that can be used when you set load, the boundary conditions, etc."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > FieldData"
macro _link: ""
---

## Description

Create a field data table that can be used when you set load, the boundary conditions, etc.

## Syntax

```psj
BoundaryConditions.FieldData(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of the table to be created.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iType

- Specify the type of table to be created.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### ilSheet

- Specify the table data.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing Field Data. If this parameter is used, the specified Field Data will be modified. If it is left _None_, a new Field Data will be created.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### bAbaqusAmp

- Specify whether the Abaqus amplitude is enabled or not.
- The default value is _False_ (Disabled).

<!-- @since:5.0.1 @optional -->
### iAmpType

- Specify the amplitude type.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bFrequencyPSDLogX

- Specify whether or not enable data interplation of LogX for Frequency-PSD table.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bFrequencyPSDLogY

- Specify whether or not enable data interplation of LogY for Frequency-PSD table.
- The default value is _False_.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {1-12}
created _lbc = BoundaryConditions.FieldData(strName="XYZ1",
                                           iType=1,
                                           ilSheet=[2,
                                                    4,
                                                    1,
                                                    1,
                                                    1,
                                                    10,
                                                    1,
                                                    2,
                                                    1,
                                                    20])

JPT.Debugger(created _lbc)
```
