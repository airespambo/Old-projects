#Feito por Aires Sealtiel Pedro Pambo Nº 24 II11A, exercício 3 do nível 3, Galeria
#Galeria capaz de editar minimamente as fotografias e abrir os vídeos no reprodutor do pc
#Obs, só funciona em PC
#Feito sem IA
#Rode esse ficheiro
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QSizePolicy, QCheckBox, QPushButton, QGridLayout, QScrollArea, QMenu
from PyQt5.QtGui import QIcon, QFont, QPixmap, QImage
from PyQt5.QtCore import QSize, Qt
from style.style import Style as s
from func.func import Func as f
import cv2

class MainWindow(QMainWindow):

    def __init__(self) -> None:

        super().__init__()
        self.screen = app.primaryScreen().availableGeometry() #type: ignore
        screen_width = self.screen.width()
        screen_heigth = self.screen.height()

        width = int(screen_width * 0.5)
        heigth = int(screen_heigth * 0.5 + (screen_heigth * 0.1))

        x = int(screen_width * 0.25)
        y = int(screen_heigth * 0.25)

        self.setGeometry(x, y, width, heigth)
        self.setMinimumSize(width, heigth)
        self.setWindowTitle('Galeria')
        self.setWindowIcon(QIcon('icons/icon.png'))
        self.setStyleSheet('background-color: #353535')

        self.files = f().get_files()
        self.opened_file = QWidget(self)
        self.opened_file.setGeometry(0, 0, self.width(), self.height())
        self.opened_file.setStyleSheet('background-color: #272727')
        self.opened_file.hide()
        self.media_opened = QPushButton(self.opened_file)

        self.back = QPushButton(self.opened_file)
        self.edit_btn = QPushButton(self.opened_file)
        self.delete_btn = QPushButton(self.opened_file)
        self.next_btn = QPushButton(self.opened_file)
        self.previuous_btn = QPushButton(self.opened_file)

        self.header = QWidget(self)
        self.title_pixmap = QLabel(self.header)
        self.title = QLabel('Galeria', self.header)
        self.delete_main_btn = QPushButton(self.header)
        self.options_menu = QMenu(self)

        self.edit_action = self.options_menu.addAction('Editar')
        self.delete_action = self.options_menu.addAction('Eliminar')
        
        self.hight_contrast_edit = QPushButton(self.opened_file)
        self.gray_edit = QPushButton(self.opened_file)
        self.save_edit = QPushButton(self.opened_file)
        self.leave_edit = QPushButton(self.opened_file)
        self.aux = dict()
        self.current_img = dict()
        self.selected_items = list()
        self.selected_files = list()
        self.thumbnails = dict()
        self.file_grid = QWidget(self)
        self.photo_grid_title = QLabel('Fotos e Vídeos', self.file_grid)
        self.photo_grid = QWidget()
        self.file_layout = QGridLayout()
        self.file_scroll = QScrollArea(self.file_grid)
        
        self.init_header()
        self.init_file_grid()
    
    def init_header(self) -> None:

        self.header.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.header.setGeometry(0, 0, self.width(), 60)
        self.header.setStyleSheet('background-color: #191919; border-bottom: 1px solid #211f1f;')

        self.title_pixmap.setPixmap(QPixmap('icons/title.png'))
        self.title_pixmap.setScaledContents(True)
        self.title_pixmap.setGeometry(20, 15, 25, 25)

        self.title.setGeometry(60, 12, self.title.width(), self.title.height())
        self.title.setFont(QFont('Segoe UI', 15, 75))
        self.title.setStyleSheet('color: white; background-color: transparent;text-decoration: none;')
        self.title.adjustSize()

        self.delete_main_btn.setIcon(QIcon('icons/delete.png'))
        self.delete_main_btn.setGeometry(self.header.width() - 60, 15, 40, 40)
        self.delete_main_btn.setIconSize(QSize(20, 20))
        self.delete_main_btn.setStyleSheet(s.button + s.button_hover + s.button_pressed)
        self.delete_main_btn.clicked.connect(self.delete_files)
        self.delete_main_btn.hide()

    def init_file_grid(self) -> None:

        self.file_grid.setGeometry(0, 60, self.width(), (self.height() - 60))
        self.file_grid.setStyleSheet('background-color: #272727;')

        self.photo_grid_title.setGeometry(30, 10, self.photo_grid_title.width(), self.photo_grid_title.height())
        self.photo_grid_title.setFont(QFont('Segoe UI', 18, 60))# type: ignore
        self.photo_grid_title.setStyleSheet('background-color: transparent; color: white;')
        self.photo_grid_title.adjustSize()
        self.photo_grid.raise_()
        self.file_scroll.setWidget(self.photo_grid)# type: ignore
        self.file_scroll.setGeometry(
            0, 60, self.file_grid.width(),
            int((len(self.files) / 6) * (self.file_grid.width() / 6)) + int(self.file_grid.width() * 0.3)
        ) #type: ignore
        self.file_scroll.setStyleSheet('border: none;')#type: ignore
        self.file_scroll.verticalScrollBar().setStyleSheet(s.scroll_bar)

        if len(self.files) <= 6:
            self.photo_grid.setGeometry(
                0, 
                60, 
                self.file_grid.width(), 
                int(self.file_grid.width() / 6) + int(self.file_grid.width() * 0.3)
            )
        else:
            self.photo_grid.setGeometry(0, 60, self.file_grid.width(), int((len(self.files) / 6) * (self.file_grid.width() / 6)))
        self.photo_grid.setStyleSheet('background-color: #353535;')

        self.file_layout.setAlignment(Qt.AlignTop) # type: ignore

        i = 0
        print(len(self.files))
        if len(self.files) % 6 == 0:
            for l in range(int(len(self.files) / 6 )):
                for c in range(6):
                    temp_widget = QWidget()
                    temp_checkbox = QCheckBox(temp_widget)
                    temp = QPushButton(temp_widget)
                    if i >= len(self.files):
                        break
                    if self.files[i].endswith(f.video_ext):#type: ignore
                        cap = cv2.VideoCapture(self.files[i])
                        cap.set(cv2.CAP_PROP_POS_MSEC, 2000)
                        _, frame = cap.read()
                        cap.release()
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        h, w, ch = frame.shape
                        img = QImage(frame.data, w, h, ch * w, QImage.Format_RGB888)
                        pix = QPixmap.fromImage(img)
                        temp.setIcon(QIcon(pix))
                        self.thumbnails[self.files[i]] = pix
                        video_icon = QLabel(temp_widget)
                        video_icon.setPixmap(QPixmap("icons/video.png"))
                        video_icon.setScaledContents(True)
                        video_icon.setGeometry(temp.width() - 25, temp.height() - 25, 20, 20)
                        video_icon.setStyleSheet('background-color: transparent;')
                        video_icon.raise_()
                        video_icon.setAttribute(Qt.WA_TransparentForMouseEvents, True)
                    else:
                        temp.setIcon(QIcon(self.files[i]))
                    temp_checkbox.setGeometry(5, 5, 15, 15)
                    temp_checkbox.setStyleSheet(s.checkbox)
                    temp_checkbox.toggled.connect(lambda checked, file = self.files[i], item = temp_widget: self.add_selected_items(checked, file, item,))
                    temp_checkbox.setStyleSheet(s.checkbox)
                    temp_checkbox.raise_()
                    temp_widget.setFixedSize(QSize(int(self.photo_grid.width() / 6) - 10, int(self.photo_grid.width() / 6) - 10))
                    temp_widget.setStyleSheet('border-radius: 5px;')
                    temp.setFixedSize(QSize(int(self.photo_grid.width() / 6) - 10, int(self.photo_grid.width() / 6) - 10))
                    temp.setIconSize(QSize(temp.width() - 20, temp.height() - 20))
                    temp.setStyleSheet(s.button + s.button_hover + s.button_pressed)
                    temp.clicked.connect(lambda _, a = self.files[i], item = temp_widget : self.open_file(a, item))
                    temp.setContextMenuPolicy(Qt.CustomContextMenu)
                    temp.customContextMenuRequested.connect(lambda _, b = self.files[i], item = temp_widget: self.show_menu(b, item))
                    self.file_layout.addWidget(temp_widget, l, c)
                    i += 1
        else:
            for l in range(int((len(self.files) / 6 ) + ((len(self.files) % 6) / (len(self.files) % 6)))):
                for c in range(6):
                    temp_widget = QWidget()
                    temp_checkbox = QCheckBox(temp_widget)
                    temp = QPushButton(temp_widget)
                    if i >= len(self.files):
                        break
                    if self.files[i].endswith(f.video_ext):#type: ignore
                        cap = cv2.VideoCapture(self.files[i])
                        cap.set(cv2.CAP_PROP_POS_MSEC, 2000)
                        _, frame = cap.read()
                        cap.release()
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        h, w, ch = frame.shape
                        img = QImage(frame.data, w, h, ch * w, QImage.Format_RGB888)
                        pix = QPixmap.fromImage(img)
                        self.thumbnails[self.files[i]] = pix
                        temp.setIcon(QIcon(pix))
                        video_icon = QLabel(temp_widget)
                        video_icon.setPixmap(QPixmap("icons/video.png"))
                        video_icon.setScaledContents(True)
                        video_icon.setGeometry(temp.width() - 25, temp.height() - 25, 20, 20)
                        video_icon.setStyleSheet('background-color: transparent;')
                        video_icon.raise_()
                        video_icon.setAttribute(Qt.WA_TransparentForMouseEvents, True)
                    else:
                        temp.setIcon(QIcon(self.files[i]))
                    temp_checkbox.setGeometry(5, 5, 15, 15)
                    temp_checkbox.setStyleSheet(s.checkbox)
                    temp_checkbox.toggled.connect(lambda checked, file = self.files[i], item = temp_widget: self.add_selected_items(checked, file, item))
                    temp_checkbox.setStyleSheet(s.checkbox)
                    temp_checkbox.setAttribute(Qt.WA_TransparentForMouseEvents, False)
                    temp_checkbox.raise_()
                    temp_widget.setFixedSize(QSize(int(self.photo_grid.width() / 6) - 10, int(self.photo_grid.width() / 6) - 10))
                    temp_widget.setStyleSheet('border-radius: 5px;')
                    temp.setFixedSize(QSize(int(self.photo_grid.width() / 6) - 10, int(self.photo_grid.width() / 6) - 10))
                    temp.setIconSize(QSize(temp.width() - 20, temp.height() - 20))
                    temp.setStyleSheet(s.button + s.button_hover + s.button_pressed)
                    temp.clicked.connect(lambda _, file = self.files[i], item = temp_widget : self.open_file(file, item))
                    temp.setContextMenuPolicy(Qt.CustomContextMenu)
                    temp.customContextMenuRequested.connect(lambda _, file = self.files[i], item = temp_widget: self.show_menu(file, item))
                    self.file_layout.addWidget(temp_widget, l, c)
                    i += 1
        self.photo_grid.setLayout(self.file_layout)
        self.photo_grid.raise_()
        self.file_scroll.resize(self.file_grid.width(), self.file_grid.height())

    def resizeEvent(self, event) -> None:

        self.header.resize(self.width(), 60)
        self.delete_main_btn.move(self.header.width() - 60, 10)
        self.file_grid.resize(self.width(), self.height() - 60)
        self.photo_grid.resize(self.file_grid.width(), int((self.file_grid.width() / 6) * (self.file_layout.count() / 6)) + int(self.file_grid.width() * 0.3))
        self.opened_file.resize(self.width(), self.height())
        self.media_opened.setFixedSize(QSize(self.opened_file.width() - 300, self.opened_file.height()))
        self.media_opened.setIconSize(QSize(self.opened_file.width() - 300, self.opened_file.height()))
        self.delete_btn.move(self.opened_file.width() - 100, 15)
        self.edit_btn.move(self.opened_file.width() - 155, 15)
        self.next_btn.move(self.width() - 100, int(self.height() / 2) - 50)
        self.previuous_btn.move(50, int(self.height() / 2) - 50)

        self.leave_edit.move(self.width() - 55, 15)
        self.save_edit.move(self.width() - 110, 15)
        self.gray_edit.move(self.width() - 110, self.height() - 55)
        self.hight_contrast_edit.move(self.width() - 55, self.height() - 55)

        for i in range(self.photo_grid.layout().count()):

            self.photo_grid.layout().itemAt(i).widget().setFixedSize(QSize(int(self.photo_grid.width() / 6) - 10, int(self.photo_grid.width() / 6) - 10))
            self.photo_grid.layout().itemAt(i).widget().findChild(QPushButton).setIconSize(QSize(int(self.photo_grid.width() / 6) - 20, int(self.photo_grid.width() / 6) - 20))
            self.photo_grid.layout().itemAt(i).widget().findChild(QPushButton).setFixedSize(QSize(int(self.photo_grid.width() / 6) - 10, int(self.photo_grid.width() / 6) - 10))
        
        self.file_scroll.resize(self.file_grid.width(), self.file_grid.height())

    def open_file(self, file: str, item: QWidget | None) -> None:

        self.delete_btn.show()
        self.edit_btn.show()
        self.back.show()
        self.next_btn.show()
        self.previuous_btn.show()

        self.hight_contrast_edit.hide()
        self.gray_edit.hide()
        self.save_edit.hide()
        self.leave_edit.hide()

        try:

            self.media_opened.clicked.disconnect()
            self.delete_btn.clicked.disconnect()

        except:

            pass

        self.back.setGeometry(15, 15, 40, 40)
        self.back.setStyleSheet(s.button + s.button_hover + s.button_pressed)
        self.back.setIcon(QIcon('icons/back.png'))
        self.back.setIconSize(QSize(25, 25))
        self.back.clicked.connect(self.hide_opened_file)

        self.delete_btn.setGeometry(self.opened_file.width() - 55, 15, 40, 40)
        self.delete_btn.setStyleSheet(s.button + s.button_hover + s.button_pressed)
        self.delete_btn.setIcon(QIcon('icons/delete.png'))
        self.delete_btn.setIconSize(QSize(25, 25))
        self.delete_btn.clicked.connect(lambda _file = file, _item = item: self.out_delete(file, item))

        self.edit_btn.setGeometry(self.opened_file.width() - 100, 15, 40, 40)
        self.edit_btn.setStyleSheet(s.c_button + s.c_button_hover + s.c_button_pressed)
        self.edit_btn.setIcon(QIcon('icons/edit.png'))
        self.edit_btn.setIconSize(QSize(25, 25))
        self.edit_btn.clicked.connect(lambda _file = file: self.edit_file(file))

        self.next_btn.setGeometry(self.width() - 100, int(self.height() / 2) - 50, 50, 50)
        self.next_btn.setIcon(QIcon('icons/next.png'))
        self.next_btn.setIconSize(QSize(50, 50))
        self.next_btn.setStyleSheet(s.button + s.button_hover + s.button_pressed)
        self.next_btn.clicked.connect(lambda _file = file, _item = item: self.next_file(file, item))

        self.previuous_btn.setGeometry(50, int(self.height() / 2) - 50, 50, 50)
        self.previuous_btn.setIcon(QIcon('icons/previous.png'))
        self.previuous_btn.setIconSize(QSize(50, 50))
        self.previuous_btn.setStyleSheet(s.button + s.button_hover + s.button_pressed)
        self.previuous_btn.clicked.connect(lambda _file = file, _item = item: self.previous_file(file, item))

        if file.endswith(f.video_ext):
            
            self.media_opened.clicked.connect(lambda _file = file:self.open_video(file))
            video_icon = QLabel(self.media_opened)
            video_icon.setPixmap(QPixmap("icons/video.png"))
            video_icon.setScaledContents(True)
            video_icon.setGeometry(25, 25, 100, 100)
            video_icon.setStyleSheet('background-color: transparent;')
            video_icon.raise_()
            video_icon.setAttribute(Qt.WA_TransparentForMouseEvents, True)
            self.edit_btn.hide()
        
        else:
            self.edit_btn.raise_()

        self.opened_file.show()
        self.opened_file.raise_()

        self.media_opened.setGeometry(150, 0, self.opened_file.width() - 300, self.opened_file.height())
        self.media_opened.setStyleSheet(s.photo_button)
        self.media_opened.setIconSize(QSize(self.opened_file.width() - 300, self.opened_file.height()))
        
        if file.endswith(f.video_ext):

            icon = self.thumbnails[file]
            self.media_opened.setIcon(QIcon(icon))
            
        else:
            self.media_opened.setIcon(QIcon(file))
            self.aux = file

        self.media_opened.setIconSize(QSize(self.media_opened.width(), self.media_opened.height()))
        self.media_opened.raise_()

    def hide_opened_file(self) -> None:

        self.opened_file.hide()

    def show_menu(self, file: str, item: QWidget) -> None:
        try:

            self.edit_action.triggered.disconnect()
            self.delete_action.triggered.disconnect()

        except:

            pass

        status = False
        if self.options_menu.actions():
            for action in self.options_menu.actions():

                if action.text() == 'Editar':

                    self.options_menu.removeAction(self.edit_action)
                    self.options_menu.removeAction(self.delete_action)
                    status = True
                    break

            if  not status:

                self.options_menu.removeAction(self.delete_action)

        self.edit_action.triggered.connect(lambda _file = file: self.show_edit(file))
        self.delete_action.triggered.connect(lambda _file = file, _item = item: self.delete_file(file, item))

        if file.endswith(f.video_ext):

            self.options_menu.addAction(self.delete_action)
        
        else:

            self.options_menu.addAction(self.edit_action)
            self.options_menu.addAction(self.delete_action)


        self.options_menu.setFont(QFont('Segoe UI', 10))
        self.setStyleSheet(
            'QMenu {background-color: #2d2d2d;color: white;border: 1px solid #444;border-radius: 10px}'+
            'QMenu::item:selected {background-color: #444;}'
        )
        self.options_menu.exec_(item.mapToGlobal(item.rect().bottomRight()))
    
    def reload_files(self) -> None:

        self.clear_layout()
        self.re_init_file_grid()

    def clear_layout(self) -> None:

        while self.file_layout.count():
            item = self.file_layout.takeAt(0)
            widget = item.widget()

            if widget:
                widget.setParent(None)
                widget.deleteLater()
    
    def delete_file(self, file: str, item: QWidget) -> None:
        try:
            self.file_layout.removeWidget(item)
            item.deleteLater()
            self.files.remove(file)
            f().delete(file)
            self.reload_files()
        except:
            pass      

    def delete_files(self) -> None:

        try:

            self.delete_main_btn.clicked.disconnect()
            for item in self.selected_items:

                self.file_layout.removeWidget(item)
                item.deleteLater()

            for file in self.selected_files:

                self.files.remove(file)
                f().delete(file)

            self.selected_items.clear()
            self.selected_files.clear()
            self.reload_files()
        except:

            pass
        self.show_del_button()     

    def edit_file(self, file: str) -> None:
        
        self.next_btn.hide()
        self.previuous_btn.hide()
        self.delete_btn.hide()
        self.edit_btn.hide()
        self.back.hide()

        self.open_edit_menu(file)      

    def open_edit_menu(self, file: str) -> None:

        try:
            self.hight_contrast_edit.clicked.disconnect()
            self.gray_edit.clicked.disconnect()
            self.save_edit.clicked.disconnect()
            self.leave_edit.clicked.disconnect()
        except:
            pass

        self.hight_contrast_edit.setGeometry(self.width() - 55, self.height() - 55, 40, 40)
        self.hight_contrast_edit.setIcon(QIcon('icons/contrast.png'))
        self.hight_contrast_edit.setIconSize(QSize(20, 20))
        self.hight_contrast_edit.setStyleSheet(s.button + s.button_hover + s.button_pressed)
        self.hight_contrast_edit.clicked.connect(lambda _file = file: self.apply_hight_contrast_filter(file))

        self.gray_edit.setGeometry(self.width() - 110, self.height() - 55, 40, 40)
        self.gray_edit.setIcon(QIcon('icons/gray_scale.png'))
        self.gray_edit.setIconSize(QSize(20, 20))
        self.gray_edit.setStyleSheet(s.button + s.button_hover + s.button_pressed)
        self.gray_edit.clicked.connect(lambda _file = file: self.apply_gray_scale_filter(file))

        self.save_edit.setGeometry(self.width() - 110, 15, 40, 40)
        self.save_edit.setIcon(QIcon('icons/save.png'))
        self.save_edit.setIconSize(QSize(20, 20))
        self.save_edit.setStyleSheet(s.button + s.c_button_hover + s.c_button_pressed)
        self.save_edit.clicked.connect(lambda _file = file: self.save_changes(file))

        self.leave_edit.setGeometry(self.width() - 55, 15, 40, 40)
        self.leave_edit.setIcon(QIcon('icons/leave.png'))
        self.leave_edit.setIconSize(QSize(20, 20))
        self.leave_edit.setStyleSheet(s.button + s.v_button_hover + s.v_button_pressed)
        self.leave_edit.clicked.connect(self.leave_changes)

        self.hight_contrast_edit.show()
        self.gray_edit.show()
        self.save_edit.show()
        self.leave_edit.show()

        self.hight_contrast_edit.raise_()
        self.gray_edit.raise_()
        self.save_edit.raise_()
        self.leave_edit.raise_()

    def add_selected_items(self, checked: bool, file: str, item: QWidget) -> None:

        if checked:

            self.selected_items.append(item)
            self.selected_files.append(file)
        
        else:

            try:

                self.selected_items.remove(item)
                self.selected_files.remove(file)

            except:

                pass

        self.show_del_button()

    def open_video(self, file: str) -> None:

        f().open_v(file)

    def re_init_file_grid(self) -> None:

        self.files.clear()
        self.files = f().get_files()
        self.file_grid.setGeometry(0, 60, self.width(), (self.height() - 60))
        self.file_grid.setStyleSheet('background-color: #272727;')

        self.photo_grid_title.setGeometry(30, 10, self.photo_grid_title.width(), self.photo_grid_title.height())
        self.photo_grid_title.setFont(QFont('Segoe UI', 18, 60))# type: ignore
        self.photo_grid_title.setStyleSheet('background-color: transparent; color: white;')
        self.photo_grid_title.adjustSize()
        self.photo_grid.raise_()
        self.file_scroll.setWidget(self.photo_grid)# type: ignore
        self.file_scroll.setGeometry(0, 60, self.file_grid.width(), int((len(self.files) / 6) * (self.file_grid.width() / 6)) + int(self.file_grid.width() * 0.3)) #type: ignore
        self.file_scroll.setStyleSheet('border: none;')#type: ignore
        self.file_scroll.verticalScrollBar().setStyleSheet(s.scroll_bar)

        if len(self.files) <= 6:
            self.photo_grid.setGeometry(0, 60, self.file_grid.width(), int(self.file_grid.width() / 6) + int(self.file_grid.width() * 0.3))
        else:
            self.photo_grid.setGeometry(0, 60, self.file_grid.width(), int((len(self.files) / 6) * (self.file_grid.width() / 6)))
        self.photo_grid.setStyleSheet('background-color: #353535;')

        self.file_layout.setAlignment(Qt.AlignTop) # type: ignore

        i = 0
        print(len(self.files))
        if len(self.files) % 6 == 0:
            for l in range(int(len(self.files) / 6 )):
                for c in range(6):
                    temp_widget = QWidget()
                    temp_checkbox = QCheckBox(temp_widget)
                    temp = QPushButton(temp_widget)
                    if i >= len(self.files):
                        break
                    if self.files[i].endswith(f.video_ext):#type: ignore

                        temp.setIcon(QIcon(self.thumbnails[self.files[i]]))
                        video_icon = QLabel(temp_widget)
                        video_icon.setPixmap(QPixmap("icons/video.png"))
                        video_icon.setScaledContents(True)
                        video_icon.setGeometry(temp.width() - 25, temp.height() - 25, 20, 20)
                        video_icon.setStyleSheet('background-color: transparent;')
                        video_icon.raise_()
                        video_icon.setAttribute(Qt.WA_TransparentForMouseEvents, True)
                
                    else:

                        temp.setIcon(QIcon(self.files[i]))

                    temp_checkbox.setGeometry(5, 5, 15, 15)
                    temp_checkbox.setStyleSheet(s.checkbox)
                    temp_checkbox.toggled.connect(lambda checked, file = self.files[i], item = temp_widget: self.add_selected_items(checked, file, item))
                    temp_checkbox.setStyleSheet(s.checkbox)
                    temp_checkbox.setAttribute(Qt.WA_TransparentForMouseEvents, False)
                    temp_checkbox.raise_()
                    temp_widget.setFixedSize(QSize(int(self.photo_grid.width() / 6) - 10, int(self.photo_grid.width() / 6) - 10))
                    temp_widget.setStyleSheet('border-radius: 5px;')
                    temp.setFixedSize(QSize(int(self.photo_grid.width() / 6) - 10, int(self.photo_grid.width() / 6) - 10))
                    temp.setIconSize(QSize(temp.width() - 20, temp.height() - 20))
                    temp.setStyleSheet(s.button + s.button_hover + s.button_pressed)
                    temp.clicked.connect(lambda _, file = self.files[i], item = temp_widget : self.open_file(file, item))
                    temp.setContextMenuPolicy(Qt.CustomContextMenu)
                    temp.customContextMenuRequested.connect(lambda _, file = self.files[i], item = temp_widget: self.show_menu(file, item))
                    self.file_layout.addWidget(temp_widget, l, c)
                    i += 1
        else:
            for l in range(int((len(self.files) / 6 ) + ((len(self.files) % 6) / (len(self.files) % 6)))):
                for c in range(6):
                    temp_widget = QWidget()
                    temp_checkbox = QCheckBox(temp_widget)
                    temp = QPushButton(temp_widget)
                    if i >= len(self.files):
                        break
                    if self.files[i].endswith(f.video_ext):#type: ignore

                        temp.setIcon(QIcon(self.thumbnails[self.files[i]]))
                        video_icon = QLabel(temp_widget)
                        video_icon.setPixmap(QPixmap("icons/video.png"))
                        video_icon.setScaledContents(True)
                        video_icon.setGeometry(temp.width() - 25, temp.height() - 25, 20, 20)
                        video_icon.setStyleSheet('background-color: transparent;')
                        video_icon.raise_()
                        video_icon.setAttribute(Qt.WA_TransparentForMouseEvents, True)

                    else:
                        temp.setIcon(QIcon(self.files[i]))

                    temp_checkbox.setGeometry(5, 5, 15, 15)
                    temp_checkbox.setStyleSheet(s.checkbox)
                    temp_checkbox.toggled.connect(lambda checked, file = self.files[i], item = temp_widget: self.add_selected_items(checked ,file, item))
                    temp_checkbox.setStyleSheet(s.checkbox)
                    temp_checkbox.setAttribute(Qt.WA_TransparentForMouseEvents, False)
                    temp_checkbox.raise_()
                    temp_widget.setFixedSize(QSize(int(self.photo_grid.width() / 6) - 10, int(self.photo_grid.width() / 6) - 10))
                    temp_widget.setStyleSheet('border-radius: 5px;')
                    temp.setFixedSize(QSize(int(self.photo_grid.width() / 6) - 10, int(self.photo_grid.width() / 6) - 10))
                    temp.setIconSize(QSize(temp.width() - 20, temp.height() - 20))
                    temp.setStyleSheet(s.button + s.button_hover + s.button_pressed)
                    temp.clicked.connect(lambda _, file = self.files[i], item = temp_widget : self.open_file(file, item))
                    temp.setContextMenuPolicy(Qt.CustomContextMenu)
                    temp.customContextMenuRequested.connect(lambda _, file = self.files[i], item = temp_widget: self.show_menu(file, item))
                    self.file_layout.addWidget(temp_widget, l, c)
                    i += 1
        self.photo_grid.setLayout(self.file_layout)
        self.photo_grid.raise_()
        self.file_scroll.resize(self.file_grid.width(), self.file_grid.height())

    def show_del_button(self) -> None:

        print(len(self.selected_items))
        if len(self.selected_items) != 0:

            self.delete_main_btn.show()
            self.delete_main_btn.raise_()
        
        else:

            self.delete_main_btn.hide()

    def out_delete(self, file: str, item: QWidget) -> None:

        self.hide_opened_file()
        self.delete_file(file, item)

    def save_changes(self, file: str) -> None:
        
        img = self.current_img['img']
        temp = f().save(img, file)

        self.delete_btn.show()
        self.edit_btn.show()
        self.back.show()

        self.hight_contrast_edit.hide()
        self.gray_edit.hide()
        self.save_edit.hide()
        self.leave_edit.hide()

        self.reload_files()
    
    def leave_changes(self) -> None:

        self.media_opened.setIcon(QIcon(self.aux))
        self.media_opened.setIconSize(QSize(self.media_opened.width(), self.media_opened.height()))
        
        self.delete_btn.show()
        self.edit_btn.show()
        self.back.show()
        self.next_btn.show()
        self.previuous_btn.show()

        self.hight_contrast_edit.hide()
        self.gray_edit.hide()
        self.save_edit.hide()
        self.leave_edit.hide()

    def apply_hight_contrast_filter(self, file: str) -> None:

        try:
            img = cv2.imread(file)
            img_contrast = cv2.convertScaleAbs(img, alpha=2.5, beta=0)
            self.current_img['img'] = img_contrast
            icon = QIcon(QPixmap.fromImage(QImage(img_contrast.data,img_contrast.shape[1],img_contrast.shape[0],img_contrast.strides[0],QImage.Format_BGR888)))
            self.media_opened.setIcon(QIcon(icon))
        except:
            print(f'imagem inválida{file}')

    def apply_gray_scale_filter(self, file: str) -> None:

        try:
            img = cv2.imread(file)
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            self.current_img['img'] = img_gray
            icon = QIcon(QPixmap.fromImage(QImage(img_gray.data, img_gray.shape[1], img_gray.shape[0], img_gray.strides[0], QImage.Format_Grayscale8)))
            self.media_opened.setIcon(QIcon(icon))
        
        except:
            print(f'imagem inválida{file}')

    def show_edit(self, file: str) -> None:

        self.open_file(file , item = None)
        self.edit_file(file)

    def next_file(self, file: str, item: QWidget) -> None:


        try:
            i = self.files.index(file)
            i += 1
            temp = self.files[i]
            self.open_file(temp, item)
        except:

            pass
    
    def previous_file(self, file: str, item: QWidget) -> None:

        try:
            i = self.files.index(file)
            i -= 1
            temp = self.files[i]
            self.open_file(temp, item)
        except:

            pass


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())