from .. import defaults
from .. import tools
from pathlib import Path


class BaseMgr:
    @staticmethod
    def env_path(env):
        return defaults.ENV_DIR / env

    @staticmethod
    def create(name):
        pass

    @staticmethod
    def activate(name):
        """
            Set shell's environment
        """
        pass

    @staticmethod
    def duplicate(model, name):
        tools.recursive_copy(env_path(model), env_path(name))

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
