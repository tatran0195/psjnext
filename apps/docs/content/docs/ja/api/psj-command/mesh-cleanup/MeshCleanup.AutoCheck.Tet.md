---
title: "MeshCleanup.AutoCheck.Tet()"
description: "Correct the solid mesh (TET4/TET10) by using multiple mesh quality standard"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MeshCleanup > AutoCheck > Tet"
macro _link: ""
---

## Description

Correct the solid mesh (TET4/TET10) by using multiple mesh quality standard.

## Syntax

```psj
MeshCleanup.AutoCheck.Tet(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### crlTargets

- Specify the targets to check mesh quality. The targets can only be part.

<!-- @since:5.1.0 @optional -->
### bStretchCheck

- Specify to check the Stretch quality.

- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bAspectRatioCheck

- Specify to check the Aspect Ratio quality.

- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bVolumeCheck

- Specify to check the Volume quality.

- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bJacobFactorCheck

- Specify to check the Jacobian Factor quality.

- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bTetCollapseCheck

- Specify to check the Tet collapse quality.

- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bTetSkewCheck

- Specify to check the Tet Skewness quality.

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
### dVolumeLimit

- Specify the threshold value of Volume. The elements with a stretch value less than or equal to the specified value will be detected and displayed on the window.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### dJacobFactorLimit

- Specify the threshold value of Jacobian Factor. The elements with a stretch value less than or equal to the specified value will be detected and displayed on the window.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### dTetCollapseLimit

- Specify the threshold value of Tet Collapse. The elements with a stretch value less than or equal to the specified value will be detected and displayed on the window.
- The default value is 0.05.

<!-- @since:5.1.0 @optional -->
### dTetSkewLimit

- Specify the threshold value of Tet Skewness. The elements with a stretch value greater than or equal to the specified value will be detected and displayed on the window.
- The default value is 0.9.

## Return Code

A _Tuple_ specifying the elements's information that violated the mesh quality in order.
1\. Succeeded(1) or Failed(0)
2\. Number of error elements.
3\. A list of ID error elements.

## Sample Code

```psj {17-19}
# Prepare model
Geometry.Part.Cube(dlLength=[0.01, 0.01, 0.0001], 
                    ilAxialNodes=[10, 10, 2], 
                    iPartColor=7697908)
JPT.Exec("View Fit To Model()")
Meshing.SolidMeshing(crlParts=[Part(1)], 
                    dGradingFactor=1.05, 
                    dStretchLimit=0.1, 
                    iSpeedVsQual=1, 
                    iRegion=1, 
                    bSafeMode=False, 
                    iParallel=16, 
                    bInternalMeshOnly=False, 
                    iPartColor=65280)

# Check mesh quality
result = MeshCleanup.AutoCheck.Tet(crlTargets=[Part(1)], 
                                    bTetSkewCheck=True, 
                                    dTetSkewLimit=0.9)
if result[1] >=1:
    print("The number of error elements is " + str(result[1]))
    print("The error elements are " + str(result[2]))
else:
    print("There is no error element")
```
