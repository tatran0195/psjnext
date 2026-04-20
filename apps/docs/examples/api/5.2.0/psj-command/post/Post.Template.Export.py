# Title:   Post.Template.Export()
# Desc:    Export the current template settings to a .xml file
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.Template.Export
# ---
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Create new Template
Post.Template.Create(strName="Template_1", strComment="")
Post.Template.AttachViewPoint(
    strName="Template_1", 
    postDataVizOptViewPoint=POST_DATA_VIZ_OPT_VIEWPOINT(
        dlCenter=[0.016, 0.005, 0.0025], 
        dScaleFactor=0.0349344))

# Export template
exportTemplate = Post.Template.Export(strPath="C:/temp/Template_1.xml")  # [hl]
JPT.Debugger(exportTemplate)
