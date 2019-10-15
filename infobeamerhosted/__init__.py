from Infobeamer import *

if __name__ == '__main__':
    import argparse

    logging.basicConfig(level=logging.INFO)
    logger.info('Script is executed as standalone file.')

    # Parse arguments for CLI use.
    parser = argparse.ArgumentParser()
    parser.add_argument('--api-key', type=str, help='API Key.')
    parser.add_argument('--api-user', type=str, help='API User.')
    parser.add_argument('--api-url', type=str, help='API URL.')
    args = parser.parse_args()

    API_KEY = os.environ.get('API_KEY') or args.api_key
    API_URL = os.environ.get('API_URL') or args.api_url
    API_USER = os.environ.get('API_USER') or args.api_user

    ibh = Infobeamer(API_KEY)
