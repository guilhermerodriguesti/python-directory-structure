import os
import yaml

def create_directory(account, app_env, region, technology, app_type, service, path):
    try:
        os.makedirs(path)
    except Exception as e:
        print(f'Failed to create directory {path}: {str(e)}')
        return False
    
    print(f'Created directory {path}')
    return True

if __name__ == '__main__':
    with open('pipe.yaml', 'r') as f:
        schema = yaml.load(f, Loader=yaml.FullLoader)

    account = schema['variables'][0]['default']
    app_env = schema['variables'][1]['default']
    region = schema['variables'][2]['default']
    technology = schema['variables'][3]['default']
    app_type = schema['variables'][4]['default']
    service = schema['variables'][5]['default']

    path = f"repo/stack-terraform-ecs/{account}/{app_env}/{region}/{technology}-{app_type}/{service}/"
    create_directory(account, app_env, region, technology, app_type, service, path)

    output = {
        f"{account}_{app_env}_{service}": {
            "account": account,
            "app_env": app_env,
            "region": region,
            "technology": technology,
            "app_type": app_type,
            "service": service,
            "path": path
        }
    }

    with open(f"repo/stack-terraform-ecs/{account}/{app_env}/{region}/{technology}-{app_type}/{service}/{account}-{app_env}-{service}.yaml", "w") as f:
        yaml.dump(output, f)
