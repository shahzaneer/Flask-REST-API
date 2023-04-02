# import os
# from flask import Blueprint, Flask

# def register_controllers(flask_app):
#     """Registers all controller blueprints with the app."""
#     for filename in os.listdir('Controllers'):
#         if filename.endswith('.py') and filename != '__init__.py' and filename != 'registerControllers':
#             module_name = f'controllers.{filename[:-3]}'
#             module = __import__(module_name, fromlist=[''])
#             blueprint = getattr(module, 'blueprint')      #!    alternatively ->        blueprint = module.blueprint

#             flask_app.register_blueprint(blueprint)



# import os
# from flask import Blueprint, Flask

# def register_controllers(flask_app):
#     """Registers all controller blueprints with the app."""
#     for filename in os.listdir('Controllers'):
#         if filename.endswith('.py') and filename != '__init__.py' and filename != 'registerControllers':
#             module_name = f'controllers.{filename[:-3]}'
#             module = __import__(module_name, fromlist=[''])
#             blueprint = module.blueprint

#             flask_app.register_blueprint(blueprint)


# import os
# from flask import Blueprint, Flask

# def register_controllers(flask_app):
#     """Registers all controller blueprints with the app."""
#     controllers_path = os.path.join(os.path.dirname(__file__))
#     for filename in os.listdir(controllers_path):
#         if filename.endswith('.py') and filename != '__init__.py' and filename != 'registerControllers':
#             # print(filename)
#             module_name = f'controllers.{filename[:-3]}'
#             module = __import__(module_name, fromlist=[''])
#             blueprint = module.Blueprint
#             flask_app.register_blueprint(blueprint)


# if __name__ == '__main__':
#     print(os.listdir("controllers"))
    