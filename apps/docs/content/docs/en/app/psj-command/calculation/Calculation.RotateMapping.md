---
title: "Calculation.RotateMapping()"
description: "Copy (mapping) stress to create continuous stress data in the direction of rotation"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > RotateMapping"
macro_link: "[PostRotateMapping](../../macro/calculation/PostRotateMapping)"
---

## Description

Copy (mapping) stress to create continuous stress data in the direction of rotation.

## Syntax

```psj
Calculation.RotateMapping(...)
```

## Inputs

### `dAngleInterval` @type(Double) @default(7.5)

- The rotation angle in degree.

### `iRotateAxis` @type(Integer) @default(3)

- The selection of rotation axis.

### `iCoordinate` @type(Integer) @default(0)

- The coordinate reference.

### `iInterpolateType` @type(Integer) @default(1)

- The interpolation type when mapping.
  - 0: Nearest Node Interpolation
  - 1: Element Inside Interpolation

### `dAreaTolerance` @type(Double) @default(1)

- The value of area tolerance.

### `dMeshTolerance` @type(Double) @default(0.05)

- Value of mesh tolerance.

### `iRegionType` @type(Integer) @default(0)

- The region type to map the result.
  - 0: By Part
  - 1: By Group

### `crTarget` @type(Cursor) @required

- The target to map the result. The target can be part if RegionType = By Part, or solid element if RegionType = By Group.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {9}
# Please set path to your sample universal file and the exported file.
filePath="C:/Temp/Sample.unv"
exportPath = "C:/Temp/Unv_Export.unv"

# Import result file
Home.ImportResults.Universal(filePath)

# Rotate mapping
Calculation.RotateMapping(dAngleInterval=90.0, iRotateAxis=1, crTarget=Part(1))
# Export Unv file
Calculation.RotateMappingExportUnv(strPath=exportPath, 
                                    veclResultSet=[[105, 1001, 0], [105, 1001, 1], [105, 1001, 2], [105, 1001, 3]], 
                                    ilComponentUnv=[0, 2, 5, 1, 4, 3])
```
