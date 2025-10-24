# user_profile.py
# Import necessary modules
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Настройки графического интерфейса приложения."""
        self.setGeometry(100, 100, 350, 600)  # Увеличил высоту для новых блоков
        self.setWindowTitle("Профиль")
        self.setUpMainWindow()
        self.show()

    def createImageLabels(self):
        """Открывает файлы изображений и создаёт метки изображений."""
        try:
            # Основное фото профиля
            image_path = r"C:\Users\vem16\Downloads\Telegram Desktop\photo_2025-10-25_01-42-46.jpg"
            profile_label = QLabel(self)
            pixmap = QPixmap(image_path)

            if not pixmap.isNull():
                # Масштабируем фото профиля с сохранением пропорций
                pixmap = pixmap.scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio,
                                       Qt.TransformationMode.SmoothTransformation)
                profile_label.setPixmap(pixmap)
                profile_label.move(115, 30)  # Центрируем по горизонтали
            else:
                print("Не удалось загрузить фото профиля")

        except Exception as error:
            print(f"Error loading image: {error}")

    def setUpMainWindow(self):
        """Создайте метки, которые будут отображаться в окне."""
        self.createImageLabels()

        # Имя пользователя - центрируем
        user_label = QLabel(self)
        user_label.setText("Егор Вольников")
        user_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        user_label.resize(300, 30)
        user_label.move(25, 160)
        user_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Заголовок "Биография"
        bio_label = QLabel(self)
        bio_label.setText("Биография")
        bio_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        bio_label.move(25, 200)
        bio_label.resize(300, 25)

        # Текст биографии
        about_label = QLabel(self)
        about_label.setText("Я студент 2 курса Московского Авиационного Института. Кафедра 317 - 'Инноватика.'")
        about_label.setFont(QFont("Arial", 11))
        about_label.setWordWrap(True)
        about_label.move(25, 230)
        about_label.resize(300, 60)

        # Блок УМЕНИЯ
        skills_title = QLabel(self)
        skills_title.setText("Умения")
        skills_title.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        skills_title.move(25, 300)  # Сдвинул ниже
        skills_title.resize(300, 25)

        skills_content = QLabel(self)
        skills_content.setText(
            "• Python\n"
            "• MySQL\n"
            "• Git и системы контроля версий\n"
        )
        skills_content.setFont(QFont("Arial", 10))
        skills_content.setWordWrap(True)
        skills_content.move(25, 330)
        skills_content.resize(300, 100)

        # Блок ОПЫТ РАБОТЫ
        experience_title = QLabel(self)
        experience_title.setText("Опыт работы")
        experience_title.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        experience_title.move(25, 440)  # Сдвинул ниже
        experience_title.resize(300, 25)

        experience_content = QLabel(self)
        experience_content.setText(
            "Подсобный рабочий\n"
            "июнь 2023 - август 2023\n"
            
            "Фриланс проекты\n"
            "август 2024 - декабрь 2024\n"

        )
        experience_content.setFont(QFont("Arial", 10))
        experience_content.setWordWrap(True)
        experience_content.move(25, 470)
        experience_content.resize(300, 130)


# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())