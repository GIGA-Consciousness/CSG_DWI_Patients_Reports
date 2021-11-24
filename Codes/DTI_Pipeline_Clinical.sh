#!/bin/bash

##### WARNING! This pipline is based on the FSL 5 (Old Version) and so is not optimized. So, do not use this pipline for the research purposes. It should be just used for the visualization of the tracts.##### 

# This is a pipeline to preprocess DWI images, perform tractography and save tractograms for further white matter tracts visualization of a single subject. 
# Developed by Sepehr Mortaheb for Coma Science Group (CSG), November 2021.  

# DWI and T1 images of a subject should be saved in a common directory as dwi.mif and T1.mif files respectively. 
 
# Here it asks for the directory of the files  
echo "Please enter the files directory:"  
read directory 
cd $directory/ 

dwifslpreproc dwi.mif dwi_den.mif \
              -pe_dir AP \
              -rpe_none  \
              -force


dwibiascorrect ants \
               dwi_den.mif dwi_den.mif \
              -force 

dwi2mask dwi_den.mif brain_mask.mif -force 


dwiextract dwi_den.mif -bzero - | mrmath -axis 3 - mean b0.nii -force
mrconvert T1.mif T1.nii -force  
flirt -dof 6       \
      -cost normmi \
      -in T1       \
      -ref b0      \
      -omat T_fsl.txt 
transformconvert T_fsl.txt T1.nii b0.nii flirt_import T_T1toDWI.txt -force \
               && rm T_fsl.txt                                      
mrtransform -linear                              \
            T_T1toDWI.txt T1.nii T1.nii \
            -force 

5ttgen fsl \
       T1.nii 5ttseg.mif\
       -force 

dwi2response dhollander dwi_den.mif wm_response.txt gm_response.txt csf_response.txt \
             -mask brain_mask.mif\
             -force 

dwi2fod msmt_csd\
 	-mask brain_mask.mif\
	dwi_den.mif\
	wm_response.txt wm.mif\
	gm_response.txt gm.mif\
	csf_response.txt csf.mif\
	-force 

mtnormalise wm.mif wm_norm.mif\
            gm.mif gm_norm.mif\
            csf.mif csf_norm.mif\
            -mask brain_mask.mif\
            -force 

tckgen wm.mif Allbrain.tck\
       -seed_dynamic wm.mif\
       -act 5ttseg.mif\
       -backtrack\
       -crop_at_gmwmi\
       -select 10000\
       -force

