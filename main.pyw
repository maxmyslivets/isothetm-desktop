import sys
from PySide6.QtGui import QGuiApplication


from Model.___ import ___
from Controller.___ import ___


def main() -> None:

    app = QGuiApplication(sys.argv)

    model = ___()
    controller = ___(model)

    app.exec()


if __name__ == '__main__':
    sys.exit(main())
