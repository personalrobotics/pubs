## What this changes

<!-- One line, e.g. "Add our ICRA 2026 paper" or "Add Jane Doe as a PhD student". -->

## Checklist

Tick what applies and delete the sections that don't. The README explains each field.

### A paper
- [ ] Added the entry to the right `.bib` file (journal, conf or misc), with a unique citation key
- [ ] Uploaded `<citation key>.pdf` to the lab's [Google Drive folder](https://drive.google.com/drive/folders/1M9fOGIIQ3e1R62dtVit5rZ5iWZqxfWV9)
- [ ] Optional: `url` (project page), `video`, `award`, `note`
- [ ] Optional: `project = {id}`, with an `id` from `projects.yaml`

### A person (optional)
- [ ] Joining: added an entry to `people.yaml` with `status: current`, `role`, `start_year`, and `aliases` for how the `.bib` files write the name
- [ ] Leaving: set `status: alumni`, added `end_year` and `current_position`, removed `website` and `bio`. Kept the entry

### A project (optional)
- [ ] Added or updated the project in `projects.yaml` (`status: active` or `completed`)

### Before asking for review
- [ ] `uvx sslabdata==5.0.0 --config lab.yaml --validate --strict` says `Validation passed.` (the `validate` check runs the same thing)
