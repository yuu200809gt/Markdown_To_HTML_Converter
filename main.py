import markdown
import sys

def main():
    
 if len(sys.argv) != 4:
    print('入力方法：python3 main.py markdown input.md output.html')
    sys.exit()

content = sys.argv[1]
inputFile = sys.argv[2]
outputFile = sys.argv[3]


try:
    with open(inputFile,'r') as f:
       read_data = f.read()
       html = markdown.markdown(read_data)
    
    with open(outputFile,'w') as f:
       f.write(html)
    
except:
     print('変換できませんでした')

