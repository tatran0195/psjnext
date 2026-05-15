---
title: "AdvcRandomProcess()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create ADVC random response process

## Syntax

```psj
AdvcRandomProcess(string m _strName,string strRefEigenDir,double dRefLowFreq,
    double  dRefHighFreq,cursor crModalDampingRatio,cursor crExcitationFreq,
    Bool bAutoFreqInterval,double dMaxFreq,double dMinFreq,int iNumFreqPoint,
    double  dBiasParam,int iPropMethod,int iPSDtype,int iPSDdir,cursor crPSDLoad,
    double  dPSDFactor,double dGravityAccel,int iOutputEigenFreqStep,
    cursor m _crEdit,list m _LoadNodeList,list m _LoadCaseNodeList,
    list m _LoadNodeContactList,list m _OutputParamList,int m _iRefType,
    string m _strRefPath,list m _ReferenceResultList)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name of ADVC random response process

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
### 10. Int

Number Frequency Point

<!-- @since:5.0.1 -->
### 11. Double

Bias Parameter

<!-- @since:5.0.1 -->
### 12. Int

MultiPointExcitation\_Correlation\[0:Uncorrelated; 1:Correlated]

<!-- @since:5.0.1 -->
### 13. Int

PSD type\[0:Displacement; 1:Velocity; 2:Acceleration]

<!-- @since:5.0.1 -->
### 14. Int

PSD direction\[0:X; 1:Y; 2:Z]

<!-- @since:5.0.1 -->
### 15. Cursor

PSD Load

<!-- @since:5.0.1 -->
### 16. Double

PSD Amplitude\_Scale\_Factor

<!-- @since:5.0.1 -->
### 17. Double

Gravity Acceleration

<!-- @since:5.0.1 -->
### 18. Int

Output Frequency Step\[-1:default; 0:No; 1:Yes]

<!-- @since:5.0.1 -->
### 19. Cursor

edit cursor

<!-- @since:5.0.1 -->
### 20. List

status of Loads

<!-- @since:5.0.1 -->
### 21. List

status of Load Cases

<!-- @since:5.0.1 -->
### 22. List

status and other data of Contacts

<!-- @since:5.0.1 -->
### 23. List

output parameters

<!-- @since:5.0.1 -->
### 24. Int

reference result type\[0:Temperature Load; 1:Stress]

<!-- @since:5.0.1 -->
### 1. String

path of reference result

<!-- @since:5.0.1 -->
### 25. List

data of reference result

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
AdvcRandomProcess("Test",,0.001,0.001,1:11,1:11,1,0.001,0.001,1,0.001,
    1,1,1,1:11,0.001,0.001,1,1:11,,,,,1,"Test",)
```
