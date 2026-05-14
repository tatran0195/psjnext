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

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlTargets`

- The target for surface remeshing. This target can be Parts, Faces, Edges, or Elements.

<!-- @since:5.0.1 @type:SURFACE _MESH @required -->
### `surfaceMesh`

- The mesh parameter.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bUseSetting`

- The to enable or disable the use of local setting. If this parameter is disabled (_False_), the existing local mesh settings will not be used.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bGrading`

- The to enable or disable the gradation of mesh. If enabled (_True_), surrounding faces will be remeshed together with the selected targets. If disabled (_False_), only selected targets will be remeshed.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bFMesher`

- The to enable or disable the use of F-mesher. F-mesher is a mesher to create only Quad4 elements. If`surfaceMesh` is set to create Tri3 element, this option does not have any effect.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iOverrideType`

- The mesh pattern type.
  - 0 (IsoMesh): Create isotropic mesh (structured mesh) on selected targets, if applicable.
  - 1 (FreeMesh): Create free mesh (unstructured mesh) on selected targets.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bKeepConnection`

- The to enable (_True_) or disable (_False_) the keeping of connection (boundary conditions) after meshing.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bProjCAD`

- The to enable (_True_) or disable (_False_) the projection of remeshed targets onto CAD models.

<!-- @since:5.0.1 @type:Boolean @optional -->
### `bIDcheck`

- The to enable or disable ID check when projecting.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bTinyFaceMerge`

- The to enable (_True_) or disable (_False_) the merge of tiny faces before remeshing. This option is equivalent to _[Geometry.MergeEntities.TinyFacesMerge](./../geometry/Geometry.MergeEntities.TinyFacesMerge)_.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dMinFaceWidth`

- The minimum face width. If`bTinyFaceMerge` is _True_, this parameter will be used to search for tiny faces.

<!-- @since:5.0.1 @type:Double @optional @default:0.001 -->
### `dMaxFaceWidth`

- The maximum face width. If`bTinyFaceMerge` is _True_, this parameter will be used to search for tiny faces.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bKeepRemeshEdge`

- The to enable (_True_) or disable (_False_) thee keeping of edges created when remeshing. This option only works when selected targets are Elements 2D. If disabled, the selected elements will be separated into new faces, new edges will also be created. If enabled, new faces and edges will not be created.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iGradingElem`

- The number of adjacent layers to be locally remeshed.

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
