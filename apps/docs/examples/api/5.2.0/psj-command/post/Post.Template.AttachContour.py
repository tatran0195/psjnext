# Title:   Post.Template.AttachContour()
# Desc:    Attach the current contour settings to the specified template
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.Template.AttachContour
# ---
Post.Template.Create(strName="Contour_Template", strComment="Attach Contour Template")
template = Post.Template.AttachContour(strName="Contour_Template",   # [hl:start]
                                    postDataVizOptContour=POST_DATA_VIZ_OPT_CONTOUR(
                                        iColorDivision=20, 
                                        dMaxUser=0, 
                                        dMinUser=0))  # [hl:end]
JPT.Debugger(template)
