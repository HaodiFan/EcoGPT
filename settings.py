import yaml
from pathlib import Path

yaml_path = Path(__file__).parent/'configs'/'configs.yaml'

with open(yaml_path, 'r') as f:
    config = yaml.safe_load(f)


openai_api_keys = config['OPENAI']['api']
openai_model = config['OPENAI']['model']
