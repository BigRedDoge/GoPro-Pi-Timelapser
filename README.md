# GoPro-Pi-Timelapser
Continuously saves timelapses from a GoPro to a Raspberry Pi that saves it to Google Drive


## Requirements

* [goprocam](https://github.com/KonradIT/gopro-py-api) 

* [PyDrive2](https://github.com/iterative/PyDrive2)


Design Plan

1. Specify valid arguments for timelapse parameters (name of time lapse, length to record), and Google Drive config json

2. Create new folder in Google Drive to save new timelapse footage

3. Start timelapse and save images according to timer

4. On each save, upload to Google Drive on a new thread

