import os
import yaml


class CreateDirectory:
    def __init__(self):
        self.path_root = "."

    def run(self):
        # Load variables from pipe.yml
        with open('pipe.yaml', 'r') as f:
            schema = yaml.safe_load(f)

        for key, value in schema.items():
            self.path_root = os.path.join(self.path_root, value)
            if self.create_directory(self.path_root):
                print(f"Directory '{self.path_root}' created.")
            else:
                print(f"Failed to create directory '{self.path_root}'.")

        print(f"Success!")

    def create_directory(self, path):
        try:
            os.makedirs(path)
        except Exception as e:
            print(f"Failed to create directory {path}: {str(e)}")
            return False

        return True


if __name__ == '__main__':
    app = CreateDirectory()
    app.run()
