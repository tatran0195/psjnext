---
title: "WatchData.Toolbar.DeleteAll()"
description: "Deletes all or all data within the specified tab of the watch window."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "WatchData > Toolbar > DeleteAll"
macro_link: ""
---

## Description

Deletes all or all data within the specified tab of the watch window.

## Syntax

```psj
WatchData.Toolbar.DeleteAll(...)
```

## Inputs

### `iTabIndex` @type(Integer) @default(-1)

- Tab.
  - -1: Deletes all data in all tabs of the watch window.
  - 0 :  Deletes all data in the Node tab.
  - 1 :  Deletes all data in the Element tab.
  - 2 :  Deletes all data in the Position tab.
  - 3 :  Deletes all data in the Node Plot Scan tab.
  - 4 :  Deletes all data in the Element Plot Scan tab.
  - 5 :  Deletes all data in the Position Plot Scan tab.
  - 6 :  Deletes all data in the Strain Gauge tab.
  - 7 :  Deletes all data in the PeakSearch tab.
  - 8 :  Deletes all data in the Max/Min tab.
  - 9 :  Deletes all data in the Area Max/Min tab.
  - 10 :  Deletes all data in the Fatigue Strength tab.
  - 11 :  Deletes all data in the Compare tab.
  - 12 :  Deletes all data in the Ustar tab.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj{47-51}
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"

Home.ImportResults.Nastran(
    strPath=samplePath
)

Post.ShowContour(
    crPostJob=TSVPostJob(1),
    lContourSettings=[
        PostContourSetting(
            postResultKey=PostResultKey(
                iAnalysisType=1,
                iResultSet=1,
                iTimeStep=1,
                strResultName="Stress",
                strResultCompName="Mises",
                iResultPos=4
            ),
            postDataOp=PostDataOp(
                iResultLocation=1,
                iOptionConversion=1,
                iOptionContinuous=8
            )
        )
    ]
)

Post.ShowDeformation(
    crPostJob=TSVPostJob(1),
    postResultKey=PostResultKey(
        iAnalysisType=1,
        iResultSet=1,
        iTimeStep=1,
        strResultName="Stress",
        strResultCompName="Mises"
    )
)

Post.Note.Node(
    crlTargets=[RONode(133, 111, 62)]
)

Post.Note.Element(
    crlTargets=[ROElem(410, 372)]
)

#Run here to delete all notes. 
#WatchData.Toolbar.DeleteAll()

#Run here to delete all notes on element.
#WatchData.Toolbar.DeleteAll(iTabIndex=1)
```
