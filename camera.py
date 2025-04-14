import argparse
from BackgroundEffect import BackgroundEffect

def parse_args():
    parser = argparse.ArgumentParser(description="Apply blur or image background to webcam feed.")
    parser.add_argument("-r", "--replace-bg", action="store_true",
                        help="Replace background with an image instead of blurring.")
    parser.add_argument("-i", "--bg-image", type=str,
                        help="Path to background image (used with --replace-bg).")
    parser.add_argument("-s", "--source", type=int, default=0,
                        help="Camera source index (default: 0).")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    try:
        blur = BackgroundEffect(
            source=args.source,
            replace_bg=args.replace_bg,
            bg_image_path=args.bg_image
        )
        blur.run()
    except Exception as e:
        print(f"Error: {e}")
