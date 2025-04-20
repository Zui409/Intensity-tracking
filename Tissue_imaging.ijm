
for (i = 1; i <8; i++) {

dir = "D:/Debasis/Tissue/2025-04-19_Analysis/0400054B control/image"+i+"/";
File.openSequence(dir, " filter=ch02");
run("Z Project...", "projection=[Max Intensity]");
saveAs("Tiff", "D:/Debasis/Tissue/2025-04-19_Analysis/Control_Analysis/Zproject_Series"+i+".tif");
run("Duplicate...", " ");
run("8-bit");
//setAutoThreshold("Default dark no-reset");
run("Threshold...");
setThreshold(20, 255);
setOption("BlackBackground", true);
run("Convert to Mask");
//run("Close");
saveAs("Tiff", "D:/Debasis/Tissue/2025-04-19_Analysis/Diluted_Analysis/Zproject_Series"+i+"_Threshold20.tif");
close();
close();
close();
}