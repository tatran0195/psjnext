---
title: "Groups.RightClick.CopyGroup()"
description: "Copy the inputted groups in the Group tree and paste them to a specified sub group"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Groups > RightClick > CopyGroup"
---
<!-- REVIEW FLAGS — requires human review
   [param_removed_unexpectedly] Param 'crSupperGroup' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Copy the inputted groups in the Group tree and paste them to a specified sub group.

## Syntax

```psj
Groups.RightClick.CopyGroup(...)
```

## Inputs

### `crlGroups` @type(List\[Cursor]) @required

- The list of group items uses for copying.

### `strlNames` @type(List\[String]) @default(\[])

- The list of new group names for the copied groups.

### `crSubGroup` @type(Cursor) @default(None) @since(5.1.0)

- The supper group destination if any.

### `bKeepOriginalGroup` @type(Boolean) @default(False)

- Enable/disable the keeping original group.

### `crSupperGroup` @type(Cursor) @default(None) @deprecated @until(5.1.0)

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

pasted_groups = Groups.RightClick.CopyGroup(crlGroups=[Group(1, 2, 3)], 
                                            crSubGroup=SubGroup(1))

JPT.Debugger(pasted_groups)
```
