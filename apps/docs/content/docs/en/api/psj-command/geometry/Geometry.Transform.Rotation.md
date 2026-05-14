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

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlParts`

- The parts to be rotated.

<!-- @since:5.0.1 @type:List @optional @default:[0,0,0] -->
### `posCenter`

- The center position of rotation.

<!-- @since:5.0.1 @type:List @optional @default:[1,0,0] -->
### `vecAxis`

- The axis of rotation.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dAngle`

- The rotation angle.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCreateNewPart`

- Whether to copy a new one and perform the transform operation.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCopyLBC`

- Whether to copy load boundary condition of the original part to rotation part. This argument will be ignored if _bCreateNewPart=False_.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCopyProperty`

- The option that copy property of the original part to rotation part. This argument will be ignored if _bCreateNewPart=False_.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iCopyCount`

- The number of copy parts. This argument will be ignored if _bCreateNewPart=False_.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bMergeNode`

- Whether to merge nodes between the original part and the transformed one. This argument will be ignored if _bCreateNewPart=False_.

<!-- @since:5.0.1 @type:Double @optional @default:1.0e-5 -->
### `dTol`

- The merge tolerance. This argument should be specified when _bMergeNode=True_.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bCopyReference`

- Whether to copy references from the existing part to the created parts or not.
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
