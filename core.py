class Alphascript:
    def __init__(self):
        self.variables = {"example": "Hello World"}
    def console(self, command: str) -> str:
        args = command.split()

        match args[0].lower():
            case "переменная" | "переменные":
                if len(args) == 1:
                    return "Ошибка! вы не указали переменные"
                for i in args[1:]:
                    self.variables[i] = "None"
                return "Переменные сохранены успешно"

            case "сделать":

