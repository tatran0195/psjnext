---
title: "AdvcModalFreqRespProcess()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create ADVC modal frequency response process

## Syntax

```psj
AdvcModalFreqRespProcess(string m _strName,string strRefEigenDir,double dRefLowFreq,
    double dRefHighFreq,Cursor crModalDampingRatio,Cursor crExcitationFreq,
    bool bAutoFreqInterval,double dMaxFreq,double dMinFreq,int iNumFreqPoint,
    double dBiasParam,Cursor m _crEdit,list m _LoadNodeList,list m _LoadCaseNodeList,
    list m _LoadNodeContactList,list m _OutputParamList,int m _iRefType,string m _strRefPath,
    list m _ReferenceResultList)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name of ADVC modal frequency response process

<!-- @since:5.0.1 -->
### 2. string

the path of result file

<!-- @since:5.0.1 -->
### 3. Double

refer low frequency

<!-- @since:5.0.1 -->
### 4. Double

refer high frequency

<!-- @since:5.0.1 -->
### 5. Cursor

modal damping ratio

<!-- @since:5.0.1 -->
### 6. Cursor

Excitation Frequencies

<!-- @since:5.0.1 -->
### 7. Bool

if auto frequency Interval

<!-- @since:5.0.1 -->
### 8. Double

Max Frequency

<!-- @since:5.0.1 -->
### 9. Double

Min Frequency

<!-- @since:5.0.1 -->
### 10 Int

Number Frequency Point

<!-- @since:5.0.1 -->
### 11. Double

Bias Parameter

<!-- @since:5.0.1 -->
### 12. Cursor

edit cursor

<!-- @since:5.0.1 -->
### 13. List

status of Loads

<!-- @since:5.0.1 -->
### 14. List

status of Load Cases

<!-- @since:5.0.1 -->
### 15. List

status and other data of Contacts

<!-- @since:5.0.1 -->
### 16. List

output parameters

<!-- @since:5.0.1 -->
### 17 Int

reference result type\[0:Temperature Load; 1:Stress]

<!-- @since:5.0.1 -->
### 18. String

path of reference result

<!-- @since:5.0.1 -->
### 19. List

data of reference result

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
AdvcModalFreqRespProcess("Test",,0.001,0.001,1:11,1:11,1,0.001,0.001,1,0.001,1:11,,,,,1,"Test",)
```
