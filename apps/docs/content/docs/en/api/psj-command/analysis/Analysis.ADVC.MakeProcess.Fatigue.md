---
title: "Analysis.ADVC.MakeProcess.Fatigue()"
description: "Create ADVC fatigue process"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > ADVC > MakeProcess > Fatigue"
macro _link: "[AdvcFatigueProcess](../../macro/analysis/AdvcFatigueProcess)"
---

## Description

Create ADVC fatigue process.

## Syntax

```psj
Analysis.ADVC.MakeProcess.Fatigue(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bFatigue`

- The fatigue.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMethod`

- The method.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iStressAxis`

- The stress axis.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSafetyType`

- The safety type.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dSearchResolution`

- The search resolution.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dSafetyMax`

- The safety maximum.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

<!-- @since:5.0.1 @type:LOAD _NODE List @optional @default:[] -->
### `listLoadNode`

- The load node.

<!-- @since:5.0.1 @type:LOAD _CASE _NODE List @optional @default:[] -->
### `listLoadCaseNode`

- The load case node.

<!-- @since:5.0.1 @type:LOAD _NODE _CONTACT List @optional @default:[] -->
### `listLoadNodeContact`

- The load node contact.

<!-- @since:5.0.1 @type:List[Integer] @optional @default:[] -->
### `ilOutputParamList`

- The output param list.

<!-- @since:5.0.1 @type:Integer @optional @default:-1 -->
### `iRefType`

- The reference type.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strRefPath`

- The reference path.

<!-- @since:5.0.1 @type:ADVC _REF _STRESS _RESULT List @optional @default:[] -->
### `listAdvcRefStressResult`

- The advc reference stress result.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Analysis.ADVC.MakeProcess.Fatigue(strName="", bFatigue=False, iMethod=0, iStressAxis=0, iSafetyType=0, dSearchResolution=DFLT _DBL, dSafetyMax=DFLT _DBL, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])
```
