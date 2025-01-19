import json

disctionary = {
    "To-do": [
        {
            7: "joga RPG",
            6: "Dar comido pra gamora",
            5: "Jogar X-Com"
        }
    ],

    "In-Progrece": [
        {
            4: "Assistindo Modern Family",
            3: "Joga RPG"
        }
    ],

    "Done": [
        {
            2: "Jogar Fallout",
            1: "Se exercitar"
        }
    ]
}


# def write_task():
#     return

# def update_task(type, id, update):
#     with open('manager.json', 'r+') as openfile:
#         json_object = json.load(openfile)

#     json_object[type][0][id] = update

#     with open("manager.json", "w") as file:
#         json.dump(json_object, file, indent=4)
    
# def delete_task(type, id):
#     with open('manager.json', 'r+') as openfile:
#         json_object = json.load(openfile)

#     del json_object[type][0][id]

#     with open("manager.json", "w") as openfile:
#         json.dump(json_object, openfile, indent=4)

# def add_task(new_task):
#     with open("manager.json", "r+") as openfile:
#         json_object = json.load(openfile)
    
#     ultimo_id = int(list(json_object["To-do"][0].keys())[-1])
#     ultimo_id += 1
#     print(ultimo_id)

#     json_object["To-do"][0][ultimo_id] = new_task
    
#     with open("manager.json", "w") as file:
#         json.dump(json_object, file, indent=4)
    


# def read_task(type, id):
#     with open('manager.json', 'r') as openfile:
#         json_object = json.load(openfile)
#         return json_object[type][0][id]
    

# add_task("Tarefa de To-do")


class TaskTracker:
    def __init__(self, type, id):
        self.type = type
        self.id = id

    def getAllTask(self):
        print("mdoamdoa")

    def updateTask(self, update):
        with open('manager.json', 'r+') as openfile:
            json_object = json.load(openfile)

        json_object[self.type][0][self.id] = update

        with open("manager.json", "w") as file:
            json.dump(json_object, file, indent=4)

    def deleteTask(self):
        with open('manager.json', 'r+') as openfile:
            json_object = json.load(openfile)

        del json_object[self.type][0][self.id]

        with open("manager.json", "w") as openfile:
            json.dump(json_object, openfile, indent=4)


    def addTask(newTask):
         with open("manager.json", "r+") as openfile:
            json_object = json.load(openfile)
        
            ultimo_id = int(list(json_object["To-do"][0].keys())[-1])
            ultimo_id += 1

            json_object["To-do"][0][ultimo_id] = newTask
            
            with open("manager.json", "w") as file:
                json.dump(json_object, file, indent=4)

    def read_task(self):
        with open('manager.json', 'r') as openfile:
            json_object = json.load(openfile)
            return json_object[self.type][0][self.id]
    
print(TaskTracker("To-do", "11").read_task())