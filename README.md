# GoPro-Pi-Timelapser
Continuously saves timelapses from a GoPro to a Raspberry Pi that saves it to Google Drive


## Requirements

* [goprocam](https://github.com/KonradIT/gopro-py-api) 

* [PyDrive2](https://github.com/iterative/PyDrive2)

Update settings.yaml in the config folder with your Google Drive Credentials

## Installation

> pip install -r requirements.txt

## Design Plan

1. [x] Specify valid arguments for timelapse parameters (name of time lapse, length of frame interval), and Google Drive settings yaml

2. [ ] Create new folder in Google Drive to save new timelapse footage

3. [x] Start timelapse and save images to timelapse directory according to timer

4. [ ] On each save, upload to Google Drive on a new thread

