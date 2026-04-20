# Title:   Post.Template.AttachVector()
# Desc:    Attach the current vector settings to the specified template
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.Template.AttachVector
# ---
Post.Template.Create(strName="Vector_Template", strComment="Attach Vector Template")
template = Post.Template.AttachVector(strName="Vector_Template",   # [hl:start]
                                    postDataVizOptVector=POST_DATA_VIZ_OPT_VECTOR(
                                        dRatioModel=0.05, 
                                        dRatioScreen=0.05))  # [hl:end]
JPT.Debugger(template)
