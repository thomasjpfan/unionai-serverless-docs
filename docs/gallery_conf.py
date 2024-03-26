from pathlib import Path

DOC_ORDER = [
    # Tutorials
    "tutorials/ml-experiment-tracking.py",
    # User Guide
    "user-guide/quick-start.py",
    "user-guide/aws-s3-access.py",
]

DOC_PATHS = [
    (Path("docs") / "src").joinpath(*path.split("/")).absolute() for path in DOC_ORDER
]


class CustomSort:
    def __call__(self, file: Path):
        return DOC_PATHS.index(file)


conf = {"within_subsection_order": CustomSort}
