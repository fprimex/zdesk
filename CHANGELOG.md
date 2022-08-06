## 2.8.0
- Regenerate API from updated mirror. see [full
  commit](https://github.com/fprimex/zdesk/commit/4982b3dad9581fbb49d71307abc229dc4169ab74).
  Most notably, Zendesk has replace many, many instances of using `id` with,
  e.g., `ticket_id`, `article_id`, etc. Most of these are positional arguments,
  so if you were using `foo(id=1234)` I recommend changing to `foo(1234)` to
  (hopefully) future proof a bit when they decide to change it again.
- Update iterable code for Python 3.10 compatibility. Tests pass with 3.10.3
  and 3.9.5.
- This is not a change, but I want to note here that several of `zdesk`'s
  dependencies have deprecations. Most notably, if you're using `zdeskcfg`,
  `plac_ini` has a deprecation that will be removed in 3.12. None of these seem
  particularly difficult to overcome, but just make sure you test before
  upgrading.

## 2.7.1
- Immediately noticed an OAuth bug. Reference private variables for some logic.

## 2.7.0
- Support for Python 3.5+
- OAuth token support, and a more clear way of choosing between password, API
  token, and OAuth token authentication.
- Regenerate API from updated mirror. See [full
  commit](https://github.com/fprimex/zdesk/commit/1cf01a3b730c84b531261bba98b2ab5aa6dd0d18)

## 2.6.0
- Fix incremental pagination by making an exception to status 422, removing the
  existing query `kwargs`, and looking for incremental and certain conditions
  to mark the end of `get_all_pages` (by Sarfaraz Soomro).
- API generator updates corresponding to the end of web portal and forums
  support, as well as the replacement of zopim with chat (by Craig Davis).
- Add `raw_query` parameter for explicitly setting and overriding the query
  string. The enables use cases where, for example, query parameters need to be
  repeated and therefore cannot go into a dictionary.
- Add `retval` parameter to allow for explicitly requesting a certain component
  of a response. Valid values are 'content', 'code', 'location', and 'headers'.
- Regenerate API from updated mirror. See [full
  commit](https://github.com/fprimex/zdesk/commit/6e22dea7af6b129a88f9ce30082660eff2eea621)

## 2.5.0
- Use Pytest and implement some basic tests
- Implement retry (major contribution by Dominik Miedziński)
- Merge the `batch` support method (by Dominik Miedziński)
- Merge 2.6 support (by Ryan Shipp)
- Check for json in content-type before attempting to deserialize (by
  Craig Davis)
- Improve API generator handling of duplicates and ambiguous parameters
- Add support for optional `locale` help center argument on many methods
- Regenerate API from updated mirror. See [full
  commit](https://github.com/fprimex/zdesk/commit/bb455aeac4ffb9c7a6f5cabb9653cf46cdcb8531)

## 2.4.0
- Support non-JSON endpoint (removed check for .json, for recordings.mp3)
- Improve generator formatting of duplicates
- Add doc-anchor-links, so docstrings link more closely to the method question
- Regenerate API from updated mirror. See [full
  commit](https://github.com/fprimex/zdesk/commit/7240295278fd596189643ae30fbcbb16a4b8c3d9)

## 2.3.0
- Switch from `httplib2` to `requests`
- Add `files` parameter to support multipart uploads for Help Center attachment
  style requests
- Enhance `api_gen.py` to handle downloading and patching of developer.zendesk.com
- Add Zopim and numerous other API endpoints
- Regenerate API from updated mirror. See [full
  commit](https://github.com/fprimex/zdesk/commit/d679a734292de5ade82cb4d4533e79368510769d)

## 2.2.1
- Remove `common_params`, allowing all kwargs to be passed as queries

## 2.2.0

- Add exception classes to top level. e.g. `from zdesk import ZendeskError` works now
- Modify `api_gen.py` so that `update_many_update` becomes just `update_many`
- Regenerate API from updated mirror. See [full
  commit](https://github.com/fprimex/zdesk/commit/8a6bac52a912ce45c3a47911331b381cf963abc1)

## 2.1.1

- Remove explicit HTTP status code checking. Success is always in the 200
  range, with some specific exceptions raised for only a few specific 400 range
  codes.

## 2.1.0

- Support non-JSON data for, e.g., creating uploads
- Add `sort_by` common parameter
- Regenerate API from updated mirror. See [full
  commit](https://github.com/fprimex/zdesk/commit/cbeb1ecd0ae4580caa3ad434c74e7e49d4378c19)
- Update `examples/__init__.py` with fixes and ticket updates and uploads
- Reorder CHANGELOG.md with most recent releases at top

## 2.0.3

- Add `get_all_pages` option to call to exhaustively follow `next_page`
- Combine and reduce multiple requests when using `get_all_pages`

## 2.0.2

- Always inject auth credentials into request when they are supplied

## 2.0.1

- Immediately fix import bug in 2.0.0

## 2.0.0

- Drop APIv1 support code completely
- Drop endpoints dicts for new API generator approach
- Support Python 2 and Python 3 in codebase without 2to3 translation

## 1.2.0

- Fork zendesk from eventbrite
- Merge PRs and apply fixes
- Python 3 compatibility

