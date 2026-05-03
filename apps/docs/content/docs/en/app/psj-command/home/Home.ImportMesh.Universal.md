---
title: "Home.ImportMesh.Universal()"
description: "Import an Universal file (*.unv) to the Jupiter Database (Mesh, boundary conditions, etc.)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Home > ImportMesh > Universal"
macro_link: "[ImportUnv](../../macro/home/ImportUnv)"
---
<!-- REVIEW FLAGS — requires human review
   [param_rename_candidate] 'strlPaths' may be a rename of 'strPath' (78% similar)
     context: {"from":"strPath","to":"strlPaths","similarity":0.7777777777777778}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Import an Universal file (\*.unv) to the Jupiter Database (Mesh, boundary conditions, etc.).

## Syntax

```psj
Home.ImportMesh.Universal(...)
```

## Inputs

### `strlPaths` @type(List\[String]) @required @since(5.1.0)

- A list of the Universal files (\*.unv file) which will be used for importing.

### `strPath` @type(String) @required @deprecated @until(5.1.0)

- The path of the Universal file (\*.unv file) which will be used for importing.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Universal file (\*.unv file) is imported successfully.
  - False: The Universal file (\*.unv file) cannot be imported.

## Sample Code

```psj {19}
from os import environ

unv_file_path = environ["Temp"] + "/TechnoStar/Exported_Universal_File_EXPORT_unv.bdf"

Geometry.Part.Cube(ilAxialNodes=[3, 3, 3])
Meshing.SolidMeshing(crlParts=[Part(1)], bTet10=True, 
                    dGradingFactor=1.0, 
                    dStretchLimit=0.1, 
                    iSpeedVsQual=1, 
                    bSafeMode=False, 
                    iParallel=8, 
                    bInternalMeshOnly=False, 
                    iPartColor=65280)

Home.EXPORT_UNIVERSAL(strFileName=unv_file_path, crlParts=[Part(1)])

JPT.CreateNewDocument()

import_status = Home.ImportMesh.Universal(strlPaths=[unv_file_path])

JPT.Debugger(import_status)
```
