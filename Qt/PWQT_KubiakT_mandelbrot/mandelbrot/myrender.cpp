
#include "myrender.h"
#include <QPainter>
#include <QPainterPath>
#define _USE_MATH_DEFINES
#include <math.h>

#include <QImage>
#include <complex>
#include <cmath>


myRender::myRender(QWidget *parent) : QWidget(parent)
{
    QPalette pal = palette();
    pal.setColor(QPalette::Window, Qt::red);
    setAutoFillBackground(true);
    setPalette(pal);
}


void myRender::paintEvent(QPaintEvent * /* _event */)
{
    QPainter painter(this);
    QRect r = this->geometry();

    double xMin = -2.5;
    double xMax = 1.5;
    double yMin = -1.25;
    double yMax = 1.25;
    int iters = 50;

    //kolory
    double w1 = 50, w2 = 50, w3 = 50;
    double p1 = 2.2, p2 = 2.2, p3 = 2.2;
    double c1 = 0.25, c2 = 0.5, c3 = 0.75;

    //wielkość
    int width = r.width();
    int height = r.height();
    double unitX = (xMax - xMin) / width;
    double unitY = (yMax - yMin) / height;

    QImage image(width, height, QImage::Format_RGB32);

    for (int i = 0; i < height; ++i) {
        for (int j = 0; j < width; ++j) {
            std::complex<double> c(xMin + j * unitX, yMax - i * unitY);
            std::complex<double> z(0, 0);

            int v = 0;
            while (v < iters && norm(z) <= 4.0) {
                z = z * z + c;
                ++v;
            }

            double cNorm = v * 1. / iters * 1.;

            //kolory
            double redV = exp(-w1 * pow(abs(cNorm - c1), p1));
            double greenV = exp(-w2 * pow(abs(cNorm - c2), p2));
            double blueV = exp(-w3 * pow(abs(cNorm - c3), p3));

            int red = redV * 255;
            int green = greenV * 255;
            int blue = blueV * 255;

            image.setPixel(j, i, qRgb(red, green, blue));
        }
    }

    painter.drawImage(0, 0, image);
}
