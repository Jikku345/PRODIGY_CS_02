from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

class ImageEncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Manipulation for Image Encryption")
        self.root.geometry("600x400")
        self.filename = None

        # Upload Button
        Button(root, text="Upload Image", command=self.upload_image, width=20, bg="lightblue").pack(pady=10)

        # Encrypt Button
        Button(root, text="Encrypt", command=self.encrypt_image, width=20, bg="lightgreen").pack(pady=5)

        # Decrypt Button
        Button(root, text="Decrypt", command=self.decrypt_image, width=20, bg="orange").pack(pady=5)

        # Display Area
        self.canvas = Canvas(root, width=400, height=300)
        self.canvas.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.filename = file_path
            img = Image.open(file_path)
            img.thumbnail((400, 300))
            self.img = ImageTk.PhotoImage(img)
            self.canvas.create_image(200, 150, image=self.img)
            messagebox.showinfo("Success", "Image uploaded successfully!")

    def encrypt_image(self):
        if not self.filename:
            messagebox.showerror("Error", "Please upload an image first!")
            return
        
        img = Image.open(self.filename)
        
        # Ensure the image is in RGB mode
        if img.mode not in ("RGB", "RGBA"):
            img = img.convert("RGB")
        
        pixels = img.load()

        key = 25  # Simple encryption key
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                pixel_values = list(pixels[i, j])  # Convert to list for RGBA support
                pixel_values[0] ^= key  # Red channel
                pixel_values[1] ^= key  # Green channel
                pixel_values[2] ^= key  # Blue channel
                pixels[i, j] = tuple(pixel_values)
        
        encrypted_path = os.path.join(os.path.dirname(self.filename), "encrypted_image.png")
        img.save(encrypted_path)
        messagebox.showinfo("Success", f"Image encrypted and saved as:\n{encrypted_path}")

    def decrypt_image(self):
        if not self.filename:
            messagebox.showerror("Error", "Please upload an image first!")
            return
        
        img = Image.open(self.filename)
        
        # Ensure the image is in RGB mode
        if img.mode not in ("RGB", "RGBA"):
            img = img.convert("RGB")
        
        pixels = img.load()

        key = 25  # Same key for decryption
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                pixel_values = list(pixels[i, j])  # Convert to list for RGBA support
                pixel_values[0] ^= key
                pixel_values[1] ^= key
                pixel_values[2] ^= key
                pixels[i, j] = tuple(pixel_values)
        
        decrypted_path = os.path.join(os.path.dirname(self.filename), "decrypted_image.png")
        img.save(decrypted_path)
        messagebox.showinfo("Success", f"Image decrypted and saved as:\n{decrypted_path}")

if __name__ == "__main__":
    root = Tk()
    app = ImageEncryptionApp(root)
    root.mainloop()
