from permissions.controllers.permission_controller import PermissionsController


class InitorSystem:
    def init(self):
        PermissionsController()._create_super_user()
