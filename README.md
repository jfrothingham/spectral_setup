# spectral_setup

Personal project to visualize spectral window selection. Plot receiver ranges, spectral windows, and spectral lines on their own or as annotations to an existing spectral visualization.

Written and tested with the Green Bank Telescope (GBT) in mind, but intended to be generalizable. 

Plan to also incorporate validation of mode selection for the GBT's spectral line backend, VEGAS. 

## Workflow
Begin with a dictionary of spectral lines, with `key:value` pairs in the form `'name': frequency in GHz`
Decide on a VEGAS spectral line mode (options are numbers 1-29, as given in the GBT Proposer's and Observer's Guides)

Run function `lines_to_windows()` to validate against your desired VEGAS mode and produce a dictionary of spectral windows.
Run function `plot_obs()` to plot a visualization of the spectral windows.

### Notes
Function `rcvr_select()` determines which receiver range will include the desired spectral lines (or windows)
No support (yet!) for multi-bank VEGAS modes. You can use a workaround by defining a different spectral line dictionary for each bank.
You can manually create your own spectral window dictionary (bypassing `lines_to_windows()`). It will not undergo any validation. The dictionary must have `key:value` pairs in the form `'name': [center frequency in GHz, bandwidth in GHz]`
