import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='tttest')
    parser.add_argument('--method', type=str, help='the http method type (get | post)',
                        choices=["get", "post"], default='get')
    
    args = parser.parse_args()
