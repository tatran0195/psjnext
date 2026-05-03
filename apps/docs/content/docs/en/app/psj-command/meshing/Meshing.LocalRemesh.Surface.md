---
title: "Meshing.LocalRemesh.Surface()"
description: "Remesh the selected faces"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Meshing > LocalRemesh > Surface"
macro_link: "[LocalRemeshTriQuad](../../macro/meshing/LocalRemeshTriQuad)"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Remesh the selected faces.

## Syntax

```psj
Meshing.LocalRemesh.Surface(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @required

- The target for surface remeshing. This target can be Parts, Faces, Edges, or Elements.

### `surfaceMesh` @type(SURFACE\_MESH) @required

- The mesh parameter.

### `bUseSetting` @type(Boolean) @default(True)

- To enable or disable the use of local setting. If this parameter is disabled (_False_), the existing local mesh settings will not be used.

### `bGrading` @type(Boolean) @default(False)

- To enable or disable the gradation of mesh. If enabled (_True_), surrounding faces will be remeshed together with the selected targets. If disabled (_False_), only selected targets will be remeshed.

### `bFMesher` @type(Boolean) @default(False)

- To enable or disable the use of F-mesher. F-mesher is a mesher to create only Quad4 elements. If`surfaceMesh`is set to create Tri3 element, this option does not have any effect.

### `iOverrideType` @type(Integer) @default(1)

- The mesh pattern type.
  - 0 (IsoMesh): Create isotropic mesh (structured mesh) on selected targets, if applicable.
  - 1 (FreeMesh): Create free mesh (unstructured mesh) on selected targets.

### `bKeepConnection` @type(Boolean) @default(False)

- To enable (_True_) or disable (_False_) the keeping of connection (boundary conditions) after meshing.

### `bProjCAD` @type(Boolean) @default(True)

- To enable (_True_) or disable (_False_) the projection of remeshed targets onto CAD models.

### `bIDcheck` @type(Boolean)

- To enable or disable ID check when projecting.

### `bTinyFaceMerge` @type(Boolean) @default(False)

- To enable (_True_) or disable (_False_) the merge of tiny faces before remeshing. This option is equivalent t&#x6F;_[Geometry.MergeEntities.TinyFacesMerge](./../geometry/Geometry.MergeEntities.TinyFacesMerge)_.

### `dMinFaceWidth` @type(Double) @default(0)

- The minimum face width. If`bTinyFaceMerge`i&#x73;_&#x54;rue_, this parameter will be used to search for tiny faces.

### `dMaxFaceWidth` @type(Double) @default(0.001)

- The maximum face width. If`bTinyFaceMerge`i&#x73;_&#x54;rue_, this parameter will be used to search for tiny faces.

### `bKeepRemeshEdge` @type(Boolean) @default(False)

- To enable (_True_) or disable (_False_) thee keeping of edges created when remeshing. This option only works when selected targets are Elements 2D. If disabled, the selected elements will be separated into new faces, new edges will also be created. If enabled, new faces and edges will not be created.

### `iGradingElem` @type(Integer) @default(0) @since(5.1.0)

- The number of adjacent layers to be locally remeshed.

## Return Code

A _Boolean_ of _True_ if success, or _False_ if fail.

## Sample Code

```psj {3,4,5,6,7,8,9,10,11,12,13,14}
Geometry.Part.Cube()

creating_status = Meshing.LocalRemesh.Surface(crlTargets=[Face(26)], 
                                              surfaceMesh=SURFACE_MESH(dAvgElemSize=0.0005,
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

JPT.Debugger(creating_status)
```
