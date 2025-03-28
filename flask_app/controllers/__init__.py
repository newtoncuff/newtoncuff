# Register all blueprints here
def register_controllers(app):
    from controllers.main import main_controller
    from controllers.delusions import delusions_controller
    from controllers.thoughts import thoughts_controller
    from controllers.passions import passions_controller
    from controllers.interests import interests_controller
    from controllers.admin import admin_controller
    
    app.register_blueprint(main_controller)
    app.register_blueprint(delusions_controller)
    app.register_blueprint(thoughts_controller)
    app.register_blueprint(passions_controller)
    app.register_blueprint(interests_controller)
    app.register_blueprint(admin_controller)