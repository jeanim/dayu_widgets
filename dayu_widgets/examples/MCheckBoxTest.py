#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.qt import *
from dayu_widgets.MCheckBox import MCheckBox
from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MLabel import MLabel
from dayu_widgets.MButton import MButton


class MCheckBoxTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MCheckBoxTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        check_box_1 = MCheckBox('Unchecked')
        check_box_1.setChecked(False)

        check_box_2 = MCheckBox('Checked')
        check_box_2.setChecked(True)

        check_box_3 = MCheckBox('Partially')
        check_box_3.setCheckState(Qt.PartiallyChecked)

        check_box_4 = MCheckBox('Unchecked Disabled')
        check_box_4.setEnabled(False)
        check_box_4.setChecked(False)

        check_box_5 = MCheckBox('Checked Disabled')
        check_box_5.setChecked(True)
        check_box_5.setEnabled(False)

        check_box_6 = MCheckBox('Partially Disabled')
        check_box_6.setEnabled(False)
        check_box_6.setCheckState(Qt.PartiallyChecked)

        grid_lay = QGridLayout()
        grid_lay.addWidget(check_box_1, 0,0)
        grid_lay.addWidget(check_box_2, 0,1)
        grid_lay.addWidget(check_box_3, 0,2)

        grid_lay.addWidget(check_box_4, 1,0)
        grid_lay.addWidget(check_box_5, 1,1)
        grid_lay.addWidget(check_box_6, 1,2)

        check_box_icon_1 = MCheckBox('Folder')
        check_box_icon_1.setIcon(MIcon(''))

        check_box_b = MCheckBox('Data Bind')
        label = MLabel()
        button = MButton(text='Change State')
        button.clicked.connect(lambda :self.set_field('checked', not self.field('checked')))
        self.register_field('checked', True)
        self.register_field('checked_text', lambda :'Yes!' if self.field('checked') else 'No!!')
        self.bind('checked', check_box_b, 'checked', signal='stateChanged')
        self.bind('checked_text', label, 'text')


        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('Basic'))
        main_lay.addLayout(grid_lay)
        main_lay.addWidget(MDivider('Icon'))
        main_lay.addWidget(check_box_icon_1)
        main_lay.addWidget(MDivider('Data Bind'))
        main_lay.addWidget(check_box_b)
        main_lay.addWidget(label)
        main_lay.addWidget(button)
        # main_lay.addWidget(MDivider('MRadioGroup: orientation=Qt.Vertical'))
        # main_lay.addWidget(radio_group_v)
        # main_lay.addWidget(MDivider('MRadioGroup: orientation=Qt.Horizontal type=button'))
        # main_lay.addWidget(radio_group_button_h)
        # main_lay.addWidget(MDivider('MRadioGroup: orientation=Qt.Vertical, type=button'))
        # main_lay.addWidget(radio_group_button_v)
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MCheckBoxTest()
    test.show()
    sys.exit(app.exec_())