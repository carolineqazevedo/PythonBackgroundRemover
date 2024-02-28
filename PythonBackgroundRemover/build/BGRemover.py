import os
import shutil
from PIL import Image, ImageTk
from rembg import remove
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, filedialog

file = Path(__file__).parent
assets = file / Path(r"assets")

def relative_to_assets(path: str) -> Path:
    return assets / Path(path)

image_path = None
imageBG_path = None

def display_image(image_path):
    pil_image = Image.open(image_path)
    pil_image = pil_image.resize((350, 350), Image.LANCZOS)
    tk_image = ImageTk.PhotoImage(pil_image)
    canvas.create_image(79.0, 120.0, anchor="nw", image=tk_image)
    canvas.tk_image_ref = tk_image

def upload_image():
    global image_path
    image_path = filedialog.askopenfilename()
    display_image(image_path)

def remove_background():
    global image_path, imageBG_path
    if image_path:
        input_image = Image.open(image_path)
        output_image = remove(input_image)
        imageBG_path = "newimage.png"
        output_image.save(imageBG_path)
        display_background_removed_image(imageBG_path)

def download_background_removed_image():
    global imageBG_path
    if imageBG_path:
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            shutil.copyfile(imageBG_path, save_path)
        os.remove(imageBG_path)

def display_background_removed_image(image_path):
    pil_image = Image.open(image_path)
    pil_image = pil_image.resize((350, 350), Image.LANCZOS)
    tk_image = ImageTk.PhotoImage(pil_image)
    canvas.create_image(471.0, 120.0, anchor="nw", image=tk_image)
    canvas.tk_image_ref = tk_image

def clear_canvas():
    items = canvas.find_all()
    for item in items:
        if canvas.type(item) == "image":
            if item not in (upload_button, remover_button, download_button, cancel_button):
                canvas.delete(item)

def cancel_image():
    global image_path, imageBG_path
    if imageBG_path is not None and os.path.exists(imageBG_path):
        os.remove(imageBG_path)
    image_path = None
    imageBG_path = None
    clear_canvas()

window = Tk()
window.title("Python Background Remover")
photo = PhotoImage(file=relative_to_assets("icon.png"))
window.wm_iconphoto(False, photo)
window.geometry("900x607")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=607,
    width=900,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

canvas.create_rectangle(
    0.0,
    73.0,
    900.0,
    607.0,
    fill="#161617",
    outline=""
)

canvas.create_rectangle(
    0.0,
    0.0,
    900.0,
    73.0,
    fill="#1E1E1F",
    outline=""
)

canvas.create_text(
    339.0,
    28.0,
    anchor="nw",
    text="Python Background Remover",
    fill="#FFFFFF",
    font=("AnonymousPro Bold", 16 * -1)
)

cancel_button = PhotoImage(
    file=relative_to_assets("cancelar.png"))
cancel = Button(
    image=cancel_button,
    borderwidth=0,
    highlightthickness=0,
    command=cancel_image,
    relief="flat"
)
cancel.place(
    x=770.0,
    y=14.0,
    width=90.0,
    height=45.0
)

upload_button = PhotoImage(
    file=relative_to_assets("upload.png"))
upload = Button(
    image=upload_button,
    borderwidth=0,
    highlightthickness=0,
    command=upload_image,
    relief="flat"
)
upload.place(
    x=79.0,
    y=532.0,
    width=65.0,
    height=55.0
)

remover_button = PhotoImage(
    file=relative_to_assets("remover.png"))
remover = Button(
    image=remover_button,
    borderwidth=0,
    highlightthickness=0,
    command=remove_background,
    relief="flat"
)
remover.place(
    x=370.0,
    y=532.0,
    width=160.0,
    height=55.0
)

download_button = PhotoImage(
    file=relative_to_assets("download.png"))
download = Button(
    image=download_button,
    borderwidth=0,
    highlightthickness=0,
    command=download_background_removed_image,
    relief="flat"
)
download.place(
    x=756.0,
    y=532.0,
    width=65.0,
    height=55.0
)

canvas.create_rectangle(
    79.0,
    120.0,
    429.0,
    470.0,
    fill="#1E1E1F",
    outline=""
)

canvas.create_rectangle(
    471.0,
    120.0,
    821.0,
    470.0,
    fill="#1E1E1F",
    outline=""
)

window.resizable(False, False)
window.mainloop()
