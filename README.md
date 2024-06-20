# sopel-inclusivity

Have your Sopel bot suggest more inclusive language

## Installing

Releases are hosted on PyPI, so after installing Sopel, all you need is `pip`:

```shell
$ pip install sopel-inclusivity
```

### Requirements

The `sopel-inclusivity` plugin is compatible with Sopel 7.1 or higher, but your
bot must run on Python 3.8 or higher; legacy Python versions are not supported.

## Functionality

`sopel-inclusivity` suggests better wordings when people don't use inclusive
language in chat. It's inspired by [this blog post][18f-post] from 18F, who
added a similar feature to their Slack rooms. It only deals with use of the word
"guys" for now, but PRs are welcome to add coverage of more vocabulary.

[18f-post]: https://18f.gsa.gov/2016/01/12/hacking-inclusion-by-customizing-a-slack-bot/
