import os
import subprocess
import magic
import shutil

mime = magic.Magic(mime=True)
mkvmerge = "/usr/bin/mkvmerge"

# path = "/home/viru/LEARNING/python_learning/My_Projects/track_automation/test"

#* this is working function for extracting subtitle and audio track 
# subprocess.run([mkvmerge, '-o', outputpath + filename, '--audio-tracks', 'und,en,hi', '--subtitle-tracks', 'und,en,hi', myfile])

# todo - 1 get file list and check video type

def get_files(path):
    videofilelist = []
    
    #* one liner command
    # onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    # print(onlyfiles)
    
    if PATH_CHECK:
        print('Processing one file.')
        print(f'Moving file to temp directory - {path}')
        shutil.move(path, temp_path)
    
    else:
        for p in os.listdir(path):
            abspath = os.path.join(path, p)
            if os.path.isfile(abspath):
                if mime.from_file(abspath).startswith('video'):
                    print(f'Moving file to temp directory - {p}')
                    shutil.move(abspath, temp_path)
        
    for _ in os.listdir(temp_path):
        videofilelist.append(temp_path + '/' + _)
    
    videofilelist.sort()
    return videofilelist

# todo - 2 remove audio track and subtitle file.

def this_is_it(pathlst):
    if PATH_CHECK:
        filename = os.path.basename(pathlst[0])
        print(f'\nProcessing video - {filename}')
        print('*' * len(f'Processing video - {filename}'))
        subprocess.run([mkvmerge, '-o', path, '--audio-tracks', 'und,en,hi', '--subtitle-tracks', 'und,en,hi', pathlst[0]])
    
    else:
        pathlst_total = len(pathlst)
        for n, p in enumerate(pathlst,start=1):
            src_file_path = p
            filename = os.path.basename(src_file_path)
            dst_file_path = path + '/' + filename
            
            # print(f'src - {src_file_path}\ndst - {dst_file_path}')
            
            print(f'\nProcessing video - {filename}')
            print(f'({n}/{pathlst_total})')
            print('*' * len(f'Processing video - {filename}'))
            subprocess.run([mkvmerge, '-o', dst_file_path, '--audio-tracks', 'und,en,hi', '--subtitle-tracks', 'und,en,hi', src_file_path])



def main():
    global PATH_CHECK 
    global path
    global temp_path

    path = input('Please input path of directory :\n')

    #* checking path is file or directory. file - True, directory - False
    PATH_CHECK = os.path.isfile(path)

    if PATH_CHECK:
        temp_path = os.path.dirname(path) + '/temp'
        # print(f'file - {temp_path}')
    else:
        temp_path = path + '/temp'
        # print(f'directory - {temp_path}')

    if not os.path.exists(temp_path):
        print("\nCreating 'temp' directory.\n")
        os.mkdir(temp_path)
    else:
        print('temp path already exist. Please check...')
        quit()

    pathlst = get_files(path)
    print(pathlst)
    this_is_it(pathlst)

    ans = input("\nDo you want to clean temp files(Yes/y or 'No/n'): ")
    if ans in ['yes','Yes','Y','y']:
        print(f'Deleting - {temp_path}')
        shutil.rmtree(temp_path)

if __name__ == '__main__':
    main()