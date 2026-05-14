---
title: "Home.ImportMesh.Universal()"
description: "Import an Universal file (*.unv) to the Jupiter Database (Mesh, boundary conditions, etc.)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Home > ImportMesh > Universal"
macro _link: "[ImportUnv](../../macro/home/ImportUnv)"
---

## Description

Import an Universal file (\*.unv) to the Jupiter Database (Mesh, boundary conditions, etc.).

## Syntax

```psj
Home.ImportMesh.Universal(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[String] @required -->
### `strlPaths`

- A list of the Universal files (\*.unv file) which will be used for importing.

<!-- @since:5.0.1 @type:String @removed:5.1.0 @required @deprecated -->
### `strPath`

- The path of the Universal file (\*.unv file) which will be used for importing.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Universal file (\*.unv file) is imported successfully.
  - False: The Universal file (\*.unv file) cannot be imported.

## Sample Code

```psj {19}
from os import environ

unv _file _path = environ["Temp"] + "/TechnoStar/Exported _Universal _File _EXPORT _unv.bdf"

Geometry.Part.Cube(ilAxialNodes=[3, 3, 3])
Meshing.SolidMeshing(crlParts=[Part(1)], bTet10=True, 
                    dGradingFactor=1.0, 
                    dStretchLimit=0.1, 
                    iSpeedVsQual=1, 
                    bSafeMode=False, 
                    iParallel=8, 
                    bInternalMeshOnly=False, 
                    iPartColor=65280)

Home.EXPORT _UNIVERSAL(strFileName=unv _file _path, crlParts=[Part(1)])

JPT.CreateNewDocument()

import _status = Home.ImportMesh.Universal(strlPaths=[unv _file _path])

JPT.Debugger(import _status)
```
