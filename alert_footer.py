from PySide2 import QtWidgets, QtCore






class AlertFooter(QtWidgets.QStatusBar):

    def __init__(self):

        super().__init__()
        self.setup_ui()
        self.message_timer = QtCore.QTimer()
        self.message_timer.timeout.connect(self.clear_message)


    def setup_ui(self):
    # Create message label
        self.message_label = QtWidgets.QLabel()
        self.message_label.setWordWrap(True)
        
        # Create permanent widget for app status
        self.status_label = QtWidgets.QLabel("Ready")
        self.status_label.setMinimumWidth(100)
        
        # Add widgets to status bar
        self.addWidget(self.message_label, 1)
        self.addPermanentWidget(self.status_label)
        

    def show_success(self, message, timeout=3000):
        """Display success message in green"""
        self.message_label.setText(f"✅ {message}")
        self.message_label.setStyleSheet("color: #388e3c; font-weight: bold;")
        if timeout > 0:
            self.message_timer.start(timeout)

    def show_warning(self, message, timeout=3000):
        """Display success message in green"""
        self.message_label.setText(f"❌ {message}")
        self.message_label.setStyleSheet("color: #ff2d00; font-weight: bold;")
        if timeout > 0:
            self.message_timer.start(timeout)

    def clear_message(self):
        self.message_timer.stop()
        self.message_label.setText("Ready")
        self.message_label.setStyleSheet("color: #000000; font-weight: normal;")