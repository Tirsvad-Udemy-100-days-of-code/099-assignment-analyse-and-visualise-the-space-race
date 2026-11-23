"""@file capture_steps.py
@brief Make one screenshot per lecture step of the notebook, with no desktop.

The notebook is executed once. The cells of each step are exported to HTML and
rendered by a headless browser (no window opens, the mouse and keyboard stay
free). Run from the repository root: python tools/capture_steps.py
"""

import subprocess
import tempfile
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbconvert import HTMLExporter
from PIL import Image, ImageChops

NOTEBOOK_PATH = Path("notebooks") / "space_missions_analysis.ipynb"
IMAGE_DIRECTORY = Path("docs") / "images"
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 3000
BROWSERS = (
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
)


def find_browser() -> Path:
    """!
    @brief Find a Chromium based browser to render HTML.

    @return Path of the browser program.
    @throws FileNotFoundError When none is installed.
    """
    for candidate in BROWSERS:
        if candidate.is_file():
            return candidate
    message = "No Edge or Chrome found; install one to make screenshots."
    raise FileNotFoundError(message)


def split_steps(
    notebook: nbformat.NotebookNode,
) -> dict[str, list[nbformat.NotebookNode]]:
    """!
    @brief Group the cells of an executed notebook by lecture step.

    @param notebook The executed notebook.
    @return Step slug mapped to the cells of that step, in order.
    """
    steps: dict[str, list[nbformat.NotebookNode]] = {}
    current: str | None = None
    for cell in notebook.cells:
        slug = cell.metadata.get("step")
        if slug:
            current = str(slug)
            steps[current] = []
        if current is not None:
            steps[current].append(cell)
    return steps


def trim_bottom(path: Path) -> None:
    """!
    @brief Cut the empty white space below the content of an image.

    @param path PNG file, changed in place.
    """
    image = Image.open(path).convert("RGB")
    background = Image.new("RGB", image.size, (255, 255, 255))
    box = ImageChops.difference(image, background).getbbox()
    if box is not None:
        image.crop((0, 0, image.width, min(image.height, box[3] + 24))).save(path)


def main() -> None:
    """!
    @brief Execute the notebook and write docs/images/<step>.png.
    """
    browser = find_browser()
    notebook = nbformat.read(NOTEBOOK_PATH, as_version=4)
    NotebookClient(notebook, timeout=600, kernel_name="python3").execute()
    IMAGE_DIRECTORY.mkdir(parents=True, exist_ok=True)
    exporter = HTMLExporter(template_name="lab")
    exporter.exclude_input_prompt = True
    exporter.exclude_output_prompt = True
    with tempfile.TemporaryDirectory() as folder:
        for slug, cells in split_steps(notebook).items():
            part = nbformat.v4.new_notebook(cells=cells, metadata=notebook.metadata)
            html_path = Path(folder) / f"{slug}.html"
            body, _ = exporter.from_notebook_node(part)
            html_path.write_text(body, encoding="utf-8")
            png_path = IMAGE_DIRECTORY / f"{slug}.png"
            # The command is built only from the fixed browser paths above and
            # temporary files this script wrote; no outside text reaches it.
            subprocess.run(  # noqa: S603  # nosemgrep: opengrep.selected-rules.python.lang.security.audit.dangerous-subprocess-use-audit
                [
                    str(browser),
                    "--headless=new",
                    "--disable-gpu",
                    f"--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}",
                    f"--screenshot={png_path.resolve()}",
                    html_path.resolve().as_uri(),
                ],
                check=True,
                timeout=120,
            )
            trim_bottom(png_path)
            print(f"wrote {png_path}")


if __name__ == "__main__":
    main()
