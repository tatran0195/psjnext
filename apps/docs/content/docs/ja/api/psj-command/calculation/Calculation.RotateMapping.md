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

<!-- @since:5.1.0 @optional -->
### dAngleInterval

- Specify the rotation angle in degree.
- The default value is 7.5.

<!-- @since:5.1.0 @optional -->
### iRotateAxis

- Specify the selection of rotation axis.
- The default value is 3.

<!-- @since:5.1.0 @optional -->
### iCoordinate

- Specify the coordinate reference.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iInterpolateType

- Specify the interpolation type when mapping.
  - 0: Nearest Node Interpolation
  - 1: Element Inside Interpolation
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### dAreaTolerance

- Specify the value of area tolerance.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### dMeshTolerance

- Specify value of mesh tolerance.
- The default value is 0.05.

<!-- @since:5.1.0 @optional -->
### iRegionType

- Specify the region type to map the result.
  - 0: By Part
  - 1: By Group
- The default value is 0.

<!-- @since:5.1.0 @required -->
### crTarget

- Specify the target to map the result. The target can be part if RegionType = By Part, or solid element if RegionType = By Group.

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
