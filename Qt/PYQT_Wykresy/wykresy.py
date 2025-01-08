import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton,QFileDialog, QHBoxLayout, QComboBox, QLineEdit

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from sklearn.linear_model import LinearRegression
import numpy as np

x = []
y = []

app = QApplication(sys.argv)
widget = QWidget()

mainLayout = QVBoxLayout()


widget.setGeometry(300, 300, 1600, 1200)
browseLayout = QHBoxLayout()
optionsLayout = QHBoxLayout()

#region browse
selectedFile = QLabel("here will be selected file")
browseButton = QPushButton("Browse")

def browseFiles():
    fname = QFileDialog.getOpenFileName(widget, 'open file', '', 'Text Files (*.txt)')
    selectedFile.setText(fname[0])
    x.clear()
    y.clear()
    with open(fname[0], 'r') as file:
        for line in file:
            values = line.strip().split(',')
            if len(values) == 2:
                x.append(int(values[0]))
                y.append(int(values[1]))
        ax.set_xlim(min(x) - 1, max(x) + 1)
        ax.set_ylim(min(y) - 1, max(y) + 1)
        update_canvas()
        print(x)
        print(y)
browseButton.clicked.connect(browseFiles)


browseLayout.addWidget(selectedFile)
browseLayout.addWidget(browseButton)
#endregion

#region informacje
infLayout = QHBoxLayout()
title = QLineEdit()
title.setPlaceholderText("graph title")
Xax = QLineEdit()
Xax.setPlaceholderText("X ax")
Yax = QLineEdit()
Yax.setPlaceholderText("Y ax")
updateInfo = QPushButton()
updateInfo.setText("ZMIEN NAZWY")
def updateCanvaLabels():
    ax.set_title(title.text())
    ax.set_xlabel(Xax.text())
    ax.set_ylabel(Yax.text())
    canvas.draw()
updateInfo.clicked.connect(updateCanvaLabels)

infLayout.addWidget(title)
infLayout.addWidget(Xax)
infLayout.addWidget(Yax)
infLayout.addWidget(updateInfo)
mainLayout.addLayout(infLayout)


#endregion



#region opcje
optionsColor = QComboBox()
optionsColor.addItem("red")
optionsColor.addItem("green")
optionsColor.addItem("blue")
optionsLayout.addWidget(optionsColor)

optionsWykres = QComboBox()
optionsWykres.addItem("liniowy")
optionsWykres.addItem("punktowy")
optionsWykres.addItem("slupkowy")
optionsWykres.addItem("histogram x")
optionsWykres.addItem("histogram y")
optionsLayout.addWidget(optionsWykres)
#endregion



#region canva
figure = Figure(figsize=(10, 6), dpi=100)
ax = figure.add_subplot(111)
canvas = FigureCanvas(figure)

# Plot data
ax.plot(x,y,color = 'red')

ax.legend()
#endregion

def update_canvas():
    selected_type = optionsWykres.currentText()
    col = optionsColor.currentText()
    ax.clear()
    if selected_type == "liniowy":
        ax.plot(x, y, color=col, label=f"Liniowy ({col})")
    elif selected_type == "punktowy":
        ax.scatter(x, y, color=col, label=f"Punktowy ({col})")
    elif selected_type == "slupkowy":
        ax.bar(x, y, color=col, label=f"Słupkowy ({col})")
    elif selected_type == "histogram x":
        ax.hist(x, bins=5, color=col, label=f"Histogram X ({col})")
    elif selected_type == "histogram y":
        ax.hist(y, bins=5, color=col, label=f"Histogram Y ({col})")
        
    ax.legend()   
    canvas.draw()
    
optionsColor.currentTextChanged.connect(update_canvas)
optionsWykres.currentTextChanged.connect(update_canvas)

DrawRegression = QPushButton("pokaz regresje liniowa")
def reg():
    if len(x) > 1 and len(y) > 1:
        #setup modelu do liczenia regresji liniowej
        model = LinearRegression()
        x_reshaped = np.array(x).reshape(-1, 1)
        model.fit(x_reshaped, y)
        y_pred = model.predict(x_reshaped)
        
        ax.plot(x, y_pred, color='purple', label=f"Liniowy (purple)")
        ax.legend() 
    canvas.draw()
DrawRegression.clicked.connect(reg)
mainLayout.addWidget(DrawRegression)


mainLayout.addLayout(optionsLayout)
mainLayout.addWidget(canvas)
mainLayout.addLayout(browseLayout)
widget.setLayout(mainLayout)
widget.show()

sys.exit(app.exec())