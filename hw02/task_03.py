import yaml
import os
dict_to_yaml = {"key1": ["item1", "item2"], "key2": 10, "key3": {"1руб": 70,"2руб": 140}}

full_name = os.path.join('output', 'data_write.yaml')
with open(full_name, 'w') as f_n:
    yaml.dump(dict_to_yaml, f_n, default_flow_style=False, allow_unicode=True)

with open(full_name) as f_n:
    print(f_n.read())
