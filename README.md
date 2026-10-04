# Personal Robotics Lab: papers, people and projects

This repository is the lab's single source for:

- **every paper**: `siddpubs-journal.bib`, `siddpubs-conf.bib`, `siddpubs-misc.bib`
- **everyone in the lab**, current and past: `people.yaml`
- **the lab's projects**: `projects.yaml`

Three things are built from it, so a change here shows up in all of them:

- the lab website, https://personalrobotics.github.io/ (built by
  [personalrobotics.github.io](https://github.com/personalrobotics/personalrobotics.github.io))
- [goodrobot.ai](https://goodrobot.ai), Sidd's website
- Sidd's CV

Paper PDFs are not stored here: they go in the lab's
[Google Drive folder](https://drive.google.com/drive/folders/1M9fOGIIQ3e1R62dtVit5rZ5iWZqxfWV9),
which syncs to the UW web server (see [Add a paper's PDF](#add-a-papers-pdf)).

## How a change gets in

1. Open a pull request. The template lists what to check.
2. The **`validate`** check runs on it (see [How mistakes are caught](#how-mistakes-are-caught)).
   Fix anything it reports; a pull request with a failing check can't be merged.
3. Once it is reviewed and merged:
   - The lab website, goodrobot.ai and the CV update on their own within
     minutes.

## Add a paper

Add an entry to the `.bib` file for its kind: `siddpubs-journal.bib`,
`siddpubs-conf.bib` or `siddpubs-misc.bib` (workshops, theses, reports,
demos). Its **citation key** must be unique and is also the name of its PDF.
For example (shortened, with a `project` tag added to show the field):

```bibtex
@inproceedings{baijal2025lrn,
    title = {Long Range Navigator (LRN) : Extending robot planning horizons beyond metric maps},
    author = {Schmittle$^{*}$, Matthew and Baijal$^{*}$, Rohan and Hatch, Nathan and Srinivasa, Siddhartha},
    booktitle = corl,
    year = {2025},
    url = {https://personalrobotics.github.io/lrn/},
    project = {interventions},
    award = {RSS-ROAR Workshop Best Paper Award Winner}
}
```

Beyond the usual title, author, venue and year, these fields change how the
paper appears on the websites:

| Field | Shows as | Notes |
|-------|----------|-------|
| `url` | a **Website** button | the paper's project page. Use a link that will outlive your time in the lab |
| `video` | a **Video** button | e.g. a YouTube link |
| `doi`, `eprint` | **DOI** and **arXiv** buttons | `eprint` is the arXiv id, e.g. `2401.12345` |
| `award` | a red award badge | the award's name only, e.g. `Best Paper Award`. For an award given in another year than the paper's: `{2026: Test of Time Award}` |
| `project` | a project tag, and the paper is listed on that project's page | an `id` from `projects.yaml`. For several: `{robotfeeding, interventions}` |
| `note` | bold text under the venue | short, e.g. `Oral` |

Mark equal contributors with `$^{*}$` after their family name, as above. The
site shows a star and explains it.

Write each author's name the way the paper does. Lab members are recognised
through the `aliases` in `people.yaml`. An author who matches no one is shown
unlinked, which is fine for anyone outside the lab.

## Add a paper's PDF

Upload it to the Publications folder of the lab's shared drive
([link](https://drive.google.com/drive/folders/1M9fOGIIQ3e1R62dtVit5rZ5iWZqxfWV9)),
named exactly `<citation key>.pdf` (e.g. `baijal2025lrn.pdf`). Within 15
minutes it is copied to
`https://personalrobotics.cs.washington.edu/publications/<citation key>.pdf`,
and a few minutes later the lab website shows a **PDF** button. Nothing in the
`.bib` entry needs to change. To make it show sooner, see "To show a new PDF
right away" in the
[website's README](https://github.com/personalrobotics/personalrobotics.github.io#what-happens-automatically).

**To replace a PDF**, right-click the existing file and choose **File
information → Manage versions → Upload new version**. Don't upload a second
file with the same name: two files with one name can't be told apart, and
lab members can't delete files from the drive.

## People: `people.yaml`

**Joining the lab:** add an entry under the right heading.

```yaml
- id: doe                   # unique; lower case, no spaces
  name: Jane Doe
  aliases: ["J. Doe"]       # every other way the .bib files write your name
  role: phd_student
  status: current
  start_year: 2026
  co_advisor: Dieter Fox    # optional
  website: https://janedoe.github.io/   # optional
  bio: >-                   # optional; plain text, shown on your page
    Jane works on robot learning for assistive manipulation.
```

`role` is one of `professor`, `faculty`, `postdoc`, `phd_student`,
`ms_student`, `research_staff`, `intern_grad` or `intern_undergrad`.

**Changing role inside the lab** (intern to PhD student, MS to PhD, postdoc
to faculty): keep your one entry. Move the old role into `earlier_roles`,
oldest first, and give the entry its new `role` and `start_year`:

```yaml
- id: faulkner
  name: Taylor Kessler Faulkner
  role: faculty
  status: current
  start_year: 2024
  earlier_roles:
    - {role: postdoc, start_year: 2022, end_year: 2024}
```

Each earlier role can also carry `degree`, `thesis_title` and `co_advisor`.
Its years must not overlap the next role's: an earlier role ends by the year
the next one starts.

**Leaving:** keep your entry. Change `status` to `alumni` and add:

```yaml
  end_year: 2030
  current_position: Research Scientist @ Example Robotics
  thesis_title: "..."       # if you wrote one
```

Remove `website` and `bio` when you leave: the sites don't link or show them
for alumni, and they go stale.

## Projects: `projects.yaml`

```yaml
- id: robotfeeding          # what a paper's `project` field names
  title: "Robot-Assisted Feeding"
  description: "One paragraph about the project."
  website: "https://robotfeeding.io"   # optional
  status: "active"          # or "completed" when it ends
```

A paper joins a project through its `project` field; nothing else links them.

## How mistakes are caught

Every pull request runs **`validate`**, which checks the `.bib` files,
`people.yaml` and `projects.yaml` together with
[sslabdata](https://github.com/siddhss5/sslabdata) in strict mode. It fails on,
among others:

- a duplicate citation key, person id or project id
- a `project` tag that `projects.yaml` doesn't define
- an author name that could be more than one lab member, such as an alias two
  people share
- a key sslabdata doesn't read, such as a misspelt `webiste`
- a value of the wrong type, such as a `start_year` in quotes

Each error names the file, the entry and the field.

## Check your change yourself

With [uv](https://docs.astral.sh/uv/) installed, from your checkout of this
repository:

```console
$ uvx sslabdata==6.0.0 --config lab.yaml --validate --strict
```

`Validation passed.` means `validate` will pass too. To list the authors that
matched no one in `people.yaml`, for instance to check that your own papers
link to you:

```console
$ uvx sslabdata==6.0.0 --config lab.yaml --unresolved
```

To see how your change looks on the lab website before it is merged, follow
"Checking a change yourself" in the
[website's README](https://github.com/personalrobotics/personalrobotics.github.io/tree/sslabdata#checking-a-change-yourself).

## Using these entries in a LaTeX paper

Add this repository to your paper's repository as a
[git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules):

```console
$ git submodule add https://github.com/personalrobotics/pubs
$ git commit -m 'Add PRL pubs submodule'
```

A fresh clone of your paper then has an empty `pubs` directory. Fill it with:

```console
$ git submodule update --init
```

Run git commands meant for the submodule from inside the `pubs` directory.
