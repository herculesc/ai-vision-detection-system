import cv2

PERSON_CLASS_ID = 0  # COCO: person


def draw_people_only(image, results):
    for r in results:
        boxes = r.boxes

        for box in boxes:
            cls = int(box.cls[0])

            if cls != PERSON_CLASS_ID:
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])

            label = f"person {conf:.2f}"

            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (0, 255, 0), 2)

    return image


def count_people(results):
    count = 0

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])

            if cls == PERSON_CLASS_ID:
                count += 1

    return count