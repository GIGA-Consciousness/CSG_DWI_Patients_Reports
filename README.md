## Codes for DTI analysis of the CSG clinical reports 

### Data Preparation

1. From the DICOM files extrct the structural image and save as `T1.mif`. Open a terminal in the dicom folder and type: 
```bash
mrconvert  dicom_folder T1.mif 
```
From the list check the number dedicated to the `t1_mp2rage_sag_p2_iso_FLAWS_fast2_INV2` sequence, type it and press `Enter`. you can check the image using `mrview`: 
```bash 
mrview T1.mif 
```

2. From the dicom files, concatenate the three shells of the dwi images and save it as `dwi.mif`. For that, in the terminal type: 
```bash 
mrcat . . . dwi.mif
```
Then it asks for the number dedicated to the first shell sequence. Write the dedicated number to the `ep2d_diff_mddw_30_p2_s4_b700_AP_DO_NOT_READJUST` and press `Enter`. 
Then it will ask for the numbers dedicated to the second and third shells accordingly. For the second shell, write the number dedicated to the `ep2d_diff_mddw_64_p2_s4_b1000_AP_DO_NOT_READJUST` and for the third shell, write the dedicated number to the `ep2d_diff_mddw_64_p2_s4_b2000_AP_DO_NOT_READJUST` sequences. After that, you can check the image using `mrview`: 
```bash
mrview dwi.mif
``` 

3. Correct the French special characters in the extracted files headers. For this purpose, we should open the mif files using any text reader software, correct for (not delete!!!!) the French special characters and save the files. As these files are big, the suggestion for the Linux users is to open the file in the terminal using `mc` package. In the terminal, write `mc` and in the new environment, for example open the `dwi.mif` file. In the CSG data, usually the problem is in the `e` letter with accents. These letters in the `mc` environment are shown with highlighted dots. You can replace these dots with a simple `e` letter and save the file. Do the same thing for the `T1.mif` file. 

### Running the Tractography Scripts 

1. Go to the folder that contains the scripts and open a terminal in that folder. 
2. In the terminal, run the script related to the tractography:
```bash 
bash DTI_Pipeline_Clinical.sh 
```
3. It then asks for the directory of the data. Copy and paste the directory that contains `dwi.mif` and `T1.mif` files and press `Enter`. If everything is done well, and the data are without problem, all the other steps will be done autonmatically and all the results will be saved in the same directory that the data exist. The final tractogram will be saved as `Allbrain.tck` file. The whole piplien will take around 1 to 2 hours.

4. After pipeline is finished, check the tracts using `mrview`. For that, 
    - open `mrview` and show the structural image: 
    ```bash 
    mrview T1.mif 
    ``` 
    - In the `Tool` tab select Tractography. 
    - Click the `Open Tractogram` icon and select the tractogram file and open it.
    - You will see the white matter tracts on the T1 image. Then you can change the view options in the `View` tab. For example, `Ortho view` will show the tractograms on the T1 in Sagital, Coronal, and Axial views. 
    - To visualize the tractogram as a whole brain, first in the `View` tab, select `Volume render`. Then in the `Tool` tab, select `View options`. And finally in the opened tab, click on the `Hide main image` icon. In the `Tool` tab, Select the `Tractography` and there you can adjust different parameters of the tracts such as their thickness, color code, opacity, etc. 

### Visualizing tracts using Trackvis and generating report images 

NOTE: Although we can generate report images using the `mrview`, CSG people prefer images of the `trackvis` software. So, we should generate desired images using this software! 

1. As `trackvis` cannot read `.tck` files, we should convert the tractogram file to a `.trk` format. In the scripts folder, there is a python script called `tck2trk.py` which does that. Simply open a terminal in the script folder and type: 
```bash 
python tck2trk.py 
``` 
It will ask you the directory which contains the `Allbrain.tck` file. Copy and paste the directory in the terminal and press `Enter`. It will automatically read the `Allbrain.tck` file and save the `Allbrain.trk` file in the same directory. 

 2. In the scripts folder, open the `dtk` folder and run the `trackvis` file to open the software. 

 3. Simply drag and drop the `Allbrain.trk` file into the software and the whole brain tracts will be shown. 
 
 4. In the right panel, in the `Property` box, 
    - set the `Annotation` to `off`.
    - set `Render` to `Tube`
    - Under the `Render`, set `Radius` to `0.2`

5. Manually put the tractogram in the different directional views (Righ2Left, Left2Right, Front2Back, Back2Front, and Top2Down) and take a screenshot (In linux you can use `Shutter` software for taking screenshots). Save each screenshots with proper names as follows:
    - Right_Left.png
    - Left_Right.png
    - Front_Back.png 
    - Back_Front.png 
    - Top_Down.png 

and put these files in a specific folder (for example the directory that all the other results also exist).

**NOTE:** If you think rotating the tractogram is lagging heavily, change the the `Render` to the `line`, rotate it easily, and change it back to `tube` before taking the screenshot. 

6. The next step is to put these images next to the images related to the control subject. Some control images and tractograms have been provided in the `Subj_ctrlF` (Female Control) and `Subj_ctrlM` (Male Control) folders. 
    - In the scripts folder, open a terminal and run the `pic_result.py` file: 
    ```bash 
    python pic_result.py
    ``` 
    - First it will ask you the directory where you put the subject tractogram images, and then it asks you the directory of a suitable control subject. Then it will automatically create the images you need for the report and will save them in the same directory that the subject images exist. 
     

