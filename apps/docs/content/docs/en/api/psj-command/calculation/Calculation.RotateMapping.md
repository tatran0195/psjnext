---
title: "Calculation.RotateMapping()"
description: "Copy (mapping) stress to create continuous stress data in the direction of rotation"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > RotateMapping"
macro _link: "[PostRotateMapping](../../macro/calculation/PostRotateMapping)"
---

## Description

Copy (mapping) stress to create continuous stress data in the direction of rotation.

## Syntax

```psj
Calculation.RotateMapping(...)
```

## Inputs

<!-- @since:5.1.0 @type:Double @optional @default:7.5 -->
### `dAngleInterval`

- The rotation angle in degree.

<!-- @since:5.1.0 @type:Integer @optional @default:3 -->
### `iRotateAxis`

- The selection of rotation axis.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iCoordinate`

- The coordinate reference.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iInterpolateType`

- The interpolation type when mapping.
  - 0: Nearest Node Interpolation
  - 1: Element Inside Interpolation

<!-- @since:5.1.0 @type:Double @optional @default:1 -->
### `dAreaTolerance`

- The value of area tolerance.

<!-- @since:5.1.0 @type:Double @optional @default:0.05 -->
### `dMeshTolerance`

- The value of mesh tolerance.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iRegionType`

- The region type to map the result.
  - 0: By Part
  - 1: By Group

<!-- @since:5.1.0 @type:Cursor @required -->
### `crTarget`

- The target to map the result. The target can be part if RegionType = By Part, or solid element if RegionType = By Group.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {9}
# Please set path to your sample universal file and the exported file.
filePath="C:/Temp/Sample.unv"
exportPath = "C:/Temp/Unv _Export.unv"

# Import result file
Home.ImportResults.Universal(filePath)

# Rotate mapping
Calculation.RotateMapping(dAngleInterval=90.0, iRotateAxis=1, crTarget=Part(1))
# Export Unv file
Calculation.RotateMappingExportUnv(strPath=exportPath, 
                                    veclResultSet=[[105, 1001, 0], [105, 1001, 1], [105, 1001, 2], [105, 1001, 3]], 
                                    ilComponentUnv=[0, 2, 5, 1, 4, 3])
```
