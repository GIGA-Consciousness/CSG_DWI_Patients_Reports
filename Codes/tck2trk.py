import os
import argparse

import nibabel as nib
from nibabel.streamlines import Field
from nibabel.orientations import aff2axcodes

main_folder = input('Directory =')

anatomy = main_folder + '/T1.nii'
tractogram = main_folder + '/Allbrain.tck'

nii = nib.load(anatomy)
output_filename = tractogram[:-4] + '.trk'
header = {}
header[Field.VOXEL_TO_RASMM] = nii.affine.copy()
header[Field.VOXEL_SIZES] = nii.header.get_zooms()[:3]
header[Field.DIMENSIONS] = nii.shape[:3]
header[Field.VOXEL_ORDER] = "".join(aff2axcodes(nii.affine))
tck = nib.streamlines.load(tractogram)
nib.streamlines.save(tck.tractogram, output_filename, header=header)
