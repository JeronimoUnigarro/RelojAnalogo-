from flask import Flask, render_template
import datetime

app = Flask(__name__)

class CircularList:
    def __init__(self, data):
        self.data = data
    
    def get(self, index):
        # Retorna el elemento en una posición, haciendo que la lista sea circular
        return self.data[index % len(self.data)]

class Clock:
    def __init__(self):
        # Círculo de números en el reloj (1 a 12)
        self.numbers = CircularList([str(i) for i in range(1, 13)])

    def get_current_time(self):
        now = datetime.datetime.now()
        hour = now.hour % 12  # Convertimos a formato de 12 horas
        minute = now.minute
        second = now.second
        return hour, minute, second

    def get_positions(self):
        hour, minute, second = self.get_current_time()
        return {
            'hour_position': self.numbers.get(hour),
            'minute_position': self.numbers.get(minute // 5),
            'second_position': self.numbers.get(second // 5)
        }

@app.route('/')
def index():
    clock = Clock()
    positions = clock.get_positions()
    return render_template('index.html', **positions)

if __name__ == "__main__":
    app.run(debug=True)
