---
title: "BoundaryConditions.FieldData()"
description: "Create a field data table that can be used when you set load, the boundary conditions, etc."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > FieldData"
macro_link: ""
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a field data table that can be used when you set load, the boundary conditions, etc.

## Syntax

```psj
BoundaryConditions.FieldData(...)
```

## Inputs

### `strName` @type(String) @default("")

- The name of the table to be created.

### `iType` @type(Integer) @default(0)

- The type of table to be created.

### `ilSheet` @type(List\[Integer]) @default(\[])

- The table data.

### `crEdit` @type(Cursor) @default(None)

- An existing Field Data. If this parameter is used, the specified Field Data will be modified. If it is lef&#x74;_&#x4E;one_, a new Field Data will be created.

### `bAbaqusAmp` @type(Boolean) @default(False (Disabled))

- Whether the Abaqus amplitude is enabled or not.

### `iAmpType` @type(Integer) @default(0)

- The amplitude type.

### `bFrequencyPSDLogX` @type(Boolean) @default(False) @since(5.1.0)

- Whether or not enable data interplation of LogX for Frequency-PSD table.

### `bFrequencyPSDLogY` @type(Boolean) @default(False) @since(5.1.0)

- Whether or not enable data interplation of LogY for Frequency-PSD table.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {1-12}
created_lbc = BoundaryConditions.FieldData(strName="XYZ1",
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

JPT.Debugger(created_lbc)
```
