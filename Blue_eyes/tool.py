import os

filenames = os.listdir('image_css')

for i in filenames:
    os.remove('image_css/'+i+'/WM/')
    # print(i)
    # try:

    #     for j in os.listdir(os.getcwd()+'/image_css/'+i+'/WM'):
    #         try:
    #             print(j)
    #             os.rename('image_css/'+i+'/WM/'+j,'image_css/'+i+'/'+j)
    #         except:
    #             pass
    # except:
    #     pass
