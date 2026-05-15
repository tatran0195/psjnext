---
title: "AdvcSpectrumProcess()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create ADVC response spectrum process

## Syntax

```psj
AdvcSpectrumProcess(string m _strName,string strRefEigenDir,double dRefLowFreq,
    double dRefHighFreq,int iPropMethod,int iSpttype,double dSptFactor[0],
    cursor crSpt[0],double dSptFactor[1],cursor crSpt[1],double dSptFactor[2],
    cursor crSpt[2],cursor m _crEdit,list m _LoadNodeList,list m _LoadCaseNodeList,
    list m _LoadNodeContactList,list m _OutputParamList,int m _iRefType,
    String m _strRefPath,list m _ReferenceResultList)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name of ADVC response spectrum process

<!-- @since:5.0.1 -->
### 2. String

the path of result file

<!-- @since:5.0.1 -->
### 3. Double

refer low frequency

<!-- @since:5.0.1 -->
### 4. Double

refer high frequency

<!-- @since:5.0.1 -->
### 5. Int

method\[0:ABS; 1:SRSS]

<!-- @since:5.0.1 -->
### 6. Int

spectrum type\[0:Displacement; 1:Velocity; 2:Acceleration]

<!-- @since:5.0.1 -->
### 7. Double

factor in CO x

<!-- @since:5.0.1 -->
### 8. Cursor

spectrum cursor in CO x

<!-- @since:5.0.1 -->
### 9. Double

factor in CO y

<!-- @since:5.0.1 -->
### 10. Cursor

spectrum cursor in CO y

<!-- @since:5.0.1 -->
### 11. Double

factor in CO z

<!-- @since:5.0.1 -->
### 12. Cursor

spectrum cursor in CO z

<!-- @since:5.0.1 -->
### 13. Cursor

edit cursor

<!-- @since:5.0.1 -->
### 14. List

status of Loads

<!-- @since:5.0.1 -->
### 15. List

status of Load Cases

<!-- @since:5.0.1 -->
### 16. List

status and other data of Contacts

<!-- @since:5.0.1 -->
### 17. List

output parameters

<!-- @since:5.0.1 -->
### 18. Int

reference result type\[0:Temperature Load; 1:Stress]

<!-- @since:5.0.1 -->
### 19. String

path of reference result

<!-- @since:5.0.1 -->
### 20. List

data of reference result

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
AdvcSpectrumProcess("Test",,0.001,0.001,1,1,0.001,1:11,0.001,1:11,0.001,1:11,1:11,,,,,1,"Test",)
```
