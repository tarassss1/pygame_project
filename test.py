from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class TodoListApp(App):
    def build(self):
        self.tasks = []  # Список для зберігання завдань

        # Основний макет програми
        layout = BoxLayout(orientation='vertical')

        # Поле для введення нового завдання
        self.task_input = TextInput(hint_text='Введіть нове завдання')
        layout.add_widget(self.task_input)

        # Кнопка для додавання завдання
        add_button = Button(text='Додати завдання')
        add_button.bind(on_press=self.add_task)
        layout.add_widget(add_button)

        # Список для відображення завдань
        self.task_list = BoxLayout(orientation='vertical')
        layout.add_widget(self.task_list)

        return layout

    def add_task(self, instance):
        task_text = self.task_input.text
        if task_text:
            self.tasks.append(task_text)
            self.update_task_list()

    def update_task_list(self):
        self.task_list.clear_widgets()  # Очищаємо список перед оновленням

        for task_text in self.tasks:
            task_layout = BoxLayout(orientation='horizontal')
            task_label = Label(text=task_text)
            delete_button = Button(text='Видалити', size_hint_x=None, width=100)
            delete_button.bind(on_press=lambda instance, task=task_text: self.delete_task(task))
            task_layout.add_widget(task_label)
            task_layout.add_widget(delete_button)
            self.task_list.add_widget(task_layout)

    def delete_task(self, task_text):
        self.tasks.remove(task_text)
        self.update_task_list()

if __name__ == '__main__':
    TodoListApp().run()
