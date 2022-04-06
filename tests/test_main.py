from unittest.mock import MagicMock, patch

from main import main


@patch("main.create_mermaid_analysis_from_python")
def test_main(mock_create_mermaid_analysis_from_python: MagicMock) -> None:
    main()

    mock_create_mermaid_analysis_from_python.assert_called_with(
        input_path="./src/", output_path="./docs/"
    )
