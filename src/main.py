import cv2

from configuration import configuration_helpers
from image_processing import processing_helpers
from statistics import StatHelpers

COLOR_AMBER = (255, 193, 7)
COLOR_AQUA = (117, 255, 234)
COLOR_BLUE = (255, 0, 0)
COLOR_CYAN = (128, 222, 234)
COLOR_GREEN = (0, 255, 0)
COLOR_INDIGO = (26, 35, 126)
COLOR_LIME = (205, 220, 57)
COLOR_MINT = (56, 247, 152)
COLOR_ORANGE = (255, 87, 34)
COLOR_PEACH = (255, 163, 84)
COLOR_PINK = (244, 143, 177)
COLOR_PURPLE = (126, 87, 194)
COLOR_TEAL = (77, 182, 172)
COLOR_RED = (0, 0, 255)
COLOR_VIOLET = (212, 52, 239)
COLOR_YELLOW = (0, 255, 255)

VIDEO_SPEED = 30

LANES = {
    '1': {'x1': 260, 'y1': 412, 'x2': 433, 'y2': 412, 'color': COLOR_RED},
    '2': {'x1': 434, 'y1': 412, 'x2': 618, 'y2': 412, 'color': COLOR_BLUE},
    '3': {'x1': 619, 'y1': 412, 'x2': 800, 'y2': 412, 'color': COLOR_PINK},
    '4': {'x1': 801, 'y1': 412, 'x2': 1050, 'y2': 412, 'color': COLOR_GREEN}
}


def main():
    small_vehicle_size = int(configuration_helpers.get_small_vehicle_size())
    large_vehicle_size = int(configuration_helpers.get_large_vehicle_size())

    stat_helper = StatHelpers.StatHelper()

    video_file_path = configuration_helpers.get_video_file_name()
    save_file_path = configuration_helpers.get_save_file_name()

    cap = cv2.VideoCapture(video_file_path)

    fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)

    while cap.isOpened():
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        fgmask = fgbg.apply(frame)

        result = processing_helpers.process_frame(fgmask)

        (_, contours, hierarchy) = cv2.findContours(result.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw lanes
        for i in LANES:
            x1 = LANES[i]['x1']
            y1 = LANES[i]['y1']
            x2 = LANES[i]['x2']
            y2 = LANES[i]['y2']
            color = LANES[i]['color']

            cv2.line(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, 'COUNT %r: %r' % (i, stat_helper.get_all_count(i)), (x1, y1 - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        for contour in contours:
            contour_area = cv2.contourArea(contour)

            if contour_area < small_vehicle_size:
                continue

            x, y, w, h = cv2.boundingRect(contour)
            center = x + w / 2
            cv2.rectangle(frame, (x, y), (x + w, y + h), COLOR_AMBER, 2)
            cv2.putText(frame, 'O', (center, y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, COLOR_RED, 5)

            # Count vehicles on each lane
            for i in LANES:
                x1 = LANES[i]['x1']
                y1 = LANES[i]['y1']
                x2 = LANES[i]['x2']

                if y1 < y < (y1 + 15) and x1 < center < x2:
                    stat_helper.increase_all_count(i)

                    if small_vehicle_size < contour_area < large_vehicle_size:
                        stat_helper.increase_small_count(i)
                    elif contour_area > large_vehicle_size:
                        stat_helper.increase_large_count(i)

        # cv2.namedWindow('camera1', cv2.WINDOW_NORMAL)
        cv2.imshow('camera1', frame)
        # cv2.imshow('test', result)

        if cv2.waitKey(VIDEO_SPEED) & 0xFF == 27:
            break

    cap.release()

    stat_helper.write_stat_to_file(save_file_path)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
