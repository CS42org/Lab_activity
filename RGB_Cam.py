"""
RGB Camera Lab — Read the Center Pixel
--------------------------------------
Opens your webcam, draws a small circle around the center pixel, and prints
its BGR values when you press 'v'. Press 'e' to exit.

Run with defaults:
    python RGB_Cam.py

Run with options:
    python RGB_Cam.py --camera 0 --radius 20 --color 50,101,254 --save-on-press
"""

import argparse
import sys
import time

import cv2


def parse_args():
    p = argparse.ArgumentParser(description="Webcam center-pixel BGR reader.")
    p.add_argument("--camera", type=int, default=0, help="Camera device index (default: 0)")
    p.add_argument("--radius", type=int, default=15, help="Radius of the circle drawn at the center (default: 15)")
    p.add_argument(
        "--color",
        default="50,101,254",
        help="Circle color as B,G,R (default: 50,101,254 → orange-ish)",
    )
    p.add_argument("--thickness", type=int, default=3, help="Circle line thickness (default: 3)")
    p.add_argument(
        "--save-on-press",
        action="store_true",
        help="Save a snapshot to disk every time 'v' is pressed",
    )
    p.add_argument(
        "--window",
        default="Camera",
        help="Window title (default: 'Camera')",
    )
    return p.parse_args()


def parse_color(s):
    parts = s.split(",")
    if len(parts) != 3:
        raise ValueError("--color must be three comma-separated integers, e.g. 50,101,254")
    b, g, r = (int(x) for x in parts)
    for v in (b, g, r):
        if not 0 <= v <= 255:
            raise ValueError("Each color channel must be in [0, 255]")
    return b, g, r


def main():
    args = parse_args()

    try:
        bgr_color = parse_color(args.color)
    except ValueError as e:
        print(f"[!] {e}", file=sys.stderr)
        sys.exit(1)

    cap = cv2.VideoCapture(args.camera)
    if not cap.isOpened():
        print(f"[!] Could not open camera index {args.camera}", file=sys.stderr)
        sys.exit(1)

    print("Controls:  press 'v' to read center BGR  |  press 'e' to exit")

    try:
        while True:
            ok, image = cap.read()
            if not ok or image is None:
                print("[!] Failed to read frame from camera.", file=sys.stderr)
                break

            h, w = image.shape[:2]
            cy, cx = h // 2, w // 2

            # Draw a circle around the center pixel
            cv2.circle(image, (cx, cy), args.radius, bgr_color, thickness=args.thickness, lineType=8)
            cv2.imshow(args.window, image)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("v"):
                bgr = image[cy, cx]
                print(f"Center pixel BGR = ({int(bgr[0])}, {int(bgr[1])}, {int(bgr[2])})")
                if args.save_on_press:
                    fname = f"snapshot_{int(time.time())}.png"
                    cv2.imwrite(fname, image)
                    print(f"Saved snapshot: {fname}")
            elif key == ord("e"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
