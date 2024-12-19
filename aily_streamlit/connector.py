from loguru import logger
from aily.openapi.assistant.beta import AssistantClient
from aily.openapi.assistant.errors import AilyTimeoutError
from aily_streamlit.config import settings

# 关闭 loguru 的日志输出
logger.remove()

# 初始化 AssistantClient
client = AssistantClient(
    app_id=settings.app.app_id,
    app_secret=settings.app.app_secret
)

app_id = settings.aily.app_id
skill_id = settings.aily.skill_id


def chat_with_stream(message):
    # 使用用户输入的 content 和固定的 app_id
    stream = client.chat_completions.create(app_id=app_id, content=message, skill_id=skill_id, stream=True)

    return stream
