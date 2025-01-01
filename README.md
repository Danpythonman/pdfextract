# pdfextract

Python-based command-line tool to extract pages from a PDF.

## Installation

To install, just clone this Git repository and install it with `pip`.

   ```bash
   git clone https://github.com/yourusername/your-repo.git pdfextract
   cd pdfextract
   pip install .
   ```

## Usage

Once installed, `pdfextract` can be used as a usual command-line tool.

```bash
pdfextract input_file.pdf 1,2,3,5 -o output_file.pdf
```

The `help` flag can be used for instructions on all the different ways to use the tool.

```bash
pdfextract --help
```

## Contributing

1. Fork the repository.

2. Create a new branch for your feature or bugfix:

   ```bash
   git checkout -b feature-name
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add feature name"
   ```

4. Push your branch:

   ```bash
   git push origin feature-name
   ```

5. Open a pull request.

## License

This project is licensed under the [MIT License](./LICENSE).

## Contact

Daniel Di Giovanni • [dannyjdigio@gmail.com](mailto:dannyjdigio@gmail.com)
