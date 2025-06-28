import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os

# -------------------------------
# Dummy file processing function
# Replace this with your actual logic
# -------------------------------
def process_txt_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        # Example: count number of lines
        line_count = content.count('\n') + 1
        return f"{os.path.basename(file_path)} has {line_count} lines."

# -------------------------------
# Folder selection
# -------------------------------
def select_folder():
    folder_path = filedialog.askdirectory(title="Select folder containing TXT files")
    folder_var.set(folder_path)

# -------------------------------
# Batch file processing
# -------------------------------
def process_files():
    folder = folder_var.get()
    if not folder:
        messagebox.showwarning("No folder selected", "Please select a folder first.")
        return

    output_text.delete("1.0", tk.END)  # Clear output box
    processed_count = 0

    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder, filename)
            try:
                result = process_txt_file(file_path)
                output_text.insert(tk.END, result + "\n")
                processed_count += 1
            except Exception as e:
                output_text.insert(tk.END, f"Error processing {filename}: {e}\n")

    output_text.insert(tk.END, f"\n✅ Done: Processed {processed_count} TXT file(s).\n")

# -------------------------------
# GUI Layout
# -------------------------------
import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext, messagebox
import os
from pathlib import Path


class ModernFileProcessor:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.setup_styles()
        self.create_widgets()

    def setup_window(self):
        """Setup main window"""
        self.root.title("Batch TXT File Processor")
        self.root.geometry("800x600")
        self.root.minsize(700, 500)

        # Center the window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (800 // 2)
        y = (self.root.winfo_screenheight() // 2) - (600 // 2)
        self.root.geometry(f"800x600+{x}+{y}")

        # Set gradient background color
        self.root.configure(bg='#f0f4f8')

    def setup_styles(self):
        """Setup theme styles"""
        self.style = ttk.Style()
        self.style.theme_use('classic')

        # Start processing button styling
        self.style.configure(
            "Modern.TButton",
            font=('Segoe UI', 13, 'bold'),
            padding=(7, 2)
        )
        self.style.map(
            "Modern.TButton",
            background=[('active', '#4CAF50'), ('!active', '#2196F3')],
            foreground=[('active', 'white'), ('!active', 'white')],
            relief=[('pressed', 'flat'), ('!pressed', 'flat')]
        )

    def create_widgets(self):
        """Create all interface components"""
        # Main container
        main_container = tk.Frame(self.root, bg='#f0f4f8')
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Folder selection area
        self.create_folder_section(main_container)

        # Control buttons area
        self.create_control_section(main_container)

        # Output area
        self.create_output_section(main_container)

        # Status bar
        self.create_status_bar(main_container)

    def create_folder_section(self, parent):
        """Create folder selection area"""
        # Combined folder selection frame
        folder_frame = tk.LabelFrame(
            parent,
            text=" Select input/output folder",
            font=('Segoe UI', 14, 'bold'),
            bg='#f0f4f8',
            bd=3,
        )
        folder_frame.pack(fill=tk.X, pady=(0, 20))

        # Input folder section
        input_inner_frame = tk.Frame(folder_frame, bg='#f0f4f8')
        input_inner_frame.pack(fill=tk.X, padx=15, pady=(15, 5))

        # Folder path variable
        self.folder_var = tk.StringVar()
        self.folder_var.set("Please select input folder")

        # Input path display box
        self.input_path_entry = tk.Entry(
            input_inner_frame, textvariable=self.folder_var, font=('Segoe UI', 13)
        )
        self.input_path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

        # Browse button for input folder
        self.input_browse_btn = ttk.Button(
            input_inner_frame, text="Browse", style="Modern.TButton", command=self.select_input_folder
        )
        self.input_browse_btn.pack(side=tk.RIGHT)

        # Output folder section
        output_inner_frame = tk.Frame(folder_frame, bg='#f0f4f8')
        output_inner_frame.pack(fill=tk.X, padx=15, pady=(5, 15))
        
        # Output folder path variable
        self.output_folder_var = tk.StringVar()
        self.output_folder_var.set("Please select output folder")

        # Output path display box
        self.output_path_entry = tk.Entry(
            output_inner_frame, textvariable=self.output_folder_var, font=('Segoe UI', 13)
        )
        self.output_path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

        # Browse button for output folder
        self.output_browse_btn = ttk.Button(
            output_inner_frame, text="Browse", style="Modern.TButton", command=self.select_output_folder
        )
        self.output_browse_btn.pack(side=tk.RIGHT)

    def create_control_section(self, parent):
        """Create control buttons area"""
        control_frame = tk.Frame(parent, bg='#f0f4f8')
        control_frame.pack(fill=tk.X, pady=(0, 20))

        # Start processing button
        self.process_btn = ttk.Button(
            control_frame,
            text="Start Processing",
            style="Modern.TButton",
            command=self.process_files
        )
        self.process_btn.pack(side=tk.LEFT, padx=(0, 10))

        # Clear log button
        self.clear_btn = ttk.Button(
            control_frame, text="Clear Log", command=self.clear_output, style="Modern.TButton"
        )
        self.clear_btn.pack(side=tk.LEFT, padx=(0, 10))

    def create_output_section(self, parent):
        """Create output area"""
        output_frame = tk.LabelFrame(parent)
        output_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        # Create text box
        self.output_text = scrolledtext.ScrolledText(
            output_frame,
            wrap=tk.WORD,
            font=('Consolas', 13),
            bg='#f5f5f5',
            fg='#2c3e50',
            insertbackground='#2c3e50',
            selectbackground='#3498db',
            bd=0,
            padx=10,
            pady=10
        )
        self.output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Add welcome message
        welcome_msg = """
🎉 Welcome to Batch File Processor!

Instructions:

1. In the "Select input/output folder" section:
   - Set "Input Folder" containing TXT files
   - Set "Output Folder" to save results

2. Click "Start Processing" to begin batch processing

3. Processing progress and results will be displayed in this area

4. Results will be saved in the selected output folder

---
        """
        self.output_text.insert(tk.END, welcome_msg)
        self.output_text.config(state=tk.DISABLED)

    def create_status_bar(self, parent):
        """Create status bar"""
        # Status bar label
        status_label_frame = tk.Frame(parent, bg='#f0f4f8')
        status_label_frame.pack(fill=tk.X, pady=(5, 0))

        status_info_label = tk.Label(
            status_label_frame,
            text="Status:",
            font=('Segoe UI', 10, 'bold'),
            fg='#34495e',
            bg='#f0f4f8',
            anchor=tk.W
        )
        status_info_label.pack(side=tk.LEFT)

        # Status bar
        self.status_frame = tk.Frame(parent, bg='#34495e', height=30)
        self.status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        self.status_frame.pack_propagate(False)

        self.status_label = tk.Label(
            self.status_frame,
            text="Ready",
            font=('Segoe UI', 10),
            fg='white',
            bg='#34495e',
            anchor=tk.W
        )
        self.status_label.pack(side=tk.LEFT, padx=10, pady=5)

        # File count label
        self.file_count_label = tk.Label(
            self.status_frame,
            text="Files: 0",
            font=('Segoe UI', 10),
            fg='#ecf0f1',
            bg='#34495e'
        )
        self.file_count_label.pack(side=tk.RIGHT, padx=10, pady=5)

    def select_input_folder(self):
        """Select input folder"""
        folder_path = filedialog.askdirectory(
            title="Select folder containing TXT files",
            mustexist=True
        )

        if folder_path:
            self.folder_var.set(folder_path)
            self.update_status(f"Selected input folder: {os.path.basename(folder_path)}")

            # Count TXT files
            txt_files = list(Path(folder_path).glob("*.txt"))
            self.file_count_label.config(text=f"TXT files: {len(txt_files)}")

            self.log_message(f"📁 Selected input folder: {folder_path}")
            self.log_message(f"📊 Found {len(txt_files)} TXT files")

    def select_output_folder(self):
        """Select output folder"""
        folder_path = filedialog.askdirectory(
            title="Select output folder for results",
            mustexist=True
        )

        if folder_path:
            self.output_folder_var.set(folder_path)
            self.update_status(f"Selected output folder: {os.path.basename(folder_path)}")
            self.log_message(f"📁 Selected output folder: {folder_path}")

    def process_files(self):
        """Process files"""
        input_folder_path = self.folder_var.get()
        output_folder_path = self.output_folder_var.get()

        if not input_folder_path or input_folder_path == "Please select input folder":
            messagebox.showwarning("Warning", "Please select an input folder to process first!")
            return

        if not output_folder_path or output_folder_path == "Please select output folder":
            messagebox.showwarning("Warning", "Please select an output folder for results!")
            return

        if not os.path.exists(input_folder_path):
            messagebox.showerror("Error", "Selected input folder does not exist!")
            return

        if not os.path.exists(output_folder_path):
            messagebox.showerror("Error", "Selected output folder does not exist!")
            return

        self.process_btn.config(state='disabled')
        self.update_status("Processing files...")

        try:
            # This is where your file processing logic goes
            txt_files = list(Path(input_folder_path).glob("*.txt"))

            if not txt_files:
                self.log_message("⚠️ No TXT files found in selected input folder")
                messagebox.showinfo("Info", "No TXT files found in selected input folder!")
                return

            self.log_message(f"🚀 Starting to process {len(txt_files)} files...")

            # Prepare results for saving
            results_content = []
            results_content.append("=== BATCH FILE PROCESSING RESULTS ===\n")
            results_content.append(f"Processing Date: {os.popen('date').read().strip()}\n")
            results_content.append(f"Input Folder: {input_folder_path}\n")
            results_content.append(f"Output Folder: {output_folder_path}\n")
            results_content.append(f"Total Files Found: {len(txt_files)}\n")
            results_content.append("=" * 50 + "\n\n")

            processed_count = 0
            for file_path in txt_files:
                try:
                    # Add your specific processing logic here
                    # For example: read file content, process, save, etc.
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Here you would add your processing operations
                        # processed_content = your_processing_function(content)
                        
                        # For now, just count lines as an example
                        line_count = len(content.splitlines())
                        file_result = f"File: {file_path.name}\nLines: {line_count}\nStatus: Processed successfully\n"
                        
                        # Add to results content
                        results_content.append(file_result)
                        results_content.append("-" * 30 + "\n")

                    processed_count += 1
                    self.log_message(f"✅ Processed: {file_path.name}")

                    # Update interface
                    self.root.update_idletasks()

                except Exception as e:
                    error_msg = f"Failed to process {file_path.name}: {str(e)}"
                    results_content.append(f"File: {file_path.name}\nStatus: ERROR - {str(e)}\n")
                    results_content.append("-" * 30 + "\n")
                    self.log_message(f"❌ {error_msg}")

            # Save results to file
            results_file_path = os.path.join(output_folder_path, "results.txt")
            try:
                with open(results_file_path, 'w', encoding='utf-8') as f:
                    f.writelines(results_content)
                self.log_message(f"💾 Results saved to: {results_file_path}")
            except Exception as e:
                self.log_message(f"❌ Failed to save results file: {str(e)}")

            self.log_message(f"🎉 Processing complete! Successfully processed {processed_count} files")
            self.update_status(f"Processing complete - Success: {processed_count}, Total: {len(txt_files)}")
            messagebox.showinfo("Complete",
                                f"File processing complete!\nSuccessfully processed: {processed_count} files\nResults saved to: {results_file_path}")

        except Exception as e:
            error_msg = f"Error occurred during processing: {str(e)}"
            self.log_message(f"❌ {error_msg}")
            messagebox.showerror("Error", error_msg)

        finally:
            self.process_btn.config(state='normal')
            if hasattr(self, 'status_label'):
                self.update_status("Processing complete")

    def clear_output(self):
        """Clear output area"""
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.config(state=tk.DISABLED)
        self.update_status("Log cleared")

    def log_message(self, message):
        """Add log message"""
        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, f"{message}\n")
        self.output_text.see(tk.END)
        self.output_text.config(state=tk.DISABLED)
        self.root.update_idletasks()

    def update_status(self, message):
        """Update status bar"""
        self.status_label.config(text=message)
        self.root.update_idletasks()


def main():
    root = tk.Tk()
    app = ModernFileProcessor(root)
    root.mainloop()


if __name__ == "__main__":
    main()
