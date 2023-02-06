class NegativeTitlesError(Exception):
    def __init__(self, message, status):
        self.message = message,
        self.status = int(status)


# Isso aqui foi uma tentativa de usar uma classe personalizada de erro
def data_processing(**data):
    firt_cup = int(data["first_cup"].split("-")[0])
    try:
        if data["titles"] < 0:
            raise NegativeTitlesError({"error": "titles cannot be negative"}, 400)
    except NegativeTitlesError as error:
        print(error.message)
