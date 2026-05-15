---
title: "AdvcTHProcess()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create ADVC heat transfer transient process

## Syntax

```psj
AdvcTHProcess(string m _strName,int end _type,double max _time,double steady _rate,
    int fixed _or _auto,double max _change,double init _dt,int define _max _dt,double max _dt,
    int define _min _dt,double min _dt,double fixed _dt,int output _last,int output _interval,
    int restart _last,int restart _interval,double output _time _interval,
    double restart _time _interval,int output _init,int list _output _interval,
    bool m _bConvergence,double cg _tol,double cg _nr _tol,double cg _disp _tol,
    double cg _nr _disp _tol,double cg _disp _limit _tol,double cg _total _disp _limit _tol,
    double newton _tol,double newton _disp _tol,double newton _disp _limit _tol,
    double newton _total _disp _limit _tol,int cgloop _max,int newton _max,
    double ht _nl _loop _tol,int ht _nl _loop _max,Cursor m _crEdit,list m _LoadNodeList,
    list m _LoadCaseNodeList,list m _LoadNodeContactList,list m _OutputParamList)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name of ADVC heat transfer transient process

<!-- @since:5.0.1 -->
### 2. Int

end type\[1:max time; 2:steady rate; 3:both]

<!-- @since:5.0.1 -->
### 3. Double

max time

<!-- @since:5.0.1 -->
### 4. Double

steady rate

<!-- @since:5.0.1 -->
### 5. Int

fixed or auto type\[0:auto; 1:fixed]

<!-- @since:5.0.1 -->
### 6. Double

max change temp

<!-- @since:5.0.1 -->
### 7. Double

init dt time

<!-- @since:5.0.1 -->
### 8. Int

if define max dt\[0:false; 1:true]

<!-- @since:5.0.1 -->
### 9. Double

max dt time

<!-- @since:5.0.1 -->
### 10. Int

if define min dt\[0:false; 1:true]

<!-- @since:5.0.1 -->
### 11. Double

min dt time

<!-- @since:5.0.1 -->
### 12. Double

fixed dt time

<!-- @since:5.0.1 -->
### 13. Int

output last\[-1:default; 0:No; 1:Yes]

<!-- @since:5.0.1 -->
### 14. Int

output interval

<!-- @since:5.0.1 -->
### 15. Int

restart last\[-1:default; 0:No; 1:Yes]

<!-- @since:5.0.1 -->
### 16. Int

restart interval

<!-- @since:5.0.1 -->
### 17. Double

output time interval

<!-- @since:5.0.1 -->
### 18. Double

restart time interval

<!-- @since:5.0.1 -->
### 19. Int

output initial result\[-1:default; 0:No; 1:Yes]

<!-- @since:5.0.1 -->
### 20. Int

list output interval

<!-- @since:5.0.1 -->
### 21. Bool

if convergence parameter defined

<!-- @since:5.0.1 -->
### 22. Double

cg\_tol

<!-- @since:5.0.1 -->
### 23. Double

cg\_nr\_tol

<!-- @since:5.0.1 -->
### 24. Double

cg\_disp\_tol

<!-- @since:5.0.1 -->
### 25. Double

cg\_nr\_disp\_tol

<!-- @since:5.0.1 -->
### 26. Double

cg\_disp\_limit\_tol

<!-- @since:5.0.1 -->
### 27. Double

cg\_total\_disp\_limit\_tol

<!-- @since:5.0.1 -->
### 28. Double

newton\_tol

<!-- @since:5.0.1 -->
### 29. Double

newton\_disp\_tol

<!-- @since:5.0.1 -->
### 30. Double

newton\_disp\_limit\_tol

<!-- @since:5.0.1 -->
### 31. Double

newton\_total\_disp\_limit\_tol

<!-- @since:5.0.1 -->
### 32. Int

cgloop\_max

<!-- @since:5.0.1 -->
### 33. Int

newton\_max

<!-- @since:5.0.1 -->
### 34. Double

ht\_nl\_loop\_tol

<!-- @since:5.0.1 -->
### 35. Int

ht\_nl\_loop\_max

<!-- @since:5.0.1 -->
### 36. Cursor

edit cursor

<!-- @since:5.0.1 -->
### 137. List

status of Loads

<!-- @since:5.0.1 -->
### 38. List

status of Load Cases

<!-- @since:5.0.1 -->
### 39. List

status and other data of Contacts

<!-- @since:5.0.1 -->
### 40. List

output parameters

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
AdvcTHProcess("Test",1,0.001,0.001,1,0.001,0.001,1,0.001,1,0.001,0.001,1,1,1,1,0.001,0.001,
    1,1,1,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,1,1,0.001,1,1:11,,,,)
```
