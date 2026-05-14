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

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strName`

- The name of the table to be created.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iType`

- The type of table to be created.

<!-- @since:5.0.1 @type:List[Integer] @optional @default:[] -->
### `ilSheet`

- The table data.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing Field Data. If this parameter is used, the specified Field Data will be modified. If it is left _None_, a new Field Data will be created.

<!-- @since:5.0.1 @type:Boolean @optional @default:False (Disabled) -->
### `bAbaqusAmp`

- Whether the Abaqus amplitude is enabled or not.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAmpType`

- The amplitude type.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bFrequencyPSDLogX`

- Whether or not enable data interplation of LogX for Frequency-PSD table.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bFrequencyPSDLogY`

- Whether or not enable data interplation of LogY for Frequency-PSD table.

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
