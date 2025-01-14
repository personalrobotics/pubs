# Personal Robotics Publications

BibTeX entries for the [Personal Robotics Lab][prl]. This repository is used to
populate the [publications][prl-pubs] page on the lab website.

Publication PDFs are stored in [Google Drive][prl-drive] and automatically
synced to the web server.

[prl]: https://personalrobotics.cs.washington.edu/
[prl-pubs]: https://personalrobotics.cs.washington.edu/publications/
[prl-drive]: https://drive.google.com/drive/folders/1M9fOGIIQ3e1R62dtVit5rZ5iWZqxfWV9

## Guidelines

- The publication title URL should point to the paper PDF on the personalrobotics domain.
- The rare exception is non-textual publications, such as videos or datasets: [example](https://github.com/personalrobotics/pubs/blob/e70ceab48d07c2efdaa4a071256fd8c1e17e861f/siddpubs-misc.bib#L68-L69).
- If the publication has a project website, the website can be linked as a `note` in the BibTex: [example](https://github.com/personalrobotics/pubs/blob/e70ceab48d07c2efdaa4a071256fd8c1e17e861f/siddpubs-conf.bib#L72).
  The project website should have a link to the paper PDF on the personalrobotics domain.

## Adding this repo to a LaTeX paper repo

One way to add this repository to a paper repository is via the [git submoudle](https://git-scm.com/book/en/v2/Git-Tools-Submodules) command. Do the following in your paper repository:
```
$ git submodule add https://github.com/personalrobotics/pubs
$ git commit -am 'added PRL pubs submodule'
$ git push origin master
```
Now if you freshly clone this repository elsewhere, you'll find an _empty_ `pubs` directory. To populate it, do:
```
$ git submodule init
$ git submodule update
```
Git submodules are tricky, and not everyone likes them, but they are one way to stay in sync. One thing to keep in mind is that you need to _be_ in the submodule subdirectory to run any git commands specific to that submodule.
