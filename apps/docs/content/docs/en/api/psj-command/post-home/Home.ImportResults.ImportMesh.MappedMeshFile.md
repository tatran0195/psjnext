---
title: "Home.ImportResults.ImportMesh.MappedMeshFile()"
description: "Import a mapped mesh file to the Jupiter Database as Post document to add result to the mesh."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > ImportResults > ImportMesh > MappedMeshFile"
macro _link: "[ImportMappedMeshFileDat](../../macro/home/ImportMappedMeshFileDat)"
---

## Description

Import a mapped mesh file (\*.dat) to the Jupiter Database as Post document to add result to the mesh.

## Syntax

```psj
Home.ImportResults.ImportMesh.MappedMeshFile(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `strPath`

- The Mapped Mesh file path.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iImportType`

- The import type. For Mapped Mesh file, it is always set to 1.

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dFaceAngle`

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dEdgeAngle`

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Mapped Mesh file is imported successfully.
  - False: The Mapped Mesh file cannot be imported.

## Sample Code

```psj {4}
#Please set path to your sample mapped mesh file.
filepath="C:/Temp/SampleFrontISTR"

Home.ImportResults.ImportMesh.MappedMeshFile(filepath)
```
