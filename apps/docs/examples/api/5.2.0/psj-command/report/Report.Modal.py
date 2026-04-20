# Title:   Report.Modal()
# Desc:    Capture the image of the displayed modal result of the eigenvalue analysis at each frequency within the specified range, and automatically paste it into Microsoft Office PowerPoint
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/report/Report.Modal
# ---
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60, dEdgeAngle=60)

# Make Modal report
reportModal = Report.Modal(iResultInOnePage=2, dStartFrequency=10000.0, dEndFrequency=100000.0)  # [hl]
JPT.Debugger(reportModal)
