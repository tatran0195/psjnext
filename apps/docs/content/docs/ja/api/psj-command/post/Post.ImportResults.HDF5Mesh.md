---
title: "Post.ImportResults.HDF5Mesh()"
description: "import Nastran HDF5Mesh file"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Post > ImportResults > HDF5Mesh"
---

## Description

Import Nastran HDF5Mesh file

## Syntax

```psj
Post.ImportResults.HDF5Mesh(strlFilePaths, iImportType=2, dFaceAngle=60.0, dEdgeAngle=60.0)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strlFilePaths

- Specify the list of the paths of the HDF5 files.

<!-- @since:5.0.1 @optional -->
### iImportType

- Specify the import type.
- 0: Standard Nastran BDF - Import the BDF model geometry only.
- 1: Standard Nastran BDF by Property with 1D2D3D-Part - Import the BDF model geometry and material property. All material parts are applied to each part.
- 2: Standard Nastran BDF by Property with 1D-Edge,2D-Face,3D-Part - Import the BDF model geometry and material property. Parts are created for each material property. The 1D, 2D material properties are applied to edges or faces of a single part. 3D material properties are applied to each part. (Hollow 1D material properties are applied to each part.)
- The default value is 2.

<!-- @since:5.0.1 @optional -->
### dFaceAngle

- Specify the angle tolerance in order to determine the face division. Define a face by creating an edge between adjacent elements with an angle smaller than the specified value.
- The default value is 60.0.

<!-- @since:5.0.1 @optional -->
### dEdgeAngle

- Specify the angle tolerance in order to determine the edge division. Divide an edge by creating a vertex on adjacent edge elements with an angle larger than the specified value.
- The default value is 60.0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Post.ImportResults.HDF5Mesh("C:/Desktop/Hdf5Sample.h5")
```
