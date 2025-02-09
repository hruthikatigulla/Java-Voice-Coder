import speech_recognition as sr
import tkinter as tk
import pyttsx3

# import symbol_mapping and template_mapping from external files
from symbols import symbol_mapping
from templates import template_mapping

engine = pyttsx3.init()

def convert_speech():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        engine.say("Say something!")
        engine.runAndWait()
        audio = r.listen(source)

    try:
        # recognize speech using Google Speech Recognition
        text = r.recognize_google(audio)
        
        # replace recognized keywords with proper syntax
        for s in symbol_mapping:
            if s in text.lower():
                text = text.replace(s, symbol_mapping[s])
  
            
        # define the template variable within its scope
        template = None
        for t in template_mapping:
            if t in text.lower():
                template = template_mapping[t]()
                text = text.replace(t, template)
                break
                
                
        if tk.INSERT:
            offset =tk.INSERT
        else:
            offset = tk.END
        # insert the modified text into the right_text widget at the cursor position
        right_text.insert(offset, text) 
    except (sr.UnknownValueError, sr.RequestError) as e:
        # catch only UnknownValueError and RequestError exceptions
        error_label.config(text=f"Could not understand audio: {e}")
        root.after(5000, error_label.config, {"text": ""})

# create GUI
root = tk.Tk()

# set the size of the window to be slightly less than the size of the screen
screen_width = root.winfo_screenwidth() - 50
screen_height = root.winfo_screenheight() - 50
root.geometry(f"{screen_width}x{screen_height}")
root.title("Java Development with Voice-Input");

# create left frame for the button
frame_left = tk.Frame(root)
frame_left.pack(side=tk.LEFT, padx=10, pady=10)

# create button in the left frame
button = tk.Button(frame_left, text="Generate Text", command=convert_speech, height=3, width=10)
button.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=10)

# create label below button to show errors
error_label = tk.Label(frame_left, text="", fg="red")
error_label.pack(padx=10, pady=10)

# create right frame for the text widget
frame_right = tk.Frame(root)
frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# ensure the right_text widget has a font size set
right_text = tk.Text(frame_right, font=("Helvetica", 12))
right_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

root.mainloop()
