# SVG to PDF Converter

This tool is designed to convert SVG images into a PDF format, arranging multiple SVG files in a grid layout on each page. It's particularly useful for quickly browsing through large collections of SVG files.

## Features

- Processes all SVG files in a specified directory, including subdirectories.
- Organizes SVG images in a grid layout within a PDF.
- Includes the folder name as a subtitle for each set of images from a distinct folder.
- Displays the file name under each image.

## Getting Started

### Prerequisites

- Python 3.x
- Miniconda or Anaconda

### Installation

1. **Clone the Repository**: Clone this repository to your local machine or download the source code.

    ```
    git clone [URL_TO_REPOSITORY]
    ```

2. **Create Conda Environment**: Navigate to the cloned directory and create a Conda environment using the provided `environment.yml` file.

    ```
    conda env create -f environment.yml
    ```

    This command will create a new environment named `svgtopdf` and install all the required dependencies.

3. **Activate the Environment**: Before running the script, activate the newly created Conda environment.

    ```
    conda activate svgtopdf
    ```

### Usage

1. **Prepare Your SVG Files**: Place your SVG files in a directory. The script will process all SVG files in this directory and its subdirectories.

2. **Run the Script**: Use the following command to run the script. Replace `[INPUT_DIRECTORY]` with the path to your SVG files and `[OUTPUT_FILENAME]` with the desired output PDF file name.

    ```
    python svg_to_pdf.py [INPUT_DIRECTORY] [OUTPUT_FILENAME]
    ```

    Example:

    ```
    python svg_to_pdf.py ./svg_files output.pdf
    ```

3. **View the PDF**: After running the script, check the specified output location for the PDF file.

### Deactivating the Environment

Once you are done, you can deactivate the Conda environment:

