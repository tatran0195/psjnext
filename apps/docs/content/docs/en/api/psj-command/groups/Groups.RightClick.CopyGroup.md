---
title: "Groups.RightClick.CopyGroup()"
description: "Copy the inputted groups in the Group tree and paste them to a specified sub group"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Groups > RightClick > CopyGroup"
---

## Description

Copy the inputted groups in the Group tree and paste them to a specified sub group.

## Syntax

```psj
Groups.RightClick.CopyGroup(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlGroups`

- The list of group items uses for copying.

<!-- @since:5.0.1 @type:List[String] @optional @default:[] -->
### `strlNames`

- The list of new group names for the copied groups.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crSubGroup`

- The supper group destination if any.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bKeepOriginalGroup`

- The enable/disable the keeping original group.

<!-- @since:5.0.1 @type:Cursor @removed:5.1.0 @optional @deprecated @default:None -->
### `crSupperGroup`

- The supper group destination if any.

## Return Code

A _List of Cursor_ specifying all the pasted groups.

## Sample Code

```psj {12,13}
Geometry.Part.Cube()

Tools.Group.CreateGroup(strGroupName="Group1", 
                        crlTargets=[Face(22)])
Tools.Group.CreateGroup(strGroupName="Group2", 
                        crlTargets=[Face(24)])
Tools.Group.CreateGroup(strGroupName="Group3",
                        crlTargets=[Face(26)])

Groups.RightClick.AddSubGroup()

pasted _groups = Groups.RightClick.CopyGroup(crlGroups=[Group(1, 2, 3)], 
                                            crSubGroup=SubGroup(1))

JPT.Debugger(pasted _groups)
```
