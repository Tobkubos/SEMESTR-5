import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog, QHBoxLayout, QComboBox, QLineEdit, QTabWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from sklearn.linear_model import LinearRegression
import numpy as np

class PlotTab(QWidget):
    def __init__(self):
        super().__init__()
        
        self.x = []
        self.y = []
        
        self.mainLayout = QVBoxLayout()
        self.browseLayout = QHBoxLayout()
        self.optionsLayout = QHBoxLayout()
        self.infLayout = QHBoxLayout()
        
        #region Browse
        self.selectedFile = QLabel("here will be selected file")
        self.browseButton = QPushButton("Browse")
        self.browseButton.clicked.connect(self.browseFiles)
        self.browseLayout.addWidget(self.selectedFile)
        self.browseLayout.addWidget(self.browseButton)
        #endregion
        
        #region info
        self.title = QLineEdit()
        self.title.setPlaceholderText("graph title")
        self.Xax = QLineEdit()
        self.Xax.setPlaceholderText("X ax")
        self.Yax = QLineEdit()
        self.Yax.setPlaceholderText("Y ax")
        self.updateInfo = QPushButton("ZMIEN NAZWY")
        self.updateInfo.clicked.connect(self.updateCanvaLabels)
        self.infLayout.addWidget(self.title)
        self.infLayout.addWidget(self.Xax)
        self.infLayout.addWidget(self.Yax)
        self.infLayout.addWidget(self.updateInfo)
        #endregion
        
        #region kolory
        self.optionsColor = QComboBox()
        self.optionsColor.addItem("red")
        self.optionsColor.addItem("green")
        self.optionsColor.addItem("blue")
        self.optionsLayout.addWidget(self.optionsColor)
        #endregion
        
        #region typy wykresów
        self.optionsWykres = QComboBox()
        self.optionsWykres.addItem("liniowy")
        self.optionsWykres.addItem("punktowy")
        self.optionsWykres.addItem("slupkowy")
        self.optionsWykres.addItem("histogram x")
        self.optionsWykres.addItem("histogram y")
        self.optionsLayout.addWidget(self.optionsWykres)
        #endregion

        # Canvas (matplotlib figure)
        self.figure = Figure(figsize=(10, 6), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.figure)
        self.ax.plot(self.x, self.y, color='red')
        self.ax.legend()
        
        #region labele
        self.optionsColor.currentTextChanged.connect(self.updateCanvas)
        self.optionsWykres.currentTextChanged.connect(self.updateCanvas)
        #endregion
        
        #region Regresja
        self.DrawRegression = QPushButton("pokaz regresje liniowa")
        self.DrawRegression.clicked.connect(self.reg)
        #endregion
        
        #region uklad
        self.mainLayout.addLayout(self.infLayout)
        self.mainLayout.addLayout(self.optionsLayout)
        self.mainLayout.addWidget(self.canvas)
        self.mainLayout.addLayout(self.browseLayout)
        self.mainLayout.addWidget(self.DrawRegression)
        
        self.setLayout(self.mainLayout)
        #endregion
    
    #region pliki
    def browseFiles(self):
        fname = QFileDialog.getOpenFileName(self, 'open file', '', 'Text Files (*.txt)')
        self.selectedFile.setText(fname[0])
        self.x.clear()
        self.y.clear()
        with open(fname[0], 'r') as file:
            for line in file:
                values = line.strip().split(',')
                if len(values) == 2:
                    self.x.append(int(values[0]))
                    self.y.append(int(values[1]))
            self.ax.set_xlim(min(self.x) - 1, max(self.x) + 1)
            self.ax.set_ylim(min(self.y) - 1, max(self.y) + 1)
            self.updateCanvas()
    #endregion
    
    #region update labelow
    def updateCanvaLabels(self):
        self.ax.set_title(self.title.text())
        self.ax.set_xlabel(self.Xax.text())
        self.ax.set_ylabel(self.Yax.text())
        self.canvas.draw()
    #endregion
    
    
    #region update canvy
    def updateCanvas(self):
        selected_type = self.optionsWykres.currentText()
        col = self.optionsColor.currentText()
        self.ax.clear()
        if selected_type == "liniowy":
            self.ax.plot(self.x, self.y, color=col, label=f"Liniowy ({col})")
        elif selected_type == "punktowy":
            self.ax.scatter(self.x, self.y, color=col, label=f"Punktowy ({col})")
        elif selected_type == "slupkowy":
            self.ax.bar(self.x, self.y, color=col, label=f"Słupkowy ({col})")
        elif selected_type == "histogram x":
            self.ax.hist(self.x, bins=5, color=col, label=f"Histogram X ({col})")
        elif selected_type == "histogram y":
            self.ax.hist(self.y, bins=5, color=col, label=f"Histogram Y ({col})")
        self.ax.legend()
        self.canvas.draw()
    #endregion
    
    #region regresja
    def reg(self):
        if len(self.x) > 1 and len(self.y) > 1:
            #model do liczenia regresji liniowej
            model = LinearRegression()
            x_reshaped = np.array(self.x).reshape(-1, 1)
            model.fit(x_reshaped, self.y)
            y_pred = model.predict(x_reshaped)
            self.ax.plot(self.x, y_pred, color='purple', label=f"Liniowy (purple)")
            self.ax.legend()
        self.canvas.draw()
    #endregion

app = QApplication(sys.argv)
widget = QTabWidget()

#region zakladki
tab1 = PlotTab()
tab2 = PlotTab()
tab3 = PlotTab()
tab4 = PlotTab()
tab5 = PlotTab()

widget.addTab(tab1, "Tab 1")
widget.addTab(tab2, "Tab 2")
widget.addTab(tab3, "Tab 3")
widget.addTab(tab4, "Tab 4")
widget.addTab(tab5, "Tab 5")
#endregion

widget.setGeometry(300, 300, 1600, 1200)
widget.show()

sys.exit(app.exec())
