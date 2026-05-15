---
title: "Meshing.LocalRemesh.Surface()"
description: "Remesh the selected faces"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Meshing > LocalRemesh > Surface"
macro _link: "[LocalRemeshTriQuad](../../macro/meshing/LocalRemeshTriQuad)"
---

## Description

Remesh the selected faces.

## Syntax

```psj
Meshing.LocalRemesh.Surface(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlTargets

- Specify the target for surface remeshing. This target can be Parts, Faces, Edges, or Elements.

<!-- @since:5.0.1 @required -->
### surfaceMesh

- Specify the mesh parameter.

### `bUseSetting`

- A _Boolean_ to enable or disable the use of local setting. If this parameter is disabled (_False_), the existing local mesh settings will not be used.
- The default value is _True_.

### `bGrading`

- A _Boolean_ to enable or disable the gradation of mesh. If enabled (_True_), surrounding faces will be remeshed together with the selected targets. If disabled (_False_), only selected targets will be remeshed.
- The default value is _False_.

### `bFMesher`

- A _Boolean_ to enable or disable the use of F-mesher. F-mesher is a mesher to create only Quad4 elements. If `surfaceMesh` is set to create Tri3 element, this option does not have any effect.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### iOverrideType

- Specify the mesh pattern type.
  - 0 (IsoMesh): Create isotropic mesh (structured mesh) on selected targets, if applicable.
  - 1 (FreeMesh): Create free mesh (unstructured mesh) on selected targets.
- The default value is 1.

### `bKeepConnection`

- A _Boolean_ to enable (_True_) or disable (_False_) the keeping of connection (boundary conditions) after meshing.
- The default value is _False_.

### `bProjCAD`

- A _Boolean_ to enable (_True_) or disable (_False_) the projection of remeshed targets onto CAD models.
- The default value is _True_.

### `bIDcheck`

- A _Boolean_ to enable or disable ID check when projecting.

### `bTinyFaceMerge`

- A _Boolean_ to enable (_True_) or disable (_False_) the merge of tiny faces before remeshing. This option is equivalent to _[Geometry.MergeEntities.TinyFacesMerge](./../geometry/Geometry.MergeEntities.TinyFacesMerge)_.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### dMinFaceWidth

- Specify the minimum face width. If`bTinyFaceMerge` is _True_, this parameter will be used to search for tiny faces.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dMaxFaceWidth

- Specify the maximum face width. If`bTinyFaceMerge` is _True_, this parameter will be used to search for tiny faces.
- The default value is 0.001.

### `bKeepRemeshEdge`

- A _Boolean_ to enable (_True_) or disable (_False_) thee keeping of edges created when remeshing. This option only works when selected targets are Elements 2D. If disabled, the selected elements will be separated into new faces, new edges will also be created. If enabled, new faces and edges will not be created.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### iGradingElem

- Specify the number of adjacent layers to be locally remeshed.
- The default value is 0.

## Return Code

A _Boolean_ of _True_ if success, or _False_ if fail.

## Sample Code

```psj {3,4,5,6,7,8,9,10,11,12,13,14}
Geometry.Part.Cube()

creating _status = Meshing.LocalRemesh.Surface(crlTargets=[Face(26)], 
                                              surfaceMesh=SURFACE _MESH(dAvgElemSize=0.0005,
                                                                       dMaxElemSize=0.001, 
                                                                       dMinElemSize=0.0001, 
                                                                       dGeomAngle=0.7853981853, 
                                                                       iPerformanceMode=1,
                                                                       dAutoMergeTinyFacesAngle=0.5235987902, 
                                                                       bLocalRemesh=True, 
                                                                       iNextEntityOffsetId=8985, 
                                                                       iNextElemOffsetId=2601),
                                              bGrading=True, 
                                              iOverrideType=0)

JPT.Debugger(creating _status)
```
