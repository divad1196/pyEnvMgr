from .basemgr import BaseMgr
import venv
from . import tools

class VenvMgr(BaseMgr):

    @classmethod
    def create(cls, name):
        venv.create(cls.env_path(name))

    @classmethod
    def activate(cls, name):
        """
            Set shell's environment
        """
        pass
    
    @classmethod
    def deactivate(cls):
        """
            Unset shell's current virtual environment if one
        """
        pass


    # @staticmethod
    # def set(name):
    #     """
    #         Set current interpretor's environment
    #     """

    # @staticmethod
    # def workon(name):
    #     """
    #         Same as activate but switch current directory to project
    #     """
