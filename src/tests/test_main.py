from penstock import get_sources_list


def test_answer(config):
    assert len(get_sources_list(config)) == 2
