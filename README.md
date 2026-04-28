# 📸 RGB Camera Lab — Read the Center Pixel

### 🔍 Overview
A short, hands-on lab activity that introduces **OpenCV** by reading the **BGR** color values of the **center pixel** of your webcam feed in real time.

A circle is drawn around the center of the frame, and pressing **`v`** prints the BGR value of that pixel to the console. Press **`e`** to exit.

> 🎓 Perfect for a first OpenCV class — students see images as **arrays of pixels** and explore the **BGR color space** interactively.

---

### 📦 Features
- Live webcam capture using OpenCV
- A visible circle drawn around the **center pixel**
- Press **`v`** → print the center pixel's `(B, G, R)` value
- Press **`e`** → quit
- **NEW:** All visual parameters (camera index, radius, color, thickness) configurable via CLI
- **NEW:** Optional `--save-on-press` to save a snapshot every time you sample a pixel

---

### 🧰 Requirements
```bash
pip install -r requirements.txt
```

You'll need a working webcam (built-in or USB).

---

### ⚙️ How to Run
**Default run:**
```bash
python RGB_Cam.py
```

**Custom run:**
```bash
python RGB_Cam.py --camera 0 --radius 25 --color 0,255,0 --thickness 4 --save-on-press
```

---

### 🛠️ Command-Line Options
| Flag | Default | Description |
|------|---------|-------------|
| `--camera` | `0` | Camera device index (0 = default webcam) |
| `--radius` | `15` | Radius of the circle drawn at the center |
| `--color` | `50,101,254` | Circle color as `B,G,R` (orange-ish by default) |
| `--thickness` | `3` | Circle line thickness |
| `--save-on-press` | _off_ | Save a `snapshot_<timestamp>.png` each time `v` is pressed |
| `--window` | `Camera` | Window title |

---

### 🎮 Controls
| Key | Action |
|-----|--------|
| `v` | Print BGR value of the **center** pixel |
| `e` | Exit the program |

---

### 🧠 Why BGR (and not RGB)?
OpenCV stores images in **BGR** order by default — a historical convention from the early days of OpenCV. This is why `image[y, x]` returns `(B, G, R)`, not `(R, G, B)`.

If you ever need RGB:
```python
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
```

---

### 🎓 Learning Goals
1. Open and read frames from a webcam with `cv2.VideoCapture`
2. Understand image shape `(height, width, channels)` and indexing `image[y, x]`
3. Learn the **BGR** vs RGB convention used by OpenCV
4. Draw on top of a live frame with `cv2.circle`
5. Handle keyboard events with `cv2.waitKey`

---

### 🛑 Troubleshooting
| Issue | Fix |
|-------|-----|
| Black screen / no frames | Try a different `--camera` index (1, 2, ...) |
| App freezes on exit | Use `e` to exit, not the window's X button |
| `ImportError: No module named cv2` | Run `pip install opencv-python` |

---

### 📁 Project Structure
```
Lab_activity/
├── RGB_Cam.py        # Main script
├── requirements.txt  # Python dependencies
└── README.md
```

---

### 📄 License
Educational use — Credits to **[CS42.org](https://cs42.org)**.
