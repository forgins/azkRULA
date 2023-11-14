import tkinter as tk
from PIL import Image, ImageTk
from main import main

def display_results(results):
    results_window = tk.Toplevel(window)
    results_window.title("RULA Results")
    results_window.geometry('200x100')
    
    # Create labels or text widgets to display your results
    # You can use the "results" list to populate these widgets
    
    # Example:
    results_label = tk.Label(results_window, text="Results:")
    results_label.pack()

    RULA_result = tk.Label(results_window, text=f'RULA score: {results[0]}')
    RULA_result.pack()

    level_act_result = tk.Label(results_window, text=f'Level action: {results[1]}')
    level_act_result.pack()


def assessment_button():
    right_wrist_coeff_gui = right_wrist_rotation_factor.get()
    left_wrist_coeff_gui = left_wrist_rotation_factor.get()
    leg_coeff_gui = leg_position_factor.get()
    muscolar_coeff_gui = muscolar_value.get()
    force_coeff_gui = force_value.get()
    frame = frame_var.get()
    file = file_name_var.get()

    results = main(frame,file,right_wrist_coeff_gui,left_wrist_coeff_gui,leg_coeff_gui,muscolar_coeff_gui,force_coeff_gui)

    display_results(results)


def on_validate_input(input_value):
    # This function is called whenever the user tries to change the entry content
    # It checks if the new value is a valid number (integer or float) or an empty string.
    # Return True to allow the change or False to prevent it.
    if input_value == "":
        return True  # Allow an empty string (e.g., when the entry is cleared)

    try:
        float(input_value)
        return True
    except ValueError:
        return False
    
def load_image():
    image_path = "Table.png"
    img = Image.open(image_path)
    photo = ImageTk.PhotoImage(img)
    image_label.config(image=photo)
    image_label.image = photo

    
window = tk.Tk()
window.geometry('1100x650')
window.title('RULA Assessment')
window.resizable(False,False)

group_A_label = tk.Label(window, text='GROUP A')
group_A_label.grid(row=0, column=0, padx=10, pady=2, sticky='W')
right_wrist_rotation_factor = tk.IntVar()

Right_wrist_rotation_label = tk.Label(window,text='Right wrist rotation:')
Right_wrist_rotation_label.grid(row=1, column=0, padx=10, pady=2, sticky='W')

optr1 = tk.Radiobutton(window, text='Rotation between the rest position and half of its maximum torsion', variable=right_wrist_rotation_factor, value=1)
optr1.grid(row=2, column=0, padx=10, pady=2, sticky='W')
optr2 = tk.Radiobutton(window, text='Other', variable=right_wrist_rotation_factor, value=2)
optr2.grid(row=3, column=0, padx=10, pady=2, sticky='W')

left_wrist_rotation_factor = tk.IntVar()

Left_wrist_rotation_label = tk.Label(window, text='Left wrist rotation:')
Left_wrist_rotation_label.grid(row=4, column=0, padx=10, pady=2, sticky='W')

optl1 = tk.Radiobutton(window, text='Rotation between the rest position and half of its maximum torsion', variable=left_wrist_rotation_factor, value=1)
optl1.grid(row=5, column=0, padx=10, pady=2, sticky='W')
optl2 = tk.Radiobutton(window, text='Other', variable=left_wrist_rotation_factor, value=2)
optl2.grid(row=6, column=0, padx=10, pady=2, sticky='W')


group_B_label = tk.Label(window, text='GROUP B')
group_B_label.grid(row=7, column=0, padx=10, pady=2, sticky='W')

leg_position_factor = tk.IntVar()

leg_position_label = tk.Label(window, text='Leg position:')
leg_position_label.grid(row=8, column=0, padx=10, pady=2, sticky='W')

optleg1 = tk.Radiobutton(window, text='The operator is standing with the body weight well distributed on both feet or sitting with his legs supported', variable=leg_position_factor, value=1)
optleg1.grid(row=9, column=0, padx=10, pady=2, sticky='W')
optleg2 = tk.Radiobutton(window, text='Other', variable=leg_position_factor, value=2)
optleg2.grid(row=10, column=0, padx=10, pady=2, sticky='W')

muscolar_label = tk.Label(window, text='MUSCOLAR GROUP')
muscolar_label.grid(row=11, column=0, padx= 10, pady= 2, sticky='W')
leg_position_label = tk.Label(window, text='Use of muscolar group:')
leg_position_label.grid(row=12, column=0, padx=10, pady=2, sticky='W')

muscolar_value = tk.IntVar()

optmusc1 = tk.Radiobutton(window, text='No muscle groups are used', variable=muscolar_value, value=0)
optmusc1.grid(row=13, column=0, padx= 10, pady= 2, sticky='W')
optmusc2 = tk.Radiobutton(window, text='Other', variable=muscolar_value, value=1)
optmusc2.grid(row=14, column=0, padx= 10, pady= 2, sticky='W')

force_label = tk.Label(window, text='FORCE GROUP')
force_label.grid(row=15, column=0, padx= 10, pady= 2, sticky='W')

force_value = tk.IntVar()

optforce1 = tk.Radiobutton(window, text='No force is used', variable=force_value, value=0)
optforce1.grid(row=16, column=0, padx= 10, pady= 2, sticky='W')
optforce2 = tk.Radiobutton(window, text='Other', variable=force_value, value=1)
optforce2.grid(row=17, column=0, padx= 10, pady= 2, sticky='W')

frame_label = tk.Label(window, text='Enter the frame for the valuation:')
frame_label.grid(row=1, column=1, padx=10, pady=10)
frame_var = tk.IntVar()
validate_cmd = window.register(on_validate_input)  # Register the validation function
frame_box = tk.Entry(window, textvariable=frame_var, validate='key', validatecommand=(validate_cmd, '%P'))
frame_box.grid(row=2, column=1, padx=10, pady=5)

file_name_label = tk.Label(window, text='Enter the name of the .csv file:')
file_name_label.grid(row=3, column=1,  padx=10, pady=5)

file_name_var = tk.StringVar()

file_name_box = tk.Entry(window,textvariable=file_name_var)
file_name_box.grid(row=4, column=1, padx=10, pady=5)


image_label = tk.Label(window)
image_label.grid(row=13, column=1, rowspan=6, columnspan=5, padx=10, pady=5, sticky='n')
load_image()


Assessment_button = tk.Button(window, text='RULA', command=assessment_button, width=20)
Assessment_button.grid(row=25, column=0, padx=10, pady=20, sticky='W')



if __name__ == "__main__":
    window.mainloop()