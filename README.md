# Cluster_Mapping
 Sample program for cluster analysis



Originally written for the paper publish in J Wood Science.



> Imai, M., Mihashi, A., Imai, T. *et al.* Selective fluorescence labeling: time-lapse enzyme visualization during sugarcane hydrolysis. *J Wood Sci* **65,** 17 (2019). https://doi.org/10.1186/s10086-019-1798-0



Requires Pillow, Savitzky-Golay algorithm and kMeans (scikit-learn)



A series of time-lapse images during the treatment by enzyme with fluorescent labelling was used as input. Intensity (Gray level)  from the each pixel of sequential image was linked and considered as a time-lapse intensity profile in 2D space. Then the profiles are clustered by using Ward method (into 8 clusters) and each spatial point was colored by the corresponding cluster number that the point belongs.

