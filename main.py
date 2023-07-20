import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from math import sin, cos, tan, log10, radians

class CalculatorApp(App):
    def build(self):
        self.expression = TextInput(font_size=40, multiline=False, readonly=True, halign='right')
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+'],
            ['sin', 'cos', 'tan', 'log']
        ]

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.expression)

        for row in buttons:
            row_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                button.bind(on_press=self.on_button_press)
                row_layout.add_widget(button)
            layout.add_widget(row_layout)

        return layout

    def on_button_press(self, instance):
        current_text = self.expression.text
        button_text = instance.text

        if button_text == 'C':
            self.expression.text = ''
        elif button_text == '=':
            try:
                result = str(eval(current_text))
                self.expression.text = result
            except Exception as e:
                self.expression.text = 'Erro'
        elif button_text == 'sin':
            try:
                radian = radians(float(current_text))
                self.expression.text = str(sin(radian))
            except Exception as e:
                self.expression.text = 'Erro'
        elif button_text == 'cos':
            try:
                radian = radians(float(current_text))
                self.expression.text = str(cos(radian))
            except Exception as e:
                self.expression.text = 'Erro'
        elif button_text == 'tan':
            try:
                radian = radians(float(current_text))
                self.expression.text = str(tan(radian))
            except Exception as e:
                self.expression.text = 'Erro'
        elif button_text == 'log':
            try:
                self.expression.text = str(log10(float(current_text)))
            except Exception as e:
                self.expression.text = 'Erro'
        else:
            self.expression.text += button_text

if __name__ == '__main__':
    CalculatorApp().run()
