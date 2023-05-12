import bpy, os, importlib
from os import listdir
from os.path import isfile, join

class TLM_NP_Filtering:

    image_output_destination = ""

    def init(self, denoise):

        scene = bpy.context.scene

        print("Beginning filtering for files: ")

        file_ending = "_denoised.hdr" if denoise else "_baked.hdr"
        dirfiles = [f for f in listdir(lightmap_dir) if isfile(join(lightmap_dir, f))]

        for file in dirfiles:

            if denoise:
                file_ending = "_denoised.hdr"
                file_split = 13
            else:
                file_ending = "_baked.hdr"
                file_split = 10

            if file.endswith(file_ending):

                file_input = os.path.join(self, file)
                os.chdir(self)

                #opencv_process_image = cv2.imread(file_input, -1)

                print(f"Filtering: {file_input}")

                print(os.path.join(self, file))

                #filter_file_output = os.path.join(lightmap_dir, file[:-file_split] + "_filtered.hdr")

                #cv2.imwrite(filter_file_output, opencv_bl_result)

                print(f"Written to: {filter_file_output}")