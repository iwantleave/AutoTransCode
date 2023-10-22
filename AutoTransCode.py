import os
import subprocess
import time

def get_filelist(file_path):
    file_list = os.listdir(file_path)
    file_list.sort()
    return file_list

def run_ffmpeg(ffmpeg_path,input_file,output_file):
    ffmpeg_cmd = ffmpeg_path + " -i " + input_file + " -c:v hevc_qsv -global_quality 25 -preset medium -profile:v main -tag:v hvc1 -c:a aac -b:a 128k " + output_file
    print(ffmpeg_cmd)
    result = subprocess.Popen(ffmpeg_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,encoding='gbk',text=True)
    for line in result.stdout:
        print(line)
        time.sleep(0.1)
    result.wait()
    if result.poll()==0:
        print("success")
    else:
        print("error")

if __name__ == '__main__':
    ffmpeg_path = "D:\\jobs\\ffmpeg\\ffmpeg.exe"
    second_filelist = get_filelist('D:\\trans_code\\second')
    first_filelist = get_filelist('D:\\trans_code\\first')
    print(second_filelist)
    print(first_filelist)
    wait_trans_code = list(set(first_filelist)-set(second_filelist))
    print("waiting for transcode", wait_trans_code)

    for i in wait_trans_code:
        run_ffmpeg(ffmpeg_path,"D:\\trans_code\\first\\"+i,"D:\\trans_code\\second\\"+i)
