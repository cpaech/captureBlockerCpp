from PySide6.QtWidgets import QApplication, QWidget

# Only needed for access to command line arguments
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

import ctypes
from ctypes import windll

if __name__ == "__main__":
    app = QApplication([])

    widget = QWidget()

    hwnd = widget.window().winId()

    widget.setWindowTitle("")

    # WDA_EXCLUDEFROMCAPTURE - 0x00000011
    # WDA_NONE - 0x00000000

    windll.user32.SetWindowDisplayAffinity(hwnd, 11)

    # Add a label to the widget
    # label = QLabel("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut finibus felis quam, sed pharetra nisi dictum sed. Pellentesque blandit ullamcorper ipsum vestibulum posuere. Maecenas purus leo, viverra cursus nisl fringilla, lacinia faucibus lorem. Proin magna urna, pretium et risus id, vestibulum feugiat ex. Mauris id condimentum ante. Nulla facilisi. Suspendisse ut tempor nulla, et viverra est.
    #                     Phasellus nec finibus felis, a efficitur nulla. Quisque ligula ligula, luctus suscipit nibh non, vehicula ullamcorper enim. Etiam leo nulla, molestie eu accumsan nec, feugiat non elit. Phasellus interdum odio turpis, a dignissim odio pellentesque nec. Proin diam tellus, condimentum sed luctus facilisis, feugiat et mauris. Vestibulum suscipit metus eu suscipit eleifend. Aliquam rutrum diam in nibh congue, eget semper urna placerat. Aenean mattis lorem pharetra dui commodo sollicitudin at ut neque. Etiam suscipit arcu blandit, scelerisque mauris vitae, mollis ex. Nunc diam sem, vehicula sed metus id, iaculis faucibus leo. Mauris volutpat orci sed est semper, vel viverra mauris maximus.
    #                     Etiam vitae finibus orci, a finibus justo. Nam et elementum mauris, in interdum sapien. Integer erat est, pulvinar gravida condimentum in, condimentum nec erat. Vivamus condimentum, dui et ullamcorper bibendum, nibh dui convallis eros, luctus convallis metus libero nec nulla. Fusce sit amet diam eget dui facilisis luctus. Maecenas sit amet semper justo, id venenatis arcu. Curabitur nec arcu vel lacus interdum semper vel non mauris. Duis condimentum, eros sed luctus vulputate, augue urna dictum ex, eu volutpat mi nulla vitae diam. Pellentesque euismod porta cursus. Integer aliquam imperdiet libero eget auctor. Nulla a erat eget justo mattis tempus vitae vitae diam.
    #                     Nam scelerisque urna vel metus aliquam, ac rhoncus erat fermentum. Donec ut ligula eu lacus blandit varius id ac lectus. Morbi venenatis est imperdiet nunc placerat sollicitudin. Maecenas mattis sem eget eros volutpat, eget tempor ligula feugiat. Nam eget rhoncus tellus. In tempor risus tellus, ac varius est efficitur eu. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec vitae ante vel ex pharetra volutpat. Maecenas interdum condimentum dui hendrerit lacinia. Vestibulum pellentesque lectus sodales mattis semper.
    #                     Suspendisse ultrices rutrum dignissim. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nulla nec iaculis lorem. Vivamus diam sem, ultricies non interdum nec, dignissim eget massa. Mauris blandit tempor elementum. Integer quis malesuada ante, quis placerat dui. Nullam ut ornare tellus, sit amet mattis est. """)
    layout = QVBoxLayout()
    # layout.addWidget(label)
    widget.setLayout(layout)
    widget.setWindowFlags(Qt.FramelessWindowHint)
    widget.setWindowFlag(Qt.WindowStaysOnTopHint, True)
    width, height = app.primaryScreen().size().toTuple()
    widget.setGeometry(0, 0, width-1, height)
    widget.window().setAttribute(Qt.WA_TranslucentBackground)
    widget.showNormal()
    app.exec()