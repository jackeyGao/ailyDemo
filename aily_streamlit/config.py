from dynaconf import Dynaconf, Validator

validators = {
    'app.app_id': Validator(
        'app.app_id',
        must_exist=True,
        condition=lambda v: isinstance(v, str),
    ),
    'app.app_secret': Validator(
        'app.app_secret',
        must_exist=True,
        condition=lambda v: isinstance(v, str),
    ),
     'aily.app_id': Validator(
        'aily.app_id',
        must_exist=True,
        condition=lambda v: isinstance(v, str),
    ),
     'aily.skill_id': Validator(
        'aily.skill_id',
        must_exist=True,
        condition=lambda v: isinstance(v, str),
    )
}

# 加载配置文件
settings = Dynaconf(
    envvar_prefix='AILY',
    load_dotenv=True,
    settings_files=[
        'settings.toml',
    ],
)

