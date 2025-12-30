import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QFrame, QLabel)
from PyQt5.QtCore import Qt

# Create application
app = QApplication(sys.argv)

# -------------------------------
# Dark Theme (Lightweight)
# -------------------------------
app.setStyleSheet("""
QMainWindow {
    background-color: #1e1e1e;
}

QWidget {
    background-color: #1e1e1e;
    color: #dcdcdc;
    font-size: 13px;
}

QFrame {
    background-color: #252526;
    border: 1px solid #3c3c3c;
}

QLabel {
    color: #dcdcdc;
}
""")

# Main window
window = QMainWindow()
window.setWindowTitle("Mobile Robot Simulator")
window.resize(1280, 720)   # 16:9 aspect ratio

# Central widget
central_widget = QWidget()
window.setCentralWidget(central_widget)

# Grid layout (2x2)
grid = QGridLayout(central_widget)
grid.setSpacing(6)

def make_panel(title):
    panel = QFrame()
    panel.setFrameShape(QFrame.Box)
    panel.setLineWidth(2)

    label = QLabel(title)
    label.setAlignment(Qt.AlignCenter)

    layout = QGridLayout(panel)
    layout.addWidget(label)

    return panel

# Create panels
panel_1 = make_panel("Panel 1: World View")
panel_2 = make_panel("Panel 2: Waypoints")
panel_3 = make_panel("Panel 3: Controller")
panel_4 = make_panel("Panel 4: State / Logs")

# Add panels to grid
grid.addWidget(panel_1, 0, 0)
grid.addWidget(panel_2, 0, 1)
grid.addWidget(panel_3, 1, 0)
grid.addWidget(panel_4, 1, 1)

# Equal stretch so all panels resize evenly
grid.setRowStretch(0, 1)
grid.setRowStretch(1, 1)
grid.setColumnStretch(0, 1)
grid.setColumnStretch(1, 1)

# Show window maximized
window.showMaximized()

# Run application
sys.exit(app.exec_())
