import os
from aiohttp import web
from server import PromptServer
from .py.utils.utils import load_json_file
from .py.nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

curr_dir = os.path.dirname(__file__)
cfg = load_json_file(os.path.join(curr_dir, 'config.json'))

# comfyui插件web目录下js会自执行，故挪个位置
PromptServer.instance.app.add_routes([
  web.static(cfg['web'], os.path.join(curr_dir, 'web/dist')),
])

WEB_DIRECTORY = "./web/extensions"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]