from flask import Blueprint
from ..controllers.store_audio_controller import (
  store_audio,
)

store_audio_bp = Blueprint('store_audio_bp', __name__)

store_audio_bp.route('/store_audio', methods=['POST'])(store_audio)