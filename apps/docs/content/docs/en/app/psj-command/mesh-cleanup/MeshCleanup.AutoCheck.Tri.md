---
title: "MeshCleanup.AutoCheck.Tri()"
description: "Correct the surface mesh (TRI3/TRI6) by using multiple mesh quality standard"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "MeshCleanup > AutoCheck > Tri"
macro_link: ""
---

## Description

Correct the surface mesh (TRI3/TRI6) by using multiple mesh quality standard.

## Syntax

```psj
MeshCleanup.AutoCheck.Tri(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @required

- The targets to check mesh quality. The targets can be part or face.

### `bStretchCheck` @type(Boolean) @default(0)

- To check the Stretch quality.

### `bAspectRatioCheck` @type(Boolean) @default(0)

- To check Aspect Ratio quality.

### `bEdgeLengthCheck` @type(Boolean) @default(0)

- To check the Edge Length quality.

### `bAreaCheck` @type(Boolean) @default(0)

- To check the Area quality.

### `bNodeValenceCheck` @type(Boolean) @default(0)

- To check the Node Valence quality.

### `bInteriorAngleCheck` @type(Boolean) @default(0)

- To check Interior Angle quality.

### `bDuplicateElemsCheck` @type(Boolean) @default(0)

- To check Duplicated Elements.

### `dStretchLimit` @type(Double) @default(0.1)

- The threshold value of Stretch. The elements with a stretch value less than or equal to the specified value will be detected and displayed on the window.

### `dAspectRatioLimit` @type(Double) @default(10)

- The threshold value of Aspect Ratio. The elements with a stretch value greater than or equal to the specified value will be detected and displayed on the window.

### `dEdgeLengthLimit` @type(Double) @default(0.1)

- The threshold value of Edge Length. The elements with a stretch value less than or equal to the specified value will be detected and displayed on the window.

### `dAreaLimit` @type(Double) @default(0.01)

- The threshold value of Area. The elements with a stretch value less than or equal to the specified value will be detected and displayed on the window.

### `dNodeValenceLimit` @type(Double) @default(10)

- The threshold value of Node Valence. The elements with a stretch value greater than or equal to the specified value will be detected and displayed on the window.

### `dInteriorAngleLimit` @type(Double) @default(10)

- The threshold value of Interior Angle. The elements with a stretch value less than or equal to the specified value will be detected and displayed on the window.

## Return Code

A _Tuple_ specifying the elements's information that violated the mesh quality in order.
1\. Succeeded(1) or Failed(0)
2\. Number of error elements.
3\. A list of ID error elements.

## Sample Code

```psj {19-21}
# Prepare model
Geometry.Part.Cube(dlLength=[0.01, 0.01, 0.0001], 
                    ilAxialNodes=[10, 10, 2], 
                    iPartColor=7697908)
Meshing.SurfaceMeshing(crlParts=[Part(1)], 
                    surfaceMesh=SURFACE_MESH(
                        dAvgElemSize=0.001, 
                        dMinElemSize=0.0001, 
                        dGeomAngle=0.7853981634, 
                        dGeomMinSize=0.0001, 
                        dGradingFactor=0.5, 
                        iPerformanceMode=1, 
                        dAutoMergeTinyFacesAngle=0.5235987756, 
                        bGeomApprox=True, 
                        iNextEntityOffsetId=0), 
                        iThreadNum=16)

# Check mesh quality
result = MeshCleanup.AutoCheck.Tri(crlTargets=[Part(1)], 
                                bEdgeLengthCheck=True, 
                                dEdgeLengthLimit=0.0001)
if result[1] >=1:
    print("The number of error elements is " + str(result[1]))
    print("The error elements are " + str(result[2]))
else:
    print("There is no error element")
```
