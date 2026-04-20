# Title:   Analysis.ExportAnsys()
# Desc:    Export Ansys Analysis Job
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/analysis/Analysis.ExportAnsys
# ---
Geometry.Part.Cube()

Analysis.Ansys.LinearStatic(strJobName="Job_1", iJobdataAnatype=1, iJobdataSoltype=3, strJobdataJobname="Job_1",
    bBasicdataBoutputdisplacements=True, bBasicdataBoutputstress=True, iLCId=1, dTransientdataFalpha=0.252506)

Analysis.ExportAnsys(strName="D:/Job_1.dat", crAnsysJob=AnsysJob(1))  # [hl]
