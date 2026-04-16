# Title:   Home.ExportPV
# Desc:    
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/home/Home.ExportPV
# ---
import os

program_path=JPT.GetAppPathInfo(JPT.PathType.PROGRAM_PATH)
temp_path=JPT.GetAppPathInfo(JPT.PathType.TEMP_PATH)

Home.ImportResults.Nastran(
    strPath=os.path.join(
        program_path, 
        'SampleData/PSJ/PSJ-Utility/PostSample/101_solid.op2')
)

Groups.RightClick.PropertyGroup()

Home.ExportGeometrySurface(strFolderName=temp_path)
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
                iResultPos=4), 
        postDataOp=PostDataOp(
            iResultLocation=1, 
            iOptionConversion=1, 
            iOptionContinuous=8)
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
            strResultCompName="Mises"))

Home.ExportPV(
    iGroupType=3, 
    strFileName=os.path.join(temp_path,'pv_test.tspv')
)
