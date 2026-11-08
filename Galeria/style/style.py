class Style():
    #album_button = 'QPushButton {border: none; background: transparent;color: white;}'
    photo_button = 'background-color: #191919; border: none;'
    button = 'QPushButton {border: none; background: transparent;}'
    button_hover = 'QPushButton:hover {background-color: #6B6B6B; border-radius: 5px;}'
    button_pressed = 'QPushButton:pressed {background-color: #A5A5A5; border-radius: 5px;}'
    album_button = 'QPushButton {border: none; background: transparent;color: white;}'
    c_button = 'QPushButton {border: none; background: #0793FF;color:white; border-radius: 5px}'
    c_button_hover = 'QPushButton:hover {background-color: #32a6ff; border-radius: 5px;}'
    c_button_pressed = 'QPushButton:pressed {background-color: #49b0ff; border-radius: 5px;}'

    v_button_pressed = 'QPushButton:pressed {background-color: #ff0000; border-radius: 5px;}'
    v_button_hover = 'QPushButton:hover {background-color: #ba3434; border-radius: 5px;}'

    checkbox = 'background-color: transparent;'

    scroll_bar = """
        QScrollBar:vertical {background: transparent;width: 10px;margin: 0px;}
        QScrollBar::handle:vertical {background: #4a4a4a;border-radius: 5px;min-height: 30px;}
        QScrollBar::handle:vertical:hover {background: #666666;}
        QScrollBar::handle:vertical:pressed {background: #808080;}
        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical {height: 0px;}
        QScrollBar::add-page:vertical,
        QScrollBar::sub-page:vertical {background: transparent;}"""
    
    checkbox = ''