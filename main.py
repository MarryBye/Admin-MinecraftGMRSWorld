from src.classes.database.modpacks_controller import ModpacksController
from src.classes.database.javas_controller import JavasController
from src.classes.database.types_controller import TypesController
from src.classes.database.tags_controller import TagsController
from src.classes.database.difficulties_controller import DifficultiesController

# difficulties = [
#     ["Easy"],
#     ["Medium"],
#     ["Hard"],
#     ["Pizdec"]
# ]

# javas = [
#     ["Java 8", "java.download.com/8"],
#     ["Java 11", "java.download.com/11"],
#     ["Java 17", "java.download.com/17"],
#     ["Java 21", "java.download.com/21"]
# ]

# tags = [
#     ["Интересно", "#ff00ff"],
#     ["Смешно", "#101010"],
#     ["Историческая", "#ffffff"],
#     ["Легендарная", "#efefef"]
# ]

# types = [
#     ["Vanilla"],
#     ["Semi-vanilla"],
#     ["Not vanilla"],
#     ["Not minecraft?"]
# ]

# for tag in tags:
#     TagsController.add_tag(tag[0], tag[1])
    
# for java in javas:
#     JavasController.add_java(java[0], java[1])
    
# for type in types:
#     TypesController.add_type(type[0])
    
# for difficulty in difficulties:
#     DifficultiesController.add_difficulty(difficulty[0])

# ModpacksController.add_modpack(
#     "Test modpack",
#     "Description for test modpack",
#     "test_modpack.ico",
#     "download.testModpack.com",
#     1,
#     2,
#     1
# )

# ModpacksController.add_modpack(
#     "Test modpack 22",
#     "Description for test modpack22222",
#     "test_modpack2.ico",
#     "download.testModpack2.com",
#     2,
#     3,
#     2
# )

# ModpacksController.add_modpack(
#     "Test modpack 3333",
#     "Description for test modpac 33333",
#     "test_modpack3.ico",
#     "download.testModpack3.com",
#     2,
#     2,
#     2
# )
# ModpacksController.add_modpack_tag(1, 2)
# ModpacksController.add_modpack_tag(1, 1)
# ModpacksController.add_modpack_tag(1, 3)

# ModpacksController.add_modpack_tag(2, 2)

# ModpacksController.add_modpack_tag(3, 1)

# for modpack in ModpacksController.get_all_modpacks():
#     modpack_tags = ModpacksController.get_modpack_tags(modpack.get_id())
#     for tag in modpack_tags:
#         print(tag.get_name())
