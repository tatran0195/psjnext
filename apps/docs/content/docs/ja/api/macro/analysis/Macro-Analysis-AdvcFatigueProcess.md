---
title: "AdvcFatigueProcess()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create ADVC fatigue process

## Syntax

```psj
AdvcFatigueProcess(string m _strName,bool m _bFatigue,int method,int stress _axis,
    int safety _type,double search _resolution,double safety _max,cursor m _crEdit,
    list m _LoadNodeList,list m _LoadCaseNodeList,list m _LoadNodeContactList,
    list m _OutputParamList,int m _iRefType,string m _strRefPath,list m _ReferenceResultList)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name of ADVC fatigue process

<!-- @since:5.0.1 -->
### 2. Bool

if fatigue parameter defined

<!-- @since:5.0.1 -->
### 3. Int

method\[-1:default; 0:Mises; 1:MaxDamage; 2:MaxDamageAllDir]

<!-- @since:5.0.1 -->
### 4. Int

stress axis\[-1:default; 0:Uniaxial; 1:Biaxial]

<!-- @since:5.0.1 -->
### 5. Int

safety type\[-1:default; 0:AmpMean; 1:Mean]

<!-- @since:5.0.1 -->
### 6. Double

search resolution

<!-- @since:5.0.1 -->
### 7. Double

safety max

<!-- @since:5.0.1 -->
### 8. Cursor

edit cursor

<!-- @since:5.0.1 -->
### 9. List

status of Loads

<!-- @since:5.0.1 -->
### 10. List

status of Load Cases

<!-- @since:5.0.1 -->
### 11. List

status and other data of Contacts

<!-- @since:5.0.1 -->
### 12. List

output parameters

<!-- @since:5.0.1 -->
### 13. Int

reference result type\[0:Temperature Load; 1:Stress]

<!-- @since:5.0.1 -->
### 14. String

path of reference result

<!-- @since:5.0.1 -->
### 15. List

data of reference result

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
AdvcFatigueProcess("Test",1,1,1,1,0.001,0.001,1:11,,,,,1,"Test",)
```
