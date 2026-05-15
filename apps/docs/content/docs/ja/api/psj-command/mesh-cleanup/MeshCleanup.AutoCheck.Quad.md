---
title: "MeshCleanup.AutoCheck.Quad()"
description: "Correct the surface mesh (QUAD4/QUAD8) by using multiple mesh quality standards"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MeshCleanup > AutoCheck > Quad"
macro _link: ""
---

## Description

Correct the surface mesh (QUAD4/QUAD8) by using multiple mesh quality standards.

## Syntax

```psj
MeshCleanup.AutoCheck.Quad(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### crlTargets

- Specify the targets to check mesh quality. The targets can be part or face.

<!-- @since:5.1.0 @optional -->
### bStretchCheck

- Specify to check the Stretch quality.

- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bAspectRatioCheck

- Specify to check the Aspect Ratio quality.

- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bWarpingCheck

- Specify to check the Warping quality.

- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bSkewnessCheck

- Specify to check the Skewness quality.

- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bEdgeLengthCheck

- Specify to check the Edge Length quality.

- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bAreaCheck

- Specify to check the Area quality.

- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bNodeValenceCheck

- Specify to check the Node Valence quality.

- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bInteriorAngleCheck

- Specify to check Interior Angle quality.

- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bTaperCheck

- Specify to check Taper quality.

- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bDuplicateElemsCheck

- Specify to check Duplicated Elements.

- The default value is 0.

<!-- @since:5.1.0 @optional -->
### dStretchLimit

- Specify the threshold value of Stretch. The elements with a stretch value less than or equal to the specified value will be detected and displayed on the window.
- The default value is 0.1.

<!-- @since:5.1.0 @optional -->
### dAspectRatioLimit

- Specify the threshold value of Aspect Ratio. The elements with a stretch value greater than or equal to the specified value will be detected and displayed on the window.
- The default value is 10.

<!-- @since:5.1.0 @optional -->
### dWarpingLimit

- Specify the threshold value of Warping. The elements with a stretch value less than or equal to the specified value will be detected and displayed on the window.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### dSkewnessLimit

- Specify the threshold value of Skewness. The elements with a stretch value less than or equal to the specified value will be detected and displayed on the window.
- The default value is 70.

<!-- @since:5.1.0 @optional -->
### dEdgeLengthLimit

- Specify the threshold value of Edge Length. The elements with a stretch value less than or equal to the specified value will be detected and displayed on the window.
- The default value is 0.1.

<!-- @since:5.1.0 @optional -->
### dAreaLimit

- Specify the threshold value of Area. The elements with a stretch value less than or equal to the specified value will be detected and displayed on the window.
- The default value is 0.01.

<!-- @since:5.1.0 @optional -->
### dNodeValenceLimit

- Specify the threshold value of Node Valence. The elements with a stretch value greater than or equal to the specified value will be detected and displayed on the window.
- The default value is 10.

<!-- @since:5.1.0 @optional -->
### dInteriorAngleLimit

- Specify the threshold value of Interior Angle. The elements with a stretch value less than or equal to the specified value will be detected and displayed on the window.
- The default value is 10.

<!-- @since:5.1.0 @optional -->
### dTaperLimit

- Specify the threshold value of Tapper. The elements with a stretch value greater than or equal to the specified value will be detected and displayed on the window.
- The default value is 0.5.

## Return Code

A _Tuple_ specifying the elements's information that violated the mesh quality in order.
1\. Succeeded(1) or Failed(0)
2\. Number of error elements.
3\. A list of ID error elements.

## Sample Code

```psj {20-24}
# Prepare model
Geometry.Part.Cube(dlLength=[0.01, 0.01, 0.0001], 
                    ilAxialNodes=[10, 10, 2], 
                    iPartColor=7697908)
JPT.Exec("View Fit To Model()")
Meshing.SurfaceMeshing(crlParts=[Part(1)], 
                    surfaceMesh=SURFACE _MESH(
                        dMaxElemSize=0.005, 
                        dMinElemSize=0.005, 
                        dGeomAngle=0.7853981634, 
                        dGradingFactor=0.5, iPerformanceMode=1, 
                        dAutoMergeTinyFacesAngle=0.5235987756, 
                        bOutputQuadMesh=True, 
                        bGeomApprox=True, 
                        iNextEntityOffsetId=0), 
                        bFMesher=True, 
                        iThreadNum=16)

# Check mesh quality
result = MeshCleanup.AutoCheck.Quad(crlTargets=[Part(1)], 
                                    bStretchCheck=True, 
                                    bWarpingCheck=True, 
                                    dStretchLimit=0.1, 
                                    dWarpingLimit=0.0174533)
if result[1] >=1:
    print("The number of error elements is " + str(result[1]))
    print("The error elements are " + str(result[2]))
else:
    print("There is no error element")
```
