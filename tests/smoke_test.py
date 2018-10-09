import pytest

import sites
from leech import create_session, open_story, create_options

@pytest.mark.parametrize("url", [
    ("http://archiveofourown.org/works/5683105/chapters/13092007"),
    ("https://www.fanfiction.net/s/4109686/3/Taking-Sights"),
    ("https://www.fictionpress.com/s/2961893/1/Mother-of-Learning"),
    ("https://fiction.live/stories/Descendant-of-a-Demon-Lord/SBBA49fQavNQMWxFT"),
    ("https://royalroad.com/fiction/6752/lament-of-the-fallen"),
    ("https://forums.sufficientvelocity.com/threads/ignition-mtg-multicross-planeswalker-pc.26099/threadmarks"),
])
def test_successful_download(url):
    session = create_session(False)
    site, url = sites.get(url)
    story = open_story(site, url, session, False, site.get_default_options())
