##############################################################################
# Copyright (c) Lawrence Livermore National Security, LLC and other Merlin
# Project developers. See top-level LICENSE and COPYRIGHT files for dates and
# other details. No copyright assignment is required to contribute to Merlin.
##############################################################################

from merlin.utils import needs_merlin_expansion


def test_does_not_modify_the_labels_it_was_given() -> None:
    """The caller's list is read, not extended with the sample keywords."""
    labels = ["X", "Y"]

    needs_merlin_expansion("echo $(X)", "", labels)

    assert labels == ["X", "Y"]


def test_sample_keywords_are_still_matched() -> None:
    assert needs_merlin_expansion("echo $(MERLIN_SAMPLE_ID)", "", ["X"])
    assert not needs_merlin_expansion("echo $(MERLIN_SAMPLE_ID)", "", ["X"], include_sample_keywords=False)


def test_repeated_calls_keep_the_same_answer() -> None:
    labels = ["X"]

    for _ in range(3):
        assert not needs_merlin_expansion("echo $(Z)", "", labels)

    assert labels == ["X"]
