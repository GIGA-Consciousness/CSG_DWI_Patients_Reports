import matplotlib.pylab as plt 
from PIL import Image 

sub_dir = input("Images direcoty: ")

ctrl_dir = input("controls Directory: ")
    
img_TD_ctrl = Image.open(ctrl_dir+'/Top_Down.png')
bh = img_TD_ctrl.size[1]
img_TD_sub = Image.open(sub_dir+'/Top_Down.png')
perc = bh/float(img_TD_sub.size[1])
img_TD_sub = img_TD_sub.resize((int(img_TD_sub.size[0]*perc),bh),Image.ANTIALIAS)
final_TD = Image.new('RGB', (img_TD_ctrl.size[0]+img_TD_sub.size[0], bh))
offset = 0
final_TD.paste(img_TD_sub, (offset,0))
offset = offset + img_TD_sub.size[0]
final_TD.paste(img_TD_ctrl, (offset,0))
fig, ax = plt.subplots(1,1, subplot_kw={'aspect':'equal'})
ax.imshow(final_TD)
ax.set_title('           Sujet                  Controle', size=20, color='white', loc='left')
fig.savefig(sub_dir+'/result_TD.png', facecolor='black')

img_RL_ctrl = Image.open(ctrl_dir+'/Right_Left.png')
bh = img_RL_ctrl.size[1]
img_RL_sub = Image.open(sub_dir+'/Right_Left.png')
perc = bh/float(img_RL_sub.size[1])
img_RL_sub = img_RL_sub.resize((int(img_RL_sub.size[0]*perc),bh),Image.ANTIALIAS)
final_RL = Image.new('RGB', (img_RL_ctrl.size[0]+img_RL_sub.size[0], bh))
offset = 0
final_RL.paste(img_RL_sub, (offset,0))
offset = offset + img_RL_sub.size[0]
final_RL.paste(img_RL_ctrl, (offset,0))
fig, ax = plt.subplots(1,1, subplot_kw={'aspect':'equal'})
ax.imshow(final_RL)
ax.set_title('         Sujet                  Controle', size=20, color='white', loc='left')
fig.savefig(sub_dir+'/result_RF.png', facecolor='black')

img_LR_ctrl = Image.open(ctrl_dir+'/Left_Right.png')
bh = img_LR_ctrl.size[1]
img_LR_sub = Image.open(sub_dir+'/Left_Right.png')
perc = bh/float(img_LR_sub.size[1])
img_LR_sub = img_LR_sub.resize((int(img_LR_sub.size[0]*perc),bh),Image.ANTIALIAS)
final_LR = Image.new('RGB', (img_LR_ctrl.size[0]+img_LR_sub.size[0], bh))
offset = 0
final_LR.paste(img_LR_sub, (offset,0))
offset = offset + img_LR_sub.size[0]
final_LR.paste(img_LR_ctrl, (offset,0))
fig, ax = plt.subplots(1,1, subplot_kw={'aspect':'equal'})
ax.imshow(final_LR)
ax.set_title('         Sujet                  Controle', size=20, color='white', loc='left')
fig.savefig(sub_dir+'/result_LR.png', facecolor='black')

img_FB_ctrl = Image.open(ctrl_dir+'/Front_Back.png')
bh = img_FB_ctrl.size[1]
img_FB_sub = Image.open(sub_dir+'/Front_Back.png')
perc = bh/float(img_FB_sub.size[1])
img_FB_sub = img_FB_sub.resize((int(img_FB_sub.size[0]*perc),bh),Image.ANTIALIAS)
final_FB = Image.new('RGB', (img_FB_ctrl.size[0]+img_FB_sub.size[0], bh))
offset = 0
final_FB.paste(img_FB_sub, (offset,0))
offset = offset + img_FB_sub.size[0]
final_FB.paste(img_FB_ctrl, (offset,0))
fig, ax = plt.subplots(1,1, subplot_kw={'aspect':'equal'})
ax.imshow(final_FB)
ax.set_title('         Sujet                  Controle', size=20, color='white', loc='left')
fig.savefig(sub_dir+'/result_FB.png', facecolor='black')

img_BF_ctrl = Image.open(ctrl_dir+'/Back_Front.png')
bh = img_BF_ctrl.size[1]
img_BF_sub = Image.open(sub_dir+'/Back_Front.png')
perc = bh/float(img_BF_sub.size[1])
img_BF_sub = img_BF_sub.resize((int(img_BF_sub.size[0]*perc),bh),Image.ANTIALIAS)
final_BF = Image.new('RGB', (img_BF_ctrl.size[0]+img_BF_sub.size[0], bh))
offset = 0
final_BF.paste(img_BF_sub, (offset,0))
offset = offset + img_BF_sub.size[0]
final_BF.paste(img_BF_ctrl, (offset,0))
fig, ax = plt.subplots(1,1, subplot_kw={'aspect':'equal'})
ax.imshow(final_BF)
ax.set_title('         Sujet                  Controle', size=20, color='white', loc='left')
fig.savefig(sub_dir+'/result_BF.png', facecolor='black')
