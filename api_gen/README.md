Unless you're really going to hack on the API generator, don't hammer the
developer site needlessly. Currently, mirroring the required files results in
about 9MB on disk.

The API generator needs Python 3, `requests`, `BeautifulSoup4`, and
`inflection` installed. See the `requirements.txt` file. There also needs to be
a POSIX compliant `patch` executable in your path for applying the patches.
Linux and OSX have this, but on Windows it will need to be installed manually
with something like Cygwin.

No arguments are required.

```
(api_gen) $ ./api_gen.py
```

When `api_gen.py` is executed for the first time, the following happens:
* `apidocs` dir is deleted if it is present
* `apidocs_orig` dir is made if it is not present
* The introduction pages for each API component is downloaded
* The intro pages are scraped for all other pages which are downloaded
* Pages are written into the `apidocs_orig` dir
* `apidocs_orig` is copied to apidocs
* `apidocs` pages are patched with the diffs in `patches` dir
* Patched `apidocs` pages are scraped for REST API info
* Duplicates, redundant, and ambiguous endpoints are resolved
* The actual `zdesk_api.py` code is generated
* The code is formatted into (appended) to the template
* `zdesk_api.py` is written to the `api_gen` directory

On subsequent runs, the following happens:
* `apidocs` dir is deleted if it is present
* The introduction pages are located in the `apidocs_orig` dir
* The intro pages are scraped for all other pages
* The needed pages are located in the `apidocs_orig` dir
* `apidocs_orig` is copied to `apidocs` and the rest happens as before

If patches are needed, then to create them I do the following:
* Remove the patched `apidocs` dir
* Copy the `apidocs_orig` dir to `apidocs` dir
* If the file needing an edit has an already existing patch, apply the patch
  first

```
(apidocs) $ patch -p1 < ../patches/core_stuff
```

* Edit the file as needed
* Generate a new patch, potentially replacing the old patch

```
(apidocs) $ cd ..
(api_gen) $ diff -r -u apidocs_orig apidocs > patches/core_stuff
```

NOTE: Work on patching only one file at a time. If another patch needs to be
made, then the `apidocs` directory needs to be removed again, then recopied
from the `apidocs_orig` directory. This ensures that the patches are for only
one file at a time.

After generation I typically review the `zdesk_api.py` file to see what has
changed and to ensure that there are no new syntax problems and so forth. I
`diff` the old and new file, and also specifically look at the methods.

```
(api_gen) $ diff -u ../zdesk/zdesk_api.py zdesk_api.py

(api_gen) $ grep -E '^ *def' ../zdesk/zdesk_api.py > methods_old
(api_gen) $ grep -E '^ *def' zdesk_api.py > methods_new
(api_gen) $ diff -u methods_old methods_new
```

Finally, once all is well and I am satisfied with the newly generated
`zdesk_api.py`:

```
cp zdesk_api.py ../zdesk/
```

Hopefully this will help if someone needs to take this over. It would be great
to get patch contributions and feedback on if the generated API needs to be
changed somehow to make it nicer.

