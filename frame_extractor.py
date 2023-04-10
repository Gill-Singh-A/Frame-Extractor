import cv2, sys, pathlib, os, time
from datetime import date
from colorama import Fore, Style

def extract_frames(file_name):
    cwd = str(pathlib.Path.cwd()) + "\\"
    video_dir = pathlib.Path.cwd() / "Frames" / file_name.split(".")[0]
    try:
        video_dir.mkdir(parents=True)
    except:
        print(f"{Fore.BLUE}[{date.today()} {time.strftime('%H:%M:%S', time.localtime())}] {Fore.YELLOW}Frame Folder of {file_name} Already Exsists{Fore.RESET}")
        return
    os.chdir(video_dir)
    try:
        video_file = cv2.VideoCapture(cwd+file_name)
    except:
        print(f"{Fore.BLUE}[{date.today()} {time.strftime('%H:%M:%S', time.localtime())}] {Fore.RED}Error opening {file_name}{Fore.RESET}")
        return
    total_frames = int(video_file.get(cv2.CAP_PROP_FRAME_COUNT))
    t1 = time.time()
    current_frame = 1
    ret, frame = video_file.read()
    while ret:
        name = f"{current_frame}.jpg"
        cv2.imwrite(name, frame)
        print(f"\r{Fore.BLUE}[{date.today()} {time.strftime('%H:%M:%S', time.localtime())}] {Fore.YELLOW}{Style.BRIGHT}Extracting Frames of {file_name} {current_frame/total_frames*100:.2f}% ({current_frame}/{total_frames}){Fore.RESET}{Style.RESET_ALL}", end="")
        current_frame += 1
        ret, frame = video_file.read()
    t2 = time.time()
    print(f"\r{Fore.BLUE}[{date.today()} {time.strftime('%H:%M:%S', time.localtime())}] {Fore.GREEN}{Style.BRIGHT}Extracted Frames of {file_name} Total Frames = {total_frames} Time Taken = {t2-t1} seconds{Fore.RESET}{Style.RESET_ALL}")
    os.chdir('../../')

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "*":
        file_names = os.listdir()
    else:
        file_names = sys.argv[1:]
    for file_name in file_names:
        extract_frames(file_name)