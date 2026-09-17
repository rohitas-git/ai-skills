import unittest
from pathlib import Path

PIPELINE = Path(__file__).resolve().parents[1] / "references" / "build-pipeline.md"


class SingleFinalChromaPassTest(unittest.TestCase):
    def test_cleanup_runs_only_after_v2_assembly(self) -> None:
        instructions = PIPELINE.read_text()

        self.assertEqual(instructions.count("despill pass"), 1)
        self.assertLess(
            instructions.index("register row 9"),
            instructions.index("despill pass"),
        )


if __name__ == "__main__":
    unittest.main()
