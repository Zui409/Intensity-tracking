# Intensity-tracking
Track the change of fluorescence intensity of cells over time using TrackMate-StarDist in ImageJ.

Software
------------
ImageJ
Spyder (any pyhton IDE) 
ImageJ Plug-in: TrackMate-StarDist: https://imagej.net/plugins/trackmate/detectors/trackmate-stardist

Description
------------
StarDist offers an efficient model for segmenting nuclei in 2D fluorescence imaging, while TrackMate is a well-established software for tracking cell movement and calculating a variety of track characteristics. The latest version of the TrackMate plug-in in ImageJ integrates advanced segmentation models from StarDist as detectors, enabling precise tracking of cell movement. However, the plug-in does not provide information on intensity changes over time for individual tracks. To address this, we present simple ImageJ macro scripts along with a Python code to measure intensity changes over time for individual tracks.

Files
------------
The ImageJ macro script is for the intensity measurement of individual tracks over time.
The Python script is for tidying up the data and plotting figures. 

Instruction
------------
ImageJ: 
1. Open the image file for segmentation and tracking in ImageJ.
2. Select 'ImageJ -> Plugins -> Tracking -> TrackMate'.
3. Select StarDist dector and run the programme with parameters of your choice.
4. In the 'Select an action' window, execute 'Spot auto-naming', 'Trim non-visible data' and 'Export spots to IJ ROIs -> All spots' sequencially. The polygon ROIs of the segmented cells will be recored in the ROI manager. 
5. Record the number of identified ROIs from the TrackMate log 'Exporting (num) spots to ImageJ ROIs.'
6. Select 'ImageJ -> Plugins -> Macros -> Startup Marcros...' and open the ImageJ macro script (ending with .ijm).
7. Modify the NumROI and SavingDirectory and run the script. 

Python:
8. Install the required packages.
9. Specify the data folder that contains the .csv files from ImageJ and parameters of your choice.
10. Run the script in Spyder or other Python IDE.
