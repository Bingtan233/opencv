import cv2

# 初始化摄像头（0 是默认摄像头）
cap = cv2.VideoCapture(0)

# 初始化二维码检测器
detector = cv2.QRCodeDetector()

print("按下 Q 键退出程序...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 检测并解码二维码
    data, bbox, _ = detector.detectAndDecode(frame)

    if bbox is not None:
        # 画出二维码边框
        n = len(bbox)
        for i in range(n):
            pt1 = tuple(map(int, bbox[i][0]))
            pt2 = tuple(map(int, bbox[(i + 1) % n][0]))
            cv2.line(frame, pt1, pt2, color=(0, 255, 0), thickness=2)

        # 显示二维码数据
        if data:
            print("检测到二维码数据：", data)
            cv2.putText(frame, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    # 显示画面
    cv2.imshow("东方红魔乡", frame)

    # 按下 Q 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
