# Title:   WatchData.Toolbar.DeleteAll()
# Desc:    Deletes all or all data within the specified tab of the watch window.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/watch-data/WatchData.Toolbar.DeleteAll
# ---
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

#Run here to delete all notes.   # [hl:start]
#WatchData.Toolbar.DeleteAll()

#Run here to delete all notes on element.
#WatchData.Toolbar.DeleteAll(iTabIndex=1)  # [hl:end]

