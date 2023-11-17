from django.conf import settings


# No need to specify a router for every single app

class Routers(object):
# All default apps that are also migrated when migration command is ran
    default_apps = {'auth', 'admin', 'sessions', 'contenttypes'}

# Can't access list of apps in the settings file (settings.INSTALLED_APPS), so add each app created to this list to it map to it's respective Database 
    installed_apps = ['products', 'review']
         
    # Map each app to its respective database for read opperations 
    def db_for_read(self, model, **hints):
    
        if model._meta.app_label in self.installed_apps:
            # return model._meta.app_label which is the name of all respective apps (Database name must match app name + '_db')
            return model._meta.app_label + '_db'
         # Map default apps to auth_db for read operations
        elif model._meta.app_label in self.default_apps:
               return 'auth_db'
        return None
         
    # Map each app to its respective database for write opperations 
    def db_for_write(self, model, **hints):

        if model._meta.app_label in self.installed_apps:
                # return model._meta.app_label which is the name of all respective apps (Database name must match app name + '_db')
                return model._meta.app_label + '_db'
        # Map default apps to auth_db for write operations
        elif model._meta.app_label in self.default_apps:
               return 'auth_db'
        return None
    # Allow relationships between objects
    # Note: Can be changed to suit your needs
    def allow_relation(self, obj1, obj2, **hints):
         
        if (obj1._meta.app_label in self.installed_apps or obj2._meta.app_label in self.installed_apps):
            return True
        return None
    # Map apps to their respective databases for migrations
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Map default apps migrations to auth_db
        if app_label in self.default_apps:
             return db == 'auth_db'
        # Map installed apps migrations to their respective databases
        elif app_label in self.installed_apps:
             return db == app_label + '_db'
             
             
         
              
         
                
        