---
title: "MeshCleanup.AutoCheck.TriQuad()"
description: "Correct the surface mesh (TRI3/TRI6/Quad4/Quad8) by using multiple mesh quality standards"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "MeshCleanup > AutoCheck > TriQuad"
macro_link: ""
---

## Description

Correct the surface mesh (TRI3/TRI6/Quad4/Quad8) by using multiple mesh quality standards.

## Syntax

```psj
MeshCleanup.AutoCheck.TriQuad(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @required

- The targets for checking the mesh qualities.

### `bStretchCheck` @type(Boolean) @default(False)

- Whether to check the Stretch quality.

### `bAspectRatioCheck` @type(Boolean) @default(False)

- Whether to check the Aspect Ratio quality.

### `bEdgeLengthCheck` @type(Boolean) @default(False)

- Whether to check the Edge Length quality.

### `bAreaCheck` @type(Boolean) @default(False)

- Whether to check the Area quality.

### `bNodeValenceCheck` @type(Boolean) @default(False)

- Whether to check the Node Valence quality.

### `bInteriorAngleCheck` @type(Boolean) @default(False)

- Whether to check the Interior Angle quality.

### `bDuplicateElemsCheck` @type(Boolean) @default(False)

- Whether to check the Duplicate Element quality.

### `dStretchLimitTri` @type(Double) @default(0)

- The threshold value of stretch to check for TRI elements. The elements with a stretch value less than or equal to the specified value will be detected and displayed on the window.

### `dAspectRatioLimitTri` @type(Double) @default(0.1)

- The threshold value of stretch to check for TRI elements. The elements with a stretch value greater than or equal to the specified value will be detected and displayed on the window.

### `dEdgeLengthLimitTri` @type(Double) @default(0)

- The threshold value of edge length to check for TRI elements. The elements with a edge length value less than or equal to the specified value will be detected and displayed on the window.

### `dAreaLimitTri` @type(Double) @default(0)

- The threshold value of area to check for TRI elements. The elements with a area value less than or equal to the specified value will be detected and displayed on the window.

### `dNodeValenceLimitTri` @type(Double) @default(0)

- The threshold value of node valence to check for TRI elements. The elements with a node valence value greater than or equal to the specified value will be detected and displayed on the window.

### `dInteriorAngleLimitTri` @type(Double) @default(0)

- The threshold value of interior angle to check for TRI elements. The elements with a interior angle value less than or equal to the specified value will be detected and displayed on the window.

### `dStretchLimitQuad` @type(Double) @default(0)

- The threshold value of stretch to check for QUAD elements. The elements with a stretch value less than or equal to the specified value will be detected and displayed on the window.

### `dAspectRatioLimitQuad` @type(Double) @default(0)

- The threshold value of aspect ratio to check for QUAD elements. The elements with a stretch value greater than or equal to the specified value will be detected and displayed on the window.

### `dEdgeLengthLimitQuad` @type(Double) @default(0)

- The threshold value of edge length to check for QUAD elements. The elements with a edge length value less than or equal to the specified value will be detected and displayed on the window.

### `dAreaLimitQuad` @type(Double) @default(0)

- The threshold value of area to check for QUAD elements. The elements with a area value less than or equal to the specified value will be detected and displayed on the window.

### `dNodeValenceLimitQuad` @type(Double) @default(0)

- The threshold value of node valence to check for QUAD elements. The elements with a node valence value greater than or equal to the specified value will be detected and displayed on the window.

### `dInteriorAngleLimitQuad` @type(Double) @default(0)

- The threshold value of interior angle to check for QUAD elements. The elements with a interior angle value less than or equal to the specified value will be detected and displayed on the window.

## Return Code

A _Tuple_ specifying the elements's information that violated the mesh quality in order.
1\. Succeeded(1) or Failed(0)
2\. Number of Tri error elements.
3\. Number of Quad error elements.
4\. A list of ID error elements.

## Sample Code

```psj {21-27}
# Prepare model
Geometry.Part.Trapezoid(dlLength=[0.01, 0.001, 0.01], 
                        dTopXLength=0.1, 
                        strName="Trapezoid_1", 
                        iPartColor=7697908)
JPT.Exec("View Fit To Model()")
Meshing.SurfaceMeshing(crlParts=[Part(1)], 
                    surfaceMesh=SURFACE_MESH(
                        dMaxElemSize=0.005, 
                        dMinElemSize=0.005, 
                        dGeomAngle=0.7853981634, 
                        dGeomMinSize=0.0001, 
                        dGradingFactor=0.5, 
                        iPerformanceMode=1, 
                        dAutoMergeTinyFacesAngle=0.5235987756, 
                        bOutputQuadMesh=True, 
                        bGeomApprox=True, 
                        iNextEntityOffsetId=0), bFMesher=True, iThreadNum=16)

# Check mesh quality
result = MeshCleanup.AutoCheck.TriQuad(crlTargets=[Part(1)], 
                                        bStretchCheck=True, 
                                        bEdgeLengthCheck=True, 
                                        dStretchLimitTri=0.1, 
                                        dEdgeLengthLimitTri=0.0001, 
                                        dStretchLimitQuad=0.1, 
                                        dEdgeLengthLimitQuad=0.0001)
if result[1] >= 1 and result[2] < 1:
    print("There is no Quad error element")
    print("The number of Tri error elements is " + str(result[1]))
    print("The error elements are " + str(result[3]))
elif result[1] < 1 and result[2] >= 1:
    print("There is no Tri error element")
    print("The number of Quad error elements is " + str(result[2]))
    print("The error elements are " + str(result[3]))
elif result[1] >= 1 and result[2] >= 1:
    print("The number of Tri error elements is " + str(result[1]))
    print("The number of Quad error elements is " + str(result[2]))
    print("The error elements are " + str(result[3]))
else:
    print("There is no Tri Quad error element")
```
