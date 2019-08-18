import subprocess # module permettant d'appeler un programme externe (js dans notre cas)
import sys # permet de recuperer les arguments passés au script python

# output = subprocess.check_output(['node', 'C:\\Users\\Mamadou\\Desktop\\cours javascript\\ulbite.js',"Welcome, { name }!"])
# argument à tester est 'sys.argv[1]]'
# on a fusionner la sortie d'erreur et la sortie standard avec 'stderr = subprocess.STDOUT'
# on requiert la sortie standard avec  'stdout = subprocess.PIPE'


process = subprocess.Popen(['node', './checker.js', sys.argv[1]], stderr = subprocess.STDOUT , stdout = subprocess.PIPE)
output, _ = process.communicate() # execute le processus externe et renvoie les sorties standard et d'erreur du processus externe (le fichier js)
output = output.decode() #la sortie etant binaire, on convertit la valeur retournée en string
index = output.find("SyntaxError") # verification si il y'a une erreur de syntaxe dans la sortie standard du processus externe, afficher "syntaxError"
if (index != -1): 
    print(output[index:])

