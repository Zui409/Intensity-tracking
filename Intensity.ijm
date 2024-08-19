//For measuring the intensity of segmented cells.

//Before running this script, you need to record the total number of segmented ROI. (See Github instructions)
//Note: If you have to re-run this script, you will have to close the current ROI manager
//      and export the ROIs again in the TrackMate window.

NumROI = 5516
SaveDirectory = "D:/Debasis"    // Result folder

for (i=0; i<NumROI;i++){
	roiManager("Select", i);
	Roi.getPosition(channel, slice, frame);
	//IJ.log(frame);
    RoiManager.setPosition(frame); 
    roiManager("Set Line Width", 0);
	run("Measure");  
	}
run("Clear Results"); // The first time 'Measure' does not give you the correct measurements so we have to clear them.
for (i=0; i<NumROI;i++){
	roiManager("Select", i);
	run("Measure");  // This time is correct.
	}
saveAs("Results", SaveDirectory + "/Results.csv");  // Save intensity measurements
roiManager("List");
saveAs("Results", SaveDirectory +"/ROI.csv");  // Save ROI info
IJ.log("Comleted");
