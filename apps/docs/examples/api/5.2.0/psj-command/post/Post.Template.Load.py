# Title:   Post.Template.Load()
# Desc:    Load the specified template in the template list to the current screen
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.Template.Load
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

# Load template
loadTemplate = Post.Template.Load(strName="Template_1")  # [hl]
JPT.Debugger(loadTemplate)
