import argparse
from Maltego import MaltegoTransform

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Maltego transform')
    parser.add_argument('DOMAIN', help='Domain value')
    parser.add_argument('FIELDS', nargs='*', help='Additional fields')
    args = parser.parse_args()

    trx = MaltegoTransform()

    for subd in ["www", "smtp", "admin"]:
        trx.addEntity("maltego.Domain", subd + '.' + args.DOMAIN)

    trx.addUIMessage("completed!")
    print(trx.returnOutput())
