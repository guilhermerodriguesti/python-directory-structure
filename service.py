import json


def check_resource(id):
    # retorna True se o recurso existe e False caso contrário
    print("Check", id)
    return False


def create_resource(id, region, cluster, name, alb, dns):
    # lógica para criar um recurso 
    print("Create", id, region, cluster, name, alb, dns)


def update_resource(id, region, cluster, name, alb, dns):
    # lógica para atualizar um recurso 
    print("Update", id, region, cluster, name, alb, dns)


def delete_resource(id, region, cluster, name, alb, dns):
    # lógica para excluir um recurso 
    print("Delete", id, region, cluster, name, alb, dns)


def check_json_file(file_path):
    try:
        with open(file_path, 'r') as f:
            json_str = f.read()
            json.loads(json_str)
            print("JSON is valid")
            return json_str
    except json.JSONDecodeError as e:
        print(f"Invalid JSON string: {e}")
        return None
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None


def load_resource_data():
    json_str = check_json_file('service.json')
    if json_str is not None:
        return json.loads(json_str)


def main(resource_data):
    id = resource_data.get("id")
    region = resource_data.get("region")
    cluster = resource_data.get("cluster")
    name = resource_data.get("name")
    alb = resource_data.get("alb")
    dns = resource_data.get("dns")
    destroy = resource_data.get("destroy", False)

    if not all([id, region, cluster, name, alb, dns]):
        print("Parameter not found in service.json")
        return

    exists = check_resource(id)

    if exists:
        update_resource(id, region, cluster, name, alb, dns)
    elif not destroy:
        create_resource(id, region, cluster, name, alb, dns)
    else:
        delete_resource(id, region, cluster, name, alb, dns)


if __name__ == '__main__':
    resource_data = load_resource_data()
    if resource_data is not None:
        main(resource_data)
