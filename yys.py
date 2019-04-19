from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import random

r = {1:r'.\yys\r\_st.jpg',2:r'.\yys\r\by.jpg',3:r'.\yys\r\cs.jpg',4:r'.\yys\r\cszn.jpg',5:r'.\yys\r\dyxs.jpg',
             6:r'.\yys\r\eg.jpg',7:r'.\yys\r\gh.jpg',8:r'.\yys\r\glh.jpg',9:r'.\yys\r\hdj.jpg',10:r'.\yys\r\ht.jpg',
             11:r'.\yys\r\j.jpg',12:r'.\yys\r\jmm.jpg',13:r'.\yys\r\jt.jpg',14:r'.\yys\r\lm.jpg',15:r'.\yys\r\lyj.jpg',
             16:r'.\yys\r\qwcq.jpg',17:r'.\yys\r\sfg.jpg',18:r'.\yys\r\st.jpg',19:r'.\yys\r\sw.jpg',20:r'.\yys\r\swh.jpg',
             21:r'.\yys\r\sz.jpg',22:r'.\yys\r\tl.jpg',23:r'.\yys\r\tn.jpg',24:r'.\yys\r\ts.jpg',25:r'.\yys\r\ttdd.jpg',
             26:r'.\yys\r\ttmm.jpg',27:r'.\yys\r\wgs.jpg',28:r'.\yys\r\wszl.jpg',29:r'.\yys\r\xxzs.jpg',30:r'.\yys\r\yc.jpg',
             31:r'.\yys\r\yn.jpg',32:r'.\yys\r\ytg.jpg',33: r'.\yys\r\zftz.jpg',}

sr = {1:r'.\yys\sr\bmg.jpg',2:r'.\yys\sr\br.jpg',3:r'.\yys\sr\btz.jpg',4:r'.\yys\sr\ekn.jpg',5:r'.\yys\sr\ffh.jpg',
             6:r'.\yys\sr\ghl.jpg',7:r'.\yys\sr\gn.jpg',8:r'.\yys\sr\gnhy.jpg',9:r'.\yys\sr\gsh.jpg',10:r'.\yys\sr\hbs.jpg',
             11:r'.\yys\sr\hfz.jpg',12:r'.\yys\sr\htz.jpg',13:r'.\yys\sr\jyj.jpg',14:r'.\yys\sr\kls.jpg',15:r'.\yys\sr\lxf.jpg',
             16:r'.\yys\sr\mp.jpg',17:r'.\yys\sr\mzg.jpg',18:r'.\yys\sr\pg.jpg',19:r'.\yys\sr\qfz.jpg',20:r'.\yys\sr\qj.jpg',
             21:r'.\yys\sr\qs.jpg',22:r'.\yys\sr\sw.jpg',23:r'.\yys\sr\thy.jpg',24:r'.\yys\sr\ttdd.jpg',25:r'.\yys\sr\x.jpg',
             26:r'.\yys\sr\xn.jpg',27:r'.\yys\sr\xsw.jpg',28:r'.\yys\sr\xxj.jpg',29:r'.\yys\sr\xzsn.jpg',30:r'.\yys\sr\y.jpg',
             31:r'.\yys\sr\yc.jpg',32:r'.\yys\sr\yh.jpg',33: r'.\yys\sr\yhy.jpg',34: r'.\yys\sr\yjzt.jpg',35: r'.\yys\sr\yqs.jpg',
             36: r'.\yys\sr\zys.jpg',37: r'.\yys\sr\rhf.jpg',38: r'.\yys\sr\z.jpg',39: r'.\yys\sr\smm.jpg',40: r'.\yys\sr\gsb.jpg',
             41: r'.\yys\sr\yyl.jpg',42: r'.\yys\sr\ly.jpg',43: r'.\yys\sr\bl.jpg',}

ssr = {1:r'.\yys\ssr\bqds.jpg',2:r'.\yys\ssr\bzz.jpg',3:r'.\yys\ssr\cmtz.jpg',4:r'.\yys\ssr\dtg.jpg',5:r'.\yys\ssr\gq.jpg',
             6:r'.\yys\ssr\h.jpg',7:r'.\yys\ssr\hyj.jpg',8:r'.\yys\ssr\jttz.jpg',9:r'.\yys\ssr\mlq.jpg',10:r'.\yys\ssr\qxd.jpg',
             11:r'.\yys\ssr\sf.jpg',12:r'.\yys\ssr\xln.jpg',13:r'.\yys\ssr\xtz.jpg',14:r'.\yys\ssr\ydj.jpg',15:r'.\yys\ssr\ym.jpg',
             16:r'.\yys\ssr\yml.jpg',17:r'.\yys\ssr\yzj.jpg',18:r'.\yys\ssr\yzq.jpg',}

class Win(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon('.\yys\yys.ico'))
        self.bt1 = QPushButton('单抽',self)
        self.setWindowTitle('阴阳师模拟抽卡2.0')
        self.bt2 = QPushButton('十连', self)

        self.pixLogo = QLabel(self)
        self.pixLogo.setPixmap(QPixmap('.\yys\logo.png'))
        self.pixLogo.move(0,220)
        self.btn1 = QRadioButton('无概率up',self)
        self.btn1.setChecked(True)
        self.btn1.toggled.connect(lambda :self.btnstate(self.btn1))
        self.btn1.move(50,200)
        self.btn2 = QRadioButton('2.5倍概率up',self)
        self.btn2.toggled.connect(lambda: self.btnstate(self.btn2))
        self.btn2.move(200, 200)
        self.btn3 = QRadioButton('百分百概率up', self)
        self.btn3.toggled.connect(lambda: self.btnstate(self.btn3))
        self.btn3.move(350, 200)
        palette1 = QPalette()
        palette1.setColor(self.backgroundRole(), QColor(192, 253, 123))
        self.setPalette(palette1)
        self.resize(800,400)
        self.bt1.move(50,50)
        self.bt2.move(50,100)
        self.la1 = QLabel(self)
        self.la1.setFont(QFont('SimSun',20,QFont.Bold))
        self.la1.setText('抽卡统计：')
        self.la1.move(500,40)
        self.num = QLabel(self)
        self.num.move(500,100)
        self.num.setText('抽卡次数：'+'            ')
        self.reset = QPushButton('重置',self)
        self.reset.move(50,150)
        self.reset.clicked.connect(self._reset)
        la_time = QLabel('                                  ', self)
        la_time.move(10, 20)
        time = QTimer(self)
        time.timeout.connect(lambda: self.time(la_time))
        time.start(1000)

        self.bt1.clicked.connect(self.bt1_Clicked1)
        self.bt2.clicked.connect(self.bt1_Clicked2)
        """self.bt2.clicked.connect(self.bt2_Clicked)"""
        self.TongJi()


        self._time = 0
        self._r = 0
        self._sr = 0
        self._ssr = 0
        self.up1 = 121
        self.up2 = 2001
    def btnstate(self,btn):
        """概率up单选按钮"""
        if btn.text() == '无概率up':
            if btn.isChecked() == True:
                self.up1 = 121
                self.up2 = 2001
        if btn.text() == '2.5倍概率up':
            if btn.isChecked() == True:
                self.up1 = 301
                self.up2 = 2301
        if btn.text() == '百分百概率up':
            if btn.isChecked() == True:
                self.up1 = 10001
                self.up2 = 10001
    def _reset(self):
        """重置按钮"""
        self._time = 0
        self._r = 0
        self._sr = 0
        self._ssr = 0
        self.num.setText('抽卡次数：' +str(self._time))
    def TongJi(self):
        """统计概率"""
        self.lbr = QLabel(self)
        self.lbr.setText('                                      ')
        self.lbr.move(500,170)
        self.lbsr = QLabel(self)
        self.lbsr.setText('                                     ')
        self.lbsr.move(500,190)
        self.lbssr = QLabel(self)
        self.lbssr.setText('                                    ')
        self.lbssr.move(500,210)
        bt = QPushButton('统计概率',self)
        bt.move(500,130)
        bt.clicked.connect(self.tongji)
    def tongji(self):
        """统计概率按钮事件"""
        try:
            g_r = self._r/self._time
            g_sr = self._sr / self._time
            g_ssr = self._ssr / self._time
            self.lbr.setText("抽出R卡："+str(self._r)+"张\t"+"概率： "+str(round(g_r*100,2))+'%')
            self.lbsr.setText("抽出SR卡："+str(self._sr)+"张\t"+"概率： "+str(round(g_sr*100,2))+'%')
            self.lbssr.setText("抽出SSR卡："+str(self._ssr)+"张\t"+"概率： "+str(round(g_ssr*100,2))+'%')
        except ZeroDivisionError:
            dialog = QDialog()
            dialog.resize(200,200)
            btn = QLabel('还没开始抽统计个毛？',dialog)
            btn.move(10,50)
            dialog.setWindowTitle('!!!?????')
            dialog.setWindowModality(Qt.ApplicationModal)
            dialog.exec_()
    def time(self,la):
        """绘制时间"""
        datetime = QDateTime.currentDateTime()
        text = datetime.toString('yyyy年MM月dd日 时间：HH:mm:ss')
        la.setText(text)

    def bt1_Clicked1(self):
        """单抽按钮设置"""
        d = QVBoxLayout()
        dialog = QDialog()
        labe1 = QLabel(dialog)
        labe2 = QLabel(dialog)
        labe2.setAlignment(Qt.AlignCenter)
        self.re(labe1,labe2)
        dialog.setWindowTitle('单抽')
        d.addWidget(labe1)
        d.addWidget(labe2)
        dialog.setLayout(d)
        dialog.setWindowModality(Qt.ApplicationModal)
        self._time+=1
        print(self._time)
        km = str(self._time)
        self.num.setText('抽卡次数：'+km)
        dialog.exec_()

    def bt1_Clicked2(self):
        """十抽按钮设置"""
        dialog = QDialog()
        labe1 = QLabel(dialog)
        labe2 = QLabel(dialog)
        labe3 = QLabel(dialog)
        labe4 = QLabel(dialog)
        labe5 = QLabel(dialog)
        labe6 = QLabel(dialog)
        labe7 = QLabel(dialog)
        labe8 = QLabel(dialog)
        labe9 = QLabel(dialog)
        labe10 = QLabel(dialog)
        labe11 = QLabel(dialog)
        labe12 = QLabel(dialog)
        labe13 = QLabel(dialog)
        labe14 = QLabel(dialog)
        labe15 = QLabel(dialog)
        labe16 = QLabel(dialog)
        labe17 = QLabel(dialog)
        labe18 = QLabel(dialog)
        labe19 = QLabel(dialog)
        labe20 = QLabel(dialog)
        labe11.setAlignment(Qt.AlignCenter)
        labe12.setAlignment(Qt.AlignCenter)
        labe13.setAlignment(Qt.AlignCenter)
        labe14.setAlignment(Qt.AlignCenter)
        labe15.setAlignment(Qt.AlignCenter)
        labe16.setAlignment(Qt.AlignCenter)
        labe17.setAlignment(Qt.AlignCenter)
        labe18.setAlignment(Qt.AlignCenter)
        labe19.setAlignment(Qt.AlignCenter)
        labe20.setAlignment(Qt.AlignCenter)
        self.re(labe1,labe11)
        self.re(labe2,labe12)
        self.re(labe3,labe13)
        self.re(labe4,labe14)
        self.re(labe5,labe15)
        self.re(labe6,labe16)
        self.re(labe7,labe17)
        self.re(labe8,labe18)
        self.re(labe9,labe19)
        self.re(labe10,labe20)
        layout = QGridLayout()
        layout.addWidget(labe1,0,0)
        layout.addWidget(labe2,0,1)
        layout.addWidget(labe3, 0, 2)
        layout.addWidget(labe4, 0, 3)
        layout.addWidget(labe5, 0, 4)
        layout.addWidget(labe11, 1, 0)
        layout.addWidget(labe12, 1, 1)
        layout.addWidget(labe13, 1, 2)
        layout.addWidget(labe14, 1, 3)
        layout.addWidget(labe15, 1, 4)
        layout.addWidget(labe6, 2, 0)
        layout.addWidget(labe7, 2, 1)
        layout.addWidget(labe8, 2, 2)
        layout.addWidget(labe9, 2, 3)
        layout.addWidget(labe10, 2, 4)
        layout.addWidget(labe16, 3, 0)
        layout.addWidget(labe17, 3, 1)
        layout.addWidget(labe18, 3, 2)
        layout.addWidget(labe19, 3, 3)
        layout.addWidget(labe20, 3, 4)
        dialog.setWindowTitle('十抽')
        dialog.setLayout(layout)
        dialog.setWindowModality(Qt.ApplicationModal)
        self._time+=10
        km = str(self._time)
        self.num.setText('抽卡次数：' + km)
        dialog.exec_()

    def re(self,la,lb):
        """抽卡概率设置"""
        wah = random.randint(1,10000)

        if wah in range(1,self.up1):
            wah_ssr = random.randint(1, 18)

            _path = ssr[wah_ssr]
            lb.setText('欧气降临 SSR！！！')
            self._ssr += 1
        elif wah in range(self.up1,self.up2):
            wah_sr = random.randint(1, 43)

            _path = sr[wah_sr]
            lb.setText('SR')
            self._sr +=1
        elif wah in range(self.up2,10000):
            wah_r = random.randint(1, 33)

            _path = r[wah_r]
            lb.setText('R')
            self._r +=1
        _pix = QPixmap(_path)
        la.setPixmap(_pix)
if __name__=='__main__':
    app = QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec())
