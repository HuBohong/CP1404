from class_coding_folder.monitor import Monitor

if __name__ == '__main__':
    monitor1 = Monitor("Dell U2723QE", 3840, 2160)
    monitor2 = Monitor("LG 27UK850", 3840, 2160)
    monitor3 = Monitor("ASUS VG248QE", 1920, 1080)
    monitor4 = Monitor("LG 27UK850", 1920, 1080)
    print(monitor1.get_resolution())
    print(type(monitor1.get_resolution()))
    print(monitor2.get_total_pixels())
    print(monitor2 == monitor1)
    print(monitor3 == monitor1)
    print(dir(monitor2))  # Should print False
