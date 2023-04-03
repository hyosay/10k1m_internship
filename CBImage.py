import cv2
import os


def CBImageDownload(video_path, output_directory):
    # str::video_path = input your video link
    # str::optput_directory = your absolute storage path
    # 비디오 캡처 객체 생성
    video_capture = cv2.VideoCapture(video_path)
    #비디오 캡처가 열렸는지 확인
    if not video_capture.isOpened():
        print("Error: Could not open video file.")
        exit()

    frame_count = 0
    save_frame_count = 0
    width = 640
    height = 640

    while True:
        # 비디오에서 프레임 읽기
        ret, frame = video_capture.read()
        # 읽기에 성공한 경우에만 이미지를 추출하고 저장
        if ret:
            # 30개 프레임마다 이미지 저장
            if frame_count % 30 == 0:
                # 이미지 크기 변경
                resized_frame = cv2.resize(frame, (width, height))

                output_path = os.path.join(output_directory, f'frame{save_frame_count:04d}.png')
                cv2.imwrite(output_path, resized_frame)
                save_frame_count += 1
            frame_count += 1
        else:
            break

    # 비디오 캡처 객체 해제
    video_capture.release()
