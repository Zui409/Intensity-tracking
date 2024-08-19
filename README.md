# Intensity-tracking
Track the change of fluorescence intensity of cells over time using TrackMate-StarDist in ImageJ.

Software
------------
ImageJ, Spyder (any pyhton IDE) 
ImageJ Plug-in: TrackMate-StarDist: https://imagej.net/plugins/trackmate/detectors/trackmate-stardist

Description
------------
StarDist offers an efficient model for segmenting nuclei in 2D fluorescence imaging, while TrackMate is a well-established software for tracking cell movement and calculating a variety of track characteristics. The latest version of the TrackMate plug-in in ImageJ integrates advanced segmentation models from StarDist as detectors, enabling precise tracking of cell movement. However, the plug-in does not provide information on intensity changes over time for individual tracks. To address this, we present simple ImageJ macro scripts along with a Python code to measure intensity changes over time for individual tracks.

Files
------------
ImageJ macro scripts are for the intensity measurement of individual tracks over time.
The Python script is for tidying up the data and plotting figures. 
