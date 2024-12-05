#ifndef MYRENDER_H
#define MYRENDER_H

#include <QWidget>

class myRender : public QWidget
{
    Q_OBJECT
public:
    explicit myRender(QWidget *parent = 0);

protected:
    void paintEvent(QPaintEvent *event) override;

signals:

public slots:
};

#endif // MYRENDER_H

