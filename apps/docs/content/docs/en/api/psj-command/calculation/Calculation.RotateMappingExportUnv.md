---
title: "Calculation.RotateMappingExportUnv()"
description: "Save the mapped result to file (*unv)."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > RotateMappingExportUnv"
macro _link: ""
---

## Description

Save the mapped result to file (\*unv).

## Syntax

```psj
Calculation.RotateMappingExportUnv(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `strPath`

- The path of \*unv file to be saved.

<!-- @since:5.1.0 @type:List[Vector] @required -->
### `veclResultSet`

- The attribute of the results to be exported.

<!-- @since:5.1.0 @type:List[Integer] @optional @default:[0, 2, 5, 1, 4, 3] -->
### `ilComponentUnv`

- The universal components.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {11-13}
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
