import argparse
import Logconfig
import os,sys
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
Logger = Logconfig.getlogger(sys.argv[0][sys.argv[0].rfind(os.sep)+1:])
Logger.error("chenggong")