---
title: "Geometry.Transform.Rotation()"
description: "Rotate given parts by the specified angle"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Transform > Rotation"
macro _link: "[RotateBody](../../macro/geometry/RotateBody)"
---

## Description

Rotate given parts by the specified angle.

## Syntax

```psj
Geometry.Transform.Rotation(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify the parts to be rotated.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### posCenter

- Specify the center position of rotation.
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### vecAxis

- Specify the axis of rotation.
- The default value is \[1,0,0].

<!-- @since:5.0.1 @optional -->
### dAngle

- Specify the rotation angle.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bCreateNewPart

- Specify whether to copy a new one and perform the transform operation.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bCopyLBC

- Specify whether to copy load boundary condition of the original part to rotation part. This argument will be ignored if _bCreateNewPart=False_.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bCopyProperty

- Specify the option that copy property of the original part to rotation part. This argument will be ignored if _bCreateNewPart=False_.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### iCopyCount

- Specify the number of copy parts. This argument will be ignored if _bCreateNewPart=False_.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### bMergeNode

- Specify whether to merge nodes between the original part and the transformed one. This argument will be ignored if _bCreateNewPart=False_.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### dTol

- Specify the merge tolerance. This argument should be specified when _bMergeNode=True_.
- The default value is 1.0e-5.

<!-- @since:5.1.0 @optional -->
### bCopyReference

- Specify whether to copy references from the existing part to the created parts or not.
- The default value is _False_.
-

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {3,4,5,6,7,8}
Geometry.Part.Cube()

rotate _status = Geometry.Transform.Rotation(crlParts=[Part(1)], 
                                            vecAxis=[0.0, 0.001, 0.0],
                                            dAngle=0.5,
                                            bCreateNewPart=True, 
                                            iCopyCount=3,
                                            dTol=1e-05)

JPT.Debugger(rotate _status)
```
