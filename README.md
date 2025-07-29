# 👁️ Iris-Controlled Cursor

An AI-powered project that allows users to control their computer cursor using their **eye movements** and **iris tracking**. This project uses computer vision to detect and track the iris, enabling hands-free control — ideal for accessibility tools or experimental HCI (Human-Computer Interaction) systems.

## 🚀 Features

- 👁️ Real-time iris tracking using webcam  
- 🖱️ Cursor movement based on gaze direction  
- 🧠 Drowsiness or blink detection (optional)  
- 📐 Calibrated mapping between eye position and screen  
- 💡 Minimal, responsive GUI overlay for feedback  

## 🧰 Tech Stack

- **Language:** Python  
- **Libraries:**  
  - OpenCV  
  - dlib or MediaPipe  
  - pyautogui  
  - numpy  
- **Tools:** PyCharm, Jupyter Notebook (optional)  

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/your-username/iris-cursor.git
cd iris-cursor

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
📦 Requirements
Python 3.7+

Webcam

Screen resolution set correctly

A well-lit environment for accurate iris detection

🧪 Usage
bash
Copy
Edit
python iris_cursor.py
Look left/right/up/down to move the cursor.

Blink detection or drowsiness alert can be added using additional logic.

🔧 Configuration
You can modify parameters like sensitivity, calibration offsets, and blink thresholds in the config section of iris_cursor.py.

📄 File Structure
bash
Copy
Edit
iris-cursor/
├── iris_cursor.py         # Main script
├── calibration.py         # Optional calibration utility
├── utils.py               # Helper functions
├── README.md
└── requirements.txt
👤 Author
Zaid Ali
📧 zaidali.za2635@gmail.com
💼 LinkedIn |

📃 License
This project is licensed under the MIT License - see the LICENSE file for details.

